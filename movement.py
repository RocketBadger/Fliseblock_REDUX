from gpio4 import GPIO as GPIO
import serial

GPIO.setmode(GPIO.BCM)
# GPIO.setup([12, 13], GPIO.IN)
# GPIO.input([12, 13])


class Fliseblock:
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyAMA0", 115200)
        print("Serial open")

    def __close__(self):
        self.ser.close()
        print("serial close")

    def pidmode(self):
        # TODO
        pass

    def servocontrol(self):
        # TODO
        pass

    def servocontrolsingle(self):
        # TODO
        pass

