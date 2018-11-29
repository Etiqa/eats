import unittest
from hamcrest import *
from eats.utils.workspace import WorkSpace
from eats.utils.root import Root
from eats.utils.screenshots_dir import ScreenshotDir
import os


class TestWorkspaceMethods(unittest.TestCase):

    def test_screenshot_dir(self):
        root = Root()
        screen = ScreenshotDir()
        assert_that(root.root(), os.getcwd())
        assert_that(screen.root(), os.getcwd() + "/screenshots")

    def test_ws_dir(self):
        root = Root()
        ws = WorkSpace()
        assert_that(root.root(), os.getcwd())
        assert_that(ws.root(), os.getcwd() + "/workspace")


if __name__ == '__main__':
    unittest.main()