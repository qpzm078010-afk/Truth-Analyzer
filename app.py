import streamlit as st
import google.generativeai as genai

# --- الإعداد الأساسي ---
# مفتاحك الذي استخرجته في الصورة رقم 72
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"

# تهيئة المفتاح مع تفعيل ميزة التوافق الشامل
genai.configure(api_key=API_KEY)

# --- واجهة المستخدم ---
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { background: linear-gradient(45deg, #007bff, #00d4ff); color: white; border-radius: 12px; height: 3.5em; width: 100%; border: none; font-weight: bold; }
    .report-card { background-color: #f8f9fa; padding: 25px; border-radius: 15px; border: 1px solid #007bff; color: #2c3e50; line-height: 1.8; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ محلل الحقيقة العلمي - النسخة المستقرة")

user_input = st.text_area("أدخل النص أو الرابط المراد فحص مصداقيته:", height=150)

if st.button("🚀 تحليل المحتوى الآن"):
    if user_input:
        with st.spinner('🤖 جاري الفحص عبر محرك Gemini...'):
            try:
                # استخدمنا هنا أبسط تعريف للموديل لضمان عدم حدوث خطأ 404
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"حلل المحتوى التالي بأسلوب علمي دقيق باللغة العربية: {user_input}. اذكر نسبة المصداقية والمغالطات المنطقية."
                
                response = model.generate_content(prompt)
                
                st.success("✅ اكتمل التحليل!")
                st.markdown(f'<div class="report-card">{response.text}</div>', unsafe_allow_html=True)
                
            except Exception as e:
                # حل بديل فوري في حال فشل الاتصال الأول
                st.info("جاري محاولة الاتصال عبر الخادم البديل...")
                try:
                    model_alt = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model_alt.generate_content(prompt)
                    st.markdown(f'<div class="report-card">{response.text}</div>', unsafe_allow_html=True)
                except:
                    st.error("هناك مشكلة في تفعيل مفتاح API من جانب جوجل. يرجى التأكد أن المفتاح في Google AI Studio يظهر بجانبه 'Free Tier' أو 'Active'.")
    else:
        st.warning("يرجى كتابة نص أو لصق رابط أولاً.")
