from behave import *
from eats.users.users import BaseUser
from app import TestApplication
from eats.webdriver import web_driver_factory
from eats.behave import application_steps, element_steps, page_steps

@given(u'"{user_name}" user')
def step_impl(context, user_name):
    environment = context.config.userdata.get('environment')
    base_url = context.eats.config.get("application.default", environment)
    driver = web_driver_factory(context)
    base_user = BaseUser(TestApplication(driver, base_url))
    context.users.add(user_name, base_user)

@when(u'"{user_name}" user go to "{page}" page')
def step_impl(context, user_name, page):
    context.users.get(user_name).application.get_page(page).goto()
