import os,re,markdown
from bs4 import BeautifulSoup

bucket = 'swit-public'
working_path = 'docs/integrations/'
local_path = 'img/'
cloud_path = 'docs/help/'
github_path = 'https://dddswit.github.io/help/integrations/img/'
from google.cloud import storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "swit-gke-resource-access.json"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

def parse_into_help(soup):
    for img in soup.find_all("img"):
        if img['src'].startswith('img/'):
            pureName = img['src'].replace(local_path,'',1)
            #upload_blob(bucket, local_path + pureName, cloud_path + pureName)
            img['src'] = github_path + pureName
        
        if not img.previous_sibling and not img.next_sibling and not 'class' in img:
            div = soup.new_tag("div")
            div['class'] = 'block-image'
            img.parent.replace_with(div)
            div.insert(1,img)
    notes = soup.find_all("div", attrs={"class": "admonition note"})
    for note in notes:
        note['class'] = 'tip-box'
        note.p.decompose()
    for h3 in soup.find_all("h3"):
        h5 = soup.new_tag("h5")
        h3.wrap(h5)
        h3.unwrap()
    for h4 in soup.find_all("h4"):
        h3 = soup.new_tag("h3")
        h4.wrap(h3)
        h4.unwrap()
    soup.h1.decompose()
    for a in soup.find_all("a"):
        a.string = '"{}"'.format(a.string)
        if a['href'].startswith("#"):
            i = soup.new_tag('i')
            a.wrap(i)
            a.unwrap()

#pattern = 'img/.+\.png'
#m = re.findall(pattern,content)

files = [f for f in os.listdir(working_path) if f.endswith('.md')]
for f in files:
    content = open(working_path + f, 'r', encoding='utf-8').read()
    html = markdown.markdown(content, extensions=['admonition', 'def_list', 'attr_list'])
    soup = BeautifulSoup(html, 'html.parser')
    parse_into_help(soup)
    with open(f + '.html', 'w', encoding='utf-8') as html_f:
        html_f.write(soup.prettify())
