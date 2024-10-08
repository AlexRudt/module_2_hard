def trap(n):
    unique = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                unique += str(i) + str(j)
    return f'{n} - {unique}'

n = int(input())

indiana_jones = trap(n)
print(indiana_jones)