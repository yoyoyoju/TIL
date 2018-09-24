import os


# helper functions
def sorted_dir(folder):
    def getmtime(name):
        path = os.path.join(folder, name)
        return os.path.getmtime(path)

    return sorted(os.listdir(folder), key=getmtime, reverse=True)


# Constants
readme = 'README.md'
basereadme = 'baseREADME.md'


# open a file to write
readme_file = open(readme, 'w')


# copy the baseREADME.md into it
basereadme_file = open(basereadme, 'r')

while True: # copy basereadme_file to readme_file
    data = basereadme_file.read(65536)
    if data:
        readme_file.write(data)
    else:
        break

basereadme_file.close()


# list the directory as category
readme_file.write('---------------\n')
readme_file.write('## Category\n')
readme_file.write('\n')

for x in os.listdir('.'):
    if os.path.isdir(x) and x[0] != '.':
        readme_file.write('* [' + x.capitalize() + ']')
        readme_file.write('(' + x + ')')
        readme_file.write('\n')


# list the files under the corresponding category
readme_file.write('\n')
readme_file.write('---------------\n')
for category in os.listdir('.'):
    if os.path.isdir(category) and category[0] != '.':
        readme_file.write('### ' + category.capitalize() + '\n')

        # for f in os.listdir(category):  # write files in the category
        for f in sorted_dir(category):
            if f[-3:] == '.md':
                readme_file.write('* [' + f[:-3].replace('_', ' ') + ']')
                readme_file.write('(' + category + '/' + f + ')\n')



# close the file
readme_file.close()
