Rails.application.routes.draw do
  scope "(:locale)", locale: /en|uk/ do
    get 'faculty_enrollees/enrollment_page'

    get 'faculty_enrollees/delete'

    get 'faculty_enrollees/index'

    post 'faculty_enrollees/add_enrollee'

    post 'enrollee/enroll_faculty'

    get 'faculty_enrollees/add'

    get 'enrollee/index'

    post 'admin/add_faculty_subject'

    get 'enrollee/faculty_list'

    get 'enrollee/my_faculties'

    get 'enrollee/enrollment_page'

    get 'enrollee/admission_page'

    get 'admin/admission_lists'

    get 'admin/users'

    get 'admin/index'

    get 'admin/add_faculty_subjects'

    get 'admin/delete_faculty_subjects'

    get 'admin/faculty_subjects'

    get 'admin/create_admission_list_page'

    get 'admin/show_admission_list'

    post 'admin/form_list'

    devise_for :admins
    devise_for :users, :controllers => { registrations: 'registrations' }
    post 'create_user' => 'users#create', as: :create_user
    root 'enrollee#index'
    resources :users, except: :create
    resources :faculties
    resources :subjects
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  end
end
