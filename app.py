import streamlit as st
import google.generativeai as genai

# الإعدادات الأساسية
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"
genai.configure(api_key=API_KEY)

# تصميم الواجهة
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")
st.title("🛡️ منصة تحليل المصداقية العلمية")

# منطقة الإدخال
user_input = st.text_area("أدخل النص أو الرابط المراد فحصه علمياً:", height=150)

if st.button("🚀 بدء التحليل الأكاديمي"):
    if user_input:
        with st.spinner('🤖 جاري فحص البيانات...'):
            try:
                # استخدام الموديل gemini-pro لضمان التوافق مع الإصدار 0.4.1
                model = genai.GenerativeModel('gemini-pro')
                prompt = f"حلل هذا المحتوى كباحث أكاديمي بالعربية: {user_input}"
                response = model.generate_content(prompt)
                
                st.success("✅ تم التحليل بنجاح!")
                st.write(response.text)
            except Exception as e:
                st.error(f"عذراً، حدث خطأ تقني: {e}")
    else:
        st.warning("يرجى إدخال محتوى أولاً.")
