import streamlit as st
import numpy as np
import pandas as pd
# from PIL import Image
import time


st.title('Streamlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4],
#     '2列目':[10, 20, 30, 40]
# })

# st.write(df)

# st.dataframe(df)
# st.dataframe(df.style.highlight_max(color="green"))
# st.dataframe(df.style.highlight_min(color="green"))

# st.table(df)
# st.table(df.style.highlight_min(color="green"))

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
df2 = df.style.highlight_max(axis=0)

# st.dataframe(df2)

# """

# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """


# """
# # My first Streamlit app

# ## How it works?

# This site is made by Streamlit command.

# ## How to run?

# streamlit run my-first-stream-app.py

# """

# st.dataframe(df)


# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)


# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)


st.write('プログレスバーの表示')

# if st.checkbox('Show Image'):
#     img = Image.open('shikun12655V7A4244_TP_V4.jpg')
#     st.image(img, caption='cat', use_column_width=True)

# option = st.selectbox(
#     'あなたの好きな数字を教えてください, ', 
#     list(range(1, 11))
# )


# text = st.text_input('あなたの趣味を教えてください')

# condition = st.slider('あなたの今の調子は？', 0, 100, 50) #最小値, 最大値, デフォルト

# 'あなたの趣味は, ', text, 'です'

# 'あなたの調子は, ', condition, 'です'


'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
    
'Done!!'
    

left_column, right_column = st.beta_columns(2)

button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラムです')
    

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1：回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3')

