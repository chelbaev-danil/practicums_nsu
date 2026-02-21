name = input()

keywords = [
    "False", "None", "True", "and", "as", "assert", "async", "await", 
    "break", "class", "continue","def", "del", "elif", "else", "except", 
    "finally", "for", "from", "global", "if", "import","in", "is", "lambda",
    "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"
]

if len(name)!=0:
    if name in keywords:
        print("Ключевое слово")
    elif name[0].isalpha() or name[0] == "_":
        if all(char.isalnum() or char == "_" for char in name):
            print("Идентификатор")
        else:
            print("Невалидный идентификатор")
    else:
        print("Невалидный идентификатор")
else: 
    print("Пустая строка")

