a, b = input(), input()

lb = [int(n) * int(a) for n in b[::-1]]
for n in lb:
    print(n)
print(int(a) * int(b))