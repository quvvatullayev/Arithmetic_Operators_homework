#Create a variable called 'number' and assign it the two-digit number
#Find the reverse of the number and assign it to a variable called 'answer'.
#Print the answer variable

answer = 0
number = 89
x1 = number%10
number = number//10

x2 = number%10
answer = x1*10 + x2

print(answer)