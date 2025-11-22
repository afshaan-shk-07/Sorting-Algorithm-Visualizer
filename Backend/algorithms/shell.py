def shell_sort(arr):
    """
    Shell Sort Algorithm with step-by-step visualization
    Time Complexity: O(n log n) to O(n²) depending on gap sequence
    Space Complexity: O(1)
    """
    steps = []
    data = arr.copy()
    n = len(data)
    
    # Start with a large gap, then reduce the gap
    gap = n // 2
    
    while gap > 0:
        steps.append({
            'array': data.copy(),
            'comparing': [],
            'swapped': [],
            'explanation': f'Starting pass with gap = {gap}'
        })
        
        # Perform gapped insertion sort
        for i in range(gap, n):
            temp = data[i]
            j = i
            
            steps.append({
                'array': data.copy(),
                'comparing': [i],
                'swapped': [],
                'explanation': f'Inserting {temp} with gap {gap}'
            })
            
            while j >= gap and data[j - gap] > temp:
                steps.append({
                    'array': data.copy(),
                    'comparing': [j, j - gap],
                    'swapped': [],
                    'explanation': f'Comparing {data[j - gap]} with {temp}'
                })
                
                data[j] = data[j - gap]
                steps.append({
                    'array': data.copy(),
                    'comparing': [],
                    'swapped': [j, j - gap],
                    'explanation': f'Shifting {data[j]} to position {j}'
                })
                j -= gap
            
            data[j] = temp
            if j != i:
                steps.append({
                    'array': data.copy(),
                    'comparing': [],
                    'swapped': [j],
                    'explanation': f'Placed {temp} at position {j}'
                })
        
        gap //= 2
    
    # Final sorted array
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Sorting complete! Array is now sorted.'
    })
    
    return steps