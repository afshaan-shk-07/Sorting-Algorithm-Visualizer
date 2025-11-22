def counting_sort(arr):
    """
    Counting Sort Algorithm with step-by-step visualization
    Time Complexity: O(n + k) where k is the range of input
    Space Complexity: O(k)
    """
    steps = []
    data = arr.copy()
    n = len(data)
    
    if n == 0:
        return steps
    
    # Find the range of input
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val + 1
    
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': f'Range of values: {min_val} to {max_val}'
    })
    
    # Create count array
    count = [0] * range_val
    output = [0] * n
    
    # Store count of each element
    for i in range(n):
        count[data[i] - min_val] += 1
        steps.append({
            'array': data.copy(),
            'comparing': [i],
            'swapped': [],
            'explanation': f'Counting occurrences of {data[i]}'
        })
    
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Count array created'
    })
    
    # Modify count array to contain actual positions
    for i in range(1, range_val):
        count[i] += count[i - 1]
    
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Modified count array for positions'
    })
    
    # Build output array
    for i in range(n - 1, -1, -1):
        output[count[data[i] - min_val] - 1] = data[i]
        count[data[i] - min_val] -= 1
        
        # Update data to show progress
        for j in range(n):
            if output[j] != 0 or j < count[data[i] - min_val]:
                data[j] = output[j] if output[j] != 0 else data[j]
        
        steps.append({
            'array': data.copy(),
            'comparing': [],
            'swapped': [count[data[i] - min_val]],
            'explanation': f'Placing element at correct position'
        })
    
    # Copy output array to data
    for i in range(n):
        data[i] = output[i]
    
    # Final sorted array
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Sorting complete! Array is now sorted.'
    })
    
    return steps