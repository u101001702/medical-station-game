import fitz, sys, re
fitz.TOOLS.mupdf_display_errors(False)
def clean(c):
    if c is None: return ''
    return re.sub(r'\s*\n\s*','',c).strip()
def table_lines(t):
    rows=[]
    for r in t.extract():
        cells=[]
        for c in map(clean,r):
            if c and (not cells or cells[-1]!=c): cells.append(c)
        if not cells: continue
        if rows:
            prev=rows[-1]
            if cells==prev: continue
            # 換行續列：前面欄位相同，只有最後一格不同 → 接到上一列最後一格
            n=len(cells)
            if n==len(prev) and n>1 and cells[:-1]==prev[:-1] and cells[-1] not in prev[-1]:
                prev[-1]+=cells[-1]; continue
            if n<len(prev) and cells==prev[:n]: continue
            # 單格續行：上一列最後一格是長句且沒有句尾標點
            if n==1 and len(prev)>=3 and len(prev[-1])>=15 and prev[-1][-1] not in '。：:）)' :
                prev[-1]+=cells[0]; continue
        rows.append(cells)
    return ['｜'.join(r) for r in rows]
if __name__=='__main__':
    d=fitz.open(sys.argv[1])
    for pn in map(int,sys.argv[2:]):
        for t in d[pn-1].find_tables().tables:
            print(f'--- p.{pn}'); print('\n'.join(table_lines(t)))
