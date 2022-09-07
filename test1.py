from operation import *

account_creation("zimo", "USD")
money_deposit("zimo", "USD", 300)

money_withdrawal("zimo", "USD", 10)
money_withdrawal("zimo", "USD", 20)
money_withdrawal("zimo", "USD", 30)
money_withdrawal("zimo", "USD", 40)
money_withdrawal("zimo", "USD", 50)
money_withdrawal("zimo", "USD", 60)

display_transaction_statement("zimo")
