from app.models.builder.PaymentStrategy import PaymentStrategy

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Cash.")

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Credit/Debit Card.")

class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using UPI.")
