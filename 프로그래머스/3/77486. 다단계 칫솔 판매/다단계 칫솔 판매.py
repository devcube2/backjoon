def solution(enroll, referral, seller, amount):
    # 이름별 이익량
    benefits = dict.fromkeys(enroll, 0)
    # 이름별 추천인
    enroll_referral = {e: r for e, r in zip(enroll, referral)}    
    
    for s, a in zip(seller, amount):
        # 본인 이익 계산
        benefit_to_upstair = a * 100 // 10
        benefit_to_mine = a * 100 - benefit_to_upstair
        benefits[s] += benefit_to_mine
        # 추천인 타면서 이익 계산
        while enroll_referral[s] != "-" and benefit_to_upstair > 0:
            # 아랫 사람에게 전달받은 이익 중 내가 받을 이익
            benefit_to_mine = benefit_to_upstair - (benefit_to_upstair // 10)
            # 아랫 사람에게 전달받은 이익 중 다시 윗사람에게 줄 이익
            benefit_to_upstair = benefit_to_upstair // 10
            # 추천인의 추천인 찾기 위해 변경
            s = enroll_referral[s]
            # 추천인 이익 계산
            benefits[s] += benefit_to_mine
            
    return list(benefits.values())