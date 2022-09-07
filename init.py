import json

with open('accounts.json','w') as f:
    json.dump({"OSL_FEE":{"HKD":[0,[],[]],"USD":[0,[],[]],"SGD":[0,[],[]]}},f)