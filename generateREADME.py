import os
from helperREADME import *



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
readme_file.write('---------------\n')
readme_file.write('## Category\n')
readme_file.write('\n')

for x in os.listdir('.'):
    if os.path.isdir(x) and check_dir_name(x):
        readme_file.write(linked_str(x))


# list the files under the corresponding category
readme_file.write('\n')
readme_file.write('---------------\n')
for category in os.listdir('.'):
    if os.path.isdir(category) and check_dir_name(category):
        readme_file.write('---------------\n')
        readme_file.write('### ' + category.capitalize() + '\n')

        ## Write a README.md inside of the directory
        dir_readme_file = open(category + '/README.md', 'w')
        dir_readme_file.write('# ' + format_title(category) + '\n')

        for f in sorted_dir(category):
            if f[-3:] == '.md' and f != 'README.md':
                readme_file.write(linked_str(f, directory = category))
                dir_readme_file.write(linked_str(f))
                ## collect h3 header from the f
                write_headers(dir_readme_file, f, path = category)
        dir_readme_file.close()


# close the file
readme_file.close()
