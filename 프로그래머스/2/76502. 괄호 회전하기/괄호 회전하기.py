from collections import deque

def is_balanced(s):
    pairs = {'[': ']', '(': ')', '{': '}'}
    stack = []    
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return 0
    return 1 if len(stack) == 0 else 0

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        s.rotate(-1)
        answer += is_balanced(s)
    return answer