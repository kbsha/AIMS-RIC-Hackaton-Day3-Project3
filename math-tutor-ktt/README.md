# 🧮 AI Math Tutor for Early Learners

**AIMS KTT Hackathon 2026 · Challenge S2.T3.1**

An offline, multilingual AI tutor for children aged 5–9 teaching foundational math through audio, visuals, and adaptive learning.

---

## 🚀 Quick Start (VS Code)

### 1. **Open in VS Code**

```bash
# Open this folder in VS Code
code math-tutor-ktt/

# Or from command line
cd math-tutor-ktt
code .
```

### 2. **Create Virtual Environment** (in VS Code terminal)

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Run Tests**

```bash
python -m pytest tests/ -v
```

### 5. **Run the Demo**

```bash
python demo.py
```

Then open: **http://localhost:7860**

---

## 📁 Project Structure

```
math-tutor-ktt/
├── tutor/                      # Main package
│   ├── __init__.py
│   ├── core.py                 # All core classes
│   └── data/
│       ├── curriculum.json     # Sample curriculum (7 items)
│       └── progress.db         # Created on first run
│
├── notebooks/                  # Jupyter notebooks
│   └── kt_eval.ipynb          # Knowledge tracing evaluation
│
├── demo.py                     # Gradio web interface
├── requirements.txt            # Dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
├── SIGNED.md                   # Honor code (sign before submitting)
└── process_log.md              # LLM usage log (update as you go)
```

---

## 🎯 What's Included

### **Core Components** (in `tutor/core.py`)

✅ **CurriculumLoader** — Load math items from JSON  
✅ **ChildASRAdapter** — Speech-to-text (Whisper) + language detection  
✅ **ResponseScorer** — Check if answer is correct  
✅ **BayesianKnowledgeTracing** — Predict learner knowledge  
✅ **LearnerState** — Track learner across all skills  
✅ **FeedbackGenerator** — Generate multilingual feedback  
✅ **LocalProgressStore** — SQLite learner progress storage  

### **Demo** (`demo.py`)

A Gradio web interface where you can:
- Enter a child's response (text or ASR transcript)
- Get immediate feedback
- See if the answer was correct
- Automatically move to next item

### **Sample Data** (`tutor/data/curriculum.json`)

7 sample curriculum items covering:
- Counting (2 items)
- Addition (2 items)
- Subtraction (1 item)
- Number Sense (1 item)
- Word Problems (1 item)

---

## 📖 How to Use

### **1. Explore the Code**

Open `tutor/core.py` in VS Code. All classes are well-documented:

```python
class BayesianKnowledgeTracing:
    """Bayesian Knowledge Tracing model for predicting learner knowledge."""
    
    def __init__(self, skill: str):
        self.p_learned = 0.1  # Initial probability
    
    def update(self, correct: bool) -> float:
        """Update P(learned) given correctness."""
        # ... Bayes rule implementation
```

### **2. Run the Demo Locally**

```bash
# Terminal in VS Code
python demo.py
```

Then:
- Click the link to open in browser
- Type an answer or paste a transcript
- Click "Submit"
- See feedback instantly

### **3. Test Individual Components**

```python
# In VS Code terminal or Python interactive
from tutor import CurriculumLoader, ResponseScorer

# Load curriculum
curriculum = CurriculumLoader()
item = curriculum.get_initial_item()
print(f"Question: {item['stem_en']}")
print(f"Expected answer: {item['answer_int']}")

# Score a response
scorer = ResponseScorer()
is_correct = scorer.score_response(3, "three", item)
print(f"Is 'three' correct? {is_correct}")
```

### **4. Extend for Your Hackathon**

Build on these classes:

```python
# Example: Add visual grounding
from tutor.core import CurriculumLoader

curriculum = CurriculumLoader()
item = curriculum.get_initial_item()

# TODO: Count objects in item['visual']
# TODO: Compare detected count with item['answer_int']
```

---

## 🔧 VS Code Extensions (Recommended)

Install these in VS Code for a better experience:

1. **Python** (Microsoft) — Syntax highlighting, linting, debugging
2. **Pylance** — Type hints, IntelliSense
3. **Jupyter** (Microsoft) — Run notebooks directly
4. **Thunder Client** or **REST Client** — Test APIs
5. **GitLens** — Git history integration

---

## 🧪 Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_scoring.py -v

# Run with coverage
python -m pytest tests/ --cov=tutor --cov-report=html
```

(Tests will be in `tests/` folder once you add them)

---

## 📊 Key Commands for Hackathon

### **Baseline Build (First 90 min)**

```bash
# 1. Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Test curriculum loader
python -c "from tutor import CurriculumLoader; c = CurriculumLoader(); print(len(c.items))"

# 3. Test knowledge tracing
python -c "from tutor import BayesianKnowledgeTracing as BKT; kt = BKT('counting'); kt.update(True); print(f'P(learned) = {kt.p_learned:.3f}')"

