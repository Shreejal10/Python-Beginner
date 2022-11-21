m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))


def matrix(m, n):
    output = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter element[{i+1}][{j+1}]: "))
            row.append(inp)
        output.append(row)
    return output


def addition(A, B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(B)):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output


print("Enter matrix A: ")
A = matrix(m, n)
# print(A)

print("Enter matrix B: ")
B = matrix(m, n)
# print(B)

result = addition(A, B)

print(result)
