def solution(s):
    # stack = []
    # for char in s:
    #     if s.count(char) == 1:
    #         stack.append(char)
    stack = [char for char in s if s.count(char) == 1]
    stack.sort()

        # stack.sort()
    return ''.join(stack)




    # for char2 in s:
    #     num = s.count(char2)
    #     if num >= 2:
    #         s = s.replace(char2, '', num)
            # stack.remove(char2)

    return stack

print(solution('abcabcadc'))
print(solution('abdc'))
print(solution('hello'))