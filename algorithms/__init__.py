# from .python_sorts import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort, radix_sort

# algorithms = {
#     "Bubble Sort": bubble_sort,
#     "Insertion Sort": insertion_sort,
#     "Selection Sort": selection_sort,
#     "Merge Sort": merge_sort,
#     "Quick Sort": quick_sort,
#     "Heap Sort": heap_sort,
#     "Radix Sort": radix_sort,
# }

# try:
#     import cpp_sorts
#     algorithms.update({
#         "C++ Quick Sort": cpp_sorts.cpp_quick_sort,
#         "C++ Merge Sort": cpp_sorts.cpp_merge_sort,
#         "C++ Heap Sort": cpp_sorts.cpp_heap_sort,
#         "C++ Radix Sort": cpp_sorts.cpp_radix_sort,
#     })
# except ImportError:
#     pass
from .python_sorts import (
    bubble_sort, insertion_sort, selection_sort,
    merge_sort, quick_sort, heap_sort, radix_sort
)

# Python algorithms
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,
    "Radix Sort": radix_sort,
}

# Try to import C++ implementations
try:
    import cpp_sorts
    algorithms.update({
        "C++ Quick Sort": cpp_sorts.cpp_quick_sort,
        "C++ Merge Sort": cpp_sorts.cpp_merge_sort,
        "C++ Heap Sort": cpp_sorts.cpp_heap_sort,
        "C++ Radix Sort": cpp_sorts.cpp_radix_sort,
        "C++ Bubble Sort": cpp_sorts.cpp_bubble_sort,
        "C++ Insertion Sort": cpp_sorts.cpp_insertion_sort,
        "C++ Selection Sort": cpp_sorts.cpp_selection_sort,
    })
except ImportError:
    # If C++ extension not built, fallback to Python only
    pass
