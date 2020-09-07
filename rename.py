import os

dir = 'temp'
for f in os.listdir(dir):
    os.rename(r'%s' % os.path.join(dir,f),r'%s' % os.path.join(dir,f.lower().replace(' ','-')))
