def solution(sizes):
    changed_sizes = []
    big_a, big_b = 0, 0

    for a, b in sizes:
        if a > b:
            changed_sizes.append([a, b])
        else:
            changed_sizes.append([b, a])

    for a, b in changed_sizes:
        if a > big_a:
            big_a = a

        if b > big_b:
            big_b = b

    return big_a * big_b