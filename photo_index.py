"""Group exported photo file lists by extension and directory."""

def analyze(text):
    import os
    images={'.jpg','.jpeg','.png','.gif','.bmp','.tif','.tiff'}
    groups={}; total=0
    for line in text.splitlines():
        path=line.strip()
        if not path:continue
        ext=os.path.splitext(path)[1].lower()
        if ext not in images:continue
        folder=os.path.dirname(path) or '.'
        groups[folder]=groups.get(folder,0)+1;total+=1
    return {'total':total,'directories':dict(sorted(groups.items()))}
