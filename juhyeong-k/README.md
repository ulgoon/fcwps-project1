# Mini project

## 공통 과제

### Requirements
1. 엘리베이터 객체는 추상클래스의 상속으로 생성되어야 한다.
2. 각 객체는 운행 층수를 기록하는 total_move라는 인스턴스 변수를 가진다.
3. 엘리베이터는 2호기로 운영되며, Elevator_1, Elevator_2의 이름을 가진다.
4. 엘리베이터의 이동은 실시간이 아닌 턴 기반으로 이루어진다.
5. 운행 중 동일한 방향으로 이동하는 승객을 태울 수 있다.
6. 다음 번째의 승객이 같은 층에 있고, 같은 방향으로 진행할 경우 동승할 수 있다.
7. 각 엘리베이터의 운행 층수를 total_move에 누적해야 한다.
8. 엘리베이터는 1층 부터 16층 까지 운행한다.

### Elevator System
1. Elevator_1은 올라가는 승객을 태우는 엘리베이터, Elevator_2는 내려가는 승객을 태우는 엘리베이터라고 한다.
2. Elevator_1과 Elevator_2는 1층에서 출발한다고 가정한다.
3. 승객 10명을 기준으로 한 턴이라고 가정하고, 승객 10명 중 올라가는 승객과 내려가는 승객을 나눈다.

4. 올라가는 승객 중 가장 낮은 층에서 탑승하는 승객의 층과 가장 높은 층에서 내리는 승객의 층을 구한다.
6. 올라가는 승객 중 가장 낮은 층으로 Elevator_1이 이동하고 이동한 층을 Elevator_1의 total_move에 누적한다.
7. 올라가는 승객 중 가장 높은 층으로 Elevator_1이 이동하고 이동한 층을 Elevator_1의 total_move에 누적한다.

5. 내려가는 승객 중 가장 높은 층에서 탑승하는 승객의 층과 가장 낮은 층에서 내리는 승객의 층을 구한다.
8. 내려가는 승객 중 가장 높은 층으로 Elevator_2가 이동하고 이동한 층을 Elevator_2의 total_move에  누적한다.
9. 내려가는 승객 중 가장 낮은 층으로 Elevator_2가 이동하고 이동한 층을 Elevator_2의 total_move에  누적한다.

10. 3번~9번 과정을 승객이 없을 때 까지 반복하고, Elevator_1과 Elevator_2의 total_move의 합을 출력하고 종료한다.


### 실행 결과
```
up_passengers: [(6, 12), (4, 13), (11, 12), (3, 9), (1, 7), (14, 16)]
start: 1 end: 16
move to passenger: current:1->passenger:1
move_counts: 15, current_floor: 16
-
down_passengers: [(11, 3), (9, 2), (14, 8), (11, 9)]
start: 14 end: 2
move to passenger: currnet:1->passenger:14
move_counts: 25, current_floor: 2
...
...
...
up_passengers: [(1, 6), (1, 12), (1, 7), (12, 15)]
start: 1 end: 15
move to passenger: current:16->passenger:1
move_counts: 124, current_floor: 15
-
down_passengers: [(10, 7), (16, 13), (5, 3), (12, 3), (13, 6), (15, 6)]
start: 16 end: 3
move to passenger: currnet:1->passenger:16
move_counts: 126, current_floor: 3


elevator's total move: 250

```

## 선택 과제

### 하노이 타워
https://en.wikipedia.org/wiki/Tower_of_Hanoi

A, B, C막대 중 A막대에 쌓여있는 원반들을 C막대로 옮겨야 한다.
- 한 번에 한 개의 원반만 움직일 수 있다.
- 어떤 원반 위의 그 보다 큰 원반이 올라갈 수 없다.

ex) A에 쌓여있는 `[3, 2, 1] [] []` 3개의 원반을 C로 옮겨라.(`[A] [B] [C]`)
1. `[3] [2, 1] []` 3을 제외한 원반들이 B로 옮겨져야
2. `[] [2, 1] [3]` A에 있는 `[3]`을 C로 옮길 수 있고
3. `[] [] [3, 2, 1]` B 에 있는 원반들을 C로 옮기면 된다.
---
4. `[2, 1] [] []`을 옮기려면 `[1]`을 B로 옮기고
5. `[2] [1] []` A에 있는 `[2]`를 C로 옮기고
6. `[] [1] [2]` B에 있는 `[1]`을 C로 옮기면
7. `[] [] [2, 1]`
---
8. `[1] [] []` 을 옮기려면 `[1]`을 C로 옮기면 된다.
9. `[] [] [1]`

결국 N-1개의 원반들을 B로 옮기고 (A->B)<br>
N번 째 원반을 C로 옮기고 (A->C)<br>
N-1개의 원반들을 C로 옮기는 과정을 반복한다. (B->C)<br>
재귀함수를 이용하고 한번에 하나씩 옮기는 조건을 추가하면

```python
def hanoi(n, A, C, B):
    if n == 1:
        print("A의 원반 하나를 C로 옮긴다.")
    else:
        hanoi(n-1, A, B, C) # A->B
        print(f"{N}번 째 원반을 C로 이동")  # A->C
        hanoi(n-1, B, C, A) # B->C
```

### 코드를 정리해서 towerofhanoi.py에 추가

실행 결과:
```
Number of disks: 5
start: [5, 4, 3, 2, 1], [], []
[5, 4, 3, 2] [] [1]
[5, 4, 3] [2] [1]
[5, 4, 3] [2, 1] []
[5, 4] [2, 1] [3]
[5, 4, 1] [2] [3]
...
...
...
[1] [2] [5, 4, 3]
[1] [] [5, 4, 3, 2]
[] [] [5, 4, 3, 2, 1]
counts: 31
```
