with open('svg-icons.svg', 'r') as f:
    g = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(g, 'html.parser')

for svg in soup.find_all('svg'):
    if svg.has_attr('id'):
        with open(svg['id'] + '.svg', 'w') as f:
            f.write(svg.prettify())