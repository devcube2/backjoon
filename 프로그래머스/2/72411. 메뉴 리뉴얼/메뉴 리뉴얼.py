from collections import Counter
from itertools import combinations, takewhile

def solution(orders, course):
    answer = []
    
    # 코스 주문별 정렬
    orders = [sorted(order) for order in orders]
    
    # 코스별 순회
    for course_count in course:
        # 코스 조합 생성
        courses = []
        for order in orders:
            courses.extend(list(combinations(order, course_count)))
        # 가장 많이 주문된 코스 추출
        courses_count = Counter(courses).most_common()
        most_courses = list(takewhile(lambda x: x[1] == courses_count[0][1], courses_count))
        most_courses = [c[0] for c in most_courses]
        
        for most_course in most_courses:
            # 손님별 2번 이상 주문된 코스만 추가
            count = 0
            for order in orders:
                if set(most_course).issubset(order):
                    count += 1
                if count >= 2:
                    answer.append(''.join(most_course))
                    break
    return sorted(answer)