import pytest
from src.translator import Translator
from src.dependency_containers.translator_container import TranslatorContainer

use_cases = [{
    "scenario": "db.user.find({name:'julio'});",
    "expected": "SELECT * FROM user WHERE  name=\"julio\";",
  },
  {
    "scenario": "db.user.find({_id:23113},{name:1,age:1});",
    "expected": "SELECT name,age FROM user WHERE  id=\"23113\";",
  },
  {
    "scenario": "db.person.find({_id:23113},{name:1,age:1});",
    "expected": "SELECT name,age FROM person WHERE  id=\"23113\";",
  },
  {
    "scenario": "db.person.find({ first_name: \"Marcos\", last_name: \"Juncos\"});",
    "expected": "SELECT * FROM person WHERE  first_name=\"Marcos\" AND  last_name=\"Juncos\";",
  },
  {
    "scenario": "db.user.find({quantity:{$lt:20}})",
    "expected": "SELECT * FROM user WHERE  quantity<\"20\";",
  },  
  {
    "scenario": "db.user.find({quantity:{$gte:20}})",
    "expected": "SELECT * FROM user WHERE  quantity>=\"20\";",
  },  
  {
    "scenario": "db.products.find({ $or: [{ quantity: { $lt: 20 }}, { price: { $lt: 10 }}] });",
    "expected": "SELECT * FROM products WHERE  ( quantity<\"20\" OR  price<\"10\") ;",  
  },
  {
    "scenario": "db.products.find({ $and: [ { quantity: { $lt: 20 }}, { price: { $lt: 10 }}] });",
    "expected": "SELECT * FROM products WHERE  ( quantity<\"20\" AND  price<\"10\") ;",  
  },  
  {
    "scenario": "db.orders.find({ qty: { $in: [ 5, 15 ] } });",
    "expected": "SELECT * FROM orders WHERE  qty IN (5,15);",
  },
  {
    "scenario": "db.store.find({ center : { $eq : Came}, homepage_featured : { $ne : 0}});",
    "expected": "SELECT * FROM store WHERE  center=\"Came\" AND  homepage_featured!=\"0\";",
  },
]

@pytest.mark.parametrize("case", use_cases)
def test_translator(case):
  container = TranslatorContainer()
  translator_service = container.translator_service()
  response = translator_service.execute(case["scenario"])
  assert response == case["expected"]