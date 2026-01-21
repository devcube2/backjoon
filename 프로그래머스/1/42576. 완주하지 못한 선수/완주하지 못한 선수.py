def solution(participant, completion):
    dic = {}
    for part in participant:
        dic[part] = dic.get(part, 0) + 1
    for complete in completion:
        dic[complete] -= 1
    for key, value in dic.items():        
        if value >= 1:
            return key    