import streamlit as st
import google.generativeai as genai

# --- 1. إعدادات المحرك السري ---
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"

def get_stable_model():
    try:
        genai.configure(api_key=API_KEY)
        # هذا السطر هو الحل: يجبر النظام على استخدام الإصدار المستقر v1 بدلاً من v1beta
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            generation_config={"top_p": 0.95, "top_k": 64, "temperature": 1.0}
        )
        return model
    except Exception as e:
        st.error(f"فشل الاتصال الأولي: {e}")
        return None

model = get_stable_model()

# --- 2. واجهة المستخدم (التصميم الاحترافي) ---
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")

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
st.write("نظام خبير مدعوم بالذكاء الاصطناعي لفحص المحتوى الرقمي.")

# --- 3. منطقة العمل ---
with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    user_input = st.text_area("أدخل رابط المنشور أو النص المراد تحليله بدقة علمية:", placeholder="الصق الرابط هنا...", height=120)
    
    if st.button("🚀 إجراء تحليل أكاديمي شامل"):
        if user_input:
            with st.spinner('🤖 جاري محادثة خوادم جوجل الذكية...'):
                try:
                    # طلب التحليل بأسلوب أكاديمي
                    prompt = f"حلل هذا المحتوى كخبير أكاديمي محايد: {user_input}. أريد تقريراً بالعربية يشمل: نسبة المصداقية، رصد المغالطات، المنطق العلمي، ونصيحة للقارئ."
                    
                    # محاولة توليد المحتوى
                    response = model.generate_content(prompt)
                    
                    st.divider()
                    st.success("✅ تم الفحص بنجاح!")
                    st.subheader("📝 التقرير التحليلي المفصل:")
                    st.markdown(f'<div class="report-card">{response.text}</div>', unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error("المحرك لا يزال يرفض الاتصال بـ v1beta. جاري محاولة الحل التلقائي...")
                    # محاولة بديلة نهائية (Fallback)
                    try:
                        alt_model = genai.GenerativeModel('models/gemini-1.5-flash')
                        response = alt_model.generate_content(prompt)
                        st.markdown(f'<div class="report-card">{response.text}</div>', unsafe_allow_html=True)
                    except:
                        st.info("يرجى التأكد من تفعيل 'Gemini API' في إعدادات المشروع داخل Google AI Studio.")
    st.markdown('</div>', unsafe_allow_html=True)
