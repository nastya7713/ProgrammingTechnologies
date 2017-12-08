class FacultyEnrolleesController < ApplicationController
  before_action :redirect_unless_admin
  def index
    @faculties = Faculty.all
  end

  # adds enrollee
  def add_enrollee
    @faculty_enrollee =FacultyEnrollee.new(:faculty_id => params[:faculty_id], :user_id => params[:user_id], :grade => params[:grade])
    @faculty_enrollee.save
    redirect_to faculty_enrollees_index_path
  end

  #deletes enrollee
  def delete
    faculty_enrollee = FacultyEnrollee.find_by(faculty_id: params[:faculty_id], user_id: params[:user_id])
    faculty_enrollee.delete
    faculty_enrollee.save
    redirect_to faculty_enrollees_index_path
  end

  #adds enrollee
  def add
    @faculty = Faculty.find(params[:faculty_id])
    @users = []
    User.all.each do |user|
      unless user.faculties.include? @faculty
        unless user.admin
        @users.push(user)
          end
      end
    end
  end

  private
  def redirect_unless_admin
    unless current_user.try(:admin?)
      redirect_to root_path
    end
  end

end
