from io import StringIO
from lab01_morse.src.morse import morse


def test_one_letter_1():
    fp = StringIO(
        "A\n"
    )
    assert morse(fp) == ".-\n"


def test_one_letter_2():
    fp = StringIO(
        "K\n"
    )
    assert morse(fp) == "-.-\n"


def test_one_letter_lowercase():
    fp = StringIO(
        "s\n"
    )
    assert morse(fp) == "...\n"


def test_word():
    fp = StringIO(
        "ALA\n"
    )
    assert morse(fp) == ".- .-.. .-\n"


def test_word_lowercase():
    fp = StringIO(
        "ala\n"
    )
    assert morse(fp) == ".- .-.. .-\n"


def test_sentence_1():
    fp = StringIO(
        "ALA MA KOTA\n"
    )
    assert morse(fp) == ".- .-.. .- / -- .- / -.- --- - .-\n"


def test_sentence_2():
    fp = StringIO(
        "LOREM IPSUM\n"
    )
    assert morse(fp) == ".-.. --- .-. . -- / .. .--. ... ..- --\n"


def test_sentence_lowercase_1():
    fp = StringIO(
        "ala ma kota\n"
    )
    assert morse(fp) == ".- .-.. .- / -- .- / -.- --- - .-\n"


def test_sentence_lowercase_2():
    fp = StringIO(
        "lorem ipsum\n"
    )
    assert morse(fp) == ".-.. --- .-. . -- / .. .--. ... ..- --\n"


def test_sentence_other_symbols():
    fp = StringIO(
        "Ala34 ma* kota|\n"
    )
    assert morse(fp) == ".- .-.. .- / -- .- / -.- --- - .-\n"


def test_sentence_other_symbols_word():
    fp = StringIO(
        "Ala34 ma* () \\ kota|\n"
    )
    assert morse(fp) == ".- .-.. .- / -- .- / -.- --- - .-\n"


def test_multiline_1():
    fp = StringIO(
        "Ala ma kota\n"
        + "a kot ma Ale\n"
        + "a12b 3 c\n"
    )
    assert morse(fp) == (".- .-.. .- / -- .- / -.- --- - .-\n" +
                         ".- / -.- --- - / -- .- / .- .-.. .\n" +
                         ".- -... / -.-.\n")


def test_multiline_2():
    fp = StringIO(
        "Lorem ipsum\n"
        + "dolor sit amet,\n"
    )
    assert morse(fp) == (".-.. --- .-. . -- / .. .--. ... ..- --\n" +
                         "-.. --- .-.. --- .-. / ... .. - / .- -- . -\n")
