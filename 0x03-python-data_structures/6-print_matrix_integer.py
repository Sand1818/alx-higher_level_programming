
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for san in range(len(matrix)):
        for jel in range(len(matrix[san])):
            print("{:d}".format(matrix[san][jel]), end="")
            if jel != (len(matrix[san]) - 1):
                print(" ", end="")
        print("")
