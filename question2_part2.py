import heapq

def merge_sorted_lists(lists):
    merged = []
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    
    while heap:
        val, list_idx, ele_idx = heapq.heappop(heap)
        merged.append(val)
        if ele_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][ele_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, ele_idx + 1))
    
    return merged

#  number of lists 
m = int(input("Enter the number of lists: "))
n = int(input("Enter the number of elements per list: "))

# Taking user input for the lists
lists = []
for i in range(m):
    lst = list(map(int, input(f"Enter space-separated elements for list {i+1}: ").split()))
    lists.append(lst)

# Merging the sorted lists and printing the result
result = merge_sorted_lists(lists)
print("Merged sorted list:", result)
