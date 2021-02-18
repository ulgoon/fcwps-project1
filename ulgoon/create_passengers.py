import random


def create_passengers(lowest, highest, num):
    def set_passenger(a, b):
        passenger = (random.randint(a, b), random.randint(a, b))
        if passenger[0]!=passenger[1]:
            return passenger
        else:
            return set_passenger(a,b)
    return [set_passenger(lowest, highest) for _ in range(num)]

if __name__=='__main__':
    print(create_passengers(1,16,50))
