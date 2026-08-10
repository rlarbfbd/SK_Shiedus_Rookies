import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import json

"""
사진 촬영 관련 질문에 답변하며, 
셔터스피드와 환산 초점거리 계산에 
Function Calling을 활용하는 챗봇입니다.

테스트 질문 1 -> 일반 질문
야경 사진을 촬영할 때 조리개는 어떻게 설정해야 해?

테스트 질문 2 -> Function Calling 함수 1
20mm 렌즈로 별 사진을 찍으려고 해. 셔터스피드 계산해줘.

테스트 질문 3 -> Function Calling 함수 2
크롭 팩터가 1.5인 카메라에서 35mm 렌즈를 사용하면 환산 초점거리가 얼마야?
"""


def calculate_shutter_speed(focal_length):
    # Function Calling 확인
    print("calculate_shutter_speed 함수 실행")
    print("입력값:", focal_length)

    shutter_speed = 500 / focal_length

    return round(shutter_speed, 1)


def calculate_equivalent_focal_length(focal_length, crop_factor):
    # Function Calling 확인
    print("calculate_equivalent_focal_length 함수 실행")
    print("입력값:", focal_length, crop_factor)

    equivalent_focal_length = focal_length * crop_factor

    return round(equivalent_focal_length, 1)


tools = [
    {
        "type": "function",
        "name": "calculate_shutter_speed" ,
        "description": "셔터 스피드를 계산하는 함수",
        "parameters": {
            "type": "object",
            "properties": {
                "focal_length": {"type": "number"}
            },
        "required": ["focal_length"],
        "additionalProperties": False
        },
        "strict": True
    },
    {
            "type": "function",
            "name": "calculate_equivalent_focal_length" ,
            "description": "렌즈 초점거리와 크롭 팩터를 이용해 풀프레임 기준 환산 초점거리를 계산하는 함수",
            "parameters": {
                "type": "object",
                "properties": {
                    "focal_length": {"type": "number"},
                    "crop_factor": {"type": "number"}
                },
            "required": ["focal_length", "crop_factor"],
            "additionalProperties": False
            },
            "strict": True
        }
]


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
st.title("AI 사진 촬영 도우미 챗봇")
st.caption("사진 관련 질문에 답변해주는 챗봇입니다.")

# ===============================================

# 대화 세션 저장 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 대화 기록 출력
for message in st.session_state.messages:
    if message.get("role") in ("user", "assistant"):
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
            instructions="너는 사진 촬영에 대해 친절하고 명확하게 답변하는 AI 어시스턴트",
            input=st.session_state.messages,
            tools=tools
        )

        msg_content = None
        tool_executed = False

        for tool_call in response.output:
            if tool_call.type == "function_call":
                args = json.loads(tool_call.arguments)

                # 별 사진 셔터스피드 계산
                if tool_call.name == "calculate_shutter_speed":
                    result = calculate_shutter_speed(
                        args["focal_length"]
                    )

                # 크롭 센서 환산 초점거리 계산
                elif tool_call.name == "calculate_equivalent_focal_length":
                    result = calculate_equivalent_focal_length(
                        args["focal_length"],
                        args["crop_factor"]
                    )
                else:
                    continue

                tool_executed = True

                # 함수 호출 정보 저장
                st.session_state.messages.append({
                    "type": "function_call",
                    "call_id": tool_call.call_id,
                    "name": tool_call.name,
                    "arguments": tool_call.arguments
                })

                # 함수 실행 결과 저장
                st.session_state.messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": str(result)
                })

        # Function Calling이 실행된 경우
        if tool_executed:
            response2 = client.responses.create(
                model="gpt-5.5",
                instructions="너는 사진 촬영에 대해 친절하고 명확하게 답변하는 AI 어시스턴트",
                input=st.session_state.messages,
                tools=tools
            )

            msg_content = response2.output_text

        # 일반 사진 질문인 경우 
        else:
            msg_content = response.output_text

        st.markdown(msg_content)

        # 최종 답변 저장
        st.session_state.messages.append({
            "role": "assistant",
            "content": msg_content
        })