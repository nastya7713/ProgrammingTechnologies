class CreateSubjectsFacultiesJoinTable < ActiveRecord::Migration[5.1]
  def change
    create_join_table :subjects, :faculties do |t|
      t.index :subject_id
      t.index :faculty_id
    end
  end
end
