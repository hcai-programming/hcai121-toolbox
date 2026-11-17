
import pytest

from toolbox.vhuang_functions import (
    get_words,
    count_words,
    most_common_words,
    longest_word,
    average_word_length,
    reading_time,
    get_text_statistics,
)


# Test 1: Word extraction
def test_get_words():
    assert get_words("Hello, World!") == ["hello", "world"]
    assert get_words("The CAT") == ["the", "cat"]
    assert get_words("") == []
    assert get_words("Hello! How are you?") == [
        "hello", "how", "are", "you"
    ]


# Test 2: Word count
def test_count_words():
    assert count_words("the cat the") == 3
    assert count_words("Hello world") == 2
    assert count_words("") == 0
    assert count_words("One") == 1
    assert count_words("Hello, world!") == 2


# Test 3: Most common words
def test_most_common_words():
    assert most_common_words("the cat the") == [
        ("the", 2),
        ("cat", 1)
    ]

    assert most_common_words("The the THE") == [
        ("the", 3)
    ]

    assert most_common_words("") == []

    assert most_common_words("cat dog cat bird", 2) == [
        ("cat", 2),
        ("dog", 1)
    ]


# Test 4: Longest words
def test_longest_word():
    assert longest_word("The elephant runs") == ["elephant"]
    assert longest_word("cat dog") == ["cat", "dog"]
    assert longest_word("") == []
    assert longest_word("Hello, world!") == ["hello", "world"]


# Test 5: Average word length
def test_average_word_length():
    assert average_word_length("cat dog") == 3.0
    assert average_word_length("a bb ccc") == 2.0
    assert average_word_length("hello world") == 5.0
    assert average_word_length("") == 0.0
    assert average_word_length("Hi, there!") == 3.5


# Test 6: Reading time
def test_reading_time():
    assert reading_time("hello world") == 0.01
    assert reading_time("") == 0.0

    # 200 words = 1 minute
    text = "word " * 200
    assert reading_time(text) == 1.0

    # 100 words = 0.5 minutes
    text = "word " * 100
    assert reading_time(text) == 0.5


# Test 7: Custom reading speed
def test_custom_reading_speed():
    text = "word " * 100

    assert reading_time(text, 100) == 1.0
    assert reading_time(text, 200) == 0.5
    assert reading_time(text, 400) == 0.25


# Test 8: Invalid reading speed
def test_invalid_reading_speed():
    with pytest.raises(ValueError):
        reading_time("hello world", 0)

    with pytest.raises(ValueError):
        reading_time("hello world", -100)


# Test 9: Punctuation handling
def test_punctuation():
    assert count_words("Hello, world!") == 2
    assert most_common_words("Hello! hello? HELLO.") == [
        ("hello", 3)
    ]
    assert longest_word("Python, Java!") == ["python"]


# Test 10: Capitalization handling
def test_capitalization():
    assert count_words("The the THE") == 3
    assert most_common_words("The the THE") == [
        ("the", 3)
    ]
    assert longest_word("ELEPHANT cat") == ["elephant"]


# Test 11: Empty input
def test_empty_text():
    assert get_words("") == []
    assert count_words("") == 0
    assert most_common_words("") == []
    assert longest_word("") == []
    assert average_word_length("") == 0.0
    assert reading_time("") == 0.0


# Test 12: Complete statistics dictionary
def test_get_text_statistics():
    text = "The cat and the dog are playing."

    expected = {
        "word_count": 7,
        "most_common_words": [
            ("the", 2),
            ("cat", 1),
            ("and", 1),
            ("dog", 1),
            ("are", 1)
        ],
        "longest_word": ["playing"],
        "average_word_length": 3.57,
        "reading_time_minutes": 0.04,
    }

    assert get_text_statistics(text) == expected


# Test 13: Whitespace handling
def test_whitespace():
    assert count_words("   hello   world   ") == 2
    assert count_words("hello\nworld") == 2
    assert count_words("hello\tworld") == 2
    assert count_words("   ") == 0


# Test 14: Apostrophe handling
def test_apostrophes():
    assert get_words("don't stop") == ["don't", "stop"]
    assert count_words("It's a test") == 3
    assert longest_word("don't go") == ["don't"]
