from collections import defaultdict

def solution(genres, plays):
    # 1. 장르별 총 재생 횟수 및 곡 정보 수집
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] += p
        genre_songs[g].append((p, i)) # 튜플로 저장
        
    # 2. 많이 재생된 장르 순서대로 정렬
    sorted_genres = sorted(genre_total.keys(), key=lambda g: genre_total[g], reverse=True)
    
    answer = []
    # 3. 각 장르 내에서 베스트 곡 선정
    for g in sorted_genres:
        # 재생 횟수 내림차순, 인덱스 오름차순으로 정렬
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))
        # 최대 2곡 추출
        answer.extend([idx for _, idx in songs[:2]])
        
    return answer