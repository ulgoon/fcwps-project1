def tower_of_hanoi(n, start, end, via):
    if n == 1:
        end.append(start.pop())
        print(a, b, c)
    else:
        tower_of_hanoi(n-1, start, via, end)
        end.append(start.pop())
        print(a, b, c)
        tower_of_hanoi(n-1, via, end, start)

num_disks = int(input("Number of disks: "))
a = [i for i in range(1, num_disks + 1)][::-1] # 입력 받은 수 만큼 리스트에 역순으로 추가
b = []
c = []

if __name__ == "__main__":
    print(f"start: {a}, {b}, {c}")
    tower_of_hanoi(num_disks, a, c, b)
    print(f"counts: {2**num_disks - 1}")
