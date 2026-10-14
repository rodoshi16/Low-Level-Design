class Task Management:
    def __init__(self):
        self.users = collections.defaultdict(list)
        self.tasks = collections.defaultdict(list)
        self.map = collections.defaultdict(list)

        def create_user(self, name, email):
            u = User(name, email)
            self.users[u.userid] = u
            return user
        
        def create_task(self, user_id, name, des, due_date, priority, assignee_id)
            if user_id in self.users:
                t = Task(name, des, due_date, priority, assignee_id)
                self.map[user_id].append(t)
                self.tasks[t.id] = t
            t.add_observer.append(self.users[assignee_id])
        
        def delete_task(self, task_id):
            if task_id in self.tasks:
                del self.task[task_id]
        
        def search_task(self, keyword: str, sorting_strategy:Strategy):
            matching_tasks = []

            for task in self.tasks:
                if keyword.lower() in task.name() or keyword.lower() in task.des.lower():
                    matching_tasks.append(task)
            
            sorting_strategy(matching_tasks)
            return matching_tasks

class TaskStatus(Enum):
    IN_PROGRESS = "In progress"
    COMPLETED = 'COMPLETED'
    PENDING = 'PENDING'


class User:
    def __init__(self, id, name, email):
        self.user_id = id
        self.name = name
        self.email = email

class Task:
    def __init__(self, builder):
        self.userid = str(uuid.uuid4())
        self.name = name
        self.des = des
        self.status = TaskStatus.PENDING
        self.due_date = due_date
        self.priority = priority
        self.assignee_id = assignee_id
        self._observers: List[TaskObserver]
    
    def add_observer(self, User):
        self._observers.append(User)
    
    def remove_observer(self, User):
        if User in self._observers:
            self._observers.remove(User)

    def notify_observers(self, change_type):
        for observer in self._observers:
            observer.update(self, change_type)


    class TaskBuilder:
        def __init__(self, name):
            self.name = name
            self._des = ""
            self.due_date = None
            self._priority = None
            self.assignee_id = None
        
        def des(self, des):
            self._des = des
            return self 
        
        def des(self, due_date):
            self._due_date = due_date
            return self 
        
        def priority(self, priority: TaskPriority) -> 'Task.TaskBuilder':
            self._priority = priority
            return self
        
        def assignee(self, assignee: User) -> 'Task.TaskBuilder':
            self._assignee = assignee
            return self
        
        def build(self):
            return Task(self)        
        
          
        
