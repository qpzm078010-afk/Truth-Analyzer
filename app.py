import streamlit as st
import requests
import json

# الإعدادات
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"
# الرابط الرسمي المستقر (v1) لضمان عدم ظهور 404
API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")
st.title("🛡️ منصة تحليل المصداقية العلمية")

user_input = st.text_area("أدخل النص المراد فحصه علمياً:", height=150)

if st.button("🚀 بدء التحليل الأكاديمي"):
    if user_input:
        with st.spinner('🤖 جاري الاتصال المباشر بمحرك جوجل...'):
            try:
                # تجهيز البيانات للإرسال اليدوي
                payload = {
                    "contents": [{
                        "parts": [{"text": f"حلل مصداقية هذا النص بالعربية باختصار: {user_input}"}]
                    }]
                }
                headers = {'Content-Type': 'application/json'}
                
                # إرسال الطلب
                response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
                result = response.json()
                
                # استخراج النص من الإجابة المعقدة
                if response.status_code == 200:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("✅ تم التحليل بنجاح!")
                    st.markdown(answer)
                else:
                    st.error(f"خطأ من جوجل: {result.get('error', {}).get('message', 'خطأ غير معروف')}")
            except Exception as e:
                st.error(f"فشل الاتصال: {e}")
    else:
        st.warning("يرجى إدخال محتوى.")
