import streamlit as st

st.set_page_config(page_title="Nemos Library", page_icon="📚", layout="wide")
st.title("📚 Nemos Library | مكتبتي الرقمية")

menu = st.sidebar.selectbox("القائمة", ["الكتب المقروءة", "قائمة الأمنيات", "الملخص السنوي"])

if menu == "الكتب المقروءة":
    st.header("📖 الكتب المقروءة")
    book = st.text_input("اسم الكتاب:")
    if st.button("إضافة"):
        st.success(f"تمت إضافة '{book}' بنجاح!")

elif menu == "قائمة الأمنيات":
    st.header("✨ قائمة الأمنيات")
    wish = st.text_input("اسم الكتاب:")
    if st.button("إضافة للأمنيات"):
        st.success(f"تمت إضافة '{wish}'!")

elif menu == "الملخص السنوي":
    st.header("📊 الملخص السنوي")
    st.metric(label="إجمالي الكتب المقروءة", value="0")