from movement import Movement
import time

movement = Movement()

time.sleep(3)
print("camera_tower_control test")
movement.camera_tower_control(1500, 1500)
time.sleep(3)
print("camera_tower_control_singleservo 1 test")
movement.camera_tower_control_singleservo(1, 2000)
time.sleep(3)
print("camera_tower_control_singleservo 2 test")
movement.camera_tower_control_singleservo(2, 2000)

time.sleep(3)
print("wheelcontrol test a")
movement.wheelcontrol(8, 0, 0, 0)
time.sleep(3)
print("wheelcontrol test b")
movement.wheelcontrol(0, 8, 0, 0)
time.sleep(3)
print("wheelcontrol test c")
movement.wheelcontrol(0, 0, 8, 0)
time.sleep(3)
print("wheelcontrol test d")
movement.wheelcontrol(0, 0, 0, 8)
