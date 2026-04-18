def count_holes_and_words(text):
    ''' 
    Counts the number of letters with 
    and without holes in the text, 
    and also finds words containing two 
    or more letters with holes.
    '''
    
    holes_letters = 'a b d e g o p q'
    
    words = text.lower().split()
    
    total_holes = 0
    total_no_holes = 0
    special_words = []          
    
    for word in words:
        holes_in_word = 0
        for char in word:
            if char.isalpha():
                if char in holes_letters:
                    holes_in_word += 1
                    total_holes += 1
                else:
                    total_no_holes += 1
        
        if holes_in_word >= 2:
            special_words.append(word)
    
    print(total_holes, total_no_holes)
    print(special_words)

sentence = input().strip()
count_holes_and_words(sentence)