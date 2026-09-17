```

class FitnessDataNaive:
    def __init__(self):
        self.steps = 0
        self.active_minutes = 0
        self.calories = 0
        
        # Direct, hardcoded references to all dependent modules
        self.live_display = LiveActivityDisplayNaive()
        self.progress_logger = ProgressLoggerNaive()
        self.notification_service = NotificationServiceNaive()
    
    def new_fitness_data_pushed(self, new_steps, new_active_minutes, new_calories):
        self.steps = new_steps
        self.active_minutes = new_active_minutes
        self.calories = new_calories
        
        print(f"\nFitnessDataNaive: New data received - Steps: {self.steps}, "
              f"ActiveMins: {self.active_minutes}, Calories: {self.calories}")
        
        # Manually notify each dependent module
        self.live_display.show_stats(self.steps, self.active_minutes, self.calories)
        self.progress_logger.log_data_point(self.steps, self.active_minutes, self.calories)
        self.notification_service.check_and_notify(self.steps)
    
    def daily_reset(self):
        # Reset logic...
        if self.notification_service is not None:
            self.notification_service.reset_daily_notifications()
        print("FitnessDataNaive: Daily data reset.")
        self.new_fitness_data_pushed(0, 0, 0)  # Notify with reset state


```

```
def fitness_app_naive_client():
    fitness_data = FitnessDataNaive()

    fitness_data.new_fitness_data_pushed(500, 5, 20)
    fitness_data.new_fitness_data_pushed(9800, 85, 350)
    fitness_data.new_fitness_data_pushed(10100, 90, 380)
    fitness_data.daily_reset()

if __name__ == "__main__":
    fitness_app_naive_client()
```

We want FitnessData to broadcast changes to multiple listeners, without knowing know they are, each module to decide for itself how to respond to changes. 

Observer - broadcasting changes from one centra object to many dependent object. 


Observer interface:

1. Define the observer interface

```
from abc import ABC, abstractmethod

class FitnessDataObserver(ABC):
    @abstractmethod
    def update(self, data):
        pass


```
