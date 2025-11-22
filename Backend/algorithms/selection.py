def selection_sort(arr):
    """
    Selection Sort Algorithm with step-by-step visualization
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    steps = []
    n = len(arr)
    data = arr.copy()
    
    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            # Finding minimum element
            steps.append({
                'array': data.copy(),
                'comparing': [min_idx, j],
                'swapped': [],
                'explanation': f'Finding minimum in unsorted portion. Current min: {data[min_idx]}, comparing with {data[j]}'
            })
            
            if data[j] < data[min_idx]:
                min_idx = j
        
        # Swap minimum element with first element of unsorted portion
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
            steps.append({
                'array': data.copy(),
                'comparing': [],
                'swapped': [i, min_idx],
                'explanation': f'Placed minimum {data[i]} at position {i}'
            })
    
    # Final sorted array
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Sorting complete! Array is now sorted.'
    })
    
    return steps