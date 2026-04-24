class Payment:
    def pay(self_kdm):
        print("Processing payment")

class CashPayment(Payment):
    def pay(self_kdm):
        print("Payment made using cash")

class CardPayment(Payment):
    def pay(self_kdm):
        print("Payment made using credit card")

payments_kdm = [CashPayment(), CardPayment()]
for p in payments_kdm:
    p.pay()
    # Montes, Karen