from Account import Account
from car import car
from main import main
from payment import payment 

if __name__ == "__main__":

    print ("car")
    print ("Account")
    car = car("que tipo de uber es ? ", Account ("uberx" ))
    print (vars (car))
    print(vars (car.uberx))

    print ("payment")
    payment = payment ("tipo de pago" ,  Account ("efectivo"))
 print (vars (payment))
    print(vars (payment.efectivo))

print ("Account")
Account = Account ("usted es" , main ("cliente"))
print (vars (Account))
print (vars (Account.cliente))
