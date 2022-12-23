import json


def task(input_filename: str, output_filename: str) -> None:

    # считать содержимое json файл input.json
    with open (input_filename) as file:
        json_file = json.load(file)
    # записать содержимое в json файл output.json с отступами
    with open(output_filename, 'w') as file:
        json.dump(json_file, file ,indent=4)




if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
