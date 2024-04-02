def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort by finish time
    solution = []
    last_finished = 0

    for start, finish in activities:
        if start >= last_finished:
            solution.append((start, finish))
            last_finished = finish

    return solution

# Example usage:
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
selected_activities = activity_selection(activities)
print(selected_activities) 
