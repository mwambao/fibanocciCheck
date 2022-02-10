#lets import the Fibanocci numbers generators module that we have created.
import  generateFibanocciSequence

#Lets print the Fibanocci numbers from the generator
print(f"Here is the Fibonacci sequence: {generateFibanocciSequence.fibanocci_sequence}")

#Lets copy the generated Fibanocci sequence numbers into another list called sequence.
sequence = generateFibanocciSequence.fibanocci_sequence

#This is a function to check if the number input by the user is in Fibanocci sequence
def checkFibanocci():
    valueToCheck = int(input("Enter an integer to check whether it is a Fibanocci number: "))
    if valueToCheck in sequence:
        print("The number is a Fibonacci number")
    else:
        print("The number is NOT a Fibonacci number")

#Calling the function
checkFibanocci()