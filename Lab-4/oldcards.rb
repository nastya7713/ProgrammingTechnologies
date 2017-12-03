#pcocess optional card value
module PROCESS
  SEND = 'send'.freeze
  UNSENT = 'unsent'.freeze
end

#value optional card value
module VALUE
  COLLECTION = 'collection'.freeze
  ORDINARY = 'ordinary'.freeze
  ADVERTISEMENT = 'advertisement'.freeze
end

#describes complextype class Type
class Type
  attr_accessor :context
  attr_reader :process
  def process=(process)
    if (process == PROCESS::SEND) || (process == PROCESS::UNSENT)
      @process = process
    else
      raise('Incorrect process data. Must be PROCESS member')
    end
  end

  def to_s
    " process: #{@process}, context: #{@context}"
  end
end

#describes oldcard element
class OldCards
  attr_accessor :country, :topic, :name, :id, :type, :authors
  attr_reader :value, :year
  #checks year value and set year
  def year=(year)
    if !(year =~ /^[0-9][0-9][0-9][0-9]$/).nil?
      @year = year.to_i
    else
      raise('Incorrect year data. Must be [0-9][0-9][0-9][0-9]')
    end
  end

  def add_authors(author)
    @authors.push(author)
  end
  #checks if value is member of VALUE module
  def value=(value)
    if (value == VALUE::COLLECTION) || (value == VALUE::ORDINARY) || (value == VALUE::ADVERTISEMENT)
      @value = value
    else
      raise('Incorrect value data. Must be VALUE member')
    end
  end

  def initialize
    @type = Type.new
    @authors = Array.new
  end

  def to_s
    "Id value: #{@id}, Name: #{@name}, Topic: #{@topic}, Type: #{@type}, Country: #{@country}, Year: #{@year}, Value: #{@value}, Authors: #{@authors}"
  end
end

