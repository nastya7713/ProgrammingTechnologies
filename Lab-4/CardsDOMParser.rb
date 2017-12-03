require 'nokogiri'
require_relative 'oldcards'

class CardsDOMParser
  def initialize(xml)
    @xml = xml
  end

  def parse
    old_cards = []
    #parse every oldCard item
    @xml.search('oldCard').each do |item|
      old_card = OldCards.new
      old_card.id = item['id']
      old_card.name = item.at('name').text
      old_card.topic = item.at('topic').text
      old_card.country = item.at('country').text
      old_card.year = item.at('year').text
      old_card.value = item.at('value').text

      item.search('author').each do |auth|
        old_card.add_authors(auth.text)
      end

      type = item.at('type')
      type_context = type.at('context').text
      type_process = type.at('process').text
      old_card.type.process = type_process
      old_card.type.context = type_context
      old_cards.push(old_card)
    end
    old_cards
  end
end
