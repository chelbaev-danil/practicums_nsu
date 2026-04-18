def sort_string(s):
    '''
    Sorts the characters in a string in alphabetical order.
    '''
    
    char_list = list(s)
    char_list.sort()

    return ''.join(char_list)

text = input("Введите строку: ")
result = sort_string(text)
print(result)