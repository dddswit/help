with open('sync-with-github.md', 'r') as f:
    content = f.read()
    for line in content.split('\n'):
        if 'img/github-aaaaaaaa.png' in line:
            content = content.replace(line, line.replace('aaaaaaaa',line.split('[')[1].split(']')[0].lower().replace(' ','-')))

with open('sync-with-github.md', 'w') as f:
    f.write(content)

            