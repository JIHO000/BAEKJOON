alphabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]
num = 0
word = input()
for i in alphabet:
    word=word.replace(i, "*")
print(len(word))
