Functional requirements:

- contains prices and volumes with which people want to buy a given stock
- bid side represents open offers to buy
- ask side represents open orders to sell
Trades are made when highest bid >= lowest ask 
- unfilled orders get stored in order book
- price time priority: orders are executed at best possible price first, if many orders of same price - earliest submitted wins 

Entities:

OrderBook

- self.price_levels = {price: [Doubly Linked List]}
- self.ids = {id: Node}
* matching() -> bool:
* add_order(order): 

check if order.price already in self.price_levels
update self.id

* cancel_order(order)

- find Node from self.id and delete 


Tradeoffs:

- buys asc, sells desc 0(1), add 0(n), 0(n): list
- heap, 0(1) access to highest bid, log(n) to insert
- PQ, (price, time) -> Order object, dict: {id: Order}, cancellation: 0(1)

Ideal Data structure ordering:

- {price: [Doubly Linked list of orders of that price based on time]}
- {id: Node}
BUT you cannot just have a normal hashmap with prices - not gonna be sorted order 
- keep a sorted order hashmap so you can have 


Order

- id
- price
- quantity
- side
- filled_amount
- type


