# VS Code Setup Guide for AIMS KTT Hackathon

## 🚀 Opening in VS Code (3 Ways)

### **Method 1: From Command Line** (Fastest)

```bash
# From any terminal
code /path/to/math-tutor-ktt
```

### **Method 2: Using VS Code File Menu**

1. Open VS Code
2. Click **File** → **Open Folder...**
3. Select `math-tutor-ktt` folder
4. Click **Open**

### **Method 3: From Project Folder**

```bash
cd math-tutor-ktt
code .
```

---

## 🔧 Initial Setup (First Time)

Once the folder is open in VS Code:

### **Step 1: Open VS Code Terminal**

```
Ctrl + ` (backtick)  # or Cmd + ` on Mac
```

Or: **Terminal** → **New Terminal**

### **Step 2: Create Virtual Environment**

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat
```

### **Step 3: Select Python Interpreter**

In VS Code:
1. Press `Ctrl + Shift + P` (Cmd + Shift + P on Mac)
2. Type: `Python: Select Interpreter`
3. Choose: `./venv/bin/python` (or equivalent)

### **Step 4: Install Dependencies**

```bash
pip install -r requirements.txt
```

This installs:
- numpy, scipy
- openai-whisper
- piper-tts
- torch, transformers
- gradio
- (and dev tools)

---

## 📁 Project Structure in VS Code

Your VS Code explorer should look like:

```
📁 math-tutor-ktt (root)
├── 📁 tutor/
│   ├── __init__.py
│   ├── core.py              👈 Main code
│   └── 📁 data/
│       ├── curriculum.json  👈 Edit this
│       └── progress.db      (created on first run)
├── 📁 notebooks/
│   └── (for your jupyter notebooks)
├── 📁 tests/
│   └── (add tests here)
├── demo.py                  👈 Run this
├── README.md                👈 Read this first
├── requirements.txt         👈 Dependencies
├── process_log.md           👈 Update this
├── SIGNED.md                👈 Sign this
├── LICENSE
└── .gitignore
```

---

## ▶️ Running Your Code

### **Method 1: Run demo.py in VS Code**

1. Open `demo.py`
2. Click the **Play button** (▶️) in top right
3. Or press: `Ctrl + F5`
4. Or right-click → **Run File**

### **Method 2: Run from Terminal**

```bash
python demo.py
```

### **Method 3: Run with Debugging**

1. Set a breakpoint by clicking on line number (red dot)
2. Press **F5** to start debugging
3. Use Debug panel to step through code

---

## 🧪 Testing Code

### **Run Individual Code Snippets**

Open VS Code **Interactive** window:

```
Ctrl + Shift + P  →  "Python: Run Selection/Line in Python Terminal"
```

Then paste:

```python
from tutor import CurriculumLoader

curriculum = CurriculumLoader()
item = curriculum.get_initial_item()
print(f"Question: {item['stem_en']}")
```

### **Run Python in Interactive Terminal**

```bash
# In VS Code terminal
python
>>> from tutor import BayesianKnowledgeTracing
>>> kt = BayesianKnowledgeTracing('counting')
>>> kt.update(True)
>>> print(f"P(learned) = {kt.p_learned:.3f}")
P(learned) = 0.111
```

---

## 📝 Editing Files

### **Key Files to Edit**

**1. `tutor/data/curriculum.json`** — Add your 60+ curriculum items

```json
{
  "id": "YOUR_ID",
  "skill": "counting|addition|subtraction|number_sense|word_problem",
  "difficulty": 1-9,
  "age_band": "5-6|6-7|7-8|8-9",
  "stem_en": "Your question in English",
  "stem_fr": "Your question in French",
  "stem_kin": "Your question in Kinyarwanda",
  "answer_int": 3
}
```

**2. `tutor/core.py`** — Add your enhancements

```python
# Add visual grounding
class VisualGroundingModule:
    def count_objects(self, image_path):
        # Your code here
        pass

# Add fine-tuning
def fine_tune_lm(dataset_path):
    # Your code here
    pass
```

**3. `process_log.md`** — Update your progress

- Add timestamps as you work
- Log LLM prompts you used
- Document decisions

