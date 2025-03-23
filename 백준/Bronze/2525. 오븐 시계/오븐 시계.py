import sys

input = sys.stdin.readline

hour, minute = map(int, input().split())
pass_minute = int(input())

q, minute = divmod(minute + pass_minute % 60, 60)
hour += pass_minute // 60 + q
hour %= 24

print(hour, minute)
