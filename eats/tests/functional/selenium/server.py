from eats.tests.functional.selenium.testserver_selenium import SimpleWebServerProcessSelenium
import time

process = SimpleWebServerProcessSelenium()
process.run()

while(True):
    stop = raw_input('Stop server: (Y/N)')
    if stop == 'Y':
        process.stop()
        break
