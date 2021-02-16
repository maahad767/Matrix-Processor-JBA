def main():
    while True:
        print('1. Add matrices\n'
              '2. Multiply matrix by a constant\n'
              '3. Multiply matrices\n'
              '4. Horizontal line\n'
              '5. Calculate a determinant\n'
              '6. Inverse matrix\n'
              '0. Exit')

        command = int(input("Your choice: "))
        if command == 1:
            rows1, cols1 = tuple(int(x) for x in input("Enter size of first matrix: ").split())
            print("Enter first matrix:")
            first_mat = take_matrix(rows1)
            rows2, cols2 = tuple(int(x) for x in input("Enter size of second matrix: ").split())
            print("Enter second matrix:")
            second_mat = take_matrix(rows2)

            if rows1 != rows2 or cols1 != cols2:
                print("The operation cannot be performed.")
                continue
            result_matrix = add_matrices(first_mat, second_mat)
            print("The result is:")
            print_matrix(result_matrix)

        elif command == 2:
            rows, cols = tuple(int(x) for x in input("Enter size of matrix: ").split())
            print("Enter matrix:")
            matrix = take_matrix(rows)
            print("Enter constant:")
            scalar = float(input())
            result_matrix = scalar_multiplication(matrix, scalar)
            print("The result is:")
            print_matrix(result_matrix)

        elif command == 3:
            rows1, cols1 = tuple(int(x) for x in input("Enter size of first matrix: ").split())
            print("Enter first matrix:")
            first_mat = take_matrix(rows1)
            rows2, cols2 = tuple(int(x) for x in input("Enter size of second matrix: ").split())
            print("Enter second matrix:")
            second_mat = take_matrix(rows2)
            if cols1 != rows2:
                print("The operation cannot be performed.")
                continue
            result_matrix = matrix_multiplication(list(first_mat), list(second_mat))
            print("The result is:")
            print_matrix(result_matrix)

        elif command == 4:
            print('1. Main diagonal\n'
                  '2. Side diagonal\n'
                  '3. Vertical line\n'
                  '4. Horizontal line')

            direction = int(input("Your choice: "))
            rows, cols = tuple(int(x) for x in input("Enter size of matrix: ").split())
            print("Enter matrix:")
            matrix = take_matrix(rows)
            result_matrix = transpose_matrix(matrix, direction)
            print_matrix(result_matrix)

        elif command == 5:
            rows, cols = tuple(int(x) for x in input("Enter size of matrix: ").split())
            print("Enter matrix:")
            matrix = take_matrix(rows)
            result = determinant(matrix)
            print(result)

        elif command == 6:
            rows, cols = tuple(int(x) for x in input("Enter size of matrix: ").split())
            print("Enter matrix:")
            matrix = take_matrix(rows)
            det = determinant(matrix)
            if det == 0:
                print("This matrix doesn't have an inverse.")
                continue
            result_matrix = inverse_matrix(matrix)
            print("here")
            print_matrix(result_matrix)
            print("printed")
        elif command == 0:
            exit()


def take_matrix(row):
    result_mat = []
    for _ in range(row):
        result_mat.append(list(float(x) for x in input().split()))
    return result_mat


def add_matrices(first, second):
    result_mat = []
    for row1, row2 in zip(first, second):
        row = []
        for col1, col2 in zip(row1, row2):
            row.append(col1 + col2)
        result_mat.append(row)

    return result_mat


def scalar_multiplication(matrix, scalar):
    result = []
    for row in matrix:
        row = [col * scalar for col in row]
        result.append(row)
    return result


def matrix_multiplication(first_mat, second_mat):
    cols = len(second_mat)

    result_mat = []
    for row in first_mat:
        new_row = []
        for i in range(len(second_mat[0])):  # number of first_row == second_column
            new_el = 0
            for j, re in zip(range(cols), row):
                new_el += re * second_mat[j][i]
            new_row.append(new_el)
        result_mat.append(new_row)

    return result_mat


def transpose_matrix(matrix, direction):
    result_matrix = []
    if direction == 1:
        # row to column
        result_matrix = [[None for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result_matrix[j][i] = matrix[i][j]

    elif direction == 2:
        # last row to first column
        result_matrix = transpose_matrix(matrix, 1)
        result_matrix = transpose_matrix(result_matrix, 3)
        result_matrix = transpose_matrix(result_matrix, 4)
    elif direction == 3:
        # last column to first column
        for row in matrix:
            result_matrix.append(reversed(row))

    elif direction == 4:
        # last row to first row
        for row in matrix:
            result_matrix.insert(0, row)

    return result_matrix


def determinant(matrix):
    lengthM = len(matrix)
    if lengthM == 1:
        return matrix[0][0]
    if lengthM == 2:
        detM = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return detM

    detM = 0
    for i in range(lengthM):
        sign = (-1) ** i
        minor = []

        for m in range(1, lengthM):
            row = []
            for n in range(lengthM):
                if i != n:
                    row.append(matrix[m][n])

            minor.append(row)
        detM += matrix[0][i] * sign * determinant(minor)

    return detM


def inverse_matrix(matrix):
    result_matrix = []
    lengthM = len(matrix)
    for i, row in enumerate(matrix):
        new_row = []
        for j, col in enumerate(row):
            sign = (-1) ** (i + j)
            minor = []
            for m in range(lengthM):
                if m != i:
                    row = []
                    for n in range(lengthM):
                        if j != n:
                            row.append(matrix[m][n])
                    minor.append(row)

            new_row.append(sign * determinant(minor))
        result_matrix.append(new_row)
    return scalar_multiplication(transpose_matrix(result_matrix, 1), 1 / determinant(matrix))


def print_matrix(mat):
    for row in mat:
        print(*row)


if __name__ == '__main__':
    main()
