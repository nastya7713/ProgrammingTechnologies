class AdminController < ApplicationController
  before_action :redirect_unless_admin

  def index
  end

  def users
    @users = User.all
  end

  #deletes all faculty enrollees
  def delete_all_enrollees(faculty_id)
    FacultyEnrollee.where(faculty_id: faculty_id).each do |faculty|
      if faculty.admission
      faculty.update_attribute(:admission, false)
      end
    end
  end

  #form admission list action
  def form_list
      delete_all_enrollees(params[:faculty_id])
      if params[:enrollee_ids].length > params[:faculty_limit].to_i
        redirect_to admin_create_admission_list_page_path(:alert => 'Faculty limit exceeded!', :faculty_id =>  params[:faculty_id])
      else
        params[:enrollee_ids].each do |id|
        enrollee = FacultyEnrollee.find_by(faculty_id: params[:faculty_id], user_id: id)
        enrollee.update_attribute(:admission, true)
        end
        redirect_to admin_show_admission_list_path(faculty_id: params[:faculty_id])
      end

  end

  #shows admission list
  def show_admission_list
    faculty = Faculty.find(params[:faculty_id])
    @faculty_enrollees = faculty.faculty_enrollees.where(admission:true).order(grade: :desc)
    @limit = faculty.limit
  end

  #finds faculty enrollees, sorts them in descending order
  def create_admission_list_page
    faculty = Faculty.find(params[:faculty_id])
    @faculty_enrollees = faculty.faculty_enrollees.order(grade: :desc).all
    @limit = faculty.limit
  end

  #shows faculties vailable to create admission list
  def admission_lists
    @faculties = Faculty.all
  end

  def faculty_subjects
    @faculties = Faculty.all
  end

  def add_faculty_subject
      Faculty.find(params[:faculty_id]).subjects << Subject.find(params[:subject_id])
      redirect_to admin_faculty_subjects_path
  end

  #add subjects to faculty
  def add_faculty_subjects
    @faculty = Faculty.find(params[:faculty_id])
    @subs = []
    Subject.all.each do |sub|
      unless sub.faculties.include? @faculty
        @subs.push(sub)
      end
    end
  end

  #deletes subjects from faculties
  def delete_faculty_subjects
    Faculty.find(params[:faculty_id]).subjects.delete(params[:subject_id])
    redirect_to admin_faculty_subjects_path
  end

  private
  #redirects if user is  not admin to root path
  def redirect_unless_admin
    unless current_user.try(:admin?)
      flash[:error] = "Only admins can do that"
      redirect_to root_path
    end
  end

end
