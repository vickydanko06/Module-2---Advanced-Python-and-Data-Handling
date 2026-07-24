"""
This exercise is 2 parts. First part is to classify 5 functions time complexity. Part 2 is to create 2 duplicate finding functions and test their time complexity for 1,000 - 5,000 - 10,000.


"""

import time


# ============================================================
# PART 1 — Classify These Functions
# For each function, fill in the Big O and explain why.
# ============================================================

def get_first(data):
    return data[0]
# TODO: What is the Big O of get_first? Why?
# Big O: O(1)
# Reason: Function is returning 1 value - [0]

def count_matches(data, target):
    count = 0
    for item in data:
        if item == target:
            count += 1
    return count
# TODO: What is the Big O of count_matches? Why?
# Big O: O(n)
# Reason: This function loops through a list and scales with the input size has it is counting


def all_pairs(data):
    pairs = []
    for i in data:             # outer loop
        for j in data:         # inner loop
            pairs.append((i, j))
    return pairs
# TODO: What is the Big O of all_pairs? Why?
# Big O: O(n^2)
# Reason: there is a nested loop in this function that leads to quadratic time


def mystery(n):
    steps = 0
    while n > 1:
        n = n // 2
        steps += 1
    return steps
# TODO: What is the Big O of mystery? Why?
# Big O: O(log n)
# Reason: Binary search - this funciton will ct the data in half until the answer is returned.


def process(data):
    total = sum(data)
    ordered = sorted(data)
    pos = ordered.index(total) if total in ordered else -1
    return pos
# TODO: What is the Big O of process? Why?
#       Hint: what is the Big O of sum()? of sorted()? Which dominates?
# Big O: O(n log n)
# Reason: The function sorts and then matches data which is the Big O of O(n log n)


# ============================================================
# PART 2 — Write and Benchmark Two Duplicate Finders
# ============================================================

def has_duplicates_slow(data):
    """Check for duplicates using nested loops. Should be O(n²).
    This function will pick an element and will compare it against every other element. It will return true once a match is found and false if it doesnt.
    Args:
        data: A list of numbers
    
    """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return True
    return False
    pass


def has_duplicates_fast(data):
    """
    This function also checks for duplicates but uses a set to pass through the data and lookup to see if there are multiple similar entries.
    """
    dupe = set()
    for item in data:           
        if item in dupe:       
            return True
        dupe.add(item)          
    return False
    pass


def benchmark(func, data, label):
    """Time a function call and return elapsed milliseconds.
    GIVEN IN STARTER CODE - NO ADDITIONAL COMMENTS ADDED
    """
    start = time.time()
    result = func(data)
    elapsed = (time.time() - start) * 1000
    print(f"  {label:<25} result={result}  time={elapsed:.3f} ms")
    return elapsed


# ============================================================
# BENCHMARKING — run this after implementing both functions
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Duplicate Detection Benchmark")
    print("=" * 60)
    print(f"  {'Function':<25} {'Result':<14} {'Time'}")
    print(f"  {'-'*25} {'-'*14} {'-'*12}")

    for size in [1000, 5000, 10_000]:
        # Build a list with no duplicates, then force one at the very end.
        # Putting the duplicate last is worst-case for the slow version.
        #NO ADDITIONAL COMMENTS GIVEN - STARTER CODE FOR MAIN 
        test_data = list(range(size))
        test_data.append(size - 1)   # duplicate of the last element

        print(f"\n  Size = {size:,}:")
        t_slow = benchmark(has_duplicates_slow, test_data, "has_duplicates_slow")
        t_fast = benchmark(has_duplicates_fast, test_data, "has_duplicates_fast")

        if t_slow and t_fast:
            print(f"  → Fast version was {t_slow / t_fast:.1f}x faster")