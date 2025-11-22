def quick_sort(arr):
    """
    Quick Sort Algorithm with step-by-step visualization
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n)
    """
    steps = []
    data = arr.copy()
    
    def partition(data, low, high):
        pivot = data[high]
        steps.append({
            'array': data.copy(),
            'comparing': [high],
            'swapped': [],
            'explanation': f'Selected pivot: {pivot} at index {high}'
        })
        
        i = low - 1
        
        for j in range(low, high):
            steps.append({
                'array': data.copy(),
                'comparing': [j, high],
                'swapped': [],
                'explanation': f'Comparing {data[j]} with pivot {pivot}'
            })
            
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                steps.append({
                    'array': data.copy(),
                    'comparing': [],
                    'swapped': [i, j],
                    'explanation': f'Swapped {data[i]} and {data[j]} (both less than pivot)'
                })
        
        # Place pivot in correct position
        data[i + 1], data[high] = data[high], data[i + 1]
        steps.append({
            'array': data.copy(),
            'comparing': [],
            'swapped': [i + 1, high],
            'explanation': f'Placed pivot {data[i + 1]} at position {i + 1}'
        })
        
        return i + 1
    
    def quick_sort_helper(data, low, high):
        if low < high:
            pi = partition(data, low, high)
            quick_sort_helper(data, low, pi - 1)
            quick_sort_helper(data, pi + 1, high)
    
    quick_sort_helper(data, 0, len(data) - 1)
    
    # Final sorted array
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Sorting complete! Array is now sorted.'
    })
    
    return steps