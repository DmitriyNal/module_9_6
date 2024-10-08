from itertools import combinations


def all_variants(text: str):
     for i in range(len(text) + 1):
        for j in combinations(text, i):
            yield "".join(j)


if __name__ == "__main__":
    a = all_variants("abc")
    for i in a:
        print(i)
