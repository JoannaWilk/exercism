# Pangram is a sentence using every letter of the alphabet at least once.
# The alphabet used consists of ASCII letters `a` to `z`, inclusive, and is case
# insensitive. Input will not contain non-ASCII symbols.

import string

def is_pangram(sentence):
    return all(letter in sentence.lower() for letter in string.ascii_lowercase)
