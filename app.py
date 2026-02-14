import streamlit as st
import google.generativeai as genai

# --- إعدادات الاتصال الآمن بالمحرك ---
# مفتاحك السري جاهز للعمل
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI" 

try:
    genai.configure(api_key=API_KEY)
    # استخدام التسمية الأكثر استقراراً للموديل
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error("فشل في تهيئة محرك الذكاء الاصطناعي.")

# --- واجهة المستخدم الاحترافية ---
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { background: linear-gradient(45deg, #007bff, #00d4ff); color: white; border-radius: 12px; height: 3.5em; width: 100%; border: none; font-weight: bold; }
    .main-box { background-color: #ffffff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-right: 10px solid #007bff; }
    .report-card { background-color: #f8f9fa; padding: 25px; border-radius: 15px; border: 1px solid #e9ecef; color: #2c3e50; line-height: 1.8; font-size: 1.1em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ منصة تحليل المصداقية العلمية المتقدمة")
st.write("نظام خبير مدعوم بالذكاء الاصطناعي لفحص المحتوى الرقمي وتفنيد الادعاءات.")

with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    user_input = st.text_area("أدخل رابط المنشور أو النص المراد تحليله بدقة علمية:", placeholder="انسخ الرابط أو النص هنا لتمحيصه...", height=120)
    
    if st.button("🚀 إجراء تحليل أكاديمي شامل"):
        if user_input:
            with st.spinner('🤖 جاري الاتصال بخادم Gemini لفحص البيانات...'):
                try:
                    # صياغة الأمر العلمي (Prompt) بذكاء
                    prompt = f"""
                    حلل المحتوى التالي بصفتك باحثاً أكاديمياً: {user_input}
                    أعطني تقريراً منظماً بالعربية يتضمن:
                    1. نسبة المصداقية التقديرية (0-100%).
                    2. رصد المغالطات المنطقية إن وجدت.
                    3. الفحص العلمي: هل يتفق الكلام مع الحقائق المثبتة؟
                    4. نصيحة للمشاهد: هل المنشور موثوق أم مضلل؟
                    """
                    
                    response = model.generate_content(prompt)
                    
                    st.divider()
                    st.success("✅ تم الفحص بنجاح")
                    st.subheader("📝 التقرير التحليلي المفصل")
                    st.markdown(f'<div class="report-card">{response.text}</div>', unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"حدث خطأ تقني: {e}")
                    st.info("تلميح: إذا استمر الخطأ، يرجى التأكد من أن المفتاح مفعل في منصة Google AI Studio.")
    st.markdown('</div>', unsafe_allow_html=True)
