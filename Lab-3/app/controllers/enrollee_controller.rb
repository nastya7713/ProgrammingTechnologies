class EnrolleeController < ApplicationController
  before_action :authenticate_user!, :is_admin!

  def faculty_list
    @faculties = Faculty.all
  end

  #finds enrollee faculties
  def my_faculties
    @faculties = nil
    if FacultyEnrollee.exists?(user_id: current_user.id)
      @faculties = current_user.faculties
    end
  end

  def index
  end

  #checks if user already has registration
  #if so sets @success true, vice versa finds faculty

  def enrollment_page
    @faculty = nil
    @success = FacultyEnrollee.exists?(faculty_id: params[:faculty_id], user_id: current_user.id)
    unless @success
      @faculty = Faculty.find(params[:faculty_id])
    end
  end

  #enrolls for the faculty, sets average grade
  def enroll_faculty
    average_grade = 0
    @success = false
    faculty = Faculty.find(params[:faculty_id])
    faculty.subjects.each do |sub|
      average_grade += params[sub.name].to_f
    end
    average_grade += params[:grade].to_f
    average_grade /= (faculty.subjects.count + 1)
    faculty_enrollee = FacultyEnrollee.new(:faculty => Faculty.find(params[:faculty_id]), :user => current_user, :grade => average_grade )
    if faculty_enrollee.save
      @success = true
    end
    render :enrollment_page
  end


  def admission_page
    faculty = Faculty.find(params[:faculty_id])
    @faculty_enrollees = faculty.faculty_enrollees.where(admission:true).order(grade: :desc)
    @limit = faculty.limit
  end

  private

  #checks if user is admin
  def is_admin!
    if current_user
      if current_user.try(:admin?)
        redirect_to admin_index_path # halts request cycle
        false
      end
     end
  end

end
