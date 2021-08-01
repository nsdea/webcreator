import os

try:
    from markdown2 import Markdown
except ModuleNotFoundError:
    os.system('pip install markdown2')
    from markdown2 import Markdown

md = Markdown()

# CHOOSE A HTML STYLE TEMPLATE
print('SELECT A HTML STYLE TEMPLATE:')

styles = ''
for s in os.listdir('webcreator/templates/'):
    styles += os.path.basename(s).replace('.html', '') + ' ' 

print(styles)
style = input('[NAME] >>>')

print()
print('=============')
print()

# WORK WITH MARKDOWN
md_text = ''

if input('Create Markdown (y) or use "input.md" (n)?') == 'y':
    print('MARKDOWN MODE ACTIVE')
    print('Type $exit when you\'re done')
    print('====================')

    while 1:
        inp = input('[MD] >>>')
        if inp == '$exit':
            break
        md_text += inp + '\n'
else:
    md_text = open('webcreator/input.md').read()

html_code = md.convert(md_text)

# CREATE HTML
html_code = open(f'webcreator/templates/{style}.html').read().replace('<!-- %CODE% -->', html_code)

# add a title for the html page
title = 'WebCreator'
for line in md_text.split('\n'):
    if line.startswith('# '):
        title = line.split('# ')[1]

html_code = html_code.replace('%TITLE%', title) 

open('webcreator/output.html', 'w').write(html_code)

# VIEW HTML
backslash = '\\' # because Python does not allow backslashes in f-strings somehow
os.system(f'start firefox "file:///{os.getcwd().replace(backslash, "/")}/webcreator/output.html')
