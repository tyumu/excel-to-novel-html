import streamlit as st
import tempfile
import os
from pathlib import Path
from simple_converter import extract_all_dialogues, create_html

st.set_page_config(page_title="Excel→小説HTML変換ツール", layout="wide")

st.title("Excel → 小説風HTML 自動変換ツール")
st.markdown("Excelファイルからテキストを抽出して、小説風のHTMLに変換するツールです")

# Excelファイルのアップロード
uploaded_file = st.file_uploader("Excelファイル (main_*.xlsx)", type=['xlsx'])

if uploaded_file is not None:
    # 読み込んだExcelを一時ファイルとして保存
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    st.success("アップロード完了です！次はテキストを抽出しましょう。")
    
    # 抽出ボタン
    if st.button("テキストを抽出する"):
        with st.spinner("抽出中です。少し待っていてください..."):
            dialogues = extract_all_dialogues(tmp_path)
            st.session_state['dialogues'] = dialogues
            st.session_state['title'] = uploaded_file.name.replace('.xlsx', '')
            st.success("抽出完了です！次はAIに送るテキストを確認してください。")

    # 抽出結果がある場合のみ表示
    if 'dialogues' in st.session_state:
        st.subheader("1. 抽出されたテキスト")
        st.markdown("これをAIにコピペして送信してください。")
        st.text_area("抽出データ", value=st.session_state['dialogues'], height=300)
        
        st.subheader("AIへのプロンプト")
        try:
            with open("ai_prompt.txt", "r", encoding="utf-8") as f:
                prompt_text = f.read()
            st.text_area("プロンプト (一緒にコピペしてください)", value=prompt_text, height=150)
        except:
            st.warning("ai_prompt.txtが見つかりません。")
            
        st.subheader("2. AIの変換結果を貼り付け")
        st.markdown("AIが書き出した小説テキストをここに貼り付けてください。")
        novel_input = st.text_area("入力エリア", height=300)
        
        if st.button("HTMLを生成する"):
            if novel_input:
                with st.spinner("HTMLを作っています..."):
                    # 出力先フォルダの確保
                    out_dir = Path("output")
                    out_dir.mkdir(exist_ok=True)
                    out_html_name = f"{st.session_state['title']}.html"
                    
                    # HTML生成
                    html_path = create_html(novel_input, output_file=out_html_name, title=st.session_state['title'])
                    
                    with open(html_path, "rb") as f:
                        html_data = f.read()
                        
                    st.download_button(
                        label="HTMLをダウンロード",
                        data=html_data,
                        file_name=out_html_name,
                        mime="text/html"
                    )
                    st.success("完成です！")
            else:
                st.error("AIの変換結果を入力してください。")