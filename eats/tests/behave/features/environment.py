from eats.webdriver import web_driver_factory
from eats.utils.workspace import WorkSpace
from eats.utils.screenshots_dir import ScreenshotDir
from eats.utils.config import Configurator
from eats.users.users import Users, BaseUser
from app import TestApplication


def before_scenario(context, scenario):
    Configurator.setup(context)
    environment = context.config.userdata.get('environment')
    if not environment:
        raise RuntimeError('missing environment')
    else:
        base_url = context.eats.config.get("application.default", environment)

    driver = web_driver_factory(context)
    base_user = BaseUser(TestApplication(driver, base_url))
    Users.setup(context)
    context.users.set_default_user(context, base_user)
    context.workspace = WorkSpace()
    context.screenshot_expected = ScreenshotDir()


def after_scenario(context, scenario):
        if hasattr(context, 'users'):
            for user in context.users:
                user.application.driver.quit()
