import sys

N = int(sys.stdin.readline())

timetable = []

for _ in range(N):
    timetable.append(list(map(int,sys.stdin.readline().split())))

timetable = sorted(timetable, key = lambda time : (time[0], time[1]))
print(timetable)