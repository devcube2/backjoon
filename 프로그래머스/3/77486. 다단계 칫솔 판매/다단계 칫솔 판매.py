def solution(enroll, referral, seller, amount):
    # 이름별 이익량 (순서 보장)
    benefits = dict.fromkeys(enroll, 0)
    # 이름별 추천인
    enroll_referral = {e: r for e, r in zip(enroll, referral)}    
    
    for s, a in zip(seller, amount):
        current_money = a * 100  # 현재 발생한 총 매출액
        current_person = s
        
        while current_person != "-" and current_money > 0:
            up_money = current_money // 10      # 윗사람에게 줄 10%
            mine_money = current_money - up_money # 내가 가질 90%
            
            benefits[current_person] += mine_money
            
            # 다음 위로 이동
            current_person = enroll_referral[current_person]
            current_money = up_money # 이제 윗사람이 처리할 돈은 10%가 됨
            
    return list(benefits.values())
