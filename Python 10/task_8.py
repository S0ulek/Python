pit = int(input("Введите глубину ямы: "))
for line in range(pit):
    for left_num in range(pit,pit - line - 1, -1):
        print(left_num, end = "")
    point_count = 2 * (pit - line -1)
    print("." * point_count, end = "")
    for right_num in range(pit - line, pit + 1):
        print(right_num, end = "")
    print()