class Faculty < ApplicationRecord
  has_and_belongs_to_many :subjects
  has_many :faculty_enrollees
  has_many :users, :through => :faculty_enrollees
end
