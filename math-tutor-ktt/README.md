# 🧠🎨 AI Multimodal Math Tutor for Early Learners by kibremoges Fenta

**AIMS KTT Hackathon 2026 · Challenge S2.T3.1**

An **offline-first, multilingual AI tutor** for children (ages 5–9) that teaches foundational math using **voice, visuals, and adaptive learning**. The system integrates **speech recognition, text-to-speech, and AI-generated images** to simulate a real tutoring experience in low-resource settings.

---

# 🚀 Key Features

### 🧠 Adaptive Learning

* Bayesian-style learner modeling (knowledge state per skill)
* Difficulty adapts based on performance

### 🌍 Multilingual + Code-Switch Support

* English 🇬🇧, French 🇫🇷, Kinyarwanda 🇷🇼
* Detects mixed-language responses
* Responds in dominant language

### 🎤 Voice Interaction

* Speech → Text (ASR via Whisper)
* Text → Speech (TTS via gTTS)
* Full tutor loop: **listen → respond → speak**

### 🖼️ Visual Learning

* Emoji-based grounding (offline-safe)
* AI-generated images using
  Stable Diffusion XL via
  Hugging Face API

### 📊 Local Progress Tracking

* SQLite database (offline)
* Tracks responses, correctness, and skill mastery

---

# ⚡ Quick Start

## 1. Clone & Open

```bash
git clone https://github.com/YOUR_USERNAME/ai-math-tutor.git
cd ai-math-tutor
code .
```

---

## 2. Create Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. (Optional) Add Hugging Face Token

For image generation:

```bash
set HF_TOKEN=your_token_here   # Windows
```

Or create:

```
.streamlit/secrets.toml
```

```toml
HF_TOKEN="your_token_here"
```

---

## 5. Run App

```bash
streamlit run demo.py
```

Open:

```
http://localhost:8501
```

---

# 🖥️ App Modes

### 📚 Tutor Mode

* Solve math problems
* Speak or type answers
* Get instant feedback (voice + text)
* Adaptive progression

### 🎨 Image Generator Mode

* Generate visual explanations (e.g. “3 apples + 2 apples”)
* Uses Stable Diffusion via Hugging Face

---

# 📁 Project Structure

```
ai-math-tutor/
├── tutor/
│   ├── core.py              # Core logic (BKT, scoring, ASR adapter)
│   └── data/
│       ├── curriculum.json
│       └── progress.db
│
├── demo.py                  # Streamlit app (UI + integration)
├── requirements.txt
├── README.md
└── process_log.md
```

---

# 🧠 System Architecture

```
🎤 Voice Input (Whisper)
        ↓
🧠 Tutor Engine (Scoring + BKT)
        ↓
🖼️ Visual Generator (Stable Diffusion)
        ↓
🔊 Feedback (gTTS)
        ↓
📊 SQLite Progress Store
```

---

# 📦 Dependencies

* streamlit
* faster-whisper
* gTTS
* huggingface_hub
* Pillow
* numpy

---

# ⚠️ Design Decisions

* **Offline-first:** Core tutor works without internet
* **Lightweight:** CPU-only inference (Whisper tiny)
* **Fallbacks:**

  * No HF token → image generation disabled
  * No ASR → text input fallback

---

# 🧪 Known Limitations

* Image generation requires internet (HF API)
* TTS uses cloud (can be replaced with offline engines like Coqui)
* Visual grounding currently heuristic (emoji-based baseline)

---

# 🏆 Hackathon Tasks Coverage

| Task                          | Status                   |
| ----------------------------- | ------------------------ |
| On-device inference pipeline  | ✅                        |
| Knowledge tracing (BKT)       | ✅                        |
| Multilingual + code-switch    | ✅                        |
| Voice interaction             | ✅                        |
| Visual grounding              | ✅ (baseline + AI images) |
| Local progress store (SQLite) | ✅                        |

---

# 📊 Future Improvements

* GRU-based Deep Knowledge Tracing
* Offline TTS (Coqui / Piper)
* Object detection (true visual grounding)
* Parent dashboard (PDF reports)
* GGUF quantized LLM for full offline tutor

---

# 📝 Process Transparency

All tool usage and development steps are documented in:

```
process_log.md
```

---

# 📜 License

MIT License

---

# 🙌 Acknowledgment

Built for AIMS KTT Hackathon 2026
Focus: **AI for education in low-resource environments**

---

# ✅ Final Note

This system demonstrates a **practical, scalable AI tutor** combining:

* Speech
* Vision
* Language
* Adaptive learning

Designed to work **where traditional EdTech fails**.

---
