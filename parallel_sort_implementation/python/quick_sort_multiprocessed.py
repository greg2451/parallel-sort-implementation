import multiprocessing as mp
import random
import time

PROCESSING_DEPTH = 2
init_depth = 1


def quick_sort_mp(to_sort):
    mp_queue = mp.Queue()
    sorter = MPQuickSort(queue=mp_queue, to_sort=to_sort)
    sorter.start()
    sorted_list = mp_queue.get()
    sorter.join()
    return sorted_list


class MPQuickSort(mp.Process):
    def __init__(self, queue, to_sort):
        super(MPQuickSort, self).__init__()

        self.queue = queue
        self.to_sort = to_sort

    def run(self):
        self.queue.put(self.quicksort(self.to_sort))

    def quicksort(self, list_to_sort):
        if len(list_to_sort) == 0:
            return []

        # Pick Pivot
        pivot = list_to_sort[0]
        to_be_left = [x for x in list_to_sort[1:] if x <= pivot]
        to_be_right = [x for x in list_to_sort[1:] if x > pivot]

        global init_depth
        if init_depth < PROCESSING_DEPTH:
            init_depth += 1
            left_queue = mp.Queue()
            right_queue = mp.Queue()
            process_1 = MPQuickSort(
                left_queue,
                to_be_left,
            )
            process_2 = MPQuickSort(
                right_queue,
                to_be_right,
            )

            process_1.start()
            process_2.start()

            left_queue = left_queue.get()
            right_queue = right_queue.get()

            process_1.join()
            process_2.join()
            return left_queue + [pivot] + right_queue
        else:
            left_side = self.quicksort(to_be_left)
            right_side = self.quicksort(to_be_right)
            return left_side + [pivot] + right_side


if __name__ == "__main__":
    example = [random.randint(0, 10000000) for i in range(100000)]
    start = time.time()
    sorted_example = quick_sort_mp(example)
    end = time.time()
    print(end - start)
