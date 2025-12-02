import math

N, K, M = map(int, input().split())

rides = 2 * N
sessions = math.ceil(rides / K)
print(sessions * M)
    
