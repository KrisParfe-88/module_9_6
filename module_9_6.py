def all_variants(text):
    for y in range(1, len(text) + 1):
        for x in range(len(text) + 1 - y):
            yield text[x:y + x]


a = all_variants("abc")
for i in a:
    print(i)