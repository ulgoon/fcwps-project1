def Hanoi_tower(disk_num, first, third, seccond):
    # recursion 함수로 disk_num이 1이 될때까지 반복
    if disk_num == 1:
        print('{}번 원반을 {}에서 {}로 이동'.format(1, first, third))
    else:
        # 시작점과 이동점, 도착점위치를 받는 위치 변경으로 변경
        Hanoi_tower(disk_num-1,first,seccond,third)
        print('{}번 원반을 {}에서 {}로 이동'.format(disk_num, first, third))
        Hanoi_tower(disk_num-1,seccond,third,first)

Hanoi_tower(3, 'First', 'Third', 'Seccond')
     # 원반갯수 , 시작점, 도착점, 이동점

