numbers = list(range(1, 5))
numbers = ['a', 'b', 'c', 'd']
n = len(numbers)

for i in range(1<<n):
# for i in range(2**n):와 동일 
    # print(i)

    temp = []
    for j in range(n):
        # print(i, bin(i), bin(1<<j))
        if i & (1<<j):
            temp.append(numbers[j])
    print(temp)