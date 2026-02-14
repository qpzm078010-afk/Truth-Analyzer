import streamlit as st
import google.generativeai as genai

# --- إعدادات المحرك الذكي ---
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI" 

genai.configure(api_key=API_KEY)

# استخدام اسم الموديل الأحدث والأكثر توافقاً
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- تصميم الواجهة الاحترافية ---
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { background: linear-gradient(45deg, #007bff, #00d4ff); color: white; border-radius: 12px; height: 3.5em; width: 100%; border: none; font-weight: bold; }
    .main-box { background-color: #ffffff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-right: 10px solid #007bff; }
    .report-card { background-color: #f8f9fa; padding: 20px; border-radius: 15px; border: 1px solid #e9ecef; color: #333; line-height: 1.8; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ منصة تحليل المصداقية العلمية المتقدمة")
st.write("نظام خبير يحلل المحتوى بناءً على قواعد المنطق، البيانات الحقيقية، والمنهج الأكاديمي.")

with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    user_input = st.text_area("أدخل رابط المنشور أو النص المراد تحليله بدقة علمية:", placeholder="انسخ الرابط أو المحتوى هنا...", height=120)
    if st.button("🚀 إجراء تحليل أكاديمي شامل"):
        if user_input:
            with st.spinner('🤖 جاري الاتصال بخادم الذكاء الاصطناعي للفحص...'):
                try:
                    prompt = f"حلل هذا المحتوى كباحث أكاديمي خبير: {user_input}. أعطني تقريراً بالعربية يشمل: 1. نسبة الموثوقية. 2. رصد المغالطات. 3. المنطق العلمي. 4. نصيحة للقارئ."
                    response = model.generate_content(prompt)
                    
                    st.divider()
                    st.success("✅ تم استلام تقرير الذكاء الاصطناعي")
                    st.subheader("📝 التقرير التحليلي المفصل")
                    st.markdown(f'<div class="report-card">{response.text}</div>', unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")
                    st.info("تلميح: تأكد من أن مفتاح API مفعل تماماً في Google AI Studio.")
    st.markdown('</div>', unsafe_allow_html=True)
