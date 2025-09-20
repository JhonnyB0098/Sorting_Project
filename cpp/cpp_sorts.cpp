#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <algorithm>

namespace py = pybind11;

std::vector<int> cpp_quick_sort(std::vector<int> arr) {
    if (arr.size() <= 1) return arr;
    int pivot = arr[arr.size()/2];
    std::vector<int> left, right, equal;
    for (int num : arr) {
        if (num < pivot) left.push_back(num);
        else if (num == pivot) equal.push_back(num);
        else right.push_back(num);
    }
    auto l = cpp_quick_sort(left);
    auto r = cpp_quick_sort(right);
    l.insert(l.end(), equal.begin(), equal.end());
    l.insert(l.end(), r.begin(), r.end());
    return l;
}

void merge(std::vector<int>& arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    std::vector<int> L(arr.begin()+l, arr.begin()+m+1);
    std::vector<int> R(arr.begin()+m+1, arr.begin()+r+1);
    int i=0, j=0, k=l;
    while(i<n1 && j<n2) {
        if(L[i]<=R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while(i<n1) arr[k++] = L[i++];
    while(j<n2) arr[k++] = R[j++];
}

void mergeSort(std::vector<int>& arr, int l, int r) {
    if(l<r) {
        int m = l+(r-l)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }
}

std::vector<int> cpp_merge_sort(std::vector<int> arr) {
    mergeSort(arr, 0, arr.size()-1);
    return arr;
}

void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i;
    int l = 2*i+1;
    int r = 2*i+2;
    if(l<n && arr[l]>arr[largest]) largest=l;
    if(r<n && arr[r]>arr[largest]) largest=r;
    if(largest!=i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

std::vector<int> cpp_heap_sort(std::vector<int> arr) {
    int n = arr.size();
    for(int i=n/2-1;i>=0;i--) heapify(arr,n,i);
    for(int i=n-1;i>0;i--) {
        std::swap(arr[0],arr[i]);
        heapify(arr,i,0);
    }
    return arr;
}

int getMax(std::vector<int>& arr) {
    int mx = arr[0];
    for(int num: arr) if(num>mx) mx=num;
    return mx;
}

void countSort(std::vector<int>& arr, int exp) {
    int n = arr.size();
    std::vector<int> output(n);
    int count[10] = {0};
    for(int i=0;i<n;i++) count[(arr[i]/exp)%10]++;
    for(int i=1;i<10;i++) count[i]+=count[i-1];
    for(int i=n-1;i>=0;i--) {
        output[count[(arr[i]/exp)%10]-1] = arr[i];
        count[(arr[i]/exp)%10]--;
    }
    for(int i=0;i<n;i++) arr[i]=output[i];
}

std::vector<int> cpp_radix_sort(std::vector<int> arr) {
    int m = getMax(arr);
    for(int exp=1; m/exp>0; exp*=10)
        countSort(arr,exp);
    return arr;
}

PYBIND11_MODULE(cpp_sorts, m) {
    m.doc() = "C++ sorting algorithms bindings";
    m.def("cpp_quick_sort", &cpp_quick_sort);
    m.def("cpp_merge_sort", &cpp_merge_sort);
    m.def("cpp_heap_sort", &cpp_heap_sort);
    m.def("cpp_radix_sort", &cpp_radix_sort);
}
