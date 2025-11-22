def heap_sort(arr):
    """
    Heap Sort Algorithm with step-by-step visualization
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    steps = []
    data = arr.copy()
    n = len(data)
    
    def heapify(data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check if left child exists and is greater than root
        if left < n:
            steps.append({
                'array': data.copy(),
                'comparing': [i, left],
                'swapped': [],
                'explanation': f'Comparing parent {data[i]} with left child {data[left]}'
            })
            if data[left] > data[largest]:
                largest = left
        
        # Check if right child exists and is greater than largest so far
        if right < n:
            steps.append({
                'array': data.copy(),
                'comparing': [largest, right],
                'swapped': [],
                'explanation': f'Comparing {data[largest]} with right child {data[right]}'
            })
            if data[right] > data[largest]:
                largest = right
        
        # If largest is not root, swap and continue heapifying
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            steps.append({
                'array': data.copy(),
                'comparing': [],
                'swapped': [i, largest],
                'explanation': f'Swapped {data[i]} and {data[largest]} to maintain heap property'
            })
            heapify(data, n, largest)
    
    # Build max heap
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Building max heap...'
    })
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
    
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Max heap built! Now extracting elements...'
    })
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        steps.append({
            'array': data.copy(),
            'comparing': [],
            'swapped': [0, i],
            'explanation': f'Moved maximum element {data[i]} to position {i}'
        })
        heapify(data, i, 0)
    
    # Final sorted array
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Sorting complete! Array is now sorted.'
    })
    
    return steps