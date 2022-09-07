from operation import *


account_creation("zimo", "USD")
money_deposit("zimo", "USD", 300)
money_withdrawal("zimo", "USD", 200)

account_creation("zimo1", "USD")
money_deposit("zimo1", "USD", 300)
money_transfer("zimo", "zimo1", "USD", 50)

list_bank_account_balance("zimo")
list_bank_account_balance("zimo1")

display_transaction_statement("zimo")
display_transaction_statement("zimo1")