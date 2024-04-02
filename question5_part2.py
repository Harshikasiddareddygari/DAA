def merge_intervals(intervals):

  
  # Sort the intervals based on their starting times
  intervals.sort(key=lambda x: x[0])

  merged_intervals = []
  # Initialize the first interval in the merged list
  current_interval = intervals[0]

  # Iterate through the remaining intervals
  for interval in intervals[1:]:
    # If the current interval overlaps with the next interval
    if current_interval[1] >= interval[0]:
      # Merge the overlapping intervals by extending the end time of the current interval
      current_interval = (current_interval[0], max(current_interval[1], interval[1]))
    else:
      # If there is no overlap, add the current interval to the merged list and start a new one
      merged_intervals.append(current_interval)
      current_interval = interval

  # Add the last interval to the merged list
  merged_intervals.append(current_interval)

  return merged_intervals

# Example usage
intervals = [(1, 4), (2, 5), (1, 3), (7, 8), (6, 9)]
merged_intervals = merge_intervals(intervals)
print(merged_intervals) 
