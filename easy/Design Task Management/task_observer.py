from abc import ABC, abstractmethod

class TaskObserver(ABC):
    @abstractmethod
    def update(self, task: 'Task'):
        pass


class ActivityLogger(TaskObserver):
    def update(self, task, change_type):
        print(f"Logger: Task was updated, Change: {change_type}")
        