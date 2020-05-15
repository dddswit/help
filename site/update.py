import os, yaml

"""
files = []
for sub in os.listdir(os.getcwd()):
    sub_path = os.path.join(os.getcwd(),sub)
    if os.path.isdir(sub_path):
        for f in os.listdir(sub_path):
            files.append(sub + '/' + f)
            
yaml.dump(files, open('bbb.yml','w'))
#print(files)
"""

for sub in os.listdir(os.getcwd()):
    sub_path = os.path.join(os.getcwd(),sub)
    if os.path.isdir(sub_path):
        for f in os.listdir(sub_path):
            if f.endswith('.md'):
                with open(sub + '/' + f, 'r', encoding='utf-8') as ff:
                    c = ff.read().split('\n')
                    if len(c) > 3 and c[0].startswith('# ') and c[1] == '' and c[3].startswith('==') and c[3].replace('=','') == '':
                        del c[1:4]
                    c = '\n'.join(c)
                with open(sub + '/' + f, 'w', encoding='utf-8') as ff:
                    ff.write(c)


"""
    f_path = dir + os.path.sep + filename
    if os.getcwd() + os.path.sep + 'results' in f_path:pass
    elif os.path.isdir(f_path):
        file_loop(f_path)
    elif filename.endswith(".html"):
        html_substitute(f_path)
        print("변환: ",f_path)
"""