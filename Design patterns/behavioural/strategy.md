Data processor can sort in multiple ways

```
class DataProcessor:
    def __init__(self, sorting_strategy):
        self.sorting_strategy = sorting_strategy

    def process(self, method):
        if method == quicksort:
            pass
        if method = bubblesort:
            pass
        if method == mergesort:
            pass

```

Instead of multiple if statements, use strategy 

```
class SortStrategy:
    def sort(self, data):
        raise NotImplementedError


class QuickSort(SortStrategy):
    def sort(self, data):
        ...


class MergeSort(SortStrategy):
    def sort(self, data):
        ...


class DataProcessor:
    def __init__(self, sorting_strategy):
        self.sorting_strategy = sorting_strategy

    def process(self, data):
        return self.sorting_strategy.sort(data)


```
processor = DataProcessor(QuickSort())

Multiple implementations = Strategy
