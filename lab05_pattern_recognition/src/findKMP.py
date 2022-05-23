from typing import List


def generate_pi(pattern: str) -> List[int]:
    pi = [0]
    prefix_len = 0
    for substring_len in range(1, len(pattern)):
        while prefix_len > 0 and pattern[prefix_len] != pattern[substring_len]:
            prefix_len = pi[prefix_len-1]
        if pattern[prefix_len] == pattern[substring_len]:
            prefix_len += 1
        pi.append(prefix_len)
    return pi


def find_kmp(pattern: str, text: str) -> List[int]:
    if not len(pattern) or not len(text):
        return []
    found_list = []
    pattern_len = len(pattern)
    pi = generate_pi(pattern)
    matched_char_count = 0
    for pos, char in enumerate(text):
        while matched_char_count > 0 and pattern[matched_char_count] != char:  # Next char is wrong
            matched_char_count = pi[matched_char_count-1]  # Decrement q to the right value
        if pattern[matched_char_count] == char:  # Next char is right
            matched_char_count += 1
        if matched_char_count == pattern_len:  # Found pattern
            found_list.append(pos - pattern_len + 1)
            matched_char_count = pi[matched_char_count-1]  # Start next search
    return found_list


if __name__ == "__main__":
    print(find_kmp("aba", "kababa"))
