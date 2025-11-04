import itertools

def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s

def solve(equation):
    # Split equation into left and right sides
    left, right = equation.upper().replace(' ', '').split('=')
    left = left.split('+')
    print(left,right)

    # Create a set of all unique letters
    letters = set(right)
    for word in left:
        letters.update(word)
    letters = list(letters)

    # Generate all possible digit permutations
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        # Skip invalid cases where a word starts with 0
        if any(sol[word[0]] == 0 for word in left + [right]):
            continue

        # Evaluate both sides
        left_sum = sum(get_value(word, sol) for word in left)
        right_val = get_value(right, sol)

        if left_sum == right_val:
            print(' + '.join(str(get_value(word, sol)) for word in left) +
                  f" = {right_val} (mapping: {sol})")
            return  # stop after finding the first valid solution

if __name__ == '__main__':
    solve('SEND + MORE = MONeY')
