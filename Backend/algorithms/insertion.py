def insertion_sort(arr):
    """
    Insertion Sort Algorithm with step-by-step visualization
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    steps = []
    n = len(arr)
    data = arr.copy()
    
    for i in range(1, n):
        key = data[i]
        j = i - 1
        
        steps.append({
            'array': data.copy(),
            'comparing': [i],
            'swapped': [],
            'explanation': f'Inserting {key} into sorted portion'
        })
        
        # Move elements greater than key one position ahead
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            steps.append({
                'array': data.copy(),
                'comparing': [j, j + 1],
                'swapped': [],
                'explanation': f'Shifting {data[j + 1]} to the right'
            })
            j -= 1
        
        # Place key at its correct position
        data[j + 1] = key
        steps.append({
            'array': data.copy(),
            'comparing': [],
            'swapped': [j + 1],
            'explanation': f'Placed {key} at position {j + 1}'
        })
    
    # Final sorted array
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Sorting complete! Array is now sorted.'
    })
    
    return steps