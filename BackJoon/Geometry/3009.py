input_points_list = []
for i in range(3):
    x, y = map(int, input().split())
    input_points_list.append([x, y])
input_points_list.sort()

x_max = 0
x_min = input_points_list[0][0]
y_max = 0
y_min = input_points_list[0][1]

for i in range(3):
    # x_max 파악
    if x_max < input_points_list[i][0]:
        x_max = input_points_list[i][0]
    elif x_min > input_points_list[i][0]:
        x_min = input_points_list[i][0]
    # y_max 파악
    if y_max < input_points_list[i][1]:
        y_max = input_points_list[i][1]
    elif y_min > input_points_list[i][1]:
        y_min = input_points_list[i][1]

points_list = [[x_min, y_min], [x_min, y_max], [x_max, y_min], [x_max, y_max]]
for points in points_list:
    if points not in input_points_list:
        print(points[0], points[1])
