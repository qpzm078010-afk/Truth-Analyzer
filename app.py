import streamlit as st
import google.generativeai as genai

# --- 1. إعدادات المفتاح ---
API_KEY = "AIzaSyCmimhzMPnRrK9G2Dc0gqdJsiaLYlnmNTI"

# إعداد المكتبة لتستخدم الإصدار المستقر v1 بدلاً من v1beta
genai.configure(api_key=API_KEY, transport='rest') # استخدام rest يحل مشاكل الاتصال

# --- 2. واجهة المستخدم الاحترافية ---
st.set_page_config(page_title="Truth Analyzer Pro", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stButton>button { background: linear-gradient(45deg, #007bff, #00d4ff); color: white; border-radius: 12px; height: 3.5em; width: 100%; border: none; font-weight: bold; }
    .main-box { background-color: #ffffff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-right: 10px solid #007bff; margin-bottom: 20px; }
    .report-card { background-color: #f8f9fa; padding: 25px; border-radius: 15px; border: 1px solid #e9ecef; color: #2c3e50; line-height: 1.8; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ منصة تحليل المصداقية العلمية")
st.write("نظام خبير مدعوم بذكاء Gemini لفحص المحتوى الرقمي.")

# --- 3. منطقة التحليل ---
with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    user_input = st.text_area("أدخل رابط المنشور أو النص المراد تحليله:", placeholder="الصق المحتوى هنا...", height=120)
    
    if st.button("🚀 بدء التحليل الأكاديمي"):
        if user_input:
            with st.spinner('🤖 جاري تمحيص البيانات عبر خوادم جوجل...'):
                try:
                    # نستخدم 'gemini-1.5-flash' بدون كلمة models/ وبدون إضافات
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    prompt = f"حلل هذا المحتوى كخبير أكاديمي محايد: {user_input}. أريد تقريراً بالعربية يشمل: نسبة المصداقية، رصد المغالطات، والمنطق العلمي."
                    
                    response = model.generate_content(prompt)
                    
                    st.divider()
                    st.success("✅ تم الفحص بنجاح")
                    st.markdown(f'<div class="report-card">{response.text}</div>', unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"حدث خطأ في الاتصال. جاري محاولة إصلاح المسار تلقائياً...")
                    # محاولة بديلة نهائية في حال فشل الأولى
                    try:
                        alt_model = genai.GenerativeModel('models/gemini-1.5-flash')
                        response = alt_model.generate_content(prompt)
                        st.markdown(f'<div class="report-card">{response.text}</div>', unsafe_allow_html=True)
                    except Exception as e2:
                        st.error("المحرك لا يستجيب حالياً. يرجى التأكد من تفعيل API في Google AI Studio.")
    st.markdown('</div>', unsafe_allow_html=True)
