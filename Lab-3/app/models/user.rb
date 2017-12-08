class User < ApplicationRecord
  has_many :faculty_enrollees
  has_many :faculties, :through => :faculty_enrollees
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable
end
