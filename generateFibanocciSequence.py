
'''
We will use a list to store the Fibanocci sequence.
Below are the initial values in the sequence.
'''
fibanocci_sequence = [0, 1]

#This is a function to generate the Fibanocci sequence

def genFibanocci():
    global i, j
    i = 0
    j = 1
    index = 0

    while index < 100:
        i = i + j
        j = i + j
        fibanocci_sequence.append(i) #appending the new Fibanocci number to the list
        fibanocci_sequence.append(j) #appending the new Fibanocci number to the list
        index = index + 1
        
genFibanocci() #calling the Fibanocci sequence generator

print(fibanocci_sequence)
