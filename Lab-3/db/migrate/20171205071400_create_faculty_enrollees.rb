class CreateFacultyEnrollees < ActiveRecord::Migration[5.1]
  def change
    create_table :faculty_enrollees do |t|
      t.belongs_to :faculty, index: true
      t.belongs_to :user, index: true
      t.float :grade

      t.timestamps
    end
  end
end
