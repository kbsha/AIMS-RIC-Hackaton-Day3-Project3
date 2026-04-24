"""
Streamlit demo for the Math Tutor with multilingual & voice support.
Run: streamlit run demo.py
"""

import streamlit as st
import io
import wave
from gtts import gTTS
import tempfile
from tutor.core import (
    CurriculumLoader,
    ChildASRAdapter,
    ResponseScorer,
    LearnerState,
    FeedbackGenerator,
    LocalProgressStore,
)

# =========================
# 🔊 VOICE ENGINE (NEW)
# =========================
def speak(text, lang="en"):
    lang_map = {
        "en": "en",
        "fr": "fr",
        "kin": "en"   # fallback safe
    }

    tts = gTTS(text=text, lang=lang_map.get(lang, "en"))

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.save(f.name)
        return f.name


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Math Tutor",
    page_icon="🧮",
    layout="centered"
)

# =========================
# SESSION STATE
# =========================
if 'curriculum' not in st.session_state:
    st.session_state.curriculum = CurriculumLoader()
if 'learner_state' not in st.session_state:
    st.session_state.learner_state = LearnerState('demo_learner')
if 'item_index' not in st.session_state:
    st.session_state.item_index = 0
if 'store' not in st.session_state:
    st.session_state.store = LocalProgressStore()
    st.session_state.store.add_learner('demo_learner', 'Demo Child', 'en')
if 'asr' not in st.session_state:
    st.session_state.asr = ChildASRAdapter()
if 'scorer' not in st.session_state:
    st.session_state.scorer = ResponseScorer()
if 'language' not in st.session_state:
    st.session_state.language = 'en'

# =========================
# MAIN UI
# =========================
st.title("🧮 AI Math Tutor for Early Learners")

curriculum = st.session_state.curriculum
learner_state = st.session_state.learner_state
store = st.session_state.store
asr = st.session_state.asr
scorer = st.session_state.scorer

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.markdown("### ⚙️ Settings")

    language_map = {
        'English 🇬🇧': 'en',
        'Français 🇫🇷': 'fr',
        'Kinyarwanda 🇷🇼': 'kin'
    }

    lang_display = st.radio(
        "Language:",
        list(language_map.keys())
    )

    st.session_state.language = language_map[lang_display]

# =========================
# GET CURRENT ITEM
# =========================
if st.session_state.item_index < len(curriculum.items):

    current_item = curriculum.items[st.session_state.item_index]

    st.markdown("### 👂 Listen and Answer")

    lang_key = f"stem_{st.session_state.language}"
    question = current_item.get(lang_key, current_item.get('stem_en'))

    st.markdown(f"**Question:** {question}")

    # =========================
    # 🔊 SPEAK QUESTION (NEW)
    # =========================
    if st.button("🔊 Listen Question"):
        audio_q = speak(question, st.session_state.language)
        st.audio(audio_q)

    # =========================
    # VISUAL GROUNDING (IMPROVED)
    # =========================
    visual = current_item.get('visual')

    if visual:
        parts = visual.split('_')
        name = parts[0]

        nums = [int(s) for s in parts if s.isdigit()]
        count = nums[0] if nums else None

        emoji_map = {
            'apples': '🍎',
            'goats': '🐐',
            'beads': '🔵',
            'default': '🔢'
        }

        symbol = emoji_map.get(name.lower(), '🔢')

        if count:
            st.markdown("### 🧠 Visual Learning")
            st.markdown(symbol * min(count, 20))

    # =========================
    # INPUT
    # =========================
    transcript = st.text_input(
        "Your Answer:"
    )

    # =========================
    # SUBMIT
    # =========================
    if st.button("Submit Answer", type="primary"):

        if transcript.strip():

            # Score
            correct = scorer.score_response(
                current_item.get('answer_int', 0),
                transcript,
                current_item
            )

            # Detect language (code-switch awareness)
            detected_lang = asr.detect_language(transcript)

            # Save
            store.add_response(
                'demo_learner',
                current_item.get('skill'),
                current_item.get('id'),
                correct,
                transcript
            )

            learner_state.record_response(
                current_item.get('skill'),
                correct
            )

            # =========================
            # FEEDBACK ENGINE
            # =========================
            feedback = FeedbackGenerator.generate_feedback(
                correct,
                st.session_state.language,
                current_item.get('answer_int')
            )

            # =========================
            # CODE-SWITCH HANDLING (NEW)
            # =========================
            if detected_lang != st.session_state.language:
                feedback += " (I noticed mixed language input 👍)"

            # =========================
            # SHOW RESULT
            # =========================
            if correct:
                st.success(f"✅ {feedback}")
            else:
                st.error(f"❌ {feedback}")

            # =========================
            # 🔊 VOICE RESPONSE (NEW)
            # =========================
            audio = speak(feedback, st.session_state.language)
            st.audio(audio, autoplay=True)

            # NEXT QUESTION
            st.session_state.item_index += 1
            st.rerun()

        else:
            st.warning("Please enter an answer")

# =========================
# END SCREEN
# =========================
else:
    st.success("🎉 Great job! You finished!")

    if st.button("Restart"):
        st.session_state.item_index = 0
        st.rerun()