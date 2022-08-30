from collections import defaultdict

from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs.
    Return a dict object mapping a word to a set of doc IDs.
    """

    dic = dict()
    for i in range(len(files)):
        text = get_text(files[i])
        text = set(words(text))

        for word in text:
            if word in dic:
                dic[word].add(i)
            else:
                dic[word] = {i}

    return dic

def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by words() function.  
    Parameter terms is a list of strings.
    """

    valid_set = {}
    for t in terms:
        if t in index:
            current_set = index[t]

            if valid_set == {}:
                valid_set = current_set
            else:
                valid_set = valid_set.intersection(current_set)

    valid_files = []
    for i in valid_set:
        valid_files.append(files[i])

    return valid_files
