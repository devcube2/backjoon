from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    want_dic = {w: n for w, n in zip(want, number)}
    
    for i in range(len(discount) - 9):
        discount_dic = defaultdict(int)
        for j in range(10):
            discount_dic[discount[i + j]] += 1
        if want_dic == discount_dic:
            answer += 1
            
    return answer