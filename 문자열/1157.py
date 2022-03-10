import collections
word = collections.Counter(input().upper())
if len(word) > 1:
    print(word.most_common(2)[0][0] if word.most_common(2)[0][1] != word.most_common(2)[1][1] else "?")
else:
    print(word.most_common(1)[0][0])