# ==============================
# 1. SORT BY FREQUENCY
# ==============================
# Time: O(n log n)
# Space: O(n)
# Why: Uses hashmap + custom sorting when frequency matters

from collections import Counter

def sort_by_freq(nums):
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (freq[x], -x))


# ==============================
# 2. MERGE INTERVALS
# ==============================
# Time: O(n log n)
# Space: O(n)
# Why: Sort first, then merge overlapping intervals (greedy)

def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])
    return res


# ==============================
# 3. LARGEST NUMBER
# ==============================
# Time: O(n log n)
# Space: O(n)
# Why: Normal sorting fails → need custom comparator

from functools import cmp_to_key

def largest_number(nums):
    nums = list(map(str, nums))
    
    def compare(a, b):
        if a + b > b + a:
            return -1
        else:
            return 1
    
    nums.sort(key=cmp_to_key(compare))
    return ''.join(nums).lstrip('0') or '0'


# ==============================
# 4. KTH LARGEST ELEMENT
# ==============================
# Time: O(n log k)
# Space: O(k)
# Why: Heap is better than full sorting for k selection

import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


# ==============================
# 5. SORT COLORS (DUTCH FLAG)
# ==============================
# Time: O(n)
# Space: O(1)
# Why: In-place sorting without using sort()

def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# ==============================
# 6. TOP K FREQUENT ELEMENTS
# ==============================
# Time: O(n log k)
# Space: O(n)
# Why: Heap avoids sorting entire dataset

def top_k(nums, k):
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)


# ==============================
# 7. SORT CHARACTERS BY FREQUENCY
# ==============================
# Time: O(n log n)
# Space: O(n)
# Why: Sorting strings based on frequency

def freq_sort(s):
    freq = Counter(s)
    return ''.join(sorted(s, key=lambda x: (-freq[x], x)))


# ==============================
# 8. MINIMUM PLATFORMS (SWEEP LINE)
# ==============================
# Time: O(n log n)
# Space: O(1)
# Why: Sort arrival & departure separately → simulate timeline

def min_platforms(arr, dep):
    arr.sort()
    dep.sort()
    
    i = j = 0
    platforms = max_p = 0
    
    while i < len(arr):
        if arr[i] <= dep[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1
        
        max_p = max(max_p, platforms)
    
    return max_p


# ==============================
# 9. REORDER LOG FILES
# ==============================
# Time: O(n log n)
# Space: O(n)
# Why: Multi-condition sorting (letters vs digits)

def reorder_logs(logs):
    def key(log):
        id_, rest = log.split(" ", 1)
        return (0, rest, id_) if rest[0].isalpha() else (1,)
    
    return sorted(logs, key=key)


# ==============================
# 10. COUNT INVERSIONS (MERGE SORT)
# ==============================
# Time: O(n log n)
# Space: O(n)
# Why: Brute force O(n²) → optimized using merge sort

def count_inversions(arr):
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums, 0
        
        mid = len(nums) // 2
        left, inv1 = merge_sort(nums[:mid])
        right, inv2 = merge_sort(nums[mid:])
        
        merged = []
        i = j = inv = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
        
        merged += left[i:]
        merged += right[j:]
        
        return merged, inv + inv1 + inv2
    
    return merge_sort(arr)[1]


# ==============================
# QUICK TEST (optional)
# ==============================
if __name__ == "__main__":
    print(sort_by_freq([1,1,2,2,2,3]))
    print(merge([[1,3],[2,6],[8,10]]))
    print(largest_number([3,30,34,5,9]))
    print(kth_largest([3,2,1,5,6,4], 2))
    
    arr = [2,0,2,1,1,0]
    sort_colors(arr)
    print(arr)
    
    print(top_k([1,1,1,2,2,3], 2))
    print(freq_sort("tree"))
    print(min_platforms([900,940,950], [910,1200,1120]))
    print(reorder_logs(["dig1 8 1", "let1 art can", "let2 own kit"]))
    print(count_inversions([2,4,1,3,5]))