import streamlit as st
import google.generativeai as genai

# --- إعدادات المحرك الذكي ---
# تم وضع مفتاحك الخاص هنا مباشرة
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- تصميم الواجهة الاحترافية ---
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { background: linear-gradient(45deg, #007bff, #00d4ff); color: white; border-radius: 12px; height: 3.5em; width: 100%; border: none; font-weight: bold; }
    .main-box { background-color: #ffffff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-right: 10px solid #007bff; }
    .report-card { background-color: #f8f9fa; padding: 20px; border-radius: 15px; border: 1px solid #e9ecef; color: #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ منصة تحليل المصداقية العلمية المتقدمة")
st.write("نظام خبير يحلل المحتوى بناءً على قواعد المنطق، البيانات الحقيقية، والمنهج الأكاديمي.")

with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    user_input = st.text_area("أدخل رابط المنشور أو النص المراد تحليله بدقة علمية:", placeholder="انسخ الرابط أو المحتوى هنا...", height=120)
    if st.button("🚀 إجراء تحليل أكاديمي شامل"):
        if user_input:
            with st.spinner('🤖 يقوم الذكاء الاصطناعي الآن بتمحيص البيانات ومطابقتها مع الحقائق العلمية...'):
                try:
                    # صياغة الأمر العلمي
                    prompt = f"""
                    قم بتحليل هذا المحتوى كباحث أكاديمي خبير: {user_input}
                    أريد تقريراً باللغة العربية يتضمن:
                    1. **نسبة المصداقية (0-100%)**: بناءً على موثوقية المصدر.
                    2. **تحليل المغالطات**: رصد أي مغالطات منطقية.
                    3. **المنطق العلمي**: هل يتفق هذا الكلام مع الحقائق العلمية؟
                    4. **توصية نهائية**: نصيحة للمشاهد بخصوص تصديق هذا المحتوى.
                    """
                    response = model.generate_content(prompt)
                    
                    st.divider()
                    st.success("✅ اكتمل التحليل الأكاديمي")
                    
                    st.subheader("📝 التقرير التحليلي المفصل")
                    st.markdown(f'<div class="report-card">{response.text}</div>', unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"حدث خطأ في الاتصال بالخدمة: {e}")
        else:
            st.warning("⚠️ يرجى تزويد النظام ببيانات للتحليل.")
    st.markdown('</div>', unsafe_allow_html=True)
