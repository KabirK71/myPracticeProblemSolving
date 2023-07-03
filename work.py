# Function to calculate the factorial of a number
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Function to calculate the combination (nCm)


def calculate_combination(n, m):
    if n < m:
        return 0  # Invalid combination
    numerator = factorial(n)
    denominator = factorial(m) * factorial(n - m)
    combination = numerator // denominator
    return combination


s = input()
s = s[0:3]
n, m = s.split(" ")
n = int(n)
m = int(m)
l1 = []
l2 = []

for i in range(m):
    l1.append(input())

for i in l1:
    i = i[0:3]
    l, k = i.split(" ")
    if l not in l2:
        l2.append(l)
    if k not in l2:
        l2.append(k)

secure = m
insecure = calculate_combination(len(l2), 2) - m

print(str(insecure) + " " + str(secure))
