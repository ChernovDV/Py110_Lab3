INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    #  перезаписать содержимое одного файла в
    with open('input.txt', 'r') as file1:  # открыть указатель на файл
        with open('output.txt','w') as file2:  # открыть указатель на файл
            for line in map(str.upper, file1):
                file2.write(line)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
