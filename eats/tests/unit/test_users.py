import unittest
from hamcrest import *
from eats.users.users import Users


class UsersTest(unittest.TestCase):

    def setUp(self):
        self._setup_users()

    def _setup_users(self):
        context = FakeContext()
        Users.setup(context)
        self.context = context

    def test_installation(self):
        context = self.context
        assert_that(context.users, is_(instance_of(Users)))

    def test_add_user(self):
        users = self.context.users
        the_user = FakeUser()
        users.add('some_user', the_user)
        assert_that(users.get('some_user'), is_(the_user))

    def test_user_not_found(self):
        users = self.context.users
        the_user = FakeUser()
        users.add('some_user', the_user)
        assert_that(users.get('some_other_user'), is_(None))

    #def test_weakref(self):
    #    users = self.context.users
    #    del self.context
    #    try:
    #        users._context.__repr__()
    #    except ReferenceError:
    #        pass
    #    else:
    #        self.fail('expected exception "ReferenceError: weakly-referenced object no longer exists" was not raised')

    def test_add_role(self):
        users = self.context.users
        users.add_role('some_role', FakeUser)
        assert_that(users.get_role('some_role'), is_(equal_to(FakeUser)))


class FakeContext(object):
    pass


class FakeUser(object):
    pass


class FakeDriver(object):
    pass
