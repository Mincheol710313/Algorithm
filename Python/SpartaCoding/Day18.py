N = int(input())  # 센서의 개수
K = int(input())  # 집중국의 개수

sensor_list = list(map(int, input().split()))  # 센서 좌표 리스트
sensor_list.sort()

array = []
for i in range(N-1):
    array.append(sensor_list[i+1] - sensor_list[i])

array.sort()

print(sum(array[:N-K]))
