numbers = list(map(int, input().split()))

if numbers: 
    average = sum(numbers) / len(numbers)
    print(average)
else:
    print(0)