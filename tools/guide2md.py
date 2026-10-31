import fitz, re, sys
sys.path.insert(0, sys.argv[3]); from tables import table_lines
fitz.TOOLS.mupdf_display_errors(False)
HDR=[r'114 年\s+4 月23 日衛部醫字第1141669299 號函訂定',r'114 年10 月23 日衛部醫字第1141669299 號函修正',r'第 ?\d+ ?頁\(共 ?70 ?頁\)']
FIG={4:'（本頁為空白頁）'}
d=fitz.open(sys.argv[1]); name=sys.argv[1].split('/')[-1]
out=[f'# 急救站設置參考指引（第二版）','',f'> 來源：{name}（衛福部 114.4.23 訂定、114.10.23 修正，衛部醫字第1141669299號）。共 {len(d)} 頁，p.N 為 PDF 頁碼（= 原文頁碼 + 1）。','> 文字由 PyMuPDF 抽取；表格以「｜」分隔欄位（合併儲存格已去重）；圖片內容以【圖】補述。','']
for i,p in enumerate(d,1):
    tabs=p.find_tables().tables
    items=[]
    for b in p.get_text('blocks'):
        x0,y0,x1,y1,txt=b[:5]
        cx,cy=(x0+x1)/2,(y0+y1)/2
        if any(fitz.Rect(t.bbox).contains(fitz.Point(cx,cy)) for t in tabs): continue
        txt=txt.strip()
        for h in HDR: txt=re.sub(h,'',txt).strip()
        if txt: items.append((y0,'\n'.join(l.rstrip() for l in txt.split('\n'))))
    for t in tabs: items.append((t.bbox[1],'\n'.join(table_lines(t))))
    items.sort(key=lambda x:x[0])
    out+=[f'## p.{i}','']
    body='\n\n'.join(x[1] for x in items)
    out+=[body or FIG.get(i,'（本頁無文字）'),'']
open(sys.argv[2],'w',encoding='utf-8').write('\n'.join(out))
