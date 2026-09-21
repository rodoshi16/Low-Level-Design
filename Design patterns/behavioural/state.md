***State***

The code depends on the state of the object. 

For example, withdrawing from an ATM depends on wat state it is in: 

IDLE
CARD_INSERTED
AUTHENTICATED

```
class ATM:
    def __init__(self):
        self.state = "IDLE"

    def withdraw(self):
        if self.state == "IDLE":
            print("Please insert your card")

        elif self.state == "CARD_INSERTED":
            print("Please enter your PIN")

        elif self.state == "AUTHENTICATED":
            print("Dispensing cash")

```

But imagine you have lots of operations:

withdraw()
insert_card()
enter_pin()
eject_card()
check_balance()
deposit()

Now every method starts doing:

if state == "IDLE":
    ...

elif state == "CARD_INSERTED":
    ...

elif state == "AUTHENTICATED":
    ...


ATM
├── withdraw()
│     ├── if IDLE
│     ├── if CARD_INSERTED
│     └── if AUTHENTICATED
│
├── insert_card()
│     ├── if IDLE
│     ├── if CARD_INSERTED
│     └── if AUTHENTICATED
│
├── enter_pin()
│     ├── if IDLE
│     ├── if CARD_INSERTED
│     └── if AUTHENTICATED
│
└── eject_card()
      ├── if IDLE
      ├── if CARD_INSERTED
      └── if AUTHENTICATED


So, we create classes for idle, card inserted and authenticated

```

class ATMState:
    def withdraw(self, atm):
        raise NotImplementedError

class IdleState(ATMState):
    def withdraw(self, atm):
        print("Insert card")


class CardInsertedState(ATMState):
    def withdraw(self, atm):
        print("Enter PIN")


class AuthenticatedState(ATMState):
    def withdraw(self, atm):
        print("Dispensing cash")

```

Now for the ATM class, 

```

class ATM:
    def __init__(self):
        self.state = IdleState()

    def withdraw(self):
        self.state.withdraw(self)


```

NOTE THE TRADEOFF: this can def create more code since you need to write all operations for each state - discuss with interviewer






