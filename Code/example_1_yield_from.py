def concat_v1(s1, s2):
    for i in s1:
        yield i
    for j in s2:
        yield j


def concat_v2(s1, s2):
    yield from s1
    yield from s2


seq1 = [1, 2, 3, 4]
seq2 = [5, 6, 7, 8]


print(*concat_v1(seq1, seq2))
print(*concat_v2(seq1, seq2))
