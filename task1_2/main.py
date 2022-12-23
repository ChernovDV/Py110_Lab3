OUTPUT_FILE = "output.txt"


def task():

    with open('output.txt','w') as file:  # записать лесенку в файл
       for i in range(1,11):
            file.write(f"{i*'*':>10}\n")

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
