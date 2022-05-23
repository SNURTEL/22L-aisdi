from typing import List


def find_kr(pattern: str, text: str) -> List[int]:
    if not len(pattern) or not len(text):
        return []

    def h(k: int) -> int:
        return k % 101

    base = 512

    def int_repr(text: str, base: int = base):
        char_vals = [ord(text[i]) * (base ** (len(text) - 1 - i))
                     for i in range(len(text))]
        return sum(char_vals)

    pattern_hash = h(int_repr(pattern))
    search_window_hash = h(int_repr(text[:len(pattern)]))

    found = []
    for i in range(len(pattern), len(text)):
        if pattern_hash == search_window_hash and text[i - len(pattern): i] == pattern:
            found.append(i - len(pattern))

        # shift the window one digit right
        first_digit_only = ord(text[i - len(pattern)]) * (base ** (len(pattern) - 1))
        new_last_digit = ord(text[i])
        search_window_hash = h((search_window_hash - first_digit_only) * base + new_last_digit)

    # make last comparison out of loop to avoid IndexError
    if pattern_hash == search_window_hash and text[-len(pattern):] == pattern:
        found.append(len(text) - len(pattern))

    return found


if __name__ == '__main__':
    text = 'abcvsjfavabcahjkdfbasbabcoajspdahsb asdbcpaibsdcaabcabcabcasboasbdabsdoiasfaaabc'
    pattern = 'abc'
    print(find_kr(pattern, text))
