import sys
import argparse

from morse_encoder import DictMorseEncoder


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()

    path = args.path

    with open(path, mode='r', encoding='utf-8') as fp:
        encoded = morse(fp)

    print(encoded)


def morse(fp) -> str:
    plaintext = ''.join(fp.readlines())

    dme = DictMorseEncoder(' ', '/')
    encoded = dme.encode_string(plaintext)

    return encoded


if __name__ == '__main__':
    main(sys.argv)
