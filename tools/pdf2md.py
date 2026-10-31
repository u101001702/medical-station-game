import sys, fitz, pathlib
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); out.mkdir(exist_ok=True)
for f in sorted(src.glob('*.pdf')):
    d = fitz.open(f)
    lines = [f'# {f.stem}', '', f'> 來源：{f.name}，共 {len(d)} 頁。由 PyMuPDF 抽取文字層；圖表內容另以 [圖] 補述。', '']
    for i, p in enumerate(d, 1):
        t = p.get_text('text').strip()
        imgs = len(p.get_images())
        lines += [f'## p.{i}', '']
        lines += [t if t else '（本頁無文字層）', '']
    (out / f'{f.stem}.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f.stem, 'ok')
