from collections import defaultdict

def solution(genres, plays):
    # 각 장르별 총 재생횟수 
    genr_count = defaultdict(int)
    for genr, play in zip(genres, plays):
        genr_count[genr] += play
    genr_count = sorted(genr_count.items(), key=lambda x: x[1], reverse=True)    
    
    # 각 장르별 노래 저장
    genr_list = defaultdict(list)
    for i, (genr, play) in enumerate(zip(genres, plays)):
        genr_list[genr].append([play, i])
        
    # 각 장르별 노래 재생 횟수 오름차순 정렬(pop 할거라)
    for key in genr_list.keys():
        genr_list[key].sort(key=lambda x: (x[0], -x[1]))
    
    answer = []
    # 가장 재생이 많이된 장르부터 시작됨
    for genr, _ in genr_count:
        # 최대 2곡
        for _ in range(2):
            # 1곡만 있을지도
            if genr_list[genr]:
                answer.append(genr_list[genr].pop()[1])    
    return answer