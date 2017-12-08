class AddAdmissionToFacultyEnrollees < ActiveRecord::Migration[5.1]
  def change
    add_column :faculty_enrollees, :admission, :boolean, :default => false
  end
end
