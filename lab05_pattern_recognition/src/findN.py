import re
from typing import List


# # TOO FAST DUE TO :STARS MAGIC PYTHON OPTIMIZATION :STARS
# def find_n(pattern: str, text: str) -> List[int]:
#     if not len(pattern) or not len(text):
#         return []
#
#     # compare text slices of size len(pattern) one by one
#     return [i for i in range(len(text) - len(pattern)+1) if text[i:i + len(pattern)] == pattern]

def find_n(pattern: str, text: str) -> List[int]:
    if not len(pattern) or not len(text):
        return []

    found = []

    for text_ptr in range(len(text) - len(pattern) + 1):

        matched = True
        temp_text_ptr = text_ptr
        for pattern_ptr in range(len(pattern)):
            if text[temp_text_ptr] != pattern[pattern_ptr]:
                matched = False
                break
            temp_text_ptr += 1

        if matched:
            found.append(text_ptr)

    return found


if __name__ == '__main__':
    text = 'abcvsjfavabcahjkdfbasbabcoajspdahsb asdbcpaibsdcaabcabcabcasboasbdabsdoiasfaaabc'
    pattern = 'abc'
    print(find_n(pattern, text))
