def merge_sort(arr):
    """
    Merge Sort Algorithm with step-by-step visualization
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    steps = []
    data = arr.copy()
    
    def merge(data, left, mid, right):
        # Create temp arrays
        left_arr = data[left:mid + 1]
        right_arr = data[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        # Merge the temp arrays
        while i < len(left_arr) and j < len(right_arr):
            steps.append({
                'array': data.copy(),
                'comparing': [left + i, mid + 1 + j],
                'swapped': [],
                'explanation': f'Merging: comparing {left_arr[i]} and {right_arr[j]}'
            })
            
            if left_arr[i] <= right_arr[j]:
                data[k] = left_arr[i]
                i += 1
            else:
                data[k] = right_arr[j]
                j += 1
            
            steps.append({
                'array': data.copy(),
                'comparing': [],
                'swapped': [k],
                'explanation': f'Placed {data[k]} at position {k}'
            })
            k += 1
        
        # Copy remaining elements
        while i < len(left_arr):
            data[k] = left_arr[i]
            steps.append({
                'array': data.copy(),
                'comparing': [],
                'swapped': [k],
                'explanation': f'Copying remaining element {data[k]}'
            })
            i += 1
            k += 1
        
        while j < len(right_arr):
            data[k] = right_arr[j]
            steps.append({
                'array': data.copy(),
                'comparing': [],
                'swapped': [k],
                'explanation': f'Copying remaining element {data[k]}'
            })
            j += 1
            k += 1
    
    def merge_sort_helper(data, left, right):
        if left < right:
            mid = (left + right) // 2
            
            steps.append({
                'array': data.copy(),
                'comparing': list(range(left, right + 1)),
                'swapped': [],
                'explanation': f'Dividing array from index {left} to {right}'
            })
            
            merge_sort_helper(data, left, mid)
            merge_sort_helper(data, mid + 1, right)
            merge(data, left, mid, right)
    
    merge_sort_helper(data, 0, len(data) - 1)
    
    # Final sorted array
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Sorting complete! Array is now sorted.'
    })
    
    return steps