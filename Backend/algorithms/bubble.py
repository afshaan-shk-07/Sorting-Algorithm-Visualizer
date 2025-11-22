def bubble_sort(arr):
    """
    Bubble Sort Algorithm with step-by-step visualization
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    steps = []
    n = len(arr)
    data = arr.copy()
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Comparing adjacent elements
            steps.append({
                'array': data.copy(),
                'comparing': [j, j + 1],
                'swapped': [],
                'explanation': f'Comparing {data[j]} and {data[j + 1]}'
            })
            
            if data[j] > data[j + 1]:
                # Swap elements
                data[j], data[j + 1] = data[j + 1], data[j]
                steps.append({
                    'array': data.copy(),
                    'comparing': [],
                    'swapped': [j, j + 1],
                    'explanation': f'Swapped {data[j]} and {data[j + 1]}'
                })
    
    # Final sorted array
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Sorting complete! Array is now sorted.'
    })
    
    return steps