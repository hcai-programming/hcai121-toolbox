
import re
from collections import Counter


def get_words(text: str) -> list[str]:
    """
    Convert text into a list of lowercase words.
    Ignore punctuation and capitalization.
    """
    return re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)*", text.lower())


def count_words(text: str) -> int:
    """
    Return the total number of words.
    """
    words = get_words(text)
    return len(words)


def most_common_words(text: str, n: int = 5) -> list[tuple[str, int]]:
    """
    Return the n most common words and their frequencies.
    """
    words = get_words(text)
    word_counts = Counter(words)
    return word_counts.most_common(n)


def longest_word(text: str) -> list[str]:
    words = get_words(text)

    if not words:
        return []

    max_length = max(len(word) for word in words)

    return [word for word in words if len(word) == max_length]


def average_word_length(text: str) -> float:
    """
    Return the average number of characters per word.
    """
    words = get_words(text)

    if not words:
        return 0.0

    total_characters = sum(len(word) for word in words)
    return round(total_characters / len(words), 2)


def reading_time(text: str, words_per_minute: int = 200) -> float:
    """
    Estimate reading time in minutes.
    Default reading speed: 200 words per minute.
    """
    if words_per_minute <= 0:
        raise ValueError("Reading speed must be positive.")

    word_count = count_words(text)
    return round(word_count / words_per_minute, 2)


def get_text_statistics(text: str) -> dict:
    """
    Return all text statistics in one dictionary.
    """
    return {
        "word_count": count_words(text),
        "most_common_words": most_common_words(text),
        "longest_word": longest_word(text),
        "average_word_length": average_word_length(text),
        "reading_time_minutes": reading_time(text),
    }
