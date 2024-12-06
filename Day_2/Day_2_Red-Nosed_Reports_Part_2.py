from pathlib import Path
import string

def evaluate(input1, input2, direction=None):
    if direction == "initial":
        if input1 < input2:
            direction = "Increasing"

        elif input1 > input2:
            direction = "Decreasing"

        return True, direction

    elif direction == "Increasing":
        if input1 < input2:
            return True, direction
        else:
            print("Direction was increasing but input1 is greater then input2")
            print(input1, input2)
            return False, direction


    elif direction == "Decreasing":
        if input1 > input2:
            return True, direction
        else:
            print("Direction was decreasing but input1 is less then input2")
            print(input1, input2)
            return False, direction


def status(input_string):
    # print(input_string, [[input_string[x], input_string[x+1]] for x in range(len(input_string)-1)])
    direction = "initial"
    # print([x for x in range(len(input_string)-1)])
    for item in range(len(input_string)-1):
        input1 = int(input_string[item])
        input2 = int(input_string[item+1])

        # Inputs are the same
        if input1 == input2:
            print("Unsafe")
            return 0

        # Difference is greater then 3
        elif abs(input1 - input2) > 3:
            print("Unsafe")
            return 0

        else:
            condition, direction = evaluate(input1, input2, direction)
            if condition == False:
                print(input_string, 0)
                print("Unsafe")
                return 0

    print(input_string, 1)
    return 1

if __name__ == "__main__":
    data = Path('input.txt').read_text()
    data = data.split("\n")

    total = 0

    # while True:
    #     input1 = int(input("Provide input1\t"))
    #     input2 = int(input("Provide input2\t"))

    #     print(evaluate(input1, input2))



    for _ in range(len(data)):
        if data[_].split(" ") == ['']:
            pass
        else:
            current = data[_].split(" ")
            result = 0
            for position in range(len(current)):
                result += status(current[:position] + current[position+1:])

            if result > 1:
                result = 1

            total += result

    print(total)













