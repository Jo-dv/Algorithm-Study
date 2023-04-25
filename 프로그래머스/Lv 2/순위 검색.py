'''
def solution(info, query):
    answer = []
    qs = []
    count = 0

    for i in query:
        i = i.replace('and', '')
        x = i.split()
        qs.append(x)

    for i in qs:
        for j in info:
            x = j.split()
            if (x[0] == i[0] or i[0] == '-') and (x[1] == i[1] or i[1] == '-') and (x[2] == i[2] or i[2] == '-') and \
                    (x[3] == i[3] or i[3] == '-') and (int(x[4]) >= int(i[4]) or i[4] == '-'):
                count += 1
        answer.append(count)
        count = 0

    return answer
'''
from collections import defaultdict
from itertools import combinations

def bin_search(x, target):
    lower, upper = 0, len(x) - 1

    while lower <= upper:  # target 이상의 값이 시작되는 최소 지점을 탐색
        mid = (lower + upper) // 2  # 값 자체를 계산하고
        if x[mid] < target:   # 해당 부분에서 index() 함수를 써버리면 O(n) ~ O(n log n)가 되므로 인덱스를 계산해서 값으로 비교함
            lower = mid + 1
        else:
            upper = mid - 1  # target 이상의 수가 몇 개인지 확인하는 것이므로 x[mid] >= target인 지점부터 마지막까지 target보다 큰 값임

    return lower

def solution(info, query):
    answer = []
    data, qs = defaultdict(list), []

    for i in info:
        x = i.split()  # 정보와 점수를 분리
        info_key, info_val = x[:-1], int(x[-1])
        for j in range(5):  # 네 가지 정보에 대해 경우의 수(=정보가 없는, 즉 - 인 상황도 고려)
            for k in combinations(info_key, j):  # 정보가 0, 정보가 1, 정보가 2, 정보가 3, 정보가 4
                data[''.join(k)].append(info_val)  # 경우의 수를 하나의 문자열로 바꾸고 키로하여 점수를 저장
                
    for i in data.values():
        i.sort()  # 탐색을 위해 정렬

    for i in query:  # 쿼리에서 불필요한 정보를 제거
        i = i.replace('-', '')
        i = i.replace('and', '')
        x = i.split()  # 키와 값으로 사용할 데이터 분리
        qs.append([''.join(x[:-1]), int(x[-1])])

    for i in qs:  # 쿼리를 하나씩 가져와서
        if i[0] in data:  # 일치하는 지원자 정보에 해당한다면
            result = bin_search(data[i[0]], i[-1])  # 이진 탐색을 통해 값의 위치 탐색
            answer.append(len(data[i[0]]) - result)  # 전체 길이 - 위치 = 타겟 이상인 사람의 수
        else:
            answer.append(0)  # 일치하는 지원자 정보가 없을 경우

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info, query))
