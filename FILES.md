# 📂 ファイル一覧

## メインファイル

### ✨ `simple_converter.py` ⭐必須⭐
**メイン変換スクリプト** - これだけ実行すればOK!
- Excelからデータ抽出
- HTMLを自動生成
- 使い方: `python simple_converter.py`

## 設定・ガイドファイル

### 📝 `ai_prompt.txt` ⭐重要⭐
**AIに送るプロンプト**
- コピーしてAIに貼り付ける
- 具体例付きで分かりやすい
- 台本形式を避ける指示が明確

### 📖 `README.md`
**詳細な使い方ガイド**
- 3ステップの使い方
- トラブルシューティング
- カスタマイズ方法

### 🚀 `QUICKSTART.md`
**クイックスタートガイド**
- すぐに始められる簡易版
- 完成イメージ付き
- よくある質問も掲載

### 🎨 `HTML_STRUCTURE.md`
**HTML構造の説明**
- ページの種類
- 縦中横の仕組み
- スタイルのカスタマイズ方法

## ユーティリティスクリプト

### 🔍 `check_excel.py`
Excelファイルの構造確認用
```bash
python check_excel.py
```

### 👥 `check_speakers.py`
話者情報の確認用
```bash
python check_speakers.py
```

### 🔍 `check_columns.py`
各列のデータ確認用
```bash
python check_columns.py
```

### 🧪 `test_html_generation.py`
サンプルHTMLの生成テスト
```bash
python test_html_generation.py
```

## 生成されるファイル（outputフォルダ内）

### 📄 `ai_input.txt`
**抽出されたExcelデータ**
- 【キャラクター名】セリフ形式
- 約36,000文字
- AIに送信するファイル

### 📄 `novel_output.txt` ⭐あなたが作成⭐
**AIで変換した小説テキスト**
- AIの出力をここに保存
- このファイルからHTMLを生成

### 🌐 `generated_novel.html`
**最終的な縦書き小説HTML**
- ブラウザで開いて読める
- 右から左にページめくり

### 🧪 `sample_novel_output.txt`
テスト用サンプル小説テキスト

### 🧪 `test_sample.html`
テスト用サンプルHTML

## データファイル

### 📊 `main_0_暗黒時代・上.xlsx` ⭐必須⭐
**元データのExcelファイル**
- 14シート
- 話者:セリフ形式

### 📄 `新規 テキスト ドキュメント (5).html`
**手動作成のサンプルHTML**
- HTML構造の参考用
- スタイルの見本

## フォルダ構造

```
プロジェクトフォルダ/
│
├── 📊 main_0_暗黒時代・上.xlsx          ← 元データ
│
├── ✨ simple_converter.py               ← メインスクリプト
├── 📝 ai_prompt.txt                     ← AIプロンプト
│
├── 📖 README.md                         ← 詳細ガイド
├── 🚀 QUICKSTART.md                     ← クイックガイド
├── 🎨 HTML_STRUCTURE.md                 ← HTML構造説明
│
├── 🔍 check_excel.py                    ← ユーティリティ
├── 👥 check_speakers.py
├── 🔍 check_columns.py
├── 🧪 test_html_generation.py
│
├── 📁 .venv/                            ← Python仮想環境
│
└── 📁 output/                           ← 生成ファイル
    ├── 📄 ai_input.txt                  ← 抽出データ
    ├── 📄 novel_output.txt              ← 小説テキスト（あなたが作成）
    ├── 🌐 generated_novel.html          ← 最終HTML
    ├── 📄 sample_novel_output.txt       ← サンプル
    └── 🌐 test_sample.html              ← テスト
```

## 実行順序

```
1. python simple_converter.py
   → output/ai_input.txt 生成

2. AIに送信
   → output/novel_output.txt に保存

3. python simple_converter.py
   → output/generated_novel.html 生成 ✨完成!
```

## ファイルサイズ目安

- `ai_input.txt`: 約35KB（36,000文字）
- `novel_output.txt`: 約50-70KB（AIが追加描写）
- `generated_novel.html`: 約100-150KB
- `main_0_暗黒時代・上.xlsx`: 約70KB

## 削除してもよいファイル

以下は開発・テスト用なので、本番では削除可能:
- ✂️ `check_*.py` (3ファイル)
- ✂️ `test_html_generation.py`
- ✂️ `output/sample_novel_output.txt`
- ✂️ `output/test_sample.html`
- ✂️ `HTML_STRUCTURE.md` (参考資料として残すのも◎)

## 必須ファイル（削除NG）

- ⚠️ `simple_converter.py`
- ⚠️ `ai_prompt.txt`
- ⚠️ `README.md` または `QUICKSTART.md`
- ⚠️ `main_0_暗黒時代・上.xlsx`
