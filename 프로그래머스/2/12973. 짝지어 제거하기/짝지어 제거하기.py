def solution(s):
    stack = []
    for char in s:
        if stack:
            last_char = stack.pop()
            if last_char != char:
                stack.append(last_char)
                stack.append(char)                
        else:
            stack.append(char)
    return 1 if len(stack) == 0 else 0