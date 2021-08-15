# mongo-sql-translator
mongo-sql-translator is a tool with which you can transform mongodb queries to SQL queries. Only `find` is implemented



## Usage
```
from src.dependency_containers.translator_container import TranslatorContainer

container = TranslatorContainer()

translator_service = container.translator_service()

sql_query = translator_service.execute(MONGODB_QUERY)
```

## Code structure

In order to process and transform the MongoDb query, it applies a set of steps, main class/entry point is `src/translator.py` which implements a "variation" of the Chain of responsibility pattern, first processing the MongoDB query unpacking it in different parts, and finally calling to `src/query_builder/query_builder.py` to build the SQL query which the result of that process.

Every behavior is encapsulated as a `Command` (`src/commands/`) each one of those commands does only one single thing, respecting the Single Responsibility Software Principle, and is reusable by just injecting them as wish.

Dependency injection is used to decouple classes and making them more testable and abstract; each class inheritances from an Abstract class (use it as programming by interfaces) which defines the `execute` method as the signature of the class to be implemented, so classes can be replaced for others ones if needed only inheriting from the Abstract class, most complex object creations are in `src/dependency_containers`.

Strategy pattern is used for build sql operators, there are 2 strategies, one when it's a regular operator and other one when it is a 'group' operator (`$and[{},{}]/$or[{},{}]`).

Test strategy follows the Piramid strategy, which adds a bunch of pure unit tests (isolated) and fewer integration tests.


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