import streamlit as st
import google.generativeai as genai

# الإعدادات
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"
# هذا السطر هو السر: نحدد الإصدار المستقر v1 بدلاً من v1beta
genai.configure(api_key=API_KEY, transport='rest')

# الواجهة
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")
st.title("🛡️ منصة تحليل المصداقية العلمية")

user_input = st.text_area("أدخل النص أو الرابط المراد فحصه علمياً:", height=150)

if st.button("🚀 بدء التحليل الأكاديمي"):
    if user_input:
        with st.spinner('🤖 جاري فحص البيانات...'):
            try:
                # نستخدم الموديل بدون كلمة models/ وبدون إضافات لضمان التوافق
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"حلل مصداقية هذا النص بالعربية: {user_input}")
                
                st.success("✅ تم التحليل بنجاح!")
                st.markdown(f"### النتيجة:\n{response.text}")
            except Exception as e:
                # محاولة بديلة نهائية إذا فشلت الأولى
                try:
                    alt_model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = alt_model.generate_content(user_input)
                    st.write(response.text)
                except:
                    st.error(f"خطأ في الاتصال: {e}")
    else:
        st.warning("يرجى إدخال محتوى أولاً.")
