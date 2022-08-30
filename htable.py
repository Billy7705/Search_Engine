"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""

    list = []
    for i in range(nbuckets):
        list.append([])

    return list

def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """

    if type(o) == int:
        return o
    elif type(o) == str:
        h = 0
        for c in o:
            h = h*31 + ord(c)
        return h
    else:
        return None

def bucket_indexof(table, key):
    """
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """

    bucket = table[hashcode(key)%len(table)]

    for i in range(len(bucket)):
        if bucket[i][0]==key:
            return i

    return None

def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    """

    bucket = table[hashcode(key) % len(table)]
    index = bucket_indexof(table, key)

    if index is not None:
        bucket[index] = (key, value)
    else:
        bucket.append((key, value))

def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Return None if key not found.
    """

    bucket = table[hashcode(key) % len(table)]
    index = bucket_indexof(table, key)
    if index is not None:
        return bucket[index][1]
    else:
        return None

def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    """
    output_string = ''
    for i in range(len(table)):
        line_string = ''
        bucket_number = str(i).zfill(4)
        line_string += bucket_number + '->'

        for j in range(len(table[i])):
            line_string += str(table[i][j][0]) + ':'
            k = table[i][j][1]
            line_string += str(k) + ', '

        # take out trailing comma
        if line_string[-2:] == ', ':
            line_string = line_string.rstrip(line_string[-2:])

        output_string += line_string + '\n'

    return output_string


def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    """

    table_string = '{'
    for i in range(len(table)):

        for j in range(len(table[i])):
            table_string += str(table[i][j][0]) + ':' + str(table[i][j][1]) + ', '

    # take out trailing comma
    if table_string[-2:] == ', ':
        table_string = table_string.rstrip(table_string[-2:])

    table_string += '}'

    return table_string
