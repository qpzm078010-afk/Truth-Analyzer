import streamlit as st
import google.generativeai as genai

# الإعدادات الأساسية
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"
# السطر السحري: إجبار المكتبة على استخدام الإصدار المستقر v1
genai.configure(api_key=API_KEY, transport='rest')

# تصميم الواجهة
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")
st.title("🛡️ منصة تحليل المصداقية العلمية")

user_input = st.text_area("أدخل النص المراد فحصه علمياً:", height=150)

if st.button("🚀 بدء التحليل الأكاديمي"):
    if user_input:
        with st.spinner('🤖 جاري الاتصال بمحرك Gemini v1 المستقر...'):
            try:
                # نستخدم الموديل باسمه المباشر
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # إرسال الطلب
                response = model.generate_content(f"حلل هذا النص علمياً بالعربية: {user_input}")
                
                st.success("✅ تم التحليل بنجاح!")
                st.markdown(f"### النتيجة:\n{response.text}")
                
            except Exception as e:
                st.error(f"خطأ تقني: {e}")
                st.info("تلميح: إذا استمر الخطأ، سنقوم بتحديث بسيط في إعدادات Google AI Studio.")
    else:
        st.warning("يرجى إدخال محتوى أولاً.")
