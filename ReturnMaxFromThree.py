#Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
#zdefiniuj funkcję max_of_three(), która bierze trzy liczby jako argumenty i zwraca największą z nich

def maxOfThree (numberA, numberB, numberC):
    if numberA>=numberB:
        if numberA>=numberC:
            return numberA
        else:
           return numberC
    elif numberB>=numberA:
        if numberB>=numberC:
            return numberB
        else:
            return numberC
    elif numberC>=numberA:
       if numberC>=numberB:
           return numberC
       else:
           return numberB

numberA = input("Write the first number ")
numberB = input("Write the second number ")
numberC = input("Write the third number ")

result=(maxOfThree(numberA, numberB, numberC))
print("The biggest number is " + (result))