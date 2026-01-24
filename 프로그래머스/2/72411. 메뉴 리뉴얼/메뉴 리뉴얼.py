from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for course_size in course:
        candidates = []
        # 각 주문별로 가능한 조합을 모두 생성하여 리스트에 담기
        for order in orders:
            # 문자열 정렬 후 조합 생성 (XY와 YX를 같게 취급하기 위해)
            candidates.extend(combinations(sorted(order), course_size))
        
        # 조합이 하나도 없으면 패스 (IndexError 방지)
        if not candidates:
            continue

        # 개수 세기 (Counter가 다 해줍니다!)
        counted = Counter(candidates)
        
        # 가장 많이 주문된 횟수 찾기
        max_count = counted.most_common(1)[0][1]
        
        # 조건: 최소 2명 이상 주문해야 함
        if max_count < 2:
            continue
            
        # 최댓값을 가진 메뉴 구성만 추출 (issubset으로 다시 검사할 필요 없음)
        for key, value in counted.items():
            if value == max_count:
                answer.append(''.join(key))

    return sorted(answer)