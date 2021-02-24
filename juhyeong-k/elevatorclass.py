from abc import ABC, abstractmethod


class Elevators(ABC):
    
    def __init__(self, current_floor):
        self.current_floor = current_floor
        # 엘리베이터 현재 층
        self.move_counts = 0
        # 엘리베이터 누적 층 수

    @abstractmethod
    def get_min_max(self):
        pass

    @abstractmethod
    def move(self, direction):
        pass

    @abstractmethod
    def move_to_passenger(self, direction):
        pass

class Elevator(Elevators):
    
    def __init__(self,current_floor=1):
        super().__init__(current_floor)
        self.passengers = passengers
        # 엘리베이터를 이용하는 승객

        
    def get_min_max(self, passengers):
        """
        올라가고 내려가는 승객들 중 최소 층과 최대 층을 구한다
        """
        in_f = []
        out_f = []
        for a, b in passengers:
            in_f.append(a)
            out_f.append(b)
        if a > b:
            self.in_floor = max(in_f)
            self.out_floor = min(out_f)
            print(f"start: {self.in_floor} end: {self.out_floor}")  
        else:
            self.in_floor = min(in_f)
            self.out_floor = max(out_f)
            print(f"start: {self.in_floor} end: {self.out_floor}")  

    def move(self, direction):
        """
        올라가거나 내려가는 엘리베이터가 승객의 층까지 이동한 층들을 move_counts에 누적
        """
        self.move_counts += abs(self.out_floor - self.in_floor)
        self.current_floor = self.out_floor
        print(f"{direction} - move_counts: {self.move_counts}, current_floor: {self.current_floor}")

    def move_to_passenger(self, direction):
        """
        올라가거나 내려가는 엘리베이터가 승객의 층까지 이동한 층들을 move_counts에 누적
        """
        self.move_counts += abs(self.current_floor - self.in_floor)        
        print(f"{direction} - move to passenger: currnet:{self.current_floor}->passenger:{self.in_floor}")


# 엘리베이터 구현
passengers = [(6, 12), (4, 13), (11, 3), (9, 2), (11, 12), (3, 9), (14, 8), (1, 7), (11, 9), (14, 16), (2, 15), (2, 9), (8, 16), (8, 9), (3, 10), (5, 4), (13, 9), (4, 6), (13, 7), (4, 8), (5, 3), (12, 14), (10, 13), (6, 12), (1, 7), (9, 2), (13, 11), (1, 14), (11, 8), (15, 12), (3, 15), (10, 3), (4, 1), (7, 1), (15, 8), (10, 16), (9, 3), (14, 13), (8, 13), (16, 9), (10, 7), (1, 6), (16, 13), (5, 3), (1, 12), (1, 7), (12, 3), (13, 6), (12, 15), (15, 6)]

Elevator_1 = Elevator()
Elevator_2 = Elevator()

while len(passengers) > 0:
    up_passengers = [person for person in passengers[:10] if person[0] < person[1]]
    down_passengers = [person for person in passengers[:10] if person[0] > person[1]]
    print(f"up_passengers: {up_passengers}")
    Elevator_1.get_min_max(up_passengers)
    Elevator_1.move_to_passenger('up')
    Elevator_1.move('up')
    print("-")
    print(f"down_passengers: {down_passengers}")
    Elevator_2.get_min_max(down_passengers)
    Elevator_2.move_to_passenger('down')
    Elevator_2.move('down')
    print("\n")
    passengers = passengers[10:]
print(f"elevator's total move: {Elevator_1.move_counts + Elevator_2.move_counts}")
