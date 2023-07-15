def solution(s):
    answer = []
    number = list(s)
    k = 0 #이진 변환의 횟수
    z = 0 #변환 과정에서 제거된 0 갯수
    t = number  # 이진 변환 이전
    len_z = len(t)
    while len_z > 1 :
        del_z = 0  # 제거할 0 의 개수
        for i in reversed(list(t)):
            if i == '0' :
                del_z = del_z + 1
        len_z = len(t) - del_z
        z = z + del_z
        k = k + 1
        t = "{0:b}".format(len_z)

    answer.append(k)
    answer.append(z)
    return answer