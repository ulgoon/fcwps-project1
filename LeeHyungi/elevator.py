from abc import ABCMeta, abstractmethod


class ElevatorAbstract(metaclass=ABCMeta):
    @abstractmethod
    def getIntoElevator(self):
        print("Elevator에 탑승했습니다.")

    @abstractmethod
    def getOffElevator(self):
        print("Elevator에서 승객이 내렸습니다.")

    @abstractmethod
    def getCurrentPassengerInfo(self):
        print("=========================================")
        print("현재 Elevator의 승객정보를 조회합니다.")

    @abstractmethod
    def moveUp(self):
        print("=========================================")
        print("엘리베이터가 위로 운전을 시작합니다.")

    @abstractmethod
    def moveDown(self):
        print("=========================================")
        print("엘리베이터가 아래로 운전을 시작합니다.")


class Elevator(ElevatorAbstract):
    def __init__(self, _num, _src_floor, _dst_floor, _direction):
        # 엘리베이터의 호차 번호 설정
        self.num = _num
        # 엘리베이터의 시작층 설정
        # 엘리베이터의 도착층 설정
        self.src_floor = _src_floor
        self.dst_floor = _dst_floor
        # 엘리베이터의 초기 방향 설정
        self.direction = _direction
        # 현재 엘리베이터 층
        self.current_floor = _src_floor
        # 엘리베이터의 탑승자 리스트
        self.move_up_passenger_list = []
        # 엘리베이터의 탑승자 리스트
        self.move_down_passenger_list = []
        # 누적 이동층수 계산
        self.acc_num_of_move_up_floor = 0
        self.acc_num_of_move_down_floor = 0

    # 탑승자 정보를 리스트에 저장하는 메서드
    def getIntoElevator(self, direction, p):
        super(Elevator, self).getIntoElevator()
        print(f"탑승자는 {p} 입니다.")
        # 탑승자 리스트에 해당 탑승자의 정보를 저장한다.
        if self.direction == "UP":
            self.move_up_passenger_list.append(p)
        else:
            self.move_down_passenger_list.append(p)

    # 탑승할때마다 해당 메서드를 실행시켜서 현재 탑승객 중에서
    def moveUp(self):
        super(Elevator, self).moveUp()
        if self.move_up_passenger_list:
            for p in self.move_up_passenger_list:
                sf, df = p
                # 만약에 현재 도착층보다 탑승객의 출발층이 높다면,
                if self.dst_floor < sf:
                    self.acc_num_of_move_up_floor += (sf - self.dst_floor)
                    self.acc_num_of_move_up_floor += (df - sf)
                    # 엘리베이터의 시작층과 도착층을 업데이트
                    self.src_floor = sf
                    self.dst_floor = df
                    # 탑승객이 내리는 처리를 한다.
                    # self.getOffElevator()
                # 만약의 기존 도착층보다 탑승객의 도착층이 크다면,
                elif self.dst_floor < df:
                    # 새로운 도착층과 기존의 도착층의 차이를 누적 이동층수에 더해준다.
                    self.acc_num_of_move_up_floor += (df - self.dst_floor)
                    # 그리고 도착층 정보를 새롭게 업데이트 해준다.
                    self.dst_floor = df
                    # self.getOffElevator()
                # 기존의 출발층과 도착층 사이에 있는 탑승객이라면 별도의 층수를 누적하지 않는다.
                # else:
                    # self.getOffElevator()

    def moveDown(self):
        super(Elevator, self).moveDown()
        if self.move_down_passenger_list:
            for p in self.move_down_passenger_list:
                sf, df = p
                # 만약에 현재 도착층보다 승객의 도착층이 더 낮은경우
                if self.dst_floor > sf:
                    self.acc_num_of_move_down_floor += (self.dst_floor - sf)
                    self.acc_num_of_move_down_floor += (sf - df)
                    # 엘리베이터의 시작층과 도착층을 업데이트
                    self.src_floor = sf
                    self.dst_floor = df
                    # 탑승객이 내리는 처리를 한다.
                    # self.getOffElevator()
                # 만약에 기존 도착층보다 탑승객의 도착층이 더 작다면,
                elif self.dst_floor > df:
                    self.acc_num_of_move_down_floor += (self.dst_floor - df)
                    # 도착층의 정보를 새롭게 업데이트 해준다.
                    self.dst_floor = df
                    # 탑승객이 내리는 처리를 한다.
                    # self.getOffElevator()
                # 기존의 출발층과 도착층 사이에 있는 탑승객이라면 별도의 층수를 누적하지 않는다.
                # else:
                    # self.getOffElevator()

                    # 현재 층이 올라갈때마다 메서드를 확인해서 탑승자가 내리도록 처리한다.
                    # 엘리베이터 탑승객 중에서 현재층이 도착층인 사람이 내리도록 하는 메서드

    def getOffElevator(self):
        super(Elevator, self).getOffElevator()
        # 엘리베이터의 탑승자가 있는지 검사
        passenger_list = self.move_up_passenger_list if self.direction == "UP" else self.move_down_passenger_list
        if passenger_list:
            # 엘리베이터 탑승자 중에 도착층이 현재 시작층과 도착층의 사이에 있다면 사람 확인
            p = [passenger_list(
                t) for t in passenger_list if t[1] in range(self.src_floor, self.dst_floor)]
            for idx in p:
                # 엘리베이터에서 내린다.
                print(f"내리는 탑승자는 {passenger_list[idx]} 입니다.")
                passenger_list.pop(idx)

    def setDirection(self, _direction):
        self.direction = _direction

    def getDirection(self):
        return self.direction

    def getSrcDstFloorInfo(self):
        return (self.src_floor, self.dst_floor)

    # 현재 엘리베이터의 정보를 출력하는 메서드
    def getCurrentPassengerInfo(self):
        super(Elevator, self).getCurrentPassengerInfo()
        print(f"현재 {self.num}호 엘리베이터의 시작층은 {self.src_floor} 입니다.")
        print(f"현재 {self.num}호 엘리베이터의 도착층은 {self.dst_floor} 입니다.")
        print(f"현재 {self.num}호 엘리베이터의 이동방향은 {self.direction} 입니다.")
        acc_floor_num = self.acc_num_of_move_up_floor + self.acc_num_of_move_down_floor
        print(f"현재 {self.num}호 엘리베이터의 누적층수는 { acc_floor_num } 입니다.")
        print("=========================================")

