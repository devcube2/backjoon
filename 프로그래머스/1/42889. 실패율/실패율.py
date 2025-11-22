def solution(N, stages):
    stage_result = []
    for stage_no in range(1, N + 1):
        # 스테이지 도전했으나 실패한 사람 수
        holder_count = stages.count(stage_no)
        # 스테이지에 도전한 모든 사람의 수
        challenger_count = len([stage for stage in stages if stage >= stage_no])
        # 스테이지와 해당 스테이지의 실패율 저장
        if challenger_count == 0:
            stage_result.append((stage_no, 0))
        else:
            stage_result.append((stage_no, holder_count / challenger_count))
    # 실패율 오름차순 정렬하고, 동일한 실패율 스페이지는 내림차순 정렬
    stage_result.sort(key=lambda item: (-item[1], item[0]))
    return [result[0] for result in stage_result]