# 4. Run demo
python demo.py
```

### **Add Your Curriculum**

```bash
# Edit tutor/data/curriculum.json
# Add your 60+ items following the schema
code tutor/data/curriculum.json
```

### **Generate Parent Report**

```python
# TODO: Implement in your code
from tutor import LocalProgressStore
store = LocalProgressStore()
stats = store.get_stats('learner_001')
print(stats)
```

### **Evaluate Knowledge Tracing**

```python
# In a Jupyter notebook (notebooks/kt_eval.ipynb)
from tutor import BayesianKnowledgeTracing
import json

# Simulate responses
kt = BayesianKnowledgeTracing('counting')
responses = [True, True, False, True, True]
for correct in responses:
    kt.update(correct)
    print(f"P(learned) = {kt.p_learned:.3f}")

# Compute AUC (pseudocode)
# TODO: Implement AUC calculation
```

---

## 🎯 Hackathon Checklist

Before submitting, complete these:

- [ ] Extend curriculum to 60+ items in `tutor/data/curriculum.json`
- [ ] Implement Task 1: Full inference pipeline (ASR → TTS feedback)
- [ ] Implement Task 2: Knowledge tracing AUC evaluation in `notebooks/kt_eval.ipynb`
- [ ] Implement Task 4: Language detection (already in `ChildASRAdapter`)
- [ ] Implement Task 5: Visual grounding (count objects in images)
- [ ] Implement Task 6: Differential privacy in `LocalProgressStore`
- [ ] Implement `generate_parent_report.py` (from curriculum schema)
- [ ] Document `process_log.md` with LLM usage
- [ ] Sign `SIGNED.md` with honor code
- [ ] Test README on fresh Colab
- [ ] Push to GitHub
- [ ] Create `footprint_report.md` with `du -sh` output

---

## 🚨 Common Issues & Fixes

### **Issue: "ModuleNotFoundError: No module named 'whisper'"**

```bash
pip install openai-whisper
```

### **Issue: "No module named 'gradio'"**

```bash
pip install gradio
```

### **Issue: "curriculum.json not found"**

Make sure you're running from the project root:

```bash
cd math-tutor-ktt
python demo.py  # ✓ Correct
```

NOT:

```bash
cd tutor
python ../demo.py  # ✗ Wrong working directory
```

### **Issue: Whisper model downloads slowly**

Whisper Tiny is 39 MB (fast). If it's slow:

```python
# In tutor/core.py, set:
self.model = whisper.load_model("tiny")  # Default: good
# self.model = whisper.load_model("base")  # Slower (74 MB)
```

---

## 📚 Documentation Files

This project includes 6 comprehensive guides (in outputs/):

1. **REFERENCE_CARD.md** — One-page cheat sheet ⭐ START HERE
2. **QUICK_START_CHECKLIST.md** — Minute-by-minute timeline
3. **DETAILED_TASK_BREAKDOWN.md** — Each task explained
4. **AIMS_KTT_ExecutionGuide.md** — Full reference manual
5. **CODE_SKELETON.py** — Extended code examples
6. **MASTER_INDEX.md** — Navigation guide

Read these in VS Code side-by-side with the code.

---

## 🔗 Useful Links

- **OpenAI Whisper:** https://github.com/openai/whisper
- **Piper TTS:** https://github.com/rhasspy/piper
- **Gradio:** https://gradio.app/
- **Anthropic Claude (for help):** https://claude.ai/

---

## 📝 Before You Submit

### **Sign the Honor Code**

Edit `SIGNED.md`:

```markdown
Your Name
2026-04-24

I will declare every LLM or assistant tool I use in my process_log.md.
I will not have another human do my work.
I will defend my own code in Live Defense.
```

### **Log LLM Usage**

Update `process_log.md`:

```markdown
# Process Log

## LLM Usage
- Tool: Claude (for code generation)
- Date: 2026-04-24
- Sample prompts:
  1. "Generate 10 counting problems in AIMS curriculum format"
  2. "Implement Bayesian Knowledge Tracing update formula"
  3. "Create Gradio interface for ASR input"

## Hardest Decision
I chose to use BKT over DKT because BKT is simpler to implement in 4 hours and still provides good prediction accuracy.
```

### **Test on Colab**

```bash
# Clone to Colab
!git clone https://github.com/YOUR_USERNAME/math-tutor-ktt.git
!cd math-tutor-ktt && pip install -r requirements.txt
!python demo.py
```

Verify it runs in < 2 commands.

---

## ✅ You're Ready!

You have:
- ✅ Working project structure
- ✅ All core components
- ✅ Sample curriculum
- ✅ Gradio demo
- ✅ Full documentation

Next steps:

1. **Read:** REFERENCE_CARD.md (5 min)
2. **Code:** Extend curriculum to 60+ items
3. **Build:** Follow QUICK_START_CHECKLIST.md (0:30–3:15)
4. **Document:** Update process_log.md + SIGNED.md
5. **Test:** Verify README works on Colab
6. **Submit:** Push to GitHub

**You've got this. Good luck!** 🚀

---

**Generated for AIMS KTT Hackathon 2026 · Challenge S2.T3.1**
