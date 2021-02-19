def run_hanoi(num):
    for i in range(num):
        print('disc moved to pole{}'.format(i))

if __name__=='__main__':
    run_hanoi(10)
