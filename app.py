import streamlit as st

from agent.classifier import classify_email
from agent.reply_generator import generate_reply
from agent.summarizer import summarize_email
from agent.tone_detector import detect_tone

from utils.logger import log_interaction

# ===================================
# PAGE CONFIG
# ===================================

st.set_page_config(
    page_title="SmartMail AI",
    page_icon="📧",
    layout="wide"
)

# ===================================
# HEADER
# ===================================

st.title("📧 SmartMail AI")
st.subheader(
    "Enterprise Email Automation Assistant"
)

st.markdown("---")

# ===================================
# INPUT
# ===================================

email_text = st.text_area(
    " Enter Email",
    height=250
)

tone = st.selectbox(
    " Reply Tone",
    [
        "professional",
        "friendly",
        "formal",
        "empathetic",
        "concise"
    ]
)

generate = st.button(
    " Generate Response"
)

# ===================================
# PROCESS
# ===================================

if generate:

    if email_text.strip() == "":
        st.warning(
            "Please enter email content."
        )

    else:

        with st.spinner(
            "Analyzing Email..."
        ):

            category = classify_email(
                email_text
            )

            detected_tone = detect_tone(
                email_text
            )

            summary = summarize_email(
                email_text
            )

            reply = generate_reply(
                email_text,
                tone
            )

            log_interaction(
                email_text,
                category,
                detected_tone
            )

        st.success(
            "AI Processing Complete!"
        )

        # ===========================
        # RESULTS
        # ===========================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                " Email Analysis"
            )

            st.info(
                f"Category: {category}"
            )

            st.info(
                f"Detected Tone: {detected_tone}"
            )

            st.subheader(
                " Email Summary"
            )

            st.write(summary)

        with col2:

            st.subheader(
                " AI Reply"
            )

            st.text_area(
                "Generated Reply",
                reply,
                height=250
            )
