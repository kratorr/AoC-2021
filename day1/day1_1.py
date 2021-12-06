from data import input_data


def main():
    a = [int(i) for i in input_data.split()]
    c = 0
    for i in range(0, len(a)-1):
        if a[i] < a[i+1]:
            c += 1
    print(c)


if __name__ == '__main__':
    main()