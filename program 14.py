number = 371

num = number
digit, sum = 0, 0

length = len(str(num))

for i in range(length):
    # Added assignment operator and used integer division compatibility
    digit = int(num % 10)
    
    # Used floor division to remove the last digit properly
    num = num // 10
    
    sum += pow(digit, length)

if sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")
