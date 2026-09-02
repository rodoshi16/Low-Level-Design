***Interfaces***

Define what a component should do, not how it should do it. It is a list of methods that any implementing class must provide. Different classes can implement them in diff ways. 

The what, not the how. 

```

class Payment(ABC):
    @abstractmethod
    def initiate_payment(self, amount):
        pass

class Stripe(Payment):
    def initiate_method(self, amount):
        print("stripe")
    
class BankCard(Payment):
    def initiate_method(self, amount):
        print("bank")


class CheckoutService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
      def set_payment_gateway(self, payment_gateway):
        self.payment_gateway = payment_gateway
```

For checkout, it doesnt matter what youre using - as long as it is accepted as a payment. 

stripe = Payment()
c = checkout(stripe)
c.set_payment_gateway(100); 





