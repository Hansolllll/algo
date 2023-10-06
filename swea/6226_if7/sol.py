numbers = range(1, 201)

result = []

for number in numbers:
    if number % 7 == 0 and number % 5 != 0:
        result.append(str(number))

print(','.join(result))