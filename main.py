

def dogs(n, d, c, m, s):
    i = 0
    count = 0
    while i < n:
        if s[i] == 'D':
            count += 1
            if d > 0:
                d -= 1
                c += m
            else:
                return 'NO'
        else:
            if c > 0:
                c -= 1
            else:
                if 'D' in s[i+1:]:
                    return 'NO'
                if count > 0:
                    return 'YES'
        i += 1
    if count == 0:
        return 'YES'
    return 'YES'


sample = int(input())
sample_list = []
for test in range(sample * 2):
    sample_list.append(input())

i = 0
count = 1
while i < len(sample_list) - 1:
    print('Case #' + str(count) + ': ' + dogs(int(sample_list[i].split(' ')[0]), int(sample_list[i].split(' ')[1]), int(sample_list[i].split(' ')[2]), int(sample_list[i].split(' ')[3]), sample_list[i + 1]))
    i += 2
    count += 1

T = int(input("Enter T: "))
for i in range(1, T+1):
    [N, D, C, M] = map(int, input("Enter N D C M: ").split(" "))
    line = input("Enter line: ")
    # print(f"length: {N}")
    if dogs(line, D, C, M):
        print(f'Case #{i}: YES')
    else:
        print(f'Case #{i}: NO')
    print(f"length: {N}")
    print(line.count('D'))




