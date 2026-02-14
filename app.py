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
        with st.spinner('🤖 جاري فحص البيانات عبر محرك Gemini...'):
            try:
                # تغيير الاسم إلى الموديل الأحدث والمتاح حالياً
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"حلل هذا المحتوى كباحث أكاديمي محايد وباللغة العربية: {user_input}"
                response = model.generate_content(prompt)
                
                st.success("✅ تم التحليل بنجاح!")
                st.markdown(f"### النتيجة:\n{response.text}")
            except Exception as e:
                st.error(f"عذراً، حدث خطأ تقني: {e}")
                st.info("تلميح: إذا ظهر خطأ 404، فقد يكون هناك تحديث في خوادم جوجل، سنحاول معاً حله.")
    else:
        st.warning("يرجى إدخال محتوى أولاً.")
