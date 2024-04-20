import streamlit as st # type: ignore
from PIL import Image
import time
#--------------------------------------------------------------------
# st.markdown(
#     f"""
#     <style>
#         /* selectboxのクラスを指定して幅を変更 */
#         div[data-baseweb="select"] > div:first-child {{
#             width: 300px;
#         }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
#--------------------------------------------------------------------
st.title('Streamlit 超入門')
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
st.write('Display Image')
#--------------------------------------------------------------------
col1, col2 = st.columns(2)
button = col1.button("cat")
if button:
    col2.write("dog")
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容')
#--------------------------------------------------------------------
# if st.checkbox('Show Image'):
#     img = Image.open('iStock-1124713019.png')
#     st.image(img, caption='Bou Ningen', use_column_width=True)
#--------------------------------------------------------------------
option = st.selectbox(
    '好きな数字を選択してください。',
    list(range(1,11))
)
'選択した数字は、', option, 'です。'
#--------------------------------------------------------------------
text = st.text_input('趣味はなんですか？')
'あなたの趣味は', text