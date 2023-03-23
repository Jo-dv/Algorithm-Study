from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)  # 반복할 때마다 sum 연산하는 것을 방지하기 위해 기준 값 우선 계산

    for _ in range(len(queue1)*4):  # 한 큐에서 원소를 하나씩 빼고 넣는 작업을 원래 큐의 길이의 4배만큼 반복하면 원래의 큐로 돌아온다.
        if q1_sum == q2_sum:  # 두 큐의 합이 같다면
            break
        if q1_sum < q2_sum:  # 한 쪽 큐의 합이 작다면 큰쪽에서 빼고 작은 쪽으로 추가
            queue1.append(queue2.popleft())
            q2_sum -= queue1[-1]
            q1_sum += queue1[-1]
        else:
            queue2.append(queue1.popleft())
            q1_sum -= queue2[-1]
            q2_sum += queue2[-1]
        answer += 1
    else:  # 원래의 큐로 돌아왔다는 의미는 무한루프, 즉 합을 같게 만들지 못한다는 의미이므로
        answer = -1

    return answer


queue1, queue2 = [1, 2, 1, 2], [1, 10, 1, 2]
print(solution(queue1, queue2))