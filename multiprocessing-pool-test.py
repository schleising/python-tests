import multiprocessing as mp
from multiprocessing.connection import Connection
from time import sleep

def poolInit(inQueue: mp.Queue, inPConn: Connection, inCConn: Connection) -> None:
    global queue
    global pConn
    global cConn

    queue = inQueue
    pConn = inPConn
    cConn = inCConn

    print('Proc Started')

def calc(x: int) -> None:
    print(f'Calculating {x}')
    cConn.send(x + x)
    print(f'Sent {x}')

def mainLoop(myQueue: mp.Queue, myPConn: Connection, myCConn: Connection) -> None:
    with mp.Pool(initializer=poolInit, initargs=(myQueue, myPConn, myCConn)) as pool:
        i = 0
        print(f'Sending {i}')
        pool.apply_async(calc, (i,))
        i += 1
        sleep(1)
        print(f'Waiting {i}')
        # x = myPConn.recv()
        print(f'Got {x}')

if __name__ == '__main__':
    queue = mp.Queue()
    pConn, cConn = mp.Pipe()
    process = mp.Process(target=mainLoop, args=(queue,pConn, cConn))
    process.start()
    sleep(2)
    print('Closing')
    queue.close()
    print('Closed')
