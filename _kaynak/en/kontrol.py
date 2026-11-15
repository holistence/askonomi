import sys, importlib.util
def load(p):
    s=importlib.util.spec_from_file_location("m"+str(abs(hash(p))),p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def cmp(a,b,path,errs):
    if type(a)!=type(b): errs.append(f"{path}: type {type(a).__name__} vs {type(b).__name__}"); return
    if isinstance(a,dict):
        if list(a.keys())!=list(b.keys()): errs.append(f"{path}: keys differ {set(a)^set(b) or 'order'}"); return
        for k in a: cmp(a[k],b[k],f"{path}.{k}",errs)
    elif isinstance(a,(list,tuple)):
        if len(a)!=len(b): errs.append(f"{path}: len {len(a)} vs {len(b)}"); return
        for i,(x,y) in enumerate(zip(a,b)): cmp(x,y,f"{path}[{i}]",errs)
    elif isinstance(a,str):
        if len(a)<=3 and a!=b and (a.isupper() or a.isdigit()): errs.append(f"{path}: short code changed {a!r}->{b!r}")
    elif a!=b: errs.append(f"{path}: value {a!r} vs {b!r}")
tr,en=load(sys.argv[1]),load(sys.argv[2])
names=[n for n in dir(tr) if not n.startswith('_') and isinstance(getattr(tr,n),(dict,list,tuple))]
errs=[]
for n in names:
    if not hasattr(en,n): errs.append(f"missing {n}"); continue
    cmp(getattr(tr,n),getattr(en,n),n,errs)
print("OK" if not errs else "ERRORS:\n"+"\n".join(errs[:60]))
