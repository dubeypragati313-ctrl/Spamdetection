import streamlit as st
import pickle
import pandas as pd

# Page Configuration (Wide layout & icon)
st.set_page_config(
    page_title="AI Spam Detector",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS for Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff2b2b;
        color: white;
    }
    .result-card-spam {
        background-color: #ffe6e6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4d4d;
        color: #990000;
    }
    .result-card-ham {
        background-color: #e6ffe6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2eb82e;
        color: #006600;
    }
    </style>
""", unsafe_allow_html=True)

# Session State for History & Counters
if 'history' not in st.session_state:
    st.session_state.history = []
if 'spam_count' not in st.session_state:
    st.session_state.spam_count = 0
if 'ham_count' not in st.session_state:
    st.session_state.ham_count = 0

# Load Model & Vectorizer
@st.cache_resource
def load_model():
    model = pickle.load(open('spam_model.pkl', 'rb'))
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    return model, tfidf

try:
    model, tfidf = load_model()
except Exception as e:
    st.error("Model files (.pkl) missing. Please make sure spam_model.pkl and vectorizer.pkl are in the same folder.")

# Sidebar - History & Analytics
st.sidebar.title("📜 Detection History")
st.sidebar.write(f"**Total Checked:** {len(st.session_state.history)}")

col_s1, col_s2 = st.sidebar.columns(2)
col_s1.metric("🚨 Spam", st.session_state.spam_count)
col_s2.metric("✅ Ham", st.session_state.ham_count)

st.sidebar.markdown("---")

if st.sidebar.button("🗑️ Clear History"):
    st.session_state.history = []
    st.session_state.spam_count = 0
    st.session_state.ham_count = 0
    st.rerun()

if st.session_state.history:
    st.sidebar.write("### Recent Checks:")
    for item in reversed(st.session_state.history):
        tag = "🔴 SPAM" if item['result'] == "Spam" else "🟢 HAM"
        st.sidebar.info(f"**{tag}**\n\n_{item['text'][:40]}..._")

# Main Interface Layout
st.title("🛡️ Smart Email & SMS Spam Detector")
st.markdown("Analyze incoming text messages, emails, or notifications using Machine Learning.")

# Sample Quick Buttons
st.write("**Try Sample Messages:**")
col_e1, col_e2 = st.columns(2)

example_text = ""
if col_e1.button("📩 Load Sample Spam"):
    example_text = "WINNER!! You have won $1,000 cash! Call 08000930701 to claim immediately."
if col_e2.button("✉️ Load Sample Normal Text"):
    example_text = "Hey, are we still meeting for lunch today at 1 PM?"

# Text Input Box
input_sms = st.text_area("Enter message below:", value=example_text, height=120, placeholder="Paste email or SMS text here...")

# Predict Action
if st.button('🔍 Analyze Message'):
    if input_sms.strip() != "":
        # Transform & Predict
        transformed_sms = tfidf.transform([input_sms])
        prediction = model.predict(transformed_sms)[0]
        
        # Display Results
        st.markdown("### Result:")
        if prediction == 1:
            st.markdown(f"""
                <div class="result-card-spam">
                    <h2>🚨 Spam Detected!</h2>
                    <p>This message contains common spam patterns or promotional phishing characteristics.</p>
                </div>
            """, unsafe_allow_html=True)
            st.session_state.spam_count += 1
            res_label = "Spam"
        else:
            st.markdown(f"""
                <div class="result-card-ham">
                    <h2>✅ Safe / Normal Message (Ham)</h2>
                    <p>This message looks legitimate and safe.</p>
                </div>
            """, unsafe_allow_html=True)
            st.session_state.ham_count += 1
            res_label = "Ham"
            
        # Append to History
        st.session_state.history.append({
            'text': input_sms,
            'result': res_label
        })
    else:
        st.warning("⚠️ Please enter a message before clicking analyze.")
