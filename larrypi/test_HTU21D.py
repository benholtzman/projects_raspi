# import time
# import board
# from adafruit_htu21d import HTU21D

import time
import board
import busio
from adafruit_htu21d import HTU21D

print('IS THIS GONNA WORK?')
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = HTU21D(i2c)

# Create sensor object, communicating over the board's default I2C bus
#i2c = board.I2C()  # uses board.SCL and board.SDA
#sensor = HTU21D(i2c)
print('got to here?') 

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
