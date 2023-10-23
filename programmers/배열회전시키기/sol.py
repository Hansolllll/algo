def solution(numbers, direction):
    for num in numbers:
        if direction == 'right':
            a = numbers[-1]
            numbers.pop()
            numbers.insert(0, a)

        elif direction == 'left':
            b = numbers[0]
            numbers.pop(0)
            numbers.insert(len(numbers), b)
        return numbers

print(solution([1,2,3], 'right'))
print(solution([4, 455, 6, 4, -1, 45, 6], 'left'))