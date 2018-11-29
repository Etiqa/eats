from eats.tests.common import SimpleWebServerProcess

process = SimpleWebServerProcess()
process.run()

while True:
    stop = raw_input('Stop server: (Y/N)')
    if stop == 'Y':
        process.stop()
        break
