if __name__ == '__main__':
    INPUT_FILE = "inputs/02_Dive.txt"
    with open(INPUT_FILE) as f:
        input = [{x.split(" ")[0]: int(x.split(" ")[1])} for x in f.read().split("\n")[:-1]]

    # Both stars
    depth, pos, aim, depth2 = 0, 0, 0, 0
    for i in input:
        for command, value in i.items():
            if command == "forward":
                pos += value
                depth2 += aim * value
            elif command == "up":
                depth -= value
                aim -= value
            elif command == "down":
                depth += value
                aim += value

    print("Dive Part 1:", depth * pos)
    print("Dive Part 2:", depth2 * pos)
