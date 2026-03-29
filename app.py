import streamlit as st

st.set_page_config(page_title="MediAssist AI", layout="centered")

# Sidebar menu
menu = st.sidebar.selectbox("📌 Menu", ["🏠 Home", "🩺 Analyze Problem", "ℹ️ About"])

# ---------------- HOME ----------------
if menu == "🏠 Home":
    st.title("🩺 MediAssist AI")
    st.subheader("AI-Powered Healthcare Assistant")

    st.write("""
    Welcome to MediAssist AI!

    This system helps patients:
    - Understand their medical problems
    - Get basic guidance
    - Reduce confusion about health conditions

    👉 Use the menu to analyze your medical problem.
    """)

# ---------------- ANALYZE ----------------
elif menu == "🩺 Analyze Problem":
    st.title("🧠 Analyze Your Medical Problem")

    user_input = st.text_area("📝 Describe your symptoms or medical issue")

    language = st.selectbox("🌐 Choose Language", ["English", "Hindi", "Telugu"])

    if st.button("Analyze Problem"):
        if user_input:

            # Response (more like conversation)
            response = f"""
            🤖 Based on your input: "{user_input}"

            It appears that this could be related to a general health condition that needs attention.

            ✔️ Possible concerns:
            - Mild to moderate health issue
            - Needs proper care and monitoring

            ✔️ What you should do:
            - Follow basic precautions
            - Maintain good diet and hydration
            - Consult a doctor if symptoms continue

            ✔️ Important:
            Do not ignore symptoms. Early care helps prevent complications.
            """

            # Language handling
            if language == "Hindi":
                response = "आपकी समस्या के आधार पर, यह एक स्वास्थ्य स्थिति हो सकती है जिसके लिए ध्यान आवश्यक है। डॉक्टर से परामर्श करें।"
            elif language == "Telugu":
                response = "మీ సమస్య ఆధారంగా ఇది ఆరోగ్య సమస్య కావచ్చు. దయచేసి డాక్టర్‌ను సంప్రదించండి."

            st.success(response)

        else:
            st.error("Please enter your problem.")

# ---------------- ABOUT ----------------
elif menu == "ℹ️ About":
    st.title("ℹ️ About MediAssist AI")

    st.write("""
    MediAssist AI is an intelligent healthcare support system designed to:

    - Simplify medical understanding
    - Assist rural and elderly patients
    - Provide basic healthcare guidance

    ⚠️ This system does not replace doctors.
    Always consult a medical professional for serious conditions.

    👩‍💻 Developed for ET AI Hackathon
    """)
