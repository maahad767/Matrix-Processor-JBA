def main():
    # print('Input:')
    rows_first, cols_first = tuple(int(x) for x in input().split())

    first_mat = []

    for _ in range(rows_first):
        first_mat.append(int(x) for x in input().split())

    # rows_second, cols_second = tuple(int(x) for x in input().split())

    # second_mat = []
    # for _ in range(rows_second):
    #     second_mat.append(int(x) for x in input().split())

    # print('Output:')
    # if rows_first != rows_second or cols_first != cols_second:
    #     print('ERROR')
    # else:
    #     result = add_matrices(first_mat, second_mat)
    #     print_matrix(result)

    scalar = int(input())
    print_matrix(scalar_multiplication(first_mat, scalar))


def add_matrices(first, second):
    result_mat = []
    for row1, row2 in zip(first, second):
        row = []
        for col1, col2 in zip(row1, row2):
            row.append(col1+col2)
        result_mat.append(row)

    return result_mat


def scalar_multiplication(matrix, scalar):
    result = []
    for row in matrix:
        row = [col * scalar for col in row]
        result.append(row)
    return result


def print_matrix(mat):
    for row in mat:
        print(*row)


if __name__ == '__main__':
    main()