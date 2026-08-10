# Streamlit
# pip install streamlit

import streamlit as st

# session_state
st.session_state.counter = 1

st.write(st.session_state.counter)



# UI 구성

# 채팅 메시지
with st.chat_message("user"):
    st.write("Hello~~")

with st.chat_message("assistant"):
    st.write("Hello!!")

# 채팅 관련 UI
prompt = st.chat_input("Say something")
if prompt:
    #st.write(f"너가 입력한 거: {prompt}")
    with st.chat_message("user"):
        st.write(prompt)

# 레이아웃
st.set_page_config(layout="centered")

# 사이드 바
with st.sidebar:
    st.header("대시보드 설정")
    user_role = st.selectbox("권한선택", ["admin", "user"])

# Tap
tab1, tab2 = st.tabs(["보고서", "설정"])

with tab1:
    st.subheader("tab1의 내용")
    st.write("보고서 내용 출력")

with tab2:
    st.subheader("tab2의 내용")
    st.write("설정 내용 출력")

# 사용자와 인터렉션 UI
if st.button("클릭하세요!"):
    st.write("버튼 클릭됨")

# 텍스트 입력
user_name = st.text_input("이름을 입력하세요", value="오디세우스")
st.write(user_name)

# 슬라이더, 셀렉트 박스
level = st.slider("난이도를 선택하세요", min_value=1, max_value=10, value=5)
st.write(level)
option = st.selectbox("언어를 선택하세요", ["영어", "중국어", "일본어"])

agree = st.checkbox("동의합니다")
st.write(agree)

gender = st.radio("성별", ["남성", "여성", "선택안함"])
st.write(gender)

st.divider()

# 제목
st.title("Streamlit 위젯 확인")
st.header("텍스트 사용")
st.subheader("마크다운, 다양한 텍스트 표현")

# 일반 텍스트
st.text("일반 텍스트 출력")
st.markdown("**강조**, *기울임*, `num = 100`")

# write
st.write("---")
st.write("### `st.write()` 활용")
st.write("숫자, 딕셔너리, 리스트")
st.write({"key":"value", "number":[100, 200, 300]})

# 메시지 박스
st.info("st.info() 안내 메시지를 표시할 때 사용")
st.warning("경고!!!")
st.success("완료!, 성공!")

