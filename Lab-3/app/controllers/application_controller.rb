class ApplicationController < ActionController::Base
  before_action :set_locale
  protect_from_forgery with: :exception
  #redirects user to required page
  def after_sign_in_path_for(resource)
    if current_user.try(:admin?)
       admin_index_url
    else
       enrollee_index_path
    end
  end

  #sets locale for the page
  def set_locale
    I18n.locale = params[:locale] || I18n.default_locale
  end

  #edits url
  def default_url_options(options={})
    {locale: I18n.locale}.merge options
  end


end
