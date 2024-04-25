from app.models.builder.PaymentStrategy import PaymentStrategy

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Cash.")
        return amount
    def authorize(self):
        print("Cash payment authorized")

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Credit/Debit Card.")
        return amount
    def authorize(self):
        print("Authorizing payment...")

class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using UPI.")
        return amount
    def authorize(self):
        print("Authorizing payment...")