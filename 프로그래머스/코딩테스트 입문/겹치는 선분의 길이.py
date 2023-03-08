lines = [[0, 5], [3, 9], [1, 10]]

def solution(lines):
    A, B, C = [set(range(i[0], i[1])) for i in lines]  # 주어진 범위의 값을 가진 집합들을 생성
    return len((A & B) | (B & C) | (A & C))
    # 겹치는 부분은 교집합으로, 겹치는 모든 부분은 합집합으로 표현 가능, 집합을 사용했기에 겹칩으로 발생하는 중복은 제거됨

print(solution(lines))
