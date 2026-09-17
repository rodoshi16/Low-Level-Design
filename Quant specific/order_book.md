Functional requirements:

- contains prices and volumes with which people want to buy a given stock
- bid side represents open offers to buy
- ask side represents open orders to sell
Trades are made when highest bid >= lowest ask 
- unfilled orders get stored in order book
- price time priority: orders are executed at best possible price first, if many orders of same price - earliest submitted wins 

Entities:

OrderBook

- self.buys: List of Order
- self.sells: List of Order
* matching() -> bool: if trade happens, return True, otherwise 
* add_order(order)
* cancel_order(order)


Tradeoffs:

- buys asc, sells desc 0(1), add 0(n), 0(n): list
- heap, 0(1) access to highest bid, log(n) to insert
- PQ, (price, time) -> Order object, dict: {id: Order}, cancellation: 0(1)


Order

- id
- price
- quantity
- side
- filled_amount
- type
