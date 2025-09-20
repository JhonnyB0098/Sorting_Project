# C++ Sorting Bindings

## Build Instructions

1. Navigate to the `cpp/` directory:
   ```bash
   cd cpp
   ```

2. Build the extension:
   ```bash
   python setup.py build_ext --inplace
   ```

3. Use in Python:
   ```python
   import cpp_sorts
   cpp_sorts.cpp_quick_sort([5,3,2,8,1])
   ```
