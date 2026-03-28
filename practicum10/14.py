def my_find(text: str, substring: str, start: int = 0, end: int = None) -> int:

    if end is None:
        end = len(text)
    

    if start < 0:
        start = 0
    if end > len(text):
        end = len(text)
    if end <= start or len(substring) == 0:
        return -1
    
    for i in range(start, end - len(substring) + 1):
        match = True
        for j in range(len(substring)):
            if text[i + j] != substring[j]:
                match = False
                break
        if match:
            return i
    
    return -1

def find_all_positions(text: str, substring: str) -> str:

    if not substring or not text:
        return ""
    
    positions = []
    start = 0
    
    while True:
        pos = my_find(text, substring, start)
        if pos == -1:
            break
        positions.append(str(pos))
        start = pos + 1  
    
    return ",".join(positions)

dna = "ATGCATGCATGCATGCGATCGATCGATCG"

print("my_find:")
print(my_find(dna, "ATG"))     

print(find_all_positions(dna, "ATG")) 
print(find_all_positions(dna, "GATC"))
