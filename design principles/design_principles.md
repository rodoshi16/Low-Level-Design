**Don't repeat yourself**

Every piece of knowledge in your system should live in exactly one place. 

When to make something a shared utility?

- if its repeated 3 times 

```
# In auth_service.py
def is_valid_email(email: str) -> bool:
    return email is not None and "@" in email and "." in email

# In payment_service.py
def is_valid_email(email: str) -> bool:
    return email is not None and "@" in email and "." in email

# In messaging_service.py
def is_valid_email(email: str) -> bool:
    return email is not None and "@" in email and "." in email
```

If the email logic is changed, it has to be updated 3 diff times. It can be harder to maintain, higher risk of bugs, bloated codebase, every copy is gonna need its own test cases which will be repeated. 

Refactored code:

```
class EmailValidator:
    @staticmethod
    def is_valid(email: str) -> bool:
        return (
            email is not None
            and "@" in email
            and "." in email
            and (email.endswith(".com") or email.endswith(".org"))
        )
```

Another example: instead of having duplicate codes where each service sends notifications and orders

```
class MessageFormatter:
    @staticmethod
    def format(category: str, user_id: str, detail: str) -> str:
        message = f"[{category}] Hi {user_id}, {detail}"
        return message[0].upper() + message[1:]

class NotificationSender:
    @staticmethod
    def send(user_id: str, message: str) -> None:
        print("Connecting to notification API...")
        print(f"Sending to {user_id}: {message}")
        print("Notification sent successfully.")

class OrderService:
    def notify_order_confirmation(self, user_id: str, order_id: str) -> None:
        message = MessageFormatter.format(
            "Order", user_id, f"your order {order_id} has been confirmed.")
        NotificationSender.send(user_id, message)

class ShippingService:
    def notify_shipment_update(self, user_id: str, tracking_id: str) -> None:
        message = MessageFormatter.format(
            "Shipping", user_id, f"your shipment {tracking_id} is on its way.")
        NotificationSender.send(user_id, message)

class SupportService:
    def notify_ticket_resolution(self, user_id: str, ticket_id: str) -> None:
        message = MessageFormatter.format(
            "Support", user_id, f"your ticket {ticket_id} has been resolved.")
        NotificationSender.send(user_id, message)
```

This is also helps with single responsibility principle because now each class is responsible for its own work - order service can focus on orders, shipping can focus on shipping where notification and messageformater can do the work they need. 