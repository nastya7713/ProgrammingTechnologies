require 'nokogiri'
require_relative 'CardsDOMParser'
require_relative 'CardsSAXParser'

include Nokogiri

xsd = Nokogiri::XML::Schema(File.read('xml/oldCards.xsd'))
doc = Nokogiri::XML(File.read('xml/oldCards.xml'))

#validation xml agains xsd
error_list = xsd.validate(doc)
if error_list.length > 0
  error_list.each do |error|
  puts("During validation error occured:")
  puts error.message
  end
else
  puts('XML is valid')
  #parses using DOMParser and shows result
  puts("Parsed by DOM:")
  dom_parser = CardsDOMParser.new(doc)
  old_cards = dom_parser.parse
  puts(old_cards)

  #parses using SAXParser and shows result
  sax_parser = CardsSAXParser.new
  parser = XML::SAX::Parser.new(sax_parser)
  parser.parse_file('xml/OldCards.xml')

  #sorts card list
  puts("Sorted:")
  old_cards.sort_by(&:year)
  puts(old_cards.reverse)
end
