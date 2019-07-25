def ucgenmi(a,b,hipotenüs):
    if a**2 + b**2 == hipotenüs**2:
        return "bu bir üçgendir."
    else:
        return "bu bir üçgen değildir."
a = ucgenmi(3,4,5)
print(a)
