# from gpio4 import GPIO as GPIO
# import pigpio
# import RPi.GPIO as GPIO # cannot be installed on Windows python(?)/raspberry pi exclusive module
import serial
# GPIO.setmode(mode=GPIO.BCM)


class Movement:
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyAMA0", 115200)  # Opens serial port on pins 8 & 10.
        # alternatively use: /dev/serial0
        print("Serial open")
        # self.pi = pigpio.pi()

    def __close__(self):
        self.ser.close()
        print("serial close")

    def pid(self):
        # TODO
        pass

    def camera_tower_control(self, angle1, angle2):
        # TODO: test this
        if angle1 < 500:
            angle1 = 500
        elif angle1 > 2500:
            angle1 = 2500

        if angle2 < 500:
            angle2 = 500
        elif angle2 > 2500:
            angle2 = 2500

        servo_upper1 = (angle1 >> 8) & 0x00ff
        servo_lower1 = angle1 & 0x00ff
        servo_upper2 = (angle2 >> 8) & 0x00ff
        servo_lower2 = angle2 & 0x00ff

        checksum = (2 + 4 + servo_upper1 + servo_lower1 + servo_upper2 + servo_lower2) & 0xff
        cmd = [0xFF, 0xFE, 2, 4, servo_upper1, servo_lower1, servo_upper2, servo_lower2, checksum]
        self.ser.write(bytes(cmd))

    def camera_tower_control_singleservo(self, servoindex, angle):
        # TODO: Test this
        if angle < 500:
            angle = 500
        elif angle > 2500:
            angle = 2500

        servo_upper = (angle >> 8) & 0x00ff
        servo_lower = angle & 0x00ff
        checksum = (2 + 3 + servoindex + servo_upper + servo_lower) & 0xff
        cmd = [0xFF, 0xFE, 2, 3, servoindex, servo_upper, servo_lower, checksum]
        self.ser.write(bytes(cmd))

    def wheelcontrol(self, wheel_a, wheel_b, wheel_c, wheel_d):
        # TODO: Test this
        wheel_a = abs(wheel_a) & 0xff
        wheel_b = abs(wheel_b) & 0xff
        wheel_c = abs(wheel_c) & 0xff
        wheel_d = abs(wheel_d) & 0xff

        wheel_a_go = 1 if wheel_a < 0 else 0
        wheel_b_go = 1 if wheel_b < 0 else 0
        wheel_c_go = 1 if wheel_c < 0 else 0
        wheel_d_go = 1 if wheel_d < 0 else 0

        wheel_direction_bits = wheel_a_go | wheel_b_go | wheel_c_go | wheel_d_go
        checksum = (3 + 8 + 0x02 + wheel_a + wheel_b + wheel_c + wheel_d + wheel_direction_bits) & 0xff
        cmd = [0xFF, 0xFE, 3, 8, 0x02, wheel_a, wheel_b, wheel_c, wheel_d, 0x00, 0x00, wheel_direction_bits, checksum]
        self.ser.write(bytes(cmd))
