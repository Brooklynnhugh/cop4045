def find_dup_str(s, n):

    for i in range(len(s) - n + 1):

        sub1 = s[i:i+n]

        for j in range(i+n, len(s) - n + 1):

            sub2 = s[j:j+n]

            if sub1 == sub2:
                return sub1

    return ""

s = input("Enter a string: ")
n = int(input("Enter substring length: "))

result = find_dup_str(s, n)

print(result)