**4. `SIGNED.md`** — Sign the honor code

```markdown
Your Full Name
2026-04-24

I will declare every LLM or assistant tool...
```

---

## 🐛 Debugging

### **Add Breakpoints**

Click on line number in `tutor/core.py`:

```python
def update(self, correct: bool):
    # Click here to add red breakpoint dot
    if correct:  # ← Execution stops here
        p_correct = (self.p_learned * (1 - self.p_s)) + ...
```

### **Run Debugger**

Press **F5** or click Debug icon (🐛) in left sidebar.

### **Common Debugging Tasks**

```python
# Print values
print(f"p_learned = {self.p_learned}")

# Check variable type
print(type(curriculum.items))

# Inspect DataFrame or list
import pprint
pprint.pprint(curriculum.items[0])
```

---

## 🔗 Useful VS Code Shortcuts

| Action | Shortcut | Mac |
|--------|----------|-----|
| Open command palette | `Ctrl + Shift + P` | `Cmd + Shift + P` |
| Open file | `Ctrl + P` | `Cmd + P` |
| Toggle terminal | `Ctrl + `` | `Cmd + `` |
| Run file | `Ctrl + F5` | `Cmd + F5` |
| Format code | `Shift + Alt + F` | `Shift + Option + F` |
| Add comment | `Ctrl + /` | `Cmd + /` |
| Go to definition | `F12` | `F12` |
| Rename symbol | `F2` | `F2` |

---

## 📚 Recommended VS Code Extensions

Install these for better experience:

1. **Python** (Microsoft)
   - Syntax highlighting, linting, debugging
   - Install: Search in Extensions, click Install

2. **Pylance** (Microsoft)
   - IntelliSense, type hints
   - Install: Extensions → Pylance → Install

3. **Jupyter** (Microsoft)
   - Run notebooks in VS Code
   - Install: Extensions → Jupyter → Install

4. **Thunder Client** (optional)
   - Test APIs without leaving VS Code
   - Install: Extensions → Thunder Client → Install

---

## 🚨 Troubleshooting

### **Issue: Python not found**

```bash
# Check Python is installed
python --version

# If not installed, download from python.org
```

### **Issue: Virtual environment not activating**

```bash
# Make sure you're in the right folder
cd math-tutor-ktt

# Try activating again
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows
```

### **Issue: "ModuleNotFoundError: No module named 'whisper'"**

```bash
# Make sure venv is activated, then:
pip install openai-whisper
```

### **Issue: Demo runs but can't open in browser**

Look for the URL in terminal output:

```
Running on local URL:  http://127.0.0.1:7860
```

Copy and paste that into your browser.

### **Issue: Code too slow**

- Disable linting: File → Preferences → Settings → Search "lint" → disable
- Use lightweight interpreter: Python: Select Interpreter → Choose latest version

---

## 💾 Saving & Version Control

### **Save File**

- `Ctrl + S` (or `Cmd + S` on Mac)
- Or Enable **Auto Save**: File → Preferences → Settings → "Auto Save" → onFocusChange

### **Initialize Git** (if not already done)

```bash
git init
git add .
git commit -m "Initial setup: Math Tutor project"
```

### **Push to GitHub**

```bash
# (Assuming you created a repo on GitHub)
git remote add origin https://github.com/YOUR_USERNAME/math-tutor-ktt.git
git branch -M main
git push -u origin main
```

---

## ✅ You're Ready!

Once setup is complete:

1. ✅ Project is open in VS Code
2. ✅ Virtual environment is active (check terminal shows `(venv)`)
3. ✅ Dependencies are installed (`pip freeze | grep -E whisper|gradio|torch`)
4. ✅ You can run `python demo.py`
5. ✅ You can edit `tutor/core.py` with IntelliSense

**Next:** Follow QUICK_START_CHECKLIST.md timeline (0:30–3:15)

---

## 🆘 Need Help?

- **VS Code docs:** https://code.visualstudio.com/docs
- **Python docs:** https://docs.python.org/
- **Whisper docs:** https://github.com/openai/whisper
- **Gradio docs:** https://gradio.app/docs

---

**Happy coding! You've got this. 🚀**
