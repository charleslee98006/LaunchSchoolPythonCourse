# Implement a Wallet class that represents a wallet with a certain amount of money. 
# You want to be able to combine (add) two wallets together to get a new wallet with the combined total amount from both wallets.
class Wallet:
    
    def __init__(self, amount):
        self._amount = amount
        
    @property
    def amount(self):
        return self._amount
    
    def __add__(self, wallet):
        if isinstance(wallet, Wallet):
            return Wallet(self.amount + wallet.amount)
        return NotImplemented
    
    def __str__(self):
        return f'Wallet with ${self.amount}.'

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet)          # Wallet with $80.