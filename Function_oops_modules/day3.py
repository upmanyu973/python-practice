def safe_divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError: 
        print("not divisible")
        return None
    else :
        return result

print(safe_divide(3,0))

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

print(set_age(12))


class InsuffiecientFundsError(Exception):
    pass

def withdraw(balance, amount):
        if balance > amount:
            return balance - amount
        else :
            raise InsuffiecientFundsError("your balance is low!!")
        
print(withdraw(300, 255))


try:
    withdraw(100,150)
except InsuffiecientFundsError as e:
    print(f"Transaction Blocked: {e}")

