from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Import sorting algorithms from the algorithms package
from algorithms.bubble import bubble_sort
from algorithms.selection import selection_sort
from algorithms.insertion import insertion_sort
from algorithms.merge import merge_sort
from algorithms.quick import quick_sort
from algorithms.heap import heap_sort
from algorithms.shell import shell_sort
from algorithms.counting import counting_sort
from algorithms.radix import radix_sort

@app.route('/')
def home():
    """
    Home endpoint - provides API information
    """
    return jsonify({
        'message': 'Sorting Algorithm Visualizer API',
        'version': '1.0',
        'endpoints': {
            '/': 'GET - API information',
            '/sort': 'POST - Sort array with specified algorithm'
        },
        'available_algorithms': [
            'bubble', 'selection', 'insertion', 'merge', 
            'quick', 'heap', 'shell', 'counting', 'radix'
        ]
    })

@app.route('/sort', methods=['POST'])
def sort_array():
    """
    Sort endpoint - receives array and algorithm, returns sorting steps
    
    Expected JSON body:
    {
        "algorithm": "bubble",
        "data": [64, 34, 25, 12, 22, 11, 90]
    }
    
    Returns:
    {
        "algorithm": "bubble",
        "steps": [...],
        "total_steps": 50
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        algorithm = data.get('algorithm', 'bubble')
        array = data.get('data', [])
        
        if not array:
            return jsonify({'error': 'No data array provided'}), 400
        
        if not isinstance(array, list):
            return jsonify({'error': 'Data must be an array'}), 400
        
        # Validate that all elements are numbers
        try:
            array = [int(x) for x in array]
        except (ValueError, TypeError):
            return jsonify({'error': 'All array elements must be numbers'}), 400
        
        # Route to appropriate sorting algorithm
        algorithm_map = {
            'bubble': bubble_sort,
            'selection': selection_sort,
            'insertion': insertion_sort,
            'merge': merge_sort,
            'quick': quick_sort,
            'heap': heap_sort,
            'shell': shell_sort,
            'counting': counting_sort,
            'radix': radix_sort
        }
        
        if algorithm not in algorithm_map:
            return jsonify({
                'error': f'Invalid algorithm: {algorithm}',
                'available_algorithms': list(algorithm_map.keys())
            }), 400
        
        # Get sorting steps
        print(f"Sorting array {array} using {algorithm} sort...")
        steps = algorithm_map[algorithm](array.copy())
        print(f"Generated {len(steps)} steps")
        
        return jsonify({
            'algorithm': algorithm,
            'steps': steps,
            'total_steps': len(steps),
            'original_array': array,
            'sorted_array': steps[-1]['array'] if steps else array
        })
        
    except Exception as e:
        print(f"Error in /sort endpoint: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'available_endpoints': {
            '/': 'GET - API information',
            '/sort': 'POST - Sort array'
        }
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'message': str(error)
    }), 500

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Sorting Algorithm Visualizer API")
    print("=" * 50)
    print("Server starting on http://localhost:5000")
    print("Available algorithms:")
    print("  - Bubble Sort")
    print("  - Selection Sort")
    print("  - Insertion Sort")
    print("  - Merge Sort")
    print("  - Quick Sort")
    print("  - Heap Sort")
    print("  - Shell Sort")
    print("  - Counting Sort")
    print("  - Radix Sort")
    print("=" * 50)
    app.run(debug=True, port=5000, host='0.0.0.0')