# 엘리베이터의 공통 처리 과정을 메서드화


def elevatorCommon(elevator, passenger):
    fd = "UP" if passenger in go_up_p else "DOWN"
    elevator.setDirection(fd)
    elevator.getIntoElevator(fd, passenger)
    elevator.moveUp() if fd == "UP" else elevator.moveDown()
    elevator.getCurrentPassengerInfo()

# 1호차, 2호차의 객체를 전달받는다.
# 1호차, 2호차 엘리베이터 객체의 현재 상태를 확인해서 다음 승객이 탑승할 엘리베이터를 선택한다.


def CommonFunc(f_elevator, s_elevator):
    # 1번 엘리베이터와 2번 엘리베이터의 도착지점[1]과 다음 탑승 승객의 출발 위치와 가까운 엘리베이터 작동
    f_src_floor, f_dst_floor = f_elevator.getSrcDstFloorInfo()
    s_src_floor, s_dst_floor = s_elevator.getSrcDstFloorInfo()

    p = passengers.pop(0)
    # 다음 승객의 출발하는 위치와 가까운 엘레베이터를 운행합니다.
    s = min([f_dst_floor, s_dst_floor], key=lambda x: abs(x - p[0]))

    if s == f_dst_floor:
        print("1호차가 운행을 시작합니다.")
        elevatorCommon(f_elevator, p)
        # 운행한 후에 시작 층과 도착층의 층수가 바뀌었을 경우
        f_src_floor, f_dst_floor = f_elevator.getSrcDstFloorInfo()
        # 나머지 승객들 중에서 현재 엘리베이터와 같은 방향이고 시작층이 기존 1호 엘리베이터의 시작과 끝 층 사이라면,
        # 동승 승객 수
        fcp = 0
        for idx, passenger in enumerate(passengers):
            d = "UP" if passenger in go_up_p else "DOWN"
            # 만약 운행 방향이 엘리베이터와 일치하면서 시작층이 f_src_floor~f_dst_floor 사이라면,
            if f_elevator.getDirection() == d and passenger[0] in range(f_src_floor, f_dst_floor):
                # 동승 승객을 passengers 리스트에서 뽑아내고 공통 엘리베이터 동작 메서드를 실행시켜준다.
                passengers.pop(idx)
                fcp += 1
                # 동승 승객 정보 출력
                print(f"동승 승객은 총 {fcp}명 입니다.")
                elevatorCommon(f_elevator, passenger)
    elif s == s_dst_floor:
        print("2호차가 운행을 시작합니다.")
        elevatorCommon(s_elevator, p)
        # 운행한 후에 시작 층과 도착층의 층수가 바뀌었을 경우
        s_src_floor, s_dst_floor = s_elevator.getSrcDstFloorInfo()
        # 동승 승객 수
        scp = 0
        for idx, passenger in enumerate(passengers):
            d = "UP" if passenger in go_up_p else "DOWN"
            # 만약 운행 방향이 엘리베이터와 일치하면서 시작층이 s_src_floor~s_dst_floor 사이라면,
            if s_elevator.getDirection() == d and passenger[0] in range(s_src_floor, s_dst_floor):
                passengers.pop(idx)
                scp += 1
                # 동승 승객 정보 출력
                print(f"동승 승객은 총 {scp}명 입니다.")
                elevatorCommon(s_elevator, passenger)


