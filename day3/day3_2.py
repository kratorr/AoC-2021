from data import input_data



def main():
    data = [(i) for i in input_data.split("\n")]
    horizontal = 0
    depth = 0
    aim = 0

    for action in data:
        if not action:
            break
        direct, value = action.split(' ')
        if direct == 'forward':
            horizontal += int(value)
            depth += aim * int(value)
        elif direct == 'down':
            aim += int(value)
        elif direct == 'up':
            aim -= int(value)

    print(horizontal * depth)


if __name__ == '__main__':
    main()