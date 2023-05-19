# Benchmark of quicksort in python

This repository contains a benchmark of quicksort in python. It compares the performance of the following implementations:

- The python implementation of quicksort
- A variant with smart partitioning
- The multithreaded python implementation of quicksort
- The multiprocessing python implementation of quicksort
- The C++ implementation of quicksort (using cython)
- A variant with smart partitioning
- (WIP) The parallel C++ implementation of quicksort (using cython and OpenMP)


## Setup

### Getting the code

Clone the repository:

```sh
git clone https://github.com/greg2451/parallel-sort-implementation.git
```

### Configuration

1. Install conda locally following this [link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html).
   We recommend [miniconda](https://docs.conda.io/en/latest/miniconda.html), it is more lightweight and will be sufficient for our usage.
2. Create a new conda environment by executing the following command in your terminal:

   ```sh
   conda create -n cloud_computing python=3.11
   conda activate cloud_computing
   conda install pip
   ```

3. Having the conda environnement activated, install the [requirements](requirements.txt):

   ```sh
   pip install -r requirements.txt
   ```
4. To use the C++ implementation, you have to build the parallel_sort_implementation package. To do that, you should run the following commands:

   ```bash
   python setup.py build_ext --inplace
   ```
   > Note: This will only work if you have a C++ compiler installed on your machine. If you don't, you can install it by running the following command (on linux):
    > ```bash
    > sudo apt-get install build-essential
    > ```
    > on mac:
    > ```bash
    > xcode-select --install
    > ```

5. (WIP/OPTIONAL) If you have OpenMP installed, and you want to use the parallel C++ implementation, you have to modify the [setup.py](setup.py) file and add these arguments to the Extension:
   ```python
   # extra_compile_args=['-fopenmp'],
   ```
   For more info, see the [official tutorial](https://cython.readthedocs.io/en/latest/src/tutorial/parallelization.html)

   Moreover, you should uncomment the line 38 to 52 in the [parallel_sort_implementation/sort.pyx](parallel_sort_implementation/cython/quicksort.pyx) file.
   Then, simply build again, and you should be able to use the parallel C++ implementation.
   Since this is not working yet, you should comment it again before running the benchmark.

   > Note: This will only work if you have OpenMP installed on your machine. If you don't, you can install it by running the following command (on linux):
    > ```bash
    > sudo apt-get install libomp-dev
    > ```
    > on mac:
    > ```bash
    > brew install libomp
    > ```

## Usage

### Run the benchmark

After installing the requirements, you can run the benchmark by executing the following command:

```sh
cd parallel_sort_implementation
python benchmark.py
```

If it's too long, you might want to reduce the size of the lists, or only run a subset of the implementations.
To do that, go into the [file](parallel_sort_implementation/benchmark.py) and change the following lines:

```python
include_multithreaded_and_multiprocessed=False
...
input_size=100
```

#### Expected output

You will see some outputs in the terminal, and then a plot will be saved in the [results](parallel_sort_implementation/results) folder. The plot will also open in a new window.

#### Known issues

- The Smart C++ implementation works (and is quite fast) but sometimes it crashes with a segmentation fault. We are still investigating this issue. In the meantime, you can comment each usage of the function `smart_quicksort_cpp`
- The parallel C++ implementation is not working yet on macOS.
- Depending on your setup, the multithreaded and multiprocessing implementations might be very slow.
- If you don't close the plot window, the script will not terminate, and your terminal will be blocked.

## Development setup

This section should only be necessary if you want to contribute to the project.

Start by installing the [dev-requirements](dev-requirements.txt):

```sh
pip install -r dev-requirements.txt
```

### Running the tests

We use python unittest for the tests.
To run the tests, execute the following command:

```bash
./run_tests.sh
```

### Enabling the pre-commit hooks

Run the following command at the root of the repository:

```sh
pre-commit install
```
