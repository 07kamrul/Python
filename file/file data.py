fh = open("data.txt","r")

unique_words = []
unique = set(unique_words)

for line in fh.readline():
    print(line.strip().split(" "))
    ln = line.strip().split(" ")
    print(ln)
    unique_words += ln
    print(unique_words)

un = open("unique.txt", "w")
for u in sorted(unique_words):
    un.write(u)

fh.close()

