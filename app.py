import streamlit as st
import google.generativeai as genai

# الإعدادات الأساسية
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"

# السر هنا: إجبار المكتبة على استخدام الإصدار المستقر v1 وتجنب v1beta
genai.configure(api_key=API_KEY, transport='rest')

# تصميم الواجهة
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")
st.title("🛡️ منصة تحليل المصداقية العلمية")

user_input = st.text_area("أدخل النص المراد فحصه علمياً:", height=150)

if st.button("🚀 بدء التحليل الأكاديمي"):
    if user_input:
        with st.spinner('🤖 جاري التحليل عبر محرك Gemini v1 المستقر...'):
            try:
                # نستخدم الموديل باسمه المباشر لضمان الاتصال
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # إرسال الطلب
                response = model.generate_content(f"حلل مصداقية هذا النص بالعربية باختصار: {user_input}")
                
                st.success("✅ تم التحليل بنجاح!")
                st.markdown(f"### النتيجة:\n{response.text}")
                
            except Exception as e:
                # محاولة أخيرة بمسار بديل إذا فشل الأول
                try:
                    model_alt = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model_alt.generate_content(user_input)
                    st.write(response.text)
                except:
                    st.error(f"خطأ في الاتصال: {e}")
    else:
        st.warning("يرجى إدخال محتوى أولاً.")
