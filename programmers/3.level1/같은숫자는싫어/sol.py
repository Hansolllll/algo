def solution(arr):
    stack = []
    for i in range(len(arr)):
        if len(stack):
            if stack[-1] != arr[i]:
                stack.append(arr[i])
        else:
            stack.append(arr[i])

    return stack

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))