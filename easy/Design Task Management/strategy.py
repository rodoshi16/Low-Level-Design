from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, task):
        pass

class SortByPriority(SortStrategy):
    def sort(self, tasks):
        tasks.sort(key=lambda task: task.priority)
        

class SortByDueDate(SortStrategy):
    def sort(self, tasks):
        #date.max ensures it sorts to the bottom, no real deadlline
        tasks.sort(key=lambda task: task.due_date if task.due_date else date.max)
