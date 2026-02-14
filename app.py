import streamlit as st
import google.generativeai as genai

# تم وضع مفتاحك الجديد هنا
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"

# إعداد الاتصال ليتخطى الأخطاء القديمة
genai.configure(api_key=API_KEY, transport='rest')

st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")
st.title("🛡️ منصة تحليل المصداقية العلمية")

user_input = st.text_area("أدخل النص المراد فحصه علمياً:", height=150)

if st.button("🚀 بدء التحليل الأكاديمي"):
    if user_input:
        with st.spinner('🤖 جاري التحليل عبر Gemini 1.5 Flash...'):
            try:
                # نستخدم الموديل المستقر والأسرع
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"حلل مصداقية هذا النص بالعربية: {user_input}")
                
                if response.text:
                    st.success("✅ تم التحليل بنجاح!")
                    st.markdown(response.text)
                else:
                    st.error("لم يتمكن النظام من صياغة رد، حاول مرة أخرى.")
            except Exception as e:
                st.error(f"عذراً، حدث خطأ: {e}")
    else:
        st.warning("يرجى إدخال محتوى للفحص.")
