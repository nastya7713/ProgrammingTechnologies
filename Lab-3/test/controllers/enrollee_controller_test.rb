require 'test_helper'

class EnrolleeControllerTest < ActionDispatch::IntegrationTest
  test "should get faculty_list" do
    get enrollee_faculty_list_url
    assert_response :success
  end

  test "should get my_faculties" do
    get enrollee_my_faculties_url
    assert_response :success
  end

  test "should get enrollment_page" do
    get enrollee_enrollment_page_url
    assert_response :success
  end

  test "should get admission_page" do
    get enrollee_admission_page_url
    assert_response :success
  end

  test "should get index" do
    get enrollee_index_url
    assert_response :success
  end

end
