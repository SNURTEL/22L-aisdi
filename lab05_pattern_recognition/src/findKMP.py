from typing import List


def generate_pi(pattern: str) -> List[int]:
    pi = [0]
    k = 0
    for q in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k-1]
        if pattern[k] == pattern[q]:
            k += 1
        pi.append(k)
    return pi


def find_kmp(pattern: str, text: str) -> List[int]:
    if not len(pattern) or not len(text):
        return []
    found = []
    pattern_len = len(pattern)
    pi = generate_pi(pattern)
    q = 0
    for i, char in enumerate(text):
        while q > 0 and pattern[q] != char:  # Next char is wrong
            q = pi[q-1]  # Decrement q to the right value
        if pattern[q] == char:  # Next char is right
            q += 1
        if q == pattern_len:  # Found pattern
            found.append(i - pattern_len + 1)
            q = pi[q-1]  # Start next search
    return found


if __name__ == "__main__":
    print(find_kmp("aba", "kababa"))
