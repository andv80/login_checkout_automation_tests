LOGIN_PAGE_URL = 'https://www.saucedemo.com/'

""" valid credentials """
STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"

PROBLEM_USER = "problem_user"
ERROR_USER = 'error_user'
PERFORMANCE_GLITCH_USER = 'performance_glitch_user'
VISUAL_USER = 'visual_user'

"""locked users"""
LOCKED_OUT_USER = "locked_out_user"

""" invalid credentials """
EMPTY_USERNAME = ''
EMPTY_PASSWORD = ''
NON_EXISTING_USER = 'TEST'
NON_EXISTING_PASSWORD = 'TEST'

"""error messages"""
EMPTY_USERNAME_ERROR = 'Epic sadface: Username is required'
EMPTY_PASSWORD_ERROR = 'Epic sadface: Password is required'
EMPTY_PASSWORD_AND_USERNAME_ERROR = EMPTY_USERNAME_ERROR
NON_VALID_CREDENTIALS_ERROR = 'Epic sadface: Username and password do not match any user in this service'
LOCKED_OUT_ERROR = 'Epic sadface: Sorry, this user has been locked out.'
