# mongo-sql-translator
mongo-sql-translator is a tool with you can transform mongodb queries to SQL queries. Only `find` is implemented



## Usage
```
from src.dependency_containers.translator_container import TranslatorContainer
container = TranslatorContainer()
translator_service = container.translator_service()
sql_query = translator_service.execute(MONGODB_QUERY)
```

## Test

In `tests/` folder there are 2 types of tests

unit: testing each command isolated

integration: testing all commands working together

Run tests:

`docker-compose -f ./docker-compose-test.yml build`

`docker-compose -f ./docker-compose-test.yml up`





## Examples

```
        Input: "db.user.find({name:'julio'});"
        Output: 'SELECT * FROM user WHERE  name="julio";',
    
        Input: "db.user.find({_id:23113},{name:1,age:1});"
        Output: 'SELECT name,age FROM user WHERE  id="23113";',
    
        Input: "db.person.find({_id:23113},{name:1,age:1});"
        Output: 'SELECT name,age FROM person WHERE  id="23113";',
    
        Input: 'db.person.find({ first_name: "Marcos", last_name: "Juncos"});'
        Output: 'SELECT * FROM person WHERE  first_name="Marcos" AND  last_name="Juncos";',
    
        Input: "db.user.find({quantity:{$lt:20}})"
        Output: 'SELECT * FROM user WHERE  quantity<"20";',
    
        Input: "db.user.find({quantity:{$gte:20}})"
        Output: 'SELECT * FROM user WHERE  quantity>="20";',
    
        Input: "db.products.find({ $or: [{ quantity: { $lt: 20 }}, { price: { $lt: 10 }}] });"
        Output: 'SELECT * FROM products WHERE  ( quantity<"20" OR  price<"10") ;',
    
        Input: "db.products.find({ $and: [ { quantity: { $lt: 20 }}, { price: { $lt: 10 }}] });"
        Output: 'SELECT * FROM products WHERE  ( quantity<"20" AND  price<"10") ;',
    
        Input: "db.orders.find({ qty: { $in: [ 5, 15 ] } });"
        Output: "SELECT * FROM orders WHERE  qty IN (5,15);",
    
        Input: "db.store.find({ center : { $eq : Came}, homepage_featured : { $ne : 0}});"
        Output: 'SELECT * FROM store WHERE  center="Came" AND  homepage_featured!="0";',
```