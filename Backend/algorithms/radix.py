def radix_sort(arr):
    """
    Radix Sort Algorithm with step-by-step visualization
    Time Complexity: O(d * (n + k)) where d is number of digits
    Space Complexity: O(n + k)
    """
    steps = []
    data = arr.copy()
    n = len(data)
    
    if n == 0:
        return steps
    
    # Find the maximum number to know number of digits
    max_val = max(data)
    
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': f'Maximum value: {max_val}, will process digits accordingly'
    })
    
    # Do counting sort for every digit
    exp = 1
    while max_val // exp > 0:
        steps.append({
            'array': data.copy(),
            'comparing': [],
            'swapped': [],
            'explanation': f'Sorting by digit at position {exp} (ones, tens, hundreds, ...)'
        })
        
        # Counting sort based on digit represented by exp
        output = [0] * n
        count = [0] * 10
        
        # Store count of occurrences
        for i in range(n):
            index = (data[i] // exp) % 10
            count[index] += 1
            steps.append({
                'array': data.copy(),
                'comparing': [i],
                'swapped': [],
                'explanation': f'Counting digit {index} of number {data[i]}'
            })
        
        # Change count[i] so that it contains actual position
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Build output array
        for i in range(n - 1, -1, -1):
            index = (data[i] // exp) % 10
            output[count[index] - 1] = data[i]
            count[index] -= 1
        
        # Copy output array to data
        for i in range(n):
            data[i] = output[i]
        
        steps.append({
            'array': data.copy(),
            'comparing': [],
            'swapped': [],
            'explanation': f'Completed sorting by digit at position {exp}'
        })
        
        exp *= 10
    
    # Final sorted array
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Sorting complete! Array is now sorted.'
    })
    
    return steps