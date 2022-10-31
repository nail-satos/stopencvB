# 必要なライブラリをインポートする
import streamlit as st
# import cv2
from PIL import Image
import time

# Streamlit Community CloudでOpenCVアプリを公開する
# https://zenn.dev/shimat/articles/baee671a1a00d0

# タブに表示されるページ名の変更
st.set_page_config(page_title="AIで群衆を認識しよう")
# Streamlit入門 – テーマの変更, ページの設定 | 楽しみながら理解するAI・機械学習入門
# https://data-analytics.fun/2022/07/10/streamlit-theme-page-settings/

st.header('アプリ「AIで群衆を認識しよう」')           # タイトル

st.sidebar.subheader('難易度を選んで「認識開始」ボタンを押してください')       # サブヘッダ

# level = st.radio("難易度を選択してください", ("初級の画像", "中級の画像", "上級の画像"), horizontal=True)
level = st.sidebar.radio("難易度を選択してください",("初級", "中級", "上級"), horizontal=True)

# st.write('レッスン1')         # キャプション
if level == '初級':
    image = Image.open('./assets/a1-010.jpg')
if level == '中級':
    image = Image.open('./assets/a1-030.jpg')
if level == '上級':
    image = Image.open('./assets/a1-040.jpg')


if st.sidebar.button('認識開始（ここをクリック）'):

    if level == '初級':
        image = Image.open('./assets/a1-011.jpg')
        count = 12
    if level == '中級':
        image = Image.open('./assets/a1-031.jpg')
        count = 65
    if level == '上級':
        image = Image.open('./assets/a1-041.jpg')
        count = 321

    status_text = st.empty()
    # プログレスバー
    progress_bar = st.progress(0)

    i = 0
    while i < 100:
        # status_text.text(f'Progress: {i}%')
        # for ループ内でプログレスバーの状態を更新する
        i = i + 5
        progress_bar.progress(i)
        time.sleep(0.1)
    
    # バルーンの表示
    st.balloons()

    st.success('AIが 写真の中から 【' + str(count) + '人】の人間を 認識しました', icon="✅")        


# 画像の表示
st.image(image, caption='群衆の画像', use_column_width=True)

# st.caption('※注釈：現在、仮サーバのため、性能の関係で見せかけのモックで動かしています（認識しているフリです）')
# st.caption('※注釈：本番サーバでは、フリではなく、ガチ認識させます（認識速度などは、ほぼダミーと変わりません）')

# st.header('レッスン1')          # ヘッダ
# st.subheader('レッスン1')       # サブヘッダ
# st.caption('レッスン1')         # キャプション
# st.code('print("レッスン1"')    # ソースコード
# st.write('レッスン1')           # 汎用的な出力
# st.latex('S_{t+1}=S_{t}\exp(\mu \Delta_t+\sigma \sqrt{\Delta_t}\epsilon_t)')    # 数式（ラテック形式/tex:テフ）