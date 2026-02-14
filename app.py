import streamlit as st
import google.generativeai as genai

# --- 1. إعدادات المحرك والربط ---
# المفتاح السري الذي استخرجته في الصورة رقم 72
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"

def initialize_gemini():
    try:
        genai.configure(api_key=API_KEY)
        # هذا السطر يضمن الوصول للموديل بأكثر الطرق استقراراً
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        return model
    except Exception as e:
        st.error(f"خطأ في تهيئة المحرك: {e}")
        return None

model = initialize_gemini()

# --- 2. واجهة المستخدم الاحترافية ---
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")

# تصميم الواجهة بلمسة احترافية (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { background: linear-gradient(45deg, #007bff, #00d4ff); color: white; border-radius: 12px; height: 3.5em; width: 100%; border: none; font-weight: bold; }
    .main-box { background-color: #ffffff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-right: 10px solid #007bff; margin-bottom: 20px; }
    .report-card { background-color: #f8f9fa; padding: 25px; border-radius: 15px; border: 1px solid #e9ecef; color: #2c3e50; line-height: 1.8; font-size: 1.1em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ منصة تحليل المصداقية العلمية المتقدمة")
st.write("نظام خبير مدعوم بذكاء Gemini 1.5 لتمحيص المحتوى الرقمي وفحص الحقائق.")

# --- 3. منطقة العمل والمدخلات ---
with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    user_input = st.text_area("أدخل رابط المنشور أو النص المراد تحليله بدقة علمية:", placeholder="الصق الرابط أو النص هنا للفحص...", height=120)
    
    if st.button("🚀 إجراء تحليل أكاديمي شامل"):
        if user_input:
            if model:
                with st.spinner('🤖 جاري الاتصال بالذكاء الاصطناعي وتحليل البيانات...'):
                    try:
                        # هندسة الأوامر (Prompt Engineering) لضمان دقة النتيجة
                        prompt = f"""
                        بصفتك باحثاً أكاديمياً وخبيراً في نقد المحتوى، حلل النص التالي: {user_input}
                        قدم تقريراً مفصلاً ومنظماً باللغة العربية يتضمن:
                        1. نسبة المصداقية التقديرية (0-100%).
                        2. رصد أي مغالطات منطقية أو انحيازات.
                        3. مراجعة الحقائق العلمية المذكورة.
                        4. نصيحة ختامية للمستخدم.
                        """
                        
                        response = model.generate_content(prompt)
                        
                        st.divider()
                        st.success("✅ تم الفحص بنجاح")
                        st.subheader("📝 التقرير التحليلي المفصل:")
                        st.markdown(f'<div class="report-card">{response.text}</div>', unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error("عذراً، المحرك يواجه ضغطاً أو مشكلة في التوافق.")
                        st.info(f"تفاصيل الخطأ: {e}")
            else:
                st.error("المحرك غير مهيأ. تأكد من صحة مفتاح API.")
        else:
            st.warning("⚠️ يرجى إدخال محتوى أو رابط أولاً.")
    st.markdown('</div>', unsafe_allow_html=True)
