def print_n_to_1(current):
    if current < 1:
        return
    print(current)
    print_n_to_1(current-1)

print_n_to_1(10)
print()