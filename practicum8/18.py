def justify_text(text, line_width):
    words = text.split()  
    lines = [] 
    current_line = []  
    current_length = 0  

    for word in words:
        
        if current_length + len(word) + len(current_line) > line_width:
            
            for i in range(line_width - current_length):
                current_line[i % (len(current_line) - 1 or 1)] += ' '
            lines.append(''.join(current_line))
            current_line = []
            current_length = 0

        
        current_line.append(word)
        current_length += len(word)

    
    lines.append(' '.join(current_line))

    return '\n'.join(lines)



text = input("Введите текст: ")
line_width = int(input("Введите ширину строки: "))


formatted_text = justify_text(text, line_width)
print(formatted_text)