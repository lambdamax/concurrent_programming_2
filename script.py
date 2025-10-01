import time
import threading
import asyncio
from multiprocessing import Process

def cal_average(num):  # Average function used for sequential programming, threading, and multiprocessing
    sum_num = 0
    for t in num:
        sum_num = sum_num + t
    avg = sum_num / len(num)
    time.sleep(1)
    return avg
    # print(avg)  # debug

def main_sequential(list1, list2, list3):  # Main wrapper for sequential example
    s = time.perf_counter()  # start timer
    outcomes = [cal_average(ls) for ls in [list1, list2, list3]]

    [print(f"Avg. list{i+1} = {outcomes[i]}") for i in range(len(outcomes))]  # debug

    elapsed = time.perf_counter() - s  # end timer
    print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

async def cal_average_async(num):  # Average function used for asynchronous programming only ( needs await asyncio.sleep() )
    sum_num = 0
    for t in num:
        sum_num = sum_num + t
    avg = sum_num / len(num)
    await asyncio.sleep(1)  # simulate an I/O operation
    return avg
    # print(avg)  # debug

async def main_async(list1, list2, list3):  # Main wrapper for asynchronous example
    s = time.perf_counter()
    # your code goes here
    tasks = [cal_average_async(ls) for ls in [list1, list2, list3]]
    await asyncio.gather(*tasks)  # run tasks concurrently

    elapsed = time.perf_counter() - s
    print("Asynchronous Programming Elapsed Time: " + str(elapsed) + " seconds")

def main_threading(list1, list2, list3):  # Main wrapper for threading example
    s = time.perf_counter()
    # your code goes here
    lists = [list1, list2, list3]
    threads = []

    for i in range(len(lists)):
        x = threading.Thread(target=cal_average, args=(lists[i],))  # create thread
        threads.append(x)  # keep track of threads
        x.start()  # start thread
    for t in threads:
        t.join()  # wait for all threads to finish

    elapsed = time.perf_counter() - s
    print("Threading Elapsed Time: " + str(elapsed) + " seconds")

# Multiprocessing or Parallele Computing
def main_multiprocessing(list1, list2, list3):  # Main wrapper for multiprocessing example
    s = time.perf_counter()
    # your code goes here
    lists = [list1, list2, list3]
    processes = [Process(target=cal_average, args=(lists[i],)) for i in range(len(lists))]

    [p.start() for p in processes]  # start processes
    [p.join() for p in processes]  # wait for all processes to finish

    elapsed = time.perf_counter() - s
    print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")


if __name__ == '__main__':  # Need to use this if-statement so multiprocessing doesn't cause an infinite loop
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Three lists we are trying to calculate average on
    l2 = [2, 4, 6, 8, 10]
    l3 = [1, 3, 5, 7, 9, 11]
    main_sequential(l1, l2, l3)
    loop = asyncio.get_event_loop()  # create event loop
    loop.run_until_complete(main_async(l1, l2, l3))  # run event loop until completion
    main_threading(l1, l2, l3)
    main_multiprocessing(l1, l2, l3)
