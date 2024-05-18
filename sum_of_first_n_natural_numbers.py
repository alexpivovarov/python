n = int(input("Enter a number: "))
sum = 0
for i in range(0, n+1):
    sum = sum + i
print(f"Sum of first {n} natural numbers is "sum")

'''
alternative:
sum = n*(n+1)//2
'''