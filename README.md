# Benchmark of quicksort in python

## Use the C++ implementation

To do that, you should first build the parallel_sort_implementation package. To do that, you should run the following commands:

```bash
python setup.py build_ext --inplace
```

If the build was successful, the best way to check if it works is by running the tests:

```bash
./run_tests.sh
```

Then, you can run the benchmark with the following command:

```bash
python python_implementation/main_python.py
```