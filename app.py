import streamlit as st
import pandas as pd

# إعداد الصفحة وتصميمها
st.set_page_config(page_title="Nemos Library", page_icon="📚", layout="wide")

# تصميم إضافي بالـ CSS لتحسين المظهر
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stCard {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation / التقال بين الصفحات
st.sidebar.title("📚 Nemos Library")
page = st.sidebar.radio("الانتقال إلى:", ["🏠 الرئيسية والكتالوج", "📖 الكتب المقروءة", "✨ قائمة الأمنيات", "📊 الإحصائيات والتحليل"])

# بيانات افتراضية للمكتبة
if "books" not in st.session_state:
    st.session_state.books = [
        {"title": "فن اللامبالاة", "author": "مارك مانسون", "category": "تطوير ذات", "status": "مقروء", "rating": 5, "progress": 100},
        {"title": "العادات الذرية", "author": "جيمس كلير", "category": "تطوير ذات", "status": "قائمة الأمنيات", "rating": 0, "progress": 0},
    ]

# --- الصفحة الأولى: الرئيسية والكتالوج ---
if page == "🏠 الرئيسية والكتالوج":
    st.title("🏛️ كتالوج المكتبة الشامل")
    st.caption("تصفحي كامل مجموعتك الكتبية وإدارتها في مكان واحد.")
    
    col_search, col_filter = st.columns([3, 1])
    with col_search:
        search_query = st.text_input("🔍 بحث عن كتاب أو مؤلف:")
    with col_filter:
        category_filter = st.selectbox("التصنيف:", ["الكل", "تطوير ذات", "روايات", "علوم", "تاريخ"])

    st.divider()

    # عرض الكتب في بطاقات أنيقة
    cols = st.columns(3)
    for idx, book in enumerate(st.session_state.books):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="stCard">
                <h3>📖 {book['title']}</h3>
                <p><b>المؤلف:</b> {book['author']}<br><b>التصنيف:</b> {book['category']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.progress(book['progress'] / 100)
            st.write(f"الحالة: **{book['status']}**")

# --- الصفحة الثانية: الكتب المقروءة ---
elif page == "📖 الكتب المقروءة":
    st.title("📖 مكتبة الكتب المقروءة")
    
    # نموذج إضافة كتاب جديد
    with st.expander("➕ إضافة كتاب جديد للمكتبة", expanded=False):
        with st.form("add_book_form"):
            new_title = st.text_input("عنوان الكتاب")
            new_author = st.text_input("اسم المؤلف")
            new_cat = st.selectbox("التصنيف", ["تطوير ذات", "روايات", "علوم", "تاريخ", "أخرى"])
            new_rating = st.slider("تقييمك للكتاب (من 5)", 1, 5, 5)
            submitted = st.form_submit_button("حفظ الكتاب")
            
            if submitted and new_title:
                st.session_state.books.append({
                    "title": new_title, "author": new_author, 
                    "category": new_cat, "status": "مقروء", 
                    "rating": new_rating, "progress": 100
                })
                st.success(f"تمت إضافة '{new_title}' بنجاح!")
                st.rerun()

# --- الصفحة الثالثة: قائمة الأمنيات ---
elif page == "✨ قائمة الأمنيات":
    st.title("✨ قائمة الكتب المراد قراءتها")
    st.info("سجلي الكتب التي تخططين لاقتنائها وقراءتها مستقبلاً.")

# --- الصفحة الرابعة: الإحصائيات ---
elif page == "📊 الإحصائيات والتحليل":
    st.title("📊 الملخص السنوي والإحصائيات")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("إجمالي الكتب", len(st.session_state.books))
    m2.metric("الكتب المقروءة", sum(1 for b in st.session_state.books if b['status'] == 'مقروء'))
    m3.metric("معدل التقييم", "4.8 / 5")
