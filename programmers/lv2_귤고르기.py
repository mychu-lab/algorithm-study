def solution(k, tangerine):
    answer = 0 # 상자 속 귤 종류
    n = k # 더 담아야하는 귤 개수
    tangerine_cnt = { id: 0 for id in tangerine} # 귤 종류별 개수 초기화
    for i in tangerine :
        tangerine_cnt[i] = tangerine_cnt[i] + 1 # 귤 종류별 개수 저장

    while n > 0 :
        tmp_max = max(tangerine_cnt.values())
        tmp_tangerine = [k for k,v in tangerine_cnt.items() if tmp_max == v]
        for i in tmp_tangerine:
            tangerine_cnt.pop(i)
            n = n - tmp_max
            answer = answer + 1
            if n <= 0 : break;
    return answer