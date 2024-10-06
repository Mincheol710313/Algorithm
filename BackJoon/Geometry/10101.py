angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

all_angle = angle1 + angle2 + angle3

if all_angle > 180 or all_angle < 180:
    print("Error")
else:
    if angle1 == 60 and angle2 == 60:
        print("Equilateral")
    elif (angle1 == angle2) or (angle1 == angle3) or (angle2 == angle3):
        print("Isosceles")
    else:
        print("Scalene")