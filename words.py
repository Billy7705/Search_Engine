import os
import re
import string


def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    docs = []
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            file_path = os.path.abspath(os.path.join(dirpath, f))
            docs.append(file_path)
    return docs

def get_text(fileName):
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s

def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words


def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  
    Arg terms is a list of string terms.
    """

    # write first lines of html string
    html_string = '<html>\n  <body>\n  <h2>Search results for <b>'

    for word in terms:
        html_string += word + ' '

    html_string += '</b> in ' + str(len(docs)) + ' files</h2>'

    # cap number of returns at 100 results
    result_num = min(len(docs), 100)

    # write data of html string
    for i in range(result_num):
        line_string = '\n\n    <p><a href=\"file://' + docs[i] + '\">' + docs[i] + '</a>'

        text = get_text(docs[i])
        text = text.split('\n')

        lines = []
        for t in terms:

            if len(lines) == 2:
                break

            for text_line in text:
                text_line = words(text_line)
                for j in range(len(text_line)):
                    if t == text_line[j]:
                        lines.append(text_line)
                if len(lines) == 2:
                    break

        for l in lines:
            line_string += '<br>\n    '
            for j in range(len(l)):
                if l[j] in terms:
                    line_string += '<b>' + l[j] + '</b> '
                else:
                    line_string += l[j] + ' '

        html_string += line_string + '<br><br>'

    html_string += '</body>\n</html>'

    return html_string


def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]
