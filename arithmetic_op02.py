#Create a varaible 'number' and assign it the value of 43.

#Create a variable 'answer' and assign it the sum of the number's digits.

#Print answer.

number = 43
answer = 0

x1 = number%10
number = number//10
answer += x1

x2 = number%10
answer += x2

print(answer)
