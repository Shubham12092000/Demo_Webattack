import time


from Setup.Get_data_from_excel import *
from Setup.Setup_files import generate_random_user_name
from Setup.generic_functions import *
from Setup.Locators import *



def register_user():
    random_user_name = generate_random_user_name()
    do_click(signin_button)
    do_click(register_here_button)
    do_sendkeys(email, random_user_name)
    do_sendkeys(password, new_user_password.value)
    do_sendkeys(confirm_password, new_user_password.value)
    do_sendkeys(first_name, new_user_first_name.value)
    do_sendkeys(last_name, new_user_last_name.value)
    do_sendkeys(current_address, new_user_current_address.value)
    do_sendkeys(Address_line2, new_user_address1.value)
    do_sendkeys(zipcode, new_user_zipcode.value)
    do_sendkeys(city, new_user_city.value)
    do_sendkeys(state, new_user_state.value)
    select_dropdown(country, "India")
    do_sendkeys(phone_number, new_user_phone_number.value)
    do_click(new_user_register_button)
    time.sleep(3)
    do_sendkeys(userID_filed, random_user_name)
    do_sendkeys(password_field, new_user_password.value)
    do_click(submit_button)
    take_screenshot("D:/Study_Project/Screenshots/image123.png")
    return get_element_text(login_success_msg)

def your_profile_options():
    do_click(login_success_msg)
    orders_text = get_element_text(your_orders_button) #Your orders
    your_profile_text = get_element_text(your_profile_button) #Your profile
    signout_text = get_element_text(signout_button) #Sign Out
    return [orders_text, your_profile_text, signout_text]

def adding_item_to_cart():
    do_click(item)
    do_click(add_to_cart_item)
    do_click(cart_button)
    return get_element_text(cart_button)

def sign_in_error_msg():
    do_click(login_success_msg)
    do_click(signout_button)
    do_click(signin_button)
    userid_text = get_element_text(UserID_label)
    password_text = get_element_text(Password_label)
    register_here_text = get_element_text(Register_here_label)
    return [userid_text, password_text, register_here_text]

