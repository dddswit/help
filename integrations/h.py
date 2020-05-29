import markdown

with open("sync-with-github.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()
html = markdown.markdown(text)

with open('aaaaa.html', 'w') as f:
    f.write(html)

