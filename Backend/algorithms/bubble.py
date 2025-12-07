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
                'explanation': (
                    f"We are comparing the elements at positions {j} and {j+1}, "
                    f"which are {data[j]} and {data[j+1]}. "
                    "If the left element is greater than the right element, we will swap them. "
                    "This is how the largest elements 'bubble up' to the end of the array."
                )

            })
            
            if data[j] > data[j + 1]:
                # Swap elements
                data[j], data[j + 1] = data[j + 1], data[j]
                steps.append({
                    'array': data.copy(),
                    'comparing': [],
                    'swapped': [j, j + 1],
                    'explanation': (
                        f"The element {data[j+1]} was greater than {data[j]}, "
                        "so we swapped them. "
                        "This helps move larger numbers toward the end of the list step by step."
                    )
                })
    
    # Final sorted array
    steps.append({
        'array': data.copy(),
        'comparing': [],
        'swapped': [],
        'explanation': 'Sorting complete! Array is now sorted.'
    })
    
    return steps