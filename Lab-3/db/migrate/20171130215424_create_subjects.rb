class CreateSubjects < ActiveRecord::Migration[5.1]
  def change
    create_table :subjects do |t|
      t.string :name, limit: 30

      t.timestamps
    end
    add_index :subjects, :name, unique: true
  end
end
