#BRYAN CHAVARRIA
#1657040
def main():
    x1 = int(input())
    y1 = int(input())
    n1 = int(input())

    x2 = int(input())
    y2 = int(input())
    n2 = int(input())

    solution_found = False

    for x in range(-10, 11):
        for y in range(-10, 11):
            if x1 * x + y1 * y == n1 and x2 * x + y2 * y == n2:
                print(x, y)
                solution_found = True

    if not solution_found:
        print("No solution")


if __name__ == '__main__':
    main()