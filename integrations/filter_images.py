import os,re

pattern = 'img/.+\.png'
img_folder = 'img'
images = []
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.md')]
for f in files:
    content = open(f, 'r', encoding='utf-8').read()
    m = re.findall(pattern,content)
    images += m

img_files = [f for f in os.listdir(img_folder) if f.endswith('.png')]
for f in img_files:
    img = os.path.join(img_folder,f)
    if not img in images:
        os.remove(img)

