# file containing standardized workloads to be used during experiments
import sys
import time

# workload 0 - square root, multithreaded
def workload0():
    import threading
    num_iter = 3000
    threads = 500
    def workload0_thread():
        for counter in range(num_iter):
            x = 0.5
            y = x ** 0.5
    threadPool = []
    for threadIdx in range(threads):
        t = threading.Thread(target=workload0_thread, name="thread_" + str(threadIdx))
        threadPool.append(t)
    for thread in threadPool:
        thread.start()
    for thread in threadPool:
        thread.join()

# workload 1 - square root, single thread
def workload1():
    num_iter = 3000
    for counter in range(num_iter):
        x = 0.5
        y = x ** 0.5

# workload 2 - matrix multiplication, multithreaded
def workload2():
    import numpy as np
    from _thread import start_new_thread
    num_iter = 250
    threads = 100
    def workload2_thread():
        for counter in range(num_iter):
            # initialize random arrays with same seed
            np.random.seed(0)
            a = np.random.rand(100, 100)
            b = np.random.rand(100, 100)
            # multiply arrays
            c = np.matmul(a, b)
            print("done!")
        print("mult complete")
    for thread in range(threads):
        start_new_thread(workload2_thread, ())

# workload 3 - matrix multiplication, single thread
def workload3():
    import numpy as np
    num_iter = 250
    for counter in range(num_iter):
        # initialize random arrays with same seed
        np.random.seed(0)
        a = np.random.rand(100, 100)
        b = np.random.rand(100, 100)
        # multiply arrays
        c = np.matmul(a, b)

# workload 4 - fibonacci, multithreaded
def workload4():
    from _thread import start_new_thread
    num_iter = 1000
    threads = 100
    def workload4_thread():
        for counter in range(num_iter):
            def fib(n):
                if n <= 1:
                    return n
                else:
                    return fib(n - 1) + fib(n - 2)
            fib(20)
    for thread in range(threads):
        start_new_thread(workload4_thread, ())

# workload 5 - fibonacci, single thread
def workload5():
    num_iter = 1000
    for counter in range(num_iter):
        def fib(n):
            if n <= 1:
                return n
            else:
                return fib(n - 1) + fib(n - 2)
        fib(20)

# workload 6 - graph traversal, multithreaded
def workload6():
    from pygraph.classes.graph import graph
    from pygraph.algorithms.searching import breadth_first_search    
    from _thread import start_new_thread
    num_iter = 1500
    threads = 500
    def workload6_thread():
        for counter in range(num_iter):
            g = graph()
            g.add_nodes(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"])
            g.add_edge(("A", "B"))
            g.add_edge(("A", "C"))
            g.add_edge(("B", "D"))
            g.add_edge(("B", "E"))
            g.add_edge(("C", "F"))
            g.add_edge(("E", "G"))
            pred, dist = breadth_first_search(g, root="A")
    for thread in range(threads):
        start_new_thread(workload6_thread, ())

# workload 7 - graph traversal, single thread
def workload7():
    from pygraph.classes.graph import graph
    from pygraph.algorithms.searching import breadth_first_search
    num_iter = 1500
    for counter in range(num_iter):
        g = graph()
        g.add_nodes(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"])
        g.add_edge(("A", "B"))
        g.add_edge(("A", "C"))
        g.add_edge(("B", "D"))
        g.add_edge(("B", "E"))
        g.add_edge(("C", "F"))
        g.add_edge(("E", "G"))
        pred, dist = breadth_first_search(g, root="A")

def main(workloadNum):
    # start time
    start_time = time.time()
    process_start = time.process_time()
    perf_start = time.perf_counter()
    # workloads
    workloads = [workload0, workload1, workload2, workload3, workload4, workload5, workload6, workload7]
    workloadNames = {"multiSqrt": workload0, "singleSqrt": workload1, "multiMatMul": workload2, "singleMatMul": workload3, "multiFib": workload4, "singleFib": workload5, "multiGraph": workload6, "singleGraph": workload7}
    # execute corresponding workload
    workloads[int(workloadNum)]()
    # end time
    print("Standard time: " + str(round(time.time() - start_time, 2)))
    print("Process time: " + str(round(time.process_time() - process_start, 2)))
    print("Perf counter: " + str(round(time.perf_counter() - perf_start, 2)))

# main method (note pip install pygraph and numpy)
if __name__ == '__main__':
    # retrieve arguments
    args = sys.argv
    # execute main method
    if len(args) == 1:
        main(0) # default workload
    else:
        main(int(args[1]))