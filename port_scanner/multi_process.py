import time
import random
import port_scanner.construct as construct 
from multiprocessing import Process, Queue, current_process, freeze_support


def worker(input, output):
    """Function run by worker processes"""
    for func, args in iter(input.get, 'STOP'):
        result = perform(func, args)
        output.put(result)

def perform(func, args):
    """Function used to calculate result"""
    result = func(*args)
    return result
            
def run(l_hosts, tasks):
    """Function used to call nmap in multithread"""
    
    number_of_processes = len(tasks)

    # Create queues
    task_queue = Queue()
    done_queue = Queue()

    # Submit tasks
    for task in tasks:
        task_queue.put(task)

    # Start worker processes
    for _ in range(number_of_processes):
        Process(target=worker, args=(task_queue, done_queue)).start()

    # Get results
    for _ in range(len(tasks)):
        result = done_queue.get()
        l_hosts = construct.create_host(result, l_hosts)
    
    # Tell child processes to stop
    for _ in range(number_of_processes):
        task_queue.put('STOP')

    return l_hosts