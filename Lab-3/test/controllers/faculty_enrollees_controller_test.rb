require 'test_helper'

class FacultyEnrolleesControllerTest < ActionDispatch::IntegrationTest
  test "should get enrollment_page" do
    get faculty_enrollees_enrollment_page_url
    assert_response :success
  end

  test "should get delete" do
    get faculty_enrollees_delete_faculty_enrollees_url
    assert_response :success
  end

  test "should get add" do
    get faculty_enrollees_add_faculty_enrollees_url
    assert_response :success
  end

end
