require 'nokogiri'
require_relative 'oldcards'

include Nokogiri

class CardsSAXParser < Nokogiri::XML::SAX::Document
  attr_reader :old_cards

  def initialize
    @old_cards = nil
    @elem = nil
  end

  def start_element(name, attributes)
    if name == 'oldCard'
      @elem = OldCards.new
      @elem.id = attributes[0][1]
    end
    @state = name
  end

  def end_element(name)
    if name == 'oldCard'
      @old_cards.push(@elem)
    end
    @state = nil
  end

  #checks characters and sets value
  def characters(value)
    case @state
      when 'id'
        @elem.id = value
      when 'name'
        @elem.name = value
      when 'country'
        @elem.country = value
      when 'topic'
        @elem.topic = value
      when 'context'
        @elem.type.context = value
      when 'process'
        @elem.type.process = value
      when 'year'
        @elem.year = value
      when 'value'
        @elem.value = value
      when 'author'
        @elem.add_authors(value)
    end
  end

  def end_document
    puts "\nParsed by SAX"
    puts @papers
  end

  def start_document
    @old_cards = Array.new
  end
end