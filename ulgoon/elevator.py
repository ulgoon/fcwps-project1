from abc import ABCMeta


# Create elevator abstract class
class Elevator(metaclass=ABCMeta):
    # this is passenger's queue.
    passengers = [(6, 12), (4, 13), (11, 3), (9, 2), (11, 12), (3, 9), (14, 8), (1, 7), (11, 9), (14, 16), (2, 15), (2, 9), (8, 16), (8, 9), (3, 10), (5, 4), (13, 9), (4, 6), (13, 7), (4, 8), (5, 3), (12, 14), (10, 13), (6, 12), (1, 7), (9, 2), (13, 11), (1, 14), (11, 8), (15, 12), (3, 15), (10, 3), (4, 1), (7, 1), (15, 8), (10, 16), (9, 3), (14, 13), (8, 13), (16, 9), (10, 7), (1, 6), (16, 13), (5, 3), (1, 12), (1, 7), (12, 3), (13, 6), (12, 15), (15, 6)]
    pass

# and then, create objects(elevator_1, elevator_2)


# if name of function is main, do your algorithm.
