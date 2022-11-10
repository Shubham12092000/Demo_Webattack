from Pages.Home_Page import register_user, your_profile_options, adding_item_to_cart, sign_in_error_msg
from Setup.Get_data_from_excel import new_user_first_name
from Setup.Setup_files import *

driver = start_browser()

def test_register_user():
    Greeting  = register_user()
    if (Greeting == "Hello,\n"+ new_user_first_name.value):
        assert True
    else:
        print("The Greeting message is: " + Greeting)
        assert False

def test_your_profile_options():
    list = your_profile_options()
    if ((list[0] == "Your orders") and (list[1] == "Your profile") and (list[2] == "Sign Out")):
        assert True
    else:
        print("The Profile Options are:" + list[0] + "," + list[1] + "," + list[2] + ".")
        assert False


def test_adding_item_to_cart():
    cart_text = adding_item_to_cart()
    if (cart_text == "CART 1"):
        assert True
    else:
        print("The Value of Cart is: " + cart_text + ".")
        assert False

def test_sign_in_error_msg():
    list = sign_in_error_msg()
    if ((list[0] == "UserID") and (list[1] == "Password") and (list[2]) == "Register here"):
        assert True
    else:
        print("The Values of Label are: " + list[0] + "," + list[1] + "," + list[2] +".")
        assert False
