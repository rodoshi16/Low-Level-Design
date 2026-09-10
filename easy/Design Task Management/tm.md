**Design Task Management**

Functional requirements:

- managing task: create task and set due dates 
- des, due date, status: [not started, in progress, cancelled, completed], priority: 1 to n 
- search from list of users tasks
- collaboration on tasks: add other users 
- users can cancel a task 
- handle concurrency
- handle data consistency
- completed tasks are stored in a diff data structure


Identify Entities:

- Task Management

* users: list
* 

- get_task_interface
@abstractmethod
* sort()


- Users

* tasks: dict (key - id value: task obj)
  name_map: dict (name: [id])

* create_task(name, des, due_date, status, priority)
* date(get_task_interface)(name, due_date) -> List[Task.name]
* priority(get_task_interface)(name, priority) -> List[Task.name]
* remove_task(name) -> None (remove key val pair)
* add_collaborator(name, User): 

* start_task(name, des): [in progress]
task = d[name]
task.status = in_progress

* finish_task(name, des): [completed]
task = d[name]
task.status = completed

- Task : 

* name,
des: str,
due_date: Date,  
status (enum class), 
priority: int
id: int

