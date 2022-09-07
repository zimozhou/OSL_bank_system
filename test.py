from operation import *


account_creation("zimo", "USD")
money_deposit("zimo", "USD", 300)
money_withdrawal("zimo", "USD", 200)

account_creation("yuhan", "USD")
money_deposit("yuhan", "USD", 300)
money_transfer("zimo", "yuhan", "USD", 50)

list_bank_account_balance("zimo")
list_bank_account_balance("yuhan")

display_transaction_statement("zimo")
display_transaction_statement("yuhan")