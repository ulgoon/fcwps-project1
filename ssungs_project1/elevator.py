from abc import ABCMeta, abstractmethod

class Total_move(metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def Move(self):
        self.current_f += self.direction
        self.total_move += 1
        print('{}가 {}층에서 {}층으로 이동, 목표층: {}층'.format(self.name,self.current_f-self.direction,self.current_f,self.dest_f))
        print('{}의 총 이동 층수는: {}층 입니다.'.format(self.name, self.total_move))
        if self.state == 'force_move':
            if self.current_f == self.dest_f:
                self.state = 'move'
class Elevator(Total_move):
    def __init__(self, name):
        super(Elevator, self).__init__(name)
        self.current_f = 6    # 시작층
        self.dest_f = 1       # 도착층
        self.direction = 1    # 운행방향 1='UP', -1='DOWN'
        self.total_move = 0   # 총 운행층수
        self.passenger_dict = {i: [] for i in range(1, 17)}
        self.state = 'stop'   # 현재 운행상태
        self.min_floor = 1    # 최저층
        self.max_floor = 16   # 최고층
    def Move(self):
        super(Elevator, self).Move()

    def Force_move(self, floor):
        self.state = 'force_move'
        self.dest_f = floor
        if self.current_f < self.dest_f:
            self.direction = 1
        else:
            self.direction = -1
    def Get_in(self, passenger):
        self.passenger_dict[passenger[1]].append(passenger)
    def Get_out(self):
        get_out_list = self.passenger_dict[self.current_f]
        self.passenger_dict[self.current_f] = []
        print('{}: {}층에서 {} 하차.'.format(self.name,self.current_f,get_out_list))
        print('{}의 총 이동 층수는: {}층 입니다.'.format(self.name, self.total_move))
    def Set_direction(self, distributor):
        if abs(self.current_f + self.direction) > self.max_floor or abs(self.current_f + self.direction) < self.min_floor:
            self.direction = -self.direction
        else:  
            # 목적지에 도착하지 않은 경우
            if self.direction * self.current_f < self.direction * self.dest_f: 
                return
            # 목적지에 도착한 경우
            else:   
                # 동일한 방향으로 진행했을 때 태울 사람이 남아 있으면 방향을 변경하지 않음
                for direction, floors in distributor.passengers_dict.items():
                    for floor, passenger_list in floors.items():
                        if self.direction * self.current_f < self.direction * floor:
                            return
                self.direction = -self.direction
    def Check_passenger(self, distributor):
        if self.state != 'force_move':
            self.state = 'move'
            # 내려야 할 사람 내려줌
            if len(self.passenger_dict[self.current_f]) != 0:
                self.Get_out()
                self.state = 'stop'
            # 탈 사람 있으면 태움
            if (self.direction == 1 and self.current_f == self.max_floor) or (self.direction == -1 and self.current_f == self.min_floor):
                self.direction = -self.direction
            passenger_list = distributor.passengers_dict[self.direction][self.current_f]
            if len(passenger_list) != 0:
                distributor.Del_floor(self.direction, self.current_f)
                get_in_list = []
                for p in passenger_list:
                    get_in_list.append(p)
                    self.Get_in(p)
                    self.state = 'stop'
                    if self.direction * self.dest_f < self.direction * p[1]:  # 목적지 갱신
                        self.dest_f = p[1]
                print('{}: {}층에서 {}층에서 탑승, 목표층: {}층'.format(self.name,self.current_f,get_in_list,self.dest_f))
                print('총 이동 층수는: {}층 입니다.'.format(self.total_move))
    def Check_state(self):
        for _,passenger_list in self.passenger_dict.items():
            if len(passenger_list) != 0:
                return True
        return False
    def Turn(self, distributor):
        # 승객이 내리거나 탑승하는 경우 또는 엘리베이터가 1층 움직이는 것을 1 turn으로 본다.       
        self.Check_passenger(distributor)
        if self.state == 'move':
            self.Set_direction(distributor)
            self.Move()
        elif self.state == 'force_move':
            self.Move()
class Distributor:
    def __init__(self, passengers):
        self.passengers_dict = {1: {f: [] for f in range(1, 17)}, -1: {f: [] for f in range(1, 17)}}
        for p in passengers:
            self.passengers_dict[1 if p[0] < p[1] else -1][p[0]].append(p)
    def Del_floor(self, direction, floor):
        self.passengers_dict[direction][floor] = []
    def Check_passengers(self):
        for direction, floors in self.passengers_dict.items():
            for floor, passenger_list in floors.items():
                if passenger_list != []:
                    return True  # 승객이 남아있으면 True
        return False  # 남은 승객이 없으면 False
    def Turn(self, elevators):
        for elevator in elevators:
            elevator.Turn(self)
def Check_state(distributor, elevators):
    state = []
    state.append(distributor.Check_passengers())
    remove_list = []
    for i, Elevator in enumerate(elevators):
        state.append(Elevator.Check_state())
        if not state[0] and not state[-1]:
            remove_list.append(i)
    [elevators.pop(i) for i in remove_list[::-1]]
    return any(state)
passengers = [(6, 12), (4, 13), (11, 3), (9, 2), (11, 12), (3, 9), (14, 8), (1, 7), (11, 9), (14, 16), (2, 15), (2, 9), (8, 16), (8, 9), (3, 10), (5, 4), (13, 9), (4, 6), (13, 7), (4, 8), (5, 3), (12, 14), (10, 13), (6, 12), (1, 7), (9, 2), (13, 11), (1, 14), (11, 8), (15, 12), (3, 15), (10, 3), (4, 1), (7, 1), (15, 8), (10, 16), (9, 3), (14, 13), (8, 13), (16, 9), (10, 7), (1, 6), (16, 13), (5, 3), (1, 12), (1, 7), (12, 3), (13, 6), (12, 15), (15, 6)]
distributor = Distributor(passengers)
elevators = [Elevator('1호기'), Elevator('2호기')]
i = 0
while True:
    if not Check_state(distributor, elevators):
        break
    if i == 0:
        elevators[1].Force_move(4) # 2호기의 처음 도착층 설정
    print('\n{} turn'.format(i))   # 턴을 출력
    distributor.Turn(elevators)
    i += 1

