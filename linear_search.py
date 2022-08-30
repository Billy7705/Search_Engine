
from words import get_text, words

def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """
    valid_files = []

    for i in range(len(files)):
        text = get_text(files[i])
        text = words(text)

        text_valid = True
        for t in terms:
            if t not in text:
                text_valid = False

        if text_valid:
            valid_files.append(files[i])

    return valid_files

