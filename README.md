# 48 緊急醫療站設置

## 素材
- `sources/*.pdf`：原始 PDF（衛福部急救站設置參考指引第二版、民防醫護教材 1 急救站設置、3 大傷應變）
- `sources/md/*.md`：轉好的 Markdown，**之後一律先讀這裡**，要看原圖才回去開 PDF
  - 每頁以 `## p.N` 標示（N = PDF 頁碼；指引的 PDF 頁碼 = 原文頁碼 + 1）
  - 表格以「｜」分欄（合併儲存格已去重）
  - 配置圖、流程圖等以【圖】補述

## 轉檔工具（tools/）
- `pdf2md.py`：純文字層抽取（投影片用）
- `guide2md.py` + `tables.py`：指引用，文字＋表格辨識
- 執行：`python3 -I tools/guide2md.py sources/<pdf> sources/md/<md> tools`
- 注意：重跑會覆蓋 md，手動補的【圖】說明會消失