# 탑승자의 정보
passengers = [(6, 12), (4, 13), (11, 3), (9, 2), (11, 12), (3, 9), (14, 8), (1, 7), (11, 9), (14, 16), (2, 15), (2, 9), (8, 16), (8, 9), (3, 10), (5, 4), (13, 9), (4, 6), (13, 7), (4, 8), (5, 3), (12, 14), (10, 13), (6, 12), (1, 7),
              (9, 2), (13, 11), (1, 14), (11, 8), (15, 12), (3, 15), (10, 3), (4, 1), (7, 1), (15, 8), (10, 16), (9, 3), (14, 13), (8, 13), (16, 9), (10, 7), (1, 6), (16, 13), (5, 3), (1, 12), (1, 7), (12, 3), (13, 6), (12, 15), (15, 6)]
print(f"초기 엘리베이터 탑승객의 수는 {len(passengers)} 입니다.")
# 올라가는 승객 리스트
go_up_p = [p for p in passengers if p[0] - p[1] < 0]
# 내려가는 승객 리스트
go_down_p = [p for p in passengers if p[0] - p[1] > 0]


# 1호, 2호 엘리베이터 초기화
# 엘리베이터의 초기 설정은 시작, 도착층을 1층으로 초기화하고,
# 올라가는 것을 처음 방향으로 설정한다.
f_elevator = Elevator(1, 1, 1, "UP")
s_elevator = Elevator(2, 1, 1, "UP")

# 우선 각 각의 엘리베이터에 첫 탑승자를 탑승시킨다.
# 1호 엘리베이터에는 passengers리스트의 첫 번째 탑승객을 탑승
# 2호 엘리베이터에는 passengers리스트의 두 번째 탑승객을 탑승
passenger = passengers.pop(0)
print(passenger)
elevatorCommon(f_elevator, passenger)

passenger = passengers.pop(0)
print(passenger)
elevatorCommon(s_elevator, passenger)

while len(passengers) > 0:
    CommonFunc(f_elevator, s_elevator)


print(f"현재 엘리베이터에 남은 승객의 수는 {len(passengers)} 입니다.")
