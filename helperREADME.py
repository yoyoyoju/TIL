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


def format_title(s):
    res = s
    ind = s.find('.')
    if ind > 0:
        res = s[:ind]
    return res.capitalize().replace('_', ' ')



def make_dir_path(path, filename):
    '''(str, str) -> str
    return the combined str of path and filename
    >>> make_dir_path('', 'README.md')
    README.md
    >>> make_dir_path('vim', 'README.md')
    vim/README.md
    '''
    result = ''
    if path != '':
        result += path + '/'
    result += filename
    return result


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
    result = '* ['
    result += format_title(s)
    result += ']('
    result += make_dir_path(directory, s)
    result += ')\n'
    return result


def make_readme(dirname):
    '''(str) -> NoneType

    make a README.md file in the given directory.
    '''

    dir_readme_file = open(dirname + '/README.md', 'w')
    dir_readme_file.write('# ' + format_title(dirname) + '\n')
    dir_readme_file.close()


### change for more input
def write_headers(writefile, readfilename, path = '', header = 3):
    '''(file, str, str, int) -> NotnType
    writefile: file to write into
    readfilename: file name to collect the headers
    path: the path to the readfilename

    write into writefile, the h-header headers from readfilename.
    default: h3 header
    '''
    def format_line(str, start = header + 1, link = False):
        if link:
            str = str.lower().replace(' ', '-')
        return str[start:].rstrip()

    readfile = open(make_dir_path(path, readfilename), 'r')
    for line in readfile:
        if line[:header + 1] == header * '#' + ' ':
            writefile.write('   * [' + format_line(line) + '](' + readfilename + \
                    '#' + format_line(line, link = True) + ')\n')
    readfile.close()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
