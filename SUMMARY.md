# 🎉 完成!Excel → 小説風HTML 自動変換ツール

## ✅ すべての改善完了

### 修正した問題
1. ✅ **B列の話者情報が消えていた** 
   → 【キャラクター名】形式で正しく抽出

2. ✅ **AIが台本形式で出力してしまう**
   → 具体例付きプロンプトで小説形式に

3. ✅ **HTMLの縦書き構造に対応**
   → `<div class="page text">` 形式で生成
   → 数字を `<span class="tcy">` で自動変換

4. ✅ **分岐システムに対応** ⭐新規⭐
   → 15個の選択肢分岐を検出・抽出
   → 【ドクターの選択肢】と【分岐】マーカー
   → 全分岐ルートを小説に含める設定

5. ✅ **ドクター名のカスタマイズ** ⭐新規⭐
   → {@nickname} を自動置換
   → config.py で簡単設定

## 📦 作成したファイル一覧

### メインファイル
- ✨ **`simple_converter.py`** - メイン変換スクリプト
- ⚙️ **`config.py`** - 設定ファイル（ドクター名・分岐設定）
- 📝 **`ai_prompt.txt`** - 最適化されたAIプロンプト

### ドキュメント
- 📖 **`README.md`** - 詳細ガイド
- 🚀 **`QUICKSTART.md`** - 3ステップガイド  
- 🎨 **`HTML_STRUCTURE.md`** - HTML構造説明
- ⚙️ **`CONFIG_GUIDE.md`** - 設定ガイド（ドクター名・分岐）⭐新規⭐
- 📂 **`FILES.md`** - ファイル一覧

### ユーティリティ
- 🔍 `check_excel.py` - Excel構造確認
- 👥 `check_speakers.py` - 話者情報確認
- 🔍 `check_columns.py` - 列データ確認
- 🔀 `check_decisions.py` - 分岐システム確認 ⭐新規⭐
- 🧪 `test_html_generation.py` - HTMLテスト生成

### テストファイル
- 📄 `output/sample_novel_output.txt` - サンプル小説
- 🌐 `output/test_sample.html` - テストHTML（22ページ）

## 🚀 使い方（超簡単3ステップ）

### ステップ1: データ抽出
```bash
python simple_converter.py
```
→ `output/ai_input.txt` 生成（36,000文字、話者情報込み）

### ステップ2: AIで変換
1. `ai_prompt.txt` をコピー
2. `output/ai_input.txt` の内容を追加
3. AIに送信
4. 結果を `output/novel_output.txt` に保存

### ステップ3: HTML生成
```bash
python simple_converter.py
```
→ `output/generated_novel.html` 生成完了!✨

## 🎯 主な機能

### データ抽出
- ✅ 14シート全てを一括処理
- ✅ 話者情報を【名前】形式で抽出
- ✅ 画像・背景URLも自動検出
- ✅ 約36,650文字を整形
- ✅ **15個の分岐を検出** ⭐新規⭐
- ✅ **{@nickname}を自動置換** ⭐新規⭐

### AI向けプロンプト
- ✅ 台本形式を避ける明確な指示
- ✅ 具体的な変換例を提示
- ✅ 情景描写の追加を促す
- ✅ 段落分割のガイドライン
- ✅ **分岐の扱い方を明記** ⭐新規⭐

### HTML生成
- ✅ 縦書き対応（`writing-mode: vertical-rl`）
- ✅ 右から左へページめくり
- ✅ 数字の縦中横（12月 → <span class="tcy">12</span>月）
- ✅ 画像ページの自動生成
- ✅ 見出しページの自動生成
- ✅ スマホ・タブレット対応

## 🎨 HTML出力例

### 数字の表示
```
入力: 12月23日、20cc
出力: <span class="tcy">12</span>月<span class="tcy">23</span>日、<span class="tcy">20</span>cc
表示: 縦書きの中で数字だけ横向き!
```

### ページ構造
```html
<div class="page text">
    <p>
        意識が、深い霧の底からゆっくりと浮上する。<br>
        最初に感じたのは、声だった。
    </p>
</div>
```

## 📊 データ処理

### 入力（Excel）
```
B列: アーミヤ  | C列: はい! お陰で助かりました
B列: ドーベルマン | C列: よくやった
```

### 中間（ai_input.txt）
```
【アーミヤ】はい! お陰で助かりました
【ドーベルマン】よくやった
```

### AI出力（novel_output.txt）
```
「はい! お陰で助かりました」
アーミヤが安堵の表情で答える。

ドーベルマンが頷く。
「よくやった」
```

### 最終（HTML）
```html
<div class="page text">
    <p>
        「はい! お陰で助かりました」<br>
        アーミヤが安堵の表情で答える。
    </p>
</div>
```

## 🔧 テスト済み機能

✅ Excel読み込み（14シート）
✅ 話者情報の抽出
✅ AIプロンプトの生成
✅ HTML構造の生成
✅ 数字の縦中横変換
✅ 画像URLの検出
✅ ページ分割

## 📱 対応環境

### ブラウザ
- ✅ Chrome / Edge
- ✅ Firefox
- ✅ Safari

### デバイス
- ✅ Windows PC
- ✅ Mac
- ✅ スマートフォン
- ✅ タブレット

### Python
- ✅ Python 3.7以上
- ✅ openpyxl（自動インストール済み）

## 💡 次のステップ

1. **今すぐ試す**: `python simple_converter.py` を実行
2. **プロンプトを確認**: `ai_prompt.txt` を開く
3. **テストHTMLを見る**: `output/test_sample.html` をブラウザで開く
4. **本番実行**: 全データをAIで変換

## 📖 ドキュメント

- **初めて使う**: `QUICKSTART.md` を読む
- **詳しく知りたい**: `README.md` を読む
- **HTMLをカスタマイズ**: `HTML_STRUCTURE.md` を読む
- **ファイル構成を確認**: `FILES.md` を読む

## 🎉 完成!

これで、Excel → AI → HTMLの完全自動化パイプラインが完成しました!

約36,000文字のゲーム会話データを、美しい縦書き小説HTMLに変換できます。

何か質問があれば、各ドキュメントを参照するか、スクリプトのコメントを確認してください!

Happy Reading! 📖✨
