This is the implementation of bank system(the second problem) with python

### file structure

accounts.json: a json file to simulate database like mysqldb, it stores account and transaction information.

init.py: run this file to clear the content in accounts.json and create the default account OSL_FEE

operation.py: the most important file that implement all the operations

test.py: a simple test file that create two accounts and make some operations

test1.py: another test file that test if the withdrawal operation satisfied the requirement that user cannot do more than 5 withdrawals of any currency; limit to be reset every 5 minutes of last withdrawal.

An example to run:

```python
python init.py
python test.py
```

