class CreateFacultiesUsersJoinTable < ActiveRecord::Migration[5.1]
  def change
    create_join_table :faculties, :users do |t|
      t.index :faculty_id
      t.index :user_id
    end
  end
end
