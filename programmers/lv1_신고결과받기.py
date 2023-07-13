def solution(id_list, report, k):
    reported_dic = {id:0 for id in id_list} #해당id가 신고당한 횟수
    reporter_dic = {id:[] for id in id_list} #해당id가 신고한놈 리스트
    blacklist = []
    answer = []
    kk = k
    for re in report:
        temptx = re.split(' ')
        reporter = temptx[0]
        reported = temptx[1]

        i = 0
        for r in reporter_dic[reporter]:
            if r == reported :
                i = i + 1
        if i == 0 :
            reporter_dic[reporter].append(reported)
            reported_dic[reported] = reported_dic[reported] + 1

    for keys in reported_dic.keys():
        if reported_dic[keys] >= kk :
            blacklist.append(keys)

    for keys in reporter_dic.keys():
        n = 0
        for kkk in reporter_dic[keys] :
            if kkk in blacklist :
                n = n + 1
        answer.append(n)

    return answer