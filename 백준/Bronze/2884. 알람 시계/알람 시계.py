hour, minute = map(int, input().split())

if hour == 0:
    hour = 24

if minute - 45 < 0:
    hour -= 1
    minute += 15 # 60 - 45
else:
    minute -= 45

if hour == 24:
    hour = 0

print(hour, minute)