# d_analysis.py
## author - nick s.

# IMPORTS
import time
import math
import matplotlib.pyplot as plt

import a_iterative_list as List_iter
import a_recursive_list as List_rec

import b_iterative_stack as Stack_iter
import b_recursive_stack as Stack_rec

import c_iterative_queue as Queue_iter
import c_recursive_queue as Queue_rec

# PLOT CONFIG
plt.suptitle('Kuhn - Lab 6 Analysis')

# CONSTANTS
N_TRIALS = 100  # TODO run on 20 trials
N_ELEMENTS = 512  # TODO run on 100 elements per trial

# DEFINITIONS
def experiment_list_iter_front(n_trials, n_elements):
    results = []
    def test_list_front(n):
        # initialize the data structure
        list = List_iter.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            list = List_iter.addToFront(list, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_list_front(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_list_iter_back(n_trials, n_elements):
    results = []
    def test_list_back(n):
        # initialize the data structure
        list = List_iter.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            list = List_iter.addToBack(list, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_list_back(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_list_rec_front(n_trials, n_elements):
    results = []
    def test_list_front(n):
        # initialize the data structure
        list = List_rec.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            list = List_rec.addToFront(list, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_list_front(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_list_rec_back(n_trials, n_elements):
    results = []
    def test_list_back(n):
        # initialize the data structure
        list = List_rec.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            list = List_rec.addToBack(list, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_list_back(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time



def experiment_stack_iter_push(n_trials, n_elements):
    results = []
    def test_stack_push(n):
        # initialize the data structure
        stack = Stack_iter.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            stack = Stack_iter.push(stack, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_stack_push(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_stack_iter_pop(n_trials, n_elements):
    results = []
    def test_stack_pop(n):
        # initialize the data structure
        stack = Stack_iter.initialize()
        for i in range(n):
            stack = Stack_iter.push(stack, i)

        # time the test
        t_0 = time.process_time_ns()
        for i in range(n):
            (_, stack) = Stack_iter.pop(stack)
        t_1 = time.process_time_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_stack_pop(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_stack_rec_push(n_trials, n_elements):
    results = []
    def test_stack_push(n):
        # initialize the data structure
        stack = Stack_rec.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            stack = Stack_rec.push(stack, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_stack_push(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_stack_rec_pop(n_trials, n_elements):
    results = []
    def test_stack_pop(n):
        # initialize the data structure
        stack = Stack_rec.initialize()
        for i in range(n):
            stack = Stack_rec.push(stack, i)

        # time the test
        t_0 = time.process_time_ns()
        for i in range(n):
            (_, stack) = Stack_rec.pop(stack)
        t_1 = time.process_time_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_stack_pop(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time



def experiment_queue_iter_enqueue(n_trials, n_elements):
    results = []
    def test_queue_enqueue(n):
        # initialize the data structure
        queue = Queue_iter.initialize()

        # time the test
        t_0 = time.process_time_ns()
        for i in range(n):
            queue = Queue_iter.enqueue(queue, i)
        t_1 = time.process_time_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_queue_enqueue(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_queue_iter_dequeue(n_trials, n_elements):
    results = []
    def test_queue_dequeue(n):
        # initialize the data structure
        queue = Queue_iter.initialize()
        for i in range(n):
            queue = Queue_iter.enqueue(queue, i)

        # time the test
        t_0 = time.process_time_ns()
        for i in range(n):
            (_, queue) = Queue_iter.dequeue(queue)
        t_1 = time.process_time_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_queue_dequeue(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_queue_rec_enqueue(n_trials, n_elements):
    results = []
    def test_queue_enqueue(n):
        # initialize the data structure
        queue = Queue_rec.initialize()

        # time the test
        t_0 = time.process_time_ns()
        for i in range(n):
            queue = Queue_rec.enqueue(queue, i)
        t_1 = time.process_time_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_queue_enqueue(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_queue_rec_dequeue(n_trials, n_elements):
    results = []
    def test_queue_dequeue(n):
        # initialize the data structure
        queue = Queue_rec.initialize()
        for i in range(n):
            queue = Queue_rec.enqueue(queue, i)

        # time the test
        t_0 = time.process_time_ns()
        for i in range(n):
            (_, queue) = Queue_rec.dequeue(queue)
        t_1 = time.process_time_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_queue_dequeue(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time



# RUN THE EXPERIMENTS
RESULTS = {
    # list
    'back  (i)': experiment_list_iter_back(N_TRIALS, N_ELEMENTS),
    'front (i)': experiment_list_iter_front(N_TRIALS, N_ELEMENTS),
    'back  (r)': experiment_list_rec_back(N_TRIALS, N_ELEMENTS),
    'front (r)': experiment_list_rec_front(N_TRIALS, N_ELEMENTS),
    # stack
    'push  (i)': experiment_stack_iter_push(N_TRIALS, N_ELEMENTS),
    'pop   (i)': experiment_stack_iter_pop(N_TRIALS, N_ELEMENTS),
    'push  (r)': experiment_stack_rec_push(N_TRIALS, N_ELEMENTS),
    'pop   (r)': experiment_stack_rec_pop(N_TRIALS, N_ELEMENTS),
    # queue
    'enq   (i)': experiment_queue_iter_enqueue(N_TRIALS, N_ELEMENTS),
    'deq   (i)': experiment_queue_iter_dequeue(N_TRIALS, N_ELEMENTS),
    'enq   (r)': experiment_queue_rec_enqueue(N_TRIALS, N_ELEMENTS),
    'deq   (r)': experiment_queue_rec_dequeue(N_TRIALS, N_ELEMENTS)
}

# NORMALIZE THE RESULTS
values = list(RESULTS.values())
squares = [ v*v for v in values ]
norm = math.sqrt(sum(squares))
for experiment in RESULTS:
    RESULTS[experiment] = RESULTS[experiment] / norm

# YOUR CODE GOES BELOW
## List
plt.subplot(1,3,1)
plt.bar(x=1, height=RESULTS['back  (i)'], label='back  (i)', width=.8, color = 'blue')
plt.bar(x=1, height=RESULTS['front (i)'], label='front (i)', width=.4, color = 'green')
plt.bar(x=2, height=RESULTS['back  (r)'], label='back  (r)', width=.8, color = 'orange')
plt.bar(x=2, height=RESULTS['front (r)'], label='front (r)', width=.4, color = 'red')
plt.legend()
plt.yticks([])
plt.xticks([])
plt.xlabel('List')


## STACK
plt.subplot(1,3,2)
plt.bar(x=1, height=RESULTS['push  (i)'], label='push  (i)', width=.8, color = 'blue')
plt.bar(x=1, height=RESULTS['pop   (i)'], label='pop (i)', width=.4, color = 'green')
plt.bar(x=2, height=RESULTS['push  (r)'], label='push  (r)', width=.8, color = 'orange')
plt.bar(x=2, height=RESULTS['pop   (r)'], label='pop (r)', width=.4, color = 'red')
plt.legend()
plt.yticks([])
plt.xticks([])
plt.xlabel('Stack')

## QUEUE
plt.subplot(1,3,3)
plt.bar(x=1, height=RESULTS['enq   (i)'], label='enq  (i)', width=.8, color = 'blue')
plt.bar(x=1, height=RESULTS['deq   (i)'], label='deq (i)', width=.4, color = 'green')
plt.bar(x=2, height=RESULTS['enq   (r)'], label='enq  (r)', width=.8, color = 'orange')
plt.bar(x=2, height=RESULTS['deq   (r)'], label='deq (r)', width=.4, color = 'red')
plt.legend()
plt.yticks([])
plt.xticks([])
plt.xlabel('Stack')

## SAVE FIGURE
plt.savefig('./figs/kuhn_lab6_analysis.png')
