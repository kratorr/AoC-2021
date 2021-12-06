from data import input_data


def main():
    a = [int(i) for i in input_data.split()]

    c = 0
    for i in range(0, len(a)-3):
        if a[i] + a[i+1] + a[i+2] < a[i+1] + a[i+2] + a[i+3]:
            c += 1
    print(c)


if __name__ == '__main__':
    main()