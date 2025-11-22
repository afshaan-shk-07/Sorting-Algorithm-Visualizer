# Sorting Algorithm Visualizer

A beautiful, interactive web application to visualize 9 different sorting algorithms with step-by-step explanations.

## Features

- **9 Sorting Algorithms**: Bubble, Selection, Insertion, Merge, Quick, Heap, Shell, Counting, and Radix Sort
- **Custom or Sample Data**: Choose to input your own numbers or use pre-defined data
- **Real-time Visualization**: Watch bars animate as the sorting happens
- **Step-by-Step Explanations**: Understand what's happening at each step
- **Adjustable Speed**: Control animation speed from 100ms to 2000ms
- **Color-Coded Actions**: 
  - Blue: Default state
  - Yellow: Comparing elements
  - Green: Swapped elements

## Project Structure

```
SORTING-ALGORITHM-VISUALIZER/
├── Backend/
│   ├── algorithms/
│   │   ├── __init__.py
│   │   ├── bubble.py
│   │   ├── selection.py
│   │   ├── insertion.py
│   │   ├── merge.py
│   │   ├── quick.py
│   │   ├── heap.py
│   │   ├── shell.py
│   │   ├── counting.py
│   │   └── radix.py
│   ├── app.py
│   └── requirements.txt
├── static/
│   └── (optional: for css/js if separated)
├── templates/
│   └── index.html
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- A modern web browser

### Step 1: Clone or Download the Project

```bash
cd SORTING-ALGORITHM-VISUALIZER
```

### Step 2: Set Up Backend

1. Navigate to the Backend folder:
```bash
cd Backend
```

2. Create a virtual environment (recommended):
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create the algorithms folder with `__init__.py`:
```bash
mkdir algorithms
# On Windows
type nul > algorithms/__init__.py
# On macOS/Linux
touch algorithms/__init__.py
```

5. Place all algorithm files (bubble.py, selection.py, etc.) in the `algorithms` folder

### Step 3: Run the Flask Server

```bash
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 4: Open the Frontend

1. Navigate to the templates folder (or root folder where index.html is located)
2. Open `index.html` in your web browser
   - You can simply double-click the file, or
   - Right-click and select "Open with" your browser, or
   - Use a local server like Live Server in VS Code

**Important**: The HTML file will connect to `http://localhost:5000` for the backend API.

## Usage

1. **Welcome Screen**: Choose between custom data input or sample data
2. **Configuration Screen**: 
   - Enter custom numbers (if selected)
   - Choose a sorting algorithm
   - Adjust animation speed
3. **Visualization Screen**:
   - Click "Play" to start the animation
   - Use "Pause" to stop temporarily
   - Click "Reset" to go back to the first step
   - Click "New Sort" to start over with different settings

## API Endpoints

### `GET /`
Returns API information

### `POST /sort`
Sorts an array using the specified algorithm

**Request Body:**
```json
{
  "algorithm": "bubble",
  "data": [64, 34, 25, 12, 22, 11, 90]
}
```

**Response:**
```json
{
  "algorithm": "bubble",
  "steps": [
    {
      "array": [64, 34, 25, 12, 22, 11, 90],
      "comparing": [0, 1],
      "swapped": [],
      "explanation": "Comparing 64 and 34"
    },
    ...
  ],
  "total_steps": 50
}
```

## Algorithms Included

1. **Bubble Sort** - O(n²) - Simple comparison-based algorithm
2. **Selection Sort** - O(n²) - Selects minimum element repeatedly
3. **Insertion Sort** - O(n²) - Builds sorted array one element at a time
4. **Merge Sort** - O(n log n) - Divide and conquer algorithm
5. **Quick Sort** - O(n log n) average - Partition-based sorting
6. **Heap Sort** - O(n log n) - Uses binary heap data structure
7. **Shell Sort** - O(n log n) to O(n²) - Generalized insertion sort
8. **Counting Sort** - O(n + k) - Non-comparison based, for integers
9. **Radix Sort** - O(d * (n + k)) - Sorts by individual digits

## Troubleshooting

### Backend Connection Error
- Ensure Flask server is running on port 5000
- Check if any other application is using port 5000
- Verify CORS is properly installed

### Import Errors
- Make sure all algorithm files are in the `algorithms` folder
- Ensure `__init__.py` exists in the algorithms folder
- Check that virtual environment is activated

### Visualization Not Working
- Ensure browser allows localhost connections
- Check browser console for any JavaScript errors
- Verify the backend URL in index.html matches your Flask server

## Technologies Used

- **Frontend**: HTML5, Tailwind CSS (via CDN), Vanilla JavaScript
- **Backend**: Python Flask
- **APIs**: RESTful API with JSON responses
- **CORS**: Flask-CORS for cross-origin requests

## Future Enhancements

- Time complexity analysis display
- Space complexity visualization
- Comparison between multiple algorithms
- Export visualization as video/GIF
- More sorting algorithms (Tim Sort, Intro Sort, etc.)
- Mobile responsive improvements

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

---

**Enjoy visualizing sorting algorithms! 🎨✨**