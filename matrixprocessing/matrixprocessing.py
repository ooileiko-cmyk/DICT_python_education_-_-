# matrixprocessing.py

def read_matrix():
    size = input("Enter matrix size: > ").split()
    if len(size) == 2:
        rows, cols = map(int, size)
    else:
        rows = int(size[0])
        cols = 1
    matrix = []
    for _ in range(rows):
        row = list(map(float, input("> ").split()))
        # добавляем недостающие элементы, если ввод короткий
        while len(row) < cols:
            row.append(0.0)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(round(x, 2)).rstrip('0').rstrip('.') if '.' in str(round(x, 2)) else str(int(x)) for x in row))

def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("ERROR")
        return
    result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    print_matrix(result)

def multiply_by_constant(matrix, const):
    result = [[x * const for x in row] for row in matrix]
    print_matrix(result)

def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        print("The operation cannot be performed.")
        return
    result = [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
    print_matrix(result)

def transpose(matrix, type="main"):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0]*rows for _ in range(cols)]
    if type == "main":
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
    elif type == "side":
        for i in range(rows):
            for j in range(cols):
                result[cols-j-1][rows-i-1] = matrix[i][j]
    elif type == "vertical":
        for i in range(rows):
            for j in range(cols):
                result[i][cols-j-1] = matrix[i][j]
    elif type == "horizontal":
        for i in range(rows):
            for j in range(cols):
                result[rows-i-1][j] = matrix[i][j]
    print_matrix(result)

def determinant(matrix):
    import copy
    def det(m):
        if len(m) == 1:
            return m[0][0]
        if len(m) == 2:
            return m[0][0]*m[1][1] - m[0][1]*m[1][0]
        res = 0
        for c in range(len(m)):
            minor = [row[:c]+row[c+1:] for row in m[1:]]
            res += ((-1)**c) * m[0][c] * det(minor)
        return res
    print(int(det(matrix)))

def inverse_matrix(matrix):
    import copy
    det_value = 0
    def det(m):
        if len(m) == 1: return m[0][0]
        if len(m) == 2: return m[0][0]*m[1][1]-m[0][1]*m[1][0]
        res = 0
        for c in range(len(m)):
            minor = [row[:c]+row[c+1:] for row in m[1:]]
            res += ((-1)**c)*m[0][c]*det(minor)
        return res
    det_value = det(matrix)
    if det_value == 0:
        print("This matrix doesn't have an inverse.")
        return
    n = len(matrix)
    # Формуємо матрицю алгебраїчних доповнень
    cofactor = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [row[:j]+row[j+1:] for row_idx,row in enumerate(matrix) if row_idx!=i]
            cofactor[i][j] = ((-1)**(i+j)) * det(minor)
    # транспонування
    adj = [[cofactor[j][i] for j in range(n)] for i in range(n)]
    # ділимо на визначник
    inv = [[adj[i][j]/det_value for j in range(n)] for i in range(n)]
    print_matrix(inv)

def main():
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: > ")
        if choice == "0":
            break
        elif choice == "1":
            print("Enter first matrix:")
            a = read_matrix()
            print("Enter second matrix:")
            b = read_matrix()
            add_matrices(a, b)
        elif choice == "2":
            print("Enter matrix:")
            a = read_matrix()
            const = float(input("Enter constant: > "))
            multiply_by_constant(a, const)
        elif choice == "3":
            print("Enter first matrix:")
            a = read_matrix()
            print("Enter second matrix:")
            b = read_matrix()
            multiply_matrices(a, b)
        elif choice == "4":
            print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
            t_choice = input("Your choice: > ")
            a = read_matrix()
            if t_choice == "1":
                transpose(a, "main")
            elif t_choice == "2":
                transpose(a, "side")
            elif t_choice == "3":
                transpose(a, "vertical")
            elif t_choice == "4":
                transpose(a, "horizontal")
        elif choice == "5":
            a = read_matrix()
            determinant(a)
        elif choice == "6":
            a = read_matrix()
            inverse_matrix(a)
        else:
            print("Invalid choice!")

        if name == "main":
            main()