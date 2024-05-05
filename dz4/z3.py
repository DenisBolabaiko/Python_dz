def text_function(text, file_name):
    with open(file_name, "a+") as f:
        f.write(text + "\n")
    with open(file_name, "r") as f:
        lines = f.readlines()
        even_lines = [line.strip() for i, line in enumerate(lines) if i % 2 != 0]
    return even_lines


text = str(input("Введите текст: "))
file_name = str(input("Введите название текстового файла: "))
res = text_function(text, file_name)
for i in res:
    print(i)
