def solution(n,a,b):
    answer = 1
    a, b = min(a, b), max(a, b)
    
    if abs(a - b) == 1 and a % 2 != 0 and b % 2 == 0:
        return answer
    
    while n > 2:
        n /= 2
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)        
        answer += 1
        if abs(a - b) == 1 and a % 2 != 0 and b % 2 == 0:
            break
            
    return answer