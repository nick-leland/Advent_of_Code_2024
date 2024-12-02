from pathlib import Path
import string

if __name__ == "__main__":
    data = Path('input.txt').read_text()
    data = data.split("\n")
    list1 = []
    list2 = []
    for _ in range(len(data)):
        current = data[_].split("   ")
        if current[0] == "":
            pass
        else:
            list1.append(current[0])
            list2.append(current[1])

    list1.sort()
    list2.sort()

    total = 0

    for _ in range(len(list1)):
        total += abs(int(list1[_]) - int(list2[_]))

    print(total)
