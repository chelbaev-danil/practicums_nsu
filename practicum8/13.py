count = 1
while True:
    ticket = input()
    if len(ticket) % 2 == 0:
        if sum(map(int, ticket[:len(ticket) // 2])) == sum(map(int, ticket[len(ticket) // 2:])):
            print(count)
            break
    count += 1