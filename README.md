# ProgrammingTechnologies
Lab-3 Programming technologies covers creating university admission system using Ruby on Rails.
Application has internationalisation (uk:Ukraine, en:English). Admin page provided. Admin can create all needed
data, including register list for the choosen faculty.
Enrollee has an opportunity to register for available faculties, filling in all required subjects' grades,
check current register list created by admin, change personal info.
Project implements MVC structure:
Models:
      *created using ActiveRecord database schema could be found in Lab-3/db/schema.rb
Views:
      *admin/*
      *devise/*
      *enrollee/*
      *faculties/*
      *faculty_enrollees/*
      *subjects/*
      *users/*
Controllers:
      *admin_controller.rb
      *application_controller.rb
      *enrollee_controller.rb
      *faculties.controller.rb
      *faculty_enrollees_controller.rb
      *registrations_controller.rb
      *subjects_controller.rb
      *users_controller.rb
