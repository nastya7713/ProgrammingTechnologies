class FacultyEnrollee < ApplicationRecord
  belongs_to :faculty
  belongs_to :user
end
