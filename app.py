import streamlit as st
import qwen
from os import getenv

app_name = getenv("APP_NAME")

st.set_page_config(page_title=app_name)
st.title(app_name)
st.caption("Your trusted government AI assistant")

chat_session = qwen.WarisAssist(
    api_key=getenv("DASHSCOPE_API_KEY"),
    app_id=getenv("APP_ID")
)

st.sidebar.title("Checklist")
with st.sidebar:
    if "checklist" in st.session_state:
        for checklist_set in st.session_state.checklist:
            with st.expander(checklist_set['title']):
                for item, checked in checklist_set['item'].items():
                    st.checkbox(item, value=checked, on_change=None)
if "session_id" in st.session_state:
    chat_session.session_id = st.session_state.session_id
if "messages" not in st.session_state:
    response = chat_session.chat("greet the user")
    response_text = response["response"]
    st.session_state.session_id = chat_session.session_id
    st.session_state["messages"] = [{"role": "assistant", "content": response_text}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(accept_file=True):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = chat_session.chat(prompt)
    print(response)
    response_text = response["response"]
    response_checklist = response.get("checklist", {})
    if response_checklist:
        item_list = response_checklist.get("item", [])
        unchecked_items = {item: False for item in item_list}
        response_checklist["item"] = unchecked_items
        try:
            st.session_state["checklist"].append(response_checklist)
        except KeyError:
            st.session_state["checklist"] = [response_checklist]
        with st.sidebar:
            with st.expander(response_checklist['title']):
                for item, checked in response_checklist['item'].items():
                    st.checkbox(item, value=checked, on_change=None)
    st.session_state.session_id = chat_session.session_id
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    st.chat_message("assistant").write(response_text)