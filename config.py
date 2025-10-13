"""
設定ファイル - ドクターの名前や分岐選択を設定

使い方:
1. DOCTOR_NAME を好きな名前に変更
2. BRANCH_CHOICES で分岐を選択（1から始まる番号）
"""

# ドクターの名前（{@nickname}の置き換え）
DOCTOR_NAME = "ドクター"  # 好きな名前に変更してください

# 分岐の選択
# キー: シーン名または行番号
# 値: 選択肢番号（1, 2, 3...）
BRANCH_CHOICES = {
    # 例: 特定の分岐で選択肢2を選ぶ場合
    # "level_main_00-01_end_decision_1": 1,
    
    # デフォルトは全て選択肢1
    "default": 1
}

# 分岐処理方法の設定
BRANCH_MODE = "include_all"  # "include_all" or "select_one"
# - "include_all": 全ての分岐ルートを小説に含める（推奨）
# - "select_one": 選択した分岐のみを含める

# 分岐の表示方法
BRANCH_DISPLAY = {
    "show_options": True,      # 選択肢を小説内に表示するか
    "options_format": "inline",  # "inline" or "separate_page"
    # - "inline": 地の文に自然に組み込む
    # - "separate_page": 独立したページとして表示
}
