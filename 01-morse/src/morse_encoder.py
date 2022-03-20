from abc import ABC, abstractmethod
import re


class MorseEncoder(ABC):
    def __init__(self, letter_separator: str, word_separator: str):
        self._letter_separator = letter_separator
        self._word_separator = word_separator

    @staticmethod
    def filter_invalid_characters(plaintext: str):
        return re.sub('( ){2,}', ' ', re.sub('[^a-zA-z\n ]', '', plaintext))

    @abstractmethod
    def encode_string(self, plaintext: str) -> str:
        pass


class DictMorseEncoder(MorseEncoder):
    def __init__(self, letter_separator: str, word_separator: str):
        super(DictMorseEncoder, self).__init__(letter_separator, word_separator)

        self._ascii_to_morse_character_table = {'A': '.-',
                                                'B': '-...',
                                                'C': '-.-.',
                                                'D': '-..',
                                                'E': '.',
                                                'F': '..-.',
                                                'G': '--.',
                                                'H': '....',
                                                'I': '..',
                                                'J': '.---',
                                                'K': '-.-',
                                                'L': '.-..',
                                                'M': '--',
                                                'N': '-.',
                                                'O': '---',
                                                'P': '.--.',
                                                'Q': '--.-',
                                                'R': '.-.',
                                                'S': '...',
                                                'T': '-',
                                                'U': '..-',
                                                'V': '...-',
                                                'X': '-..-',
                                                'Y': '-.--',
                                                'Z': '--..',
                                                ' ': self._word_separator,
                                                '\n': '\n'}

    def encode_string(self, plaintext: str) -> str:
        return '\n'.join(
            [self._letter_separator.join([self._ascii_to_morse_character_table[char]
                                          for char in line])
             for line in
             MorseEncoder.filter_invalid_characters(plaintext.upper()).split('\n')])
