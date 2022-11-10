from selenium.webdriver.common.by import By

signin_button = (By.XPATH, '//*[@id="title"]/a[1]')

userID_filed = (By.XPATH, '//*[@id="loginEmail"]')
password_field = (By.XPATH, '//*[@id="loginPassword"]')
submit_button = (By.XPATH, '//*[@id="loginForm"]/div[3]/input')
msg_invalid = (By.XPATH, '/html/body/h1')


register_here_button = (By.XPATH, '//*[@id="loginForm"]/div[4]/a')
email = (By.XPATH, '/html/body/form/p[1]/input')
password = (By.XPATH, '//*[@id="password"]')
confirm_password = (By.XPATH, '//*[@id="cpassword"]')
first_name = (By.XPATH, '/html/body/form/p[4]/input')
last_name = (By.XPATH, '/html/body/form/p[5]/input')
current_address = (By.XPATH, '/html/body/form/p[6]/input')
Address_line2 = (By.XPATH, '/html/body/form/p[7]/input')
zipcode = (By.XPATH, '/html/body/form/p[8]/input')
city = (By.XPATH, '/html/body/form/p[9]/input')
state = (By.XPATH, '/html/body/form/p[10]/input')
country = (By.XPATH, '//*[@id="country"]')
phone_number = (By.XPATH, '/html/body/form/p[12]/input')
new_user_register_button = (By.XPATH, '/html/body/form/p[13]/input')
registration_sucess_msg = (By.XPATH, '/html/body/h1')

login_success_msg = (By.XPATH, '//*[@id="title"]/div[2]/button')

your_orders_button = (By.XPATH, '//*[@id="title"]/div[2]/div/a[1]')
your_profile_button = (By.XPATH, '//*[@id="title"]/div[2]/div/a[2]')
signout_button = (By.XPATH, '//*[@id="title"]/div[2]/div/a[3]')

item = (By.XPATH, '//*[@id="itemImage"]')
add_to_cart_item = (By.XPATH, '//*[@id="addToCart"]/a')
cart_button = (By.XPATH, '//*[@id="title"]/a')  # CART 1\ //*[@id="title"]/a

procced_to_checkout = (By.XPATH, '/html/body/a')
remove_button = (By.XPATH, '//*[@id="itemName"]/a')

men_category_button = (By.XPATH, "/html/body/div[2]/div[1]/ul/li[1]/a")
men_product_button = (By.XPATH, '//*[@id="itemImage"]')

men_item_price = (By.XPATH, '//*[@id="itemPrice"]')
logo = (By.XPATH, '//*[@id="logo"]')
women_item = (By.XPATH, '//*[@id="itemImage"]')
cart_total = (By.XPATH, '//*[@id="total"]')

search_bar = (By.XPATH, '//*[@id="searchBox"]')
search_button = (By.XPATH, '//*[@id="searchButton"]')
msg_after_seach = (By.XPATH, '/html/body/div[2]/h1')

searched_item = (By.XPATH, '//*[@id="itemImage"]')

tv_catagory = (By.XPATH, '/html/body/div[2]/div[1]/ul/li[3]/a')

UserID_label = (By.XPATH, '//*[@id="loginForm"]/div[1]/label')
Password_label = (By.XPATH, '//*[@id="loginForm"]/div[2]/label')
Register_here_label = (By.XPATH, '//*[@id="loginForm"]/div[4]/a')