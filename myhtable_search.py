from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.
    Returns a list-of-buckets hashtable representation.
    """

    table = htable(4011)
    for i in range(len(files)):
        text = get_text(files[i])
        text = set(words(text))

        for word in text:
            bucket = table[hashcode(word) % len(table)]
            index = bucket_indexof(table, word)

            if index is not None:
                bucket[index][1].add(i)
            else:
                htable_put(table, word, {i})

    return table

def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    """

    valid_set = {}
    for t in terms:
        current_set = htable_get(index, t)

        if current_set is not None:
            if valid_set == {}:
                valid_set = current_set
            else:
                valid_set = valid_set.intersection(current_set)

    valid_files = []
    for i in valid_set:
        valid_files.append(files[i])

    return valid_files
