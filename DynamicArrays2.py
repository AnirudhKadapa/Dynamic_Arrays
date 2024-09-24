import time

# Opening and reading the file
with open('E:/Python_Workbase/College/CS5115/assg1/english-words/words3.txt') as f:
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
def insert_calculatetime(eowl, word1, fibseq1, fib_sequence, increment10, incrementdouble):
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
        print(f"{len(eowl)} 🡪 {time_elapsed:.8f} seconds")

    position = binarysearch_insert(eowl, word1)
    eowl.insert(position, word1)
    eowl.pop()
    return eowl


def printing(eowl):
    word1 = eowl[0]
    word2 = eowl[len(eowl)//4]
    word3 = eowl[len(eowl)//2]
    word4 = eowl[3 * len(eowl)//4]
    word5 = eowl[len(eowl)-1]
    print(f"{word1} 🡪 {word2} 🡪 {word3} 🡪 {word4} 🡪 {word5}")


# Main function
if __name__ == "__main__":
    eowl_10 = [None] * 2
    eowl_double = [None] * 2
    eowl_fib = [None] * 2
    fib_seq = [1, 1]
    # Enter Input strategy type: A or B or C
    strategy = input("Enter Strategy type:")
    if strategy == 'A':
        for word in words:
            eowl_10 = insert_calculatetime(eowl_10, word, fib_seq, False, True, False)
        printing(eowl_10)
    elif strategy == 'B':
        for word in words:
            eowl_double = insert_calculatetime(eowl_double, word, fib_seq, False, False, True)
        printing(eowl_double)
    elif strategy == 'C':
        for word in words:
            eowl_fib = insert_calculatetime(eowl_fib, word, fib_seq, True, False, False)
        printing(eowl_fib)
