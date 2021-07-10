def cayley_table(op, size):

    table = []
    table.append("⊙ | " + " ".join(str(i) for i in range(size)))
    table.append("-" * len(table[0]))

    for a in range(size):
        table.append(f"{a} | " + " ".join(str(op(a, b)) for b in range(size)))
    return "\n".join(table) + "\n"


def triangle_group(a, b):
    return (a%2)*(1 - 2*(b%2)) + (2*(1 - 2*(b%2))*(a//2) + b) % 6