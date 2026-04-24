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

# Page config
st.set_page_config(
    page_title="Math Tutor",
    page_icon="🧮",
    layout="centered"
)

# Initialize session state
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
if 'use_audio' not in st.session_state:
    st.session_state.use_audio = False

# Main UI
st.title("🧮 AI Math Tutor for Early Learners")

curriculum = st.session_state.curriculum
learner_state = st.session_state.learner_state
store = st.session_state.store
asr = st.session_state.asr
scorer = st.session_state.scorer

# Sidebar - Settings & Progress
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    language_map = {'English 🇬🇧': 'en', 'Français 🇫🇷': 'fr', 'Kinyarwanda 🇷🇼': 'kin'}
    lang_display = st.radio(
        "Language:",
        list(language_map.keys()),
        index=list(language_map.keys()).index('English 🇬🇧')
    )
    st.session_state.language = language_map[lang_display]
    
    st.session_state.use_audio = st.checkbox("🎤 Enable Voice Input", value=False)
    
    st.markdown("---")
    st.markdown("### 📊 Progress")
    total_items = len(curriculum.items)
    completed = st.session_state.item_index
    st.progress(completed / total_items if total_items > 0 else 0)
    st.markdown(f"**{completed}/{total_items}** items completed")
    
    # Show learner state
    st.markdown("### 🧠 Knowledge State")
    for skill, bkt in learner_state.skills.items():
        st.metric(f"{skill}", f"{bkt.p_learned:.1%}")


# Get current item
if st.session_state.item_index < len(curriculum.items):
    current_item = curriculum.items[st.session_state.item_index]
    
    st.markdown("### 👂 Listen and Answer")
    
    # Get question in selected language
    lang_key = f"stem_{st.session_state.language}"
    question = current_item.get(lang_key, current_item.get('stem_en', 'N/A'))
    st.markdown(f"**Question:** {question}")

    # Visual aid (use emoji fallbacks if image assets are not available)
    visual = current_item.get('visual')
    if visual:
        # Expected format like 'apples_3' or 'goats_5' or 'beads_2_plus_1'
        try:
            parts = visual.split('_')
            name = parts[0]
            # extract a numeric count if present anywhere in the visual string
            nums = [int(s) for s in parts if s.isdigit()]
            count = nums[0] if nums else None
        except Exception:
            name = visual
            count = None

        emoji_map = {
            'apples': '🍎',
            'apple': '🍎',
            'goats': '🐐',
            'goat': '🐐',
            'beads': '🔵',
            'default': '🔢'
        }

        symbol = emoji_map.get(name.lower(), emoji_map['default'])
        if count and count > 0:
            # show a reasonable number of emojis (cap at 20)
            display_count = min(count, 20)
            st.markdown("**Visual:** " + (symbol * display_count))
        else:
            st.markdown(f"**Visual:** {visual}")
    
    # Input method selection
    col1, col2 = st.columns(2)
    with col1:
        use_voice = st.checkbox("Use voice" if st.session_state.language == 'en' else 
                               "Utiliser la voix" if st.session_state.language == 'fr' else
                               "Koresha amajwi")
    
    # Input based on selection
    transcript = ""
    
    if use_voice:
        st.info("🎤 You can upload a short audio clip or use your microphone (if supported).")
        audio_file = st.file_uploader("Upload audio (wav/mp3)", type=['wav', 'mp3', 'm4a'])
        transcript = ""
        if audio_file is not None:
            # Save uploaded audio to a temporary file and try to transcribe
            try:
                with open('temp_audio_input', 'wb') as f:
                    f.write(audio_file.getbuffer())
                # Attempt ASR using the project adapter (Whisper) if available
                if asr and getattr(asr, 'asr_available', False):
                    trans = asr.transcribe('temp_audio_input')
                    transcript = trans or ''
                    st.info("ASR transcript: " + transcript)
                else:
                    st.warning("ASR not available in this environment. Please type your answer instead.")
            except Exception as e:
                st.error(f"Audio handling error: {e}")
        else:
            # fallback to typed transcript if no upload provided
            transcript = st.text_input(
                "Your Answer (or ASR transcript):" if st.session_state.language == 'en' else
                "Votre réponse (ou transcription ASR):" if st.session_state.language == 'fr' else
                "Igisubizo cyawe (cyangwa ASR transcript):",
                placeholder="Type your answer here" if st.session_state.language == 'en' else
                           "Tapez votre réponse ici" if st.session_state.language == 'fr' else
                           "Andika igisubizo cyawe hano"
            )
    else:
        transcript = st.text_input(
            "Your Answer:" if st.session_state.language == 'en' else
            "Votre réponse:" if st.session_state.language == 'fr' else
            "Igisubizo cyawe:",
            placeholder="Type your answer here" if st.session_state.language == 'en' else
                       "Tapez votre réponse ici" if st.session_state.language == 'fr' else
                       "Andika igisubizo cyawe hano"
        )
    
    if st.button("Submit Answer" if st.session_state.language == 'en' else
                "Soumettre la réponse" if st.session_state.language == 'fr' else
                "Kohereza Igisubizo", type="primary"):
        if transcript.strip():
            # Score response
            correct = scorer.score_response(
                current_item.get('answer_int', 0),
                transcript,
                current_item
            )
            
            # Detect language
            detected_lang = asr.detect_language(transcript)
            
            # Record response
            store.add_response(
                'demo_learner',
                current_item.get('skill', 'unknown'),
                current_item.get('id', 'unknown'),
                correct,
                transcript
            )
            
            # Update learner state
            learner_state.record_response(current_item.get('skill', 'unknown'), correct)
            
            # Generate feedback
            feedback = FeedbackGenerator.generate_feedback(
                correct,
                st.session_state.language,
                current_item.get('answer_int', 0)
            )
            
            # Display result
            if correct:
                st.success(f"✅ {feedback}")
            else:
                st.error(f"❌ {feedback}")
            
            # Move to next item
            st.session_state.item_index += 1
            st.rerun()
        else:
            st.warning("Please enter an answer" if st.session_state.language == 'en' else
                      "Veuillez entrer une réponse" if st.session_state.language == 'fr' else
                      "Nyamuneka andika igisubizo")
else:
    st.success("🎉 Great job! You completed all items!" if st.session_state.language == 'en' else
              "🎉 Excellent! Vous avez terminé tous les éléments!" if st.session_state.language == 'fr' else
              "🎉 Mwarakaza! Warangije ibintu byose!")
    if st.button("Start Over" if st.session_state.language == 'en' else
                "Recommencer" if st.session_state.language == 'fr' else
                "Tangira Hanyuma"):
        st.session_state.item_index = 0
        st.session_state.learner_state = LearnerState('demo_learner')
        st.rerun()

# Sidebar - Debug info
with st.sidebar:
    st.markdown("---")
    st.markdown("### 🔍 Debug Info")
    st.write(f"Language: {st.session_state.language}")
    st.write(f"Voice enabled: {st.session_state.use_audio}")
    if st.session_state.item_index < len(curriculum.items):
        current_item = curriculum.items[st.session_state.item_index]
        st.write(f"Expected answer: {current_item.get('answer_int', 'N/A')}")
