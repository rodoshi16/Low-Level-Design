**Keep it simple**

Principle of keeping it simple - its easier to work through bugs, extend and modify. 

Ex:

```
from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass

class Addition(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a + b

class Subtraction(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a - b

class Multiplication(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a * b

class Division(Operation):
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

class Calculator:
    def execute(self, op: Operation, a: float, b: float) -> float:
        return op.calculate(a, b)
```


This has an interface, 4 seperate classes and extra layers - which could easily be refactored into a few if else statements. 


```
class Calculator:
    def calculate(self, operator, a, b):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        else:
            raise NotImplementedError(f"Unknown operator: {operator}")
```

*Signs you're violating KISS*

- added an interface before a second implementation
- introduce an extra layer as just in case
- added functionality 
- Your method has five optional parameters and deeply nested conditionals.
- You used recursion when a loop would have been simpler and clearer.
- A new developer cannot understand your class without reading three other classes first

*How to apply this principle*

1. others should be able to easily read and understand 
2. if there is only one implementation - dont create abstractions 
3. if inheritance is harder to trace, dont use it 
4. each function should be short and easy to test 
5. no need to reinvent the wheel when familiar DSA like list, map, for loop can do the job 