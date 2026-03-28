def make_payment(P):

    credit_limit = 1000

    min_payment = 20

    if P <= 0:
        print("Повторить попытку")
    elif P < min_payment:
        print("Повторить попытку")
    elif P > credit_limit:
        print("Повторить попытку")
    else:
        print("Успех")

payment = int(input("Введите сумму платежа: "))
make_payment(payment)             