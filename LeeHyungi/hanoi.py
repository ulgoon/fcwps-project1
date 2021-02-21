def run_hanoi(n, disk_stack, through_stack, to_stack):
    if n > 0:
        # disk_stack에 있는 원반을 through_stack으로 옮겨준다.
        # 큰 원반을 제외한 원반 이동
        run_hanoi(n-1, disk_stack, through_stack, to_stack)
        # 만약에 disk_stack에 원반이 남아있다면
        if disk_stack:
            # 최종적으로 옮길 to_stack에 disk_stack에서 pop한 원반을 넣어준다.
            to_stack.append(disk_stack.pop())
        # 가장 큰 원반을 제외한 원반들을 옮겨 놓은 through_stack에서 to_stack으로 옮겨준다.
        run_hanoi(n-1, through_stack, disk_stack, to_stack)


num_of_disk = int(input('원반의 갯수 입력 : '))
# 입력받은 원반의 수만큼 역순으로 리스트에 담아주기 (원반을 꺼내는 구조가 stack이기 때문에 pop을 이용해서 꺼낸다.)
disk_stack = list(reversed([disk for disk in range(1, num_of_disk+1)]))
# 최종적으로 이동시킬 to_stack을 생성한다.
to_stack = []
# 임시로 큰 원반을 제외한 원반들을 옮길 스택을 생성한다. (through_stack)
through_stack = []
print(f"disk_stack : {disk_stack}")
run_hanoi(len(disk_stack), disk_stack, through_stack, to_stack)
print(f"disk_stack : {disk_stack}")
print(f"through_stack : {through_stack}")
print(f"to_stack : {to_stack}")
