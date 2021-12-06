from data import input_data



def main():
    data = [(i) for i in input_data.split("\n")]
    gamma_bits = ''

    for i in range(len(data[0])):
        s = sum(int(x[i]) for x in data)
        if s > len(data)/2:
            gamma_bits = gamma_bits + '1'
        else:
            gamma_bits = gamma_bits + '0'
    mask = ''.join([str(1) for i in range(len(data[0]))])
    mask = int(mask, 2)
    gamma = int(gamma_bits, 2)
    epsilon = gamma ^ mask
    print(gamma * epsilon)


if __name__ == '__main__':
    main()