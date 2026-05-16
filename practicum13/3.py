sladk_likes = set(input().split())
n = int(input())

friends_likes = set()
for _ in range(n):
    friends_likes.update(input().split())

unique_to_sladk = sladk_likes - friends_likes

print(len(unique_to_sladk))