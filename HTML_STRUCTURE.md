# 🎨 HTML構造とスタイルの説明

## HTMLの基本構造

生成されるHTMLは縦書き表示に最適化されています。

### ページの種類

#### 1. タイトルページ
```html
<div class="page">
    <h1>暗黒時代・上</h1>
</div>
```

#### 2. 見出しページ
```html
<div class="page">
    <h2>プロローグ<br>覚醒</h2>
</div>
```

#### 3. テキストページ
```html
<div class="page text">
    <p>
        意識が、深い霧の底からゆっくりと浮上する。<br>
        最初に感じたのは、声だった。
    </p>
</div>
```

#### 4. 画像ページ
```html
<div class="page">
    <img class="illustration" src="画像URL" alt="説明">
</div>
```

## 縦中横（数字の横表示）

縦書きの中で数字を横向きに表示するため、`<span class="tcy">` タグを使用:

```html
<span class="tcy">12</span>月<span class="tcy">23</span>日
<span class="tcy">20</span>cc
```

### 自動変換される数字

スクリプトが以下のパターンを自動で `<span class="tcy">` で囲みます:
- `年` の前の数字: 2024年 → <span class="tcy">2024</span>年
- `月` の前の数字: 12月 → <span class="tcy">12</span>月
- `日` の前の数字: 23日 → <span class="tcy">23</span>日
- `時` の前の数字: 14時 → <span class="tcy">14</span>時
- `分` の前の数字: 30分 → <span class="tcy">30</span>分
- `秒` の前の数字: 45秒 → <span class="tcy">45</span>秒
- `cc` の前の数字: 20cc → <span class="tcy">20</span>cc

## スタイルのカスタマイズ

`simple_converter.py` のHTML生成部分を編集してカスタマイズできます:

### フォントサイズを変更
```css
font-size: 16px;  /* この値を変更 */
```

### 行間を調整
```css
line-height: 2.4;  /* この値を変更（1.8〜3.0推奨）*/
```

### 文字間隔を調整
```css
letter-spacing: 0.08em;  /* この値を変更 */
```

### 背景色を変更
```css
background-color: #FDFCF7;  /* 任意の色コード */
```

### ページ幅を調整
```css
width: calc(100vw - 10em);  /* 10emの値を変更 */
```

## 改行とページ分割

### AIに推奨する出力形式

```
短い段落1（1-3文）

少し長めの段落2（3-5文）
複数の文がある場合は適度に改行。

別の段落3
```

この形式で出力すると、見やすいページ分割になります。

### 段落間の空行

- **1つの空行**: 同じシーン内の段落区切り
- **2つの空行**: 場面転換

## レスポンシブ対応

以下のデバイスで最適表示:
- 📱 スマートフォン（縦・横）
- 📱 タブレット
- 💻 デスクトップブラウザ

## 画像の表示

### 画像ページの特徴
- 自動的に幅が広くなる（`width: calc(100vw + 10em)`）
- 画像は縦横比を保ちながらフィット
- スクロールで画像全体を閲覧可能

### 対応形式
- PNG
- JPG
- GIF
- WebP
- 外部URL（https://）

## ブラウザ互換性

### 完全対応
- Chrome / Edge
- Firefox
- Safari

### 縦書き対応
- `writing-mode: vertical-rl`
- `text-orientation: mixed`
- `text-combine-upright: all` (縦中横)

## トラブルシューティング

### 画像が表示されない
→ URLが正しいか、インターネット接続を確認

### 数字が縦向きのまま
→ `<span class="tcy">` タグが正しく適用されているか確認

### ページが横スクロールしない
→ `overflow-x: scroll` が有効か確認

### モバイルでスクロールできない
→ `-webkit-overflow-scrolling: touch` を確認

## パフォーマンス最適化

### 大量のページがある場合
1. 画像は適切なサイズに圧縮
2. 外部CDNを使用
3. ページ数を分割（章ごとに別ファイル）

### 読み込み速度改善
- 画像の遅延読み込み（Lazy Loading）を追加可能
- プログレッシブJPEGを使用
