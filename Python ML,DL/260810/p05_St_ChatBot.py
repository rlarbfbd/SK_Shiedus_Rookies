import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

# 기본 설정
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("api 키가 존재하지 않음")
    st.stop()

client = OpenAI(api_key=api_key)

# ===============================================

# 페이지 레이아웃
st.set_page_config(page_title="AI 챗봇")
st.title("Open AI를 이용한 챗봇")
st.caption("Responses API를 이용한 챗봇입니다.")

# ===============================================

# 대화 세션 저장 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 대화 기록 출력
# [ { "role": "user|assistant", "content": "~~~" }, {}, ... ]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("질문을 입력하세요."):
    # 화면에 대화 메시지 출력
    st.chat_message("user").markdown(prompt)

    # messages에 대화 내용 추가
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Responses API를 이용해서 모델 활용
    with st.chat_message("assistant"):
        response = client.responses.create(
            model="gpt-5.5",
            instructions="너는 친절하고 명확하게 답변하는 AI 어시스턴트",
            input=st.session_state.messages,
            stream=True
        )

        # 스트리밍 청크 생성 함수
        def gen_chunck():
            for event in response:
                # delta 텍스트 처리
                if hasattr(event, "delta") and event.delta:
                    yield event.delta
                elif getattr(event, "type", None) == "response.output_text.delta":
                    yield event.delta

        # 화면 출력 -> 완전한 응답 데이터 저장
        full_response = st.write_stream(gen_chunck())

        # 세션에 저장된 대화 메시지에 응답 데이터 저장
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": full_response
            }
        )