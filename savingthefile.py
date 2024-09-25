import time
import json

# Opening and reading the file
with open('E:/Python_Workbase/College/CS5115/assg1/english-words/words5.txt') as f:
    words = f.read().splitlines()


# Strategy A: increment by 10
def increaseby_10(eowl):
    return eowl + [None] * 10


# Strategy B: increment by double
def increase_double(eowl):
    return eowl + [None] * len(eowl)


# Strategy C: increment by fibonacci
def increase_fibsequence(eowl, fibseq):
    next_number = fibseq[-1] + fibseq[-2]
    fibseq.append(next_number)
    return eowl + [None] * (next_number - len(eowl))


# Find the element position in the array using binary search
def binarysearch_insert(arr, word2):
    start = 0
    end = len(arr)-1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] is None or arr[mid] > word2:
            end = mid
        else:
            start = mid + 1
    return start


# Insert element into the array and calculate the time at search and increase point
def insert_calculatetime(eowl, word1, fibseq1, fib_sequence, increment10, incrementdouble, timetaken, arraysizes):
    if eowl.count(None) == 0:
        start = time.perf_counter()
        if fib_sequence:
            eowl = increase_fibsequence(eowl, fibseq1)
        elif increment10:
            eowl = increaseby_10(eowl)
        elif incrementdouble:
            eowl = increase_double(eowl)
        position = binarysearch_insert(eowl, word1)
        eowl.insert(position, word1)
        eowl.pop()
        end = time.perf_counter()
        time_elapsed = end - start
        timetaken.append(time_elapsed)
        arraysizes.append(len(eowl))
        print(f"{len(eowl)} 🡪 {time_elapsed:.8f} seconds")

    position = binarysearch_insert(eowl, word1)
    eowl.insert(position, word1)
    eowl.pop()
    return eowl, timetaken, arraysizes


def save_data_to_file(strategy, time_taken, array_sizes):
    data = {
        "strategy": strategy,
        "time_taken": time_taken,
        "array_sizes": array_sizes
    }
    with open(f'E:/Python_Workbase/College/CS5115/assg1/Dynamic_Arrays/data_log/{strategy}_data.json', 'w') as f:
        json.dump(data, f)


# We are printing the 1st, n/4, n/2, 3n/4, nth elements of eowl array
def printing(eowl):
    word1 = eowl[0]
    word2 = eowl[len(eowl)//4]
    word3 = eowl[len(eowl)//2]
    word4 = eowl[3 * len(eowl)//4]
    word5 = eowl[len(eowl)-1]
    print(f"{word1} 🡪 {word2} 🡪 {word3} 🡪 {word4} 🡪 {word5}")


# Main function
# Now we can choose the strategy we want to proceed with and print the output of the necessary
if __name__ == "__main__":
    eowl_10 = [None] * 2
    eowl_double = [None] * 2
    eowl_fib = [None] * 2
    fib_seq = [1, 1]
    time_taken = []
    array_sizes = []

    strategy = input("Enter Strategy type:")
    if strategy == 'A':
        for word in words:
            eowl_10, time_taken, array_sizes = insert_calculatetime(eowl_10, word, fib_seq, False, True, False, time_taken, array_sizes)
        printing(eowl_10)
        save_data_to_file('A', time_taken, array_sizes)
    elif strategy == 'B':
        for word in words:
            eowl_double, time_taken, array_sizes = insert_calculatetime(eowl_double, word, fib_seq, False, False, True, time_taken, array_sizes)
        printing(eowl_double)
        save_data_to_file('B', time_taken, array_sizes)
    elif strategy == 'C':
        for word in words:
            eowl_fib, time_taken, array_sizes = insert_calculatetime(eowl_fib, word, fib_seq, True, False, False, time_taken, array_sizes)
        printing(eowl_fib)
        save_data_to_file('C', time_taken, array_sizes)
