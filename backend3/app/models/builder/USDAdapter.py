from app.models.builder.PaymentStrategy import PaymentStrategy
from app.models.builder.ConcreteStrategy import CashPayment

class CurrencyConverter:
    def convert_to_usd(self, amount):
        return int(amount)*83

class PaymentStrategyAdapter(PaymentStrategy):
    def __init__(self, adaptee, currency_converter):
        self.adaptee = adaptee
        self.currency_converter = currency_converter

    def pay(self, amount):
        amount_usd = self.currency_converter.convert_to_usd(amount)
        print(amount_usd)
        self.adaptee.pay(amount_usd)
        return amount_usd

    def authorize(self):
        self.adaptee.authorize()

# Usage example:
# cash_payment = CashPayment()
# currency_converter = CurrencyConverter()
# adapter = PaymentStrategyAdapter(cash_payment, currency_converter)

# # Now you can use the adapter as if it were a PaymentStrategy
# adapter.pay(100)  # Paying 120.0 USD using Cash.
# adapter.authorize()
