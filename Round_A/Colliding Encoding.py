def has_collision(mapping, words):
    encodings = set()
    for word in words:
        encoding = ''.join(str(mapping[letter]) for letter in word)
        if encoding in encodings:
            return True
        encodings.add(encoding)
    return False

t = int(input())
for i in range(1, t+1):
    mapping = input().split()
    mapping = {chr(ord('A') + i): int(mapping[i]) for i in range(26)}
    n = int(input())
    words = [input().strip() for _ in range(n)]
    if has_collision(mapping, words):
        print(f"Case #{i}: YES")
    else:
        print(f"Case #{i}: NO")
