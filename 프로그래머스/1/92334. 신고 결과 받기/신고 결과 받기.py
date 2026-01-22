from collections import defaultdict

def solution(id_list, report, k):
    # ID별 신고한 ID 저장
    report_map = defaultdict(set)
    for r in report:
        report_id, reported_id = r.split()
        report_map[report_id].add(reported_id)
    # print(report_map.items())
    
    # ID별 신고된 횟수 저장
    reported_id_count_map = defaultdict(int)
    for values in report_map.values():
        for reported_id in values:
            reported_id_count_map[reported_id] += 1
    # print(reported_id_count_map.items())
    
    # 차단할 ID 결정
    black_list = []
    for reported_id, reported_count in reported_id_count_map.items():
        if reported_count >= k:
            black_list.append(reported_id)
    # print(black_list)
    
    # ID별 신고한 ID 리스트와 차단할 ID 리스트 기반으로 카운팅
    answer = [0] * len(id_list)
    for report_id, reported_id in report_map.items():
        for black_id in black_list:
            if black_id in reported_id:
                answer[id_list.index(report_id)] += 1
    return answer