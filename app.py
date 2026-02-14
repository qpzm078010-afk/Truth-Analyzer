import streamlit as st
import google.generativeai as genai
import os

# الإعدادات الأساسية
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"

# السر هنا: إجبار المكتبة على استخدام الإصدار المستقر v1 وتجاوز v1beta كلياً
genai.configure(api_key=API_KEY, transport='rest')

# تصميم الواجهة
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")
st.title("🛡️ منصة تحليل المصداقية العلمية")

user_input = st.text_area("أدخل النص المراد فحصه علمياً:", height=150)

if st.button("🚀 بدء التحليل الأكاديمي"):
    if user_input:
        with st.spinner('🤖 جاري الاتصال بمحرك Gemini الرسمي...'):
            try:
                # نحدد الموديل بدون أي لواحق تجريبية
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # إرسال الطلب مع تحديد الأمان (اختياري لضمان الرد)
                response = model.generate_content(f"حلل مصداقية النص التالي باختصار وبالعربية: {user_input}")
                
                st.success("✅ تم التحليل بنجاح!")
                st.markdown(f"### النتيجة:\n{response.text}")
                
            except Exception as e:
                st.error(f"حدث خطأ في الاتصال: {e}")
                st.info("تلميح: إذا استمر الخطأ، سنقوم بتغيير اسم الموديل إلى gemini-pro كخيار بديل.")
    else:
        st.warning("يرجى إدخال محتوى أولاً.")
