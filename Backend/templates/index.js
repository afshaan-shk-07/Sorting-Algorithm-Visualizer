// Global state
        let useCustomData = false;
        let sortingSteps = [];
        let currentStepIndex = 0;
        let isPlaying = false;
        let playInterval = null;
        let speed = 500;
        let currentAlgorithmName = '';
        let customArray=[];
        const algorithmDescriptions = {
            bubble: 'Compares adjacent elements and swaps them if they are in wrong order. Pass through the list repeatedly.',
            selection: 'Finds the minimum element and places it at the beginning. Repeats for remaining unsorted portion.',
            insertion: 'Builds final sorted array one item at a time by inserting elements into their correct position.',
            merge: 'Divides array into halves, recursively sorts them, then merges the sorted halves.',
            quick: 'Picks a pivot element and partitions array around it, then recursively sorts partitions.',
            heap: 'Builds a max heap, then repeatedly extracts maximum element and rebuilds heap.',
            shell: 'Generalization of insertion sort that allows exchange of far apart elements.',
            counting: 'Counts occurrences of each value, then reconstructs sorted array from counts.',
            radix: 'Sorts numbers digit by digit starting from least significant digit.'
        };

        const algorithmNames = {
            bubble: 'Bubble Sort',
            selection: 'Selection Sort',
            insertion: 'Insertion Sort',
            merge: 'Merge Sort',
            quick: 'Quick Sort',
            heap: 'Heap Sort',
            shell: 'Shell Sort',
            counting: 'Counting Sort',
            radix: 'Radix Sort'
        };

        const algorithmTimeComplexity = {
            bubble: {
                name: "Bubble Sort",
                best: "O(n)",
                average: "O(n²)",
                worst: "O(n²)",
                space: "O(1)"
            },
            selection: {
                name: "Selection Sort",
                best: "O(n²)",
                average: "O(n²)",
                worst: "O(n²)",
                space: "O(1)"
            },
            insertion: {
                name: "Insertion Sort",
                best: "O(n)",
                average: "O(n²)",
                worst: "O(n²)",
                space: "O(1)"
            },
            merge: {
                name: "Merge Sort",
                best: "O(n log n)",
                average: "O(n log n)",
                worst: "O(n log n)",
                space: "O(n)"
            },
            quick: {
                name: "Quick Sort",
                best: "O(n log n)",
                average: "O(n log n)",
                worst: "O(n²)",
                space: "O(n)"
            },
            heap: {
                name: "Heap Sort",
                best: "O(n log n)",
                average: "O(n log n)",
                worst: "O(n log n)",
                space: "O(1)"
            },
            shell: {
                name: "Shell Sort",
                best: "O(n log n)",
                average: "O(n log n)",
                worst: "O(n²)",
                space: "O(1)"
            },
            counting: {
                name: "Counting Sort",
                best: "O(n + k)",
                average: "O(n + k)",
                worst: "O(n + k)",
                space: "O(k)"
            },
            radix: {
                name: "Radix Sort",
                best: "O(nk)",
                average: "O(nk)",
                worst: "O(nk)",
                space: "O(n + k)"
            }
        };


        function generateRandomData(len,min,max){
            const arr=[];
            for(let i=0;i<len;i++){
                arr.push(Math.floor(Math.random()*(max-min+1))+min)
            }
            console.log(arr)
            customArray = arr
            return arr;
        }

        function updateArrayLength(){
            const len = document.getElementById("arraySlider").value;
            document.getElementById("arrayLengthDisplay").innerText = `Current: ${len}`
            generateRandomData(len,5,100)
        }

        function goToInput(custom) {
            useCustomData = custom;
            document.getElementById('welcomeScreen').classList.add('hidden');
            document.getElementById('inputScreen').classList.remove('hidden');

            if (custom) {
                document.getElementById('customInputSection').classList.remove('hidden');
            }else{
                document.getElementById('arrayLength').classList.remove('hidden');
                updateArrayLength(10,5,10)
            }
            updateAlgorithmDescription();
        }

        function updateAlgorithmDescription() {
            const select = document.getElementById('algorithmSelect');
            const description = document.getElementById('algorithmDescription');
            description.textContent = algorithmDescriptions[select.value];
        }

        function updateSpeedDisplay() {
            const slider = document.getElementById('speedSlider');
            speed = parseInt(slider.value);
            document.getElementById('speedDisplay').textContent = `Current: ${speed}ms`;
        }

        async function startVisualization() {
            const algorithm = document.getElementById('algorithmSelect').value;
            currentAlgorithmName = algorithmNames[algorithm];
            const complexity = algorithmTimeComplexity[algorithm]

            let data;
            if (useCustomData) {
                const input = document.getElementById('customInput').value;
                const numbers = input.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
                if (numbers.length === 0) {
                    alert('Please enter valid numbers separated by commas');
                    return;
                }
                data = numbers;
            } else {
                data = customArray
            }

            // Call Flask backend
            try {
                const response = await fetch('http://localhost:5000/sort', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        algorithm: algorithm,
                        data: data
                    })
                });

                const result = await response.json();
                sortingSteps = result.steps;
                currentStepIndex = 0;

                // Show visualization screen
                document.getElementById('inputScreen').classList.add('hidden');
                document.getElementById('visualizationScreen').classList.remove('hidden');

                // Update UI
                document.getElementById('algorithmTitle').textContent = currentAlgorithmName;
                document.getElementById('algorithmInfo').textContent = algorithmDescriptions[algorithm];
                document.getElementById('currentAlgorithm').textContent = currentAlgorithmName;
                document.getElementById('arraySize').textContent = `${data.length} elements`;
                document.getElementById('speedText').textContent = `Speed: ${speed}ms`;
                document.getElementById('currentComplexity').innerHTML = `
                        <strong>Best:</strong> ${complexity.best}<br>
                        <strong>Average:</strong> ${complexity.average}<br>
                        <strong>Worst:</strong> ${complexity.worst}<br>
                        <strong>Space:</strong> ${complexity.space}
                        `;
                updateVisualization();
            } catch (error) {
                alert('Error connecting to backend. Make sure Flask server is running on http://localhost:5000');
                console.error('Error:', error);
            }
        }

        function updateVisualization() {
            if (sortingSteps.length === 0) return;

            const step = sortingSteps[currentStepIndex];
            const container = document.getElementById('barsContainer');
            const maxValue = Math.max(...step.array);

            // Clear and rebuild bars
            container.innerHTML = '';

            step.array.forEach((value, index) => {
                const barWrapper = document.createElement('div');
                barWrapper.className = 'flex flex-col items-center gap-2 flex-1';

                const bar = document.createElement('div');
                bar.className = 'bar w-full rounded-t-lg';
                bar.style.height = `${(value / maxValue) * 100}px`;

                // Determine bar color
                if (step.swapped && step.swapped.includes(index)) {
                    bar.classList.add('bg-green-500');
                } else if (step.comparing && step.comparing.includes(index)) {
                    bar.classList.add('bg-yellow-500');
                } else {
                    bar.classList.add('bg-blue-500');
                }

                const label = document.createElement('span');
                label.className = 'text-white text-xs font-semibold';
                label.textContent = value;

                barWrapper.appendChild(bar);
                barWrapper.appendChild(label);
                container.appendChild(barWrapper);
            });

            // Update explanation and info
            document.getElementById('stepExplanation').textContent = step.explanation;
            document.getElementById('currentStep').textContent = `${currentStepIndex + 1} of ${sortingSteps.length}`;
            document.getElementById('currentArray').textContent = `[${step.array.join(', ')}]`;
            document.getElementById('progressText').textContent = `Progress: ${currentStepIndex + 1} / ${sortingSteps.length}`;
            document.getElementById('progressBar').style.width = `${((currentStepIndex + 1) / sortingSteps.length) * 100}%`;
        }

        function togglePlay() {
            isPlaying = !isPlaying;

            if (isPlaying) {
                document.getElementById('playText').textContent = 'Pause';
                document.getElementById('playIcon').innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 9v6m4-6v6m7-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>';

                playInterval = setInterval(() => {
                    if (currentStepIndex < sortingSteps.length - 1) {
                        currentStepIndex++;
                        updateVisualization();
                    } else {
                        togglePlay();
                    }
                }, speed);
            } else {
                document.getElementById('playText').textContent = 'Play';
                document.getElementById('playIcon').innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>';

                if (playInterval) {
                    clearInterval(playInterval);
                    playInterval = null;
                }
            }
        }

        function resetVisualization() {
            if (isPlaying) {
                togglePlay();
            }
            currentStepIndex = 0;
            updateVisualization();
        }

        function newSort() {
            if (isPlaying) {
                togglePlay();
            }
            document.getElementById('visualizationScreen').classList.add('hidden');
            document.getElementById('welcomeScreen').classList.remove('hidden');
            sortingSteps = [];
            currentStepIndex = 0;
        }