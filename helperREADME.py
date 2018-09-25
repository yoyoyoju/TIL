import os

### helper functions for generateREADME.py


def sorted_dir(folder):
    '''(str) -> list of str
    Return a list of files in folder
    sorted based on the time since epoch oldest to newest.
    '''
    def getmtime(name):
        path = os.path.join(folder, name)
        return os.path.getmtime(path)

    return sorted(os.listdir(folder), key=getmtime, reverse=True)


def check_dir_name(dirname):
    '''(str) -> bool
    return True if the dirname is to be listed.
    '''
    notgood = ['.', '_']
    return dirname[0] not in notgood

def linked_str(s, directory = ''):
    '''(str) -> str
    return a formatted to link based on the s and directory.
    s: file name or directory name. Does not start with '.'

    >>> a = 'how_to_vim'
    >>> linked_str(a)
    '* [How to vim](how_to_vim)\\n'
    >>> linked_str(a, directory = 'vim')
    '* [How to vim](vim/how_to_vim)\\n'
    '''
    def format_title(s):
        res = s
        ind = s.find('.')
        if ind > 0:
            res = s[:ind]
        return res.capitalize().replace('_', ' ')

    result = '* ['

    result += format_title(s)
    result += ']('
    if directory != '':
        result += directory + '/'
    result += s
    result += ')\n'
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
