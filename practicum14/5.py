def count_descendants(tree, name):
    '''
    Рекурсивная функция для каждого потомка прибавляет 1 
    и рекурсивно считает его потомков.
    '''
    if name not in tree:
        return 0
    total = 0
    
    for child in tree[name]:
        total += 1 + count_descendants(tree, child)
    return total


n = int(input())

tree = {}
for _ in range(n):
    parent, child = input().split()

    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

name = input()
print(count_descendants(tree, name))