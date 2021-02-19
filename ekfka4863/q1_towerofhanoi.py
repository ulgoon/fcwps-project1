'''
하노이의 탑이란? 
- 세 개의 축과 n개의 원반이 주어지는데 각각의 원반은 크기가 상이하다.
- 축은 A,B,C라고 부르기로 하고 원반은 가장 작은 원반을 1로, 가장 큰 원반을 n이라고 번호를 
매긴다고 가정하고... 처음에는 모든 n개의 원반이 크기 순서대로 위에서 아래로, 즉 1이 가장 위에
그리고 n이 가장 아래인 상태로 축 A에 놓여있다고 가정해 봅시다...
- 목표: 모든 n개의 원반을 축 A에서 B로 옮기는 것. 단, 지켜야 될 규칙이 두가지가 있다. 
- 규칙: 
    1. 한 번에 하나의 원반만 움직일 수 있다 
    2. 자신보다 작은 원반이 그 아래에 놓일 수 없다. 예를 들면 원반 3이 축에 있다면 
        원반 3 밑에 있는 원반은 모두 3보다 큰 숫자로 되어있어야 한다 

- 팁: 하노이탑을 옯기려면 원반을 보두 (2의 n승)-1번만큼 옮겨야 한다.
'''

[pseudocode]
# 입력: 옭기려는 원반의 개수 n은 사용자로부터 입력을 받는다 
# 옮길 원반이 현재 끼워져있는 출발기둥은 from_pos
# 원반을 옮겨서 결구 n개의 원반이 크기의 순서대로 도착해야 하는 기둥은 to_pos
# 옮기는 과정에서 중간거점으로 활용하게 될 보조기둥은 aux_pos
# 출력: 사용자가 disk_num을 입ㄹㄱ하여 함수 towerOfHanoi를 실행하면 
#      풀이과정을 출력한다 
# 유의사항: disk_num == 1 이면, 원반 한 개를 그냥 옮기면 된다 


disk_num = input("How tall would you like your tower to be?? Enter number: ")

def towerOfHanoi(disk_num, from_pos, to_pos, aux_pos):
    if disk_num == 1:
        print(from_pos, '-->', to_pos)
        return
    # 원반이 n-1개를 aux_pos로 이동(to_pos를 보조 기둥으로)
    towerOfHanoi(int(disk_num)-1, from_pos, aux_pos, to_pos)
    # 가장 큰 원반을 목적지 기둥으로 이동시킨다 
    print(from_pos, '-->', to_pos)
    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
    towerOfHanoi(int(disk_num)-1, aux_pos, to_pos, from_pos)


print('disk_num = ', disk_num)
towerOfHanoi(disk_num, 1, 3, 2)