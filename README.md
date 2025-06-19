# 🧠 Prompt Debugger Bot

A GPT-powered prompt debugging assistant that identifies flaws in natural language prompts and suggests optimized alternatives — built to showcase real-world prompt engineering skills.

---

## ✨ What It Does

This tool takes in:
- A **broken or unclear prompt**
- The **unsatisfactory output** it generated

It then uses GPT-4o to:
1. **Analyze what went wrong**
2. **Explain why the output failed**
3. **Suggest a revised prompt**
4. **Provide rationale** for the fix

---

## 🧪 Example

### ❌ Original Prompt
> Write a professional but quirky email that’s super casual but formal at the same time, and not too long or too short, with lots of personality but also concise.

### 🛑 Bad Output
A confused, overly balanced email trying to be everything at once — neither clearly casual nor formal.

### ✅ Fixed Prompt
> Write a professional email with a touch of quirkiness. The email should be concise, around 150–200 words, and aim to establish a friendly tone. It's intended for a potential collaboration proposal.

📎 [Full Debug Report](examples/casual_vs_formal_email.md)

---

## 🚀 How to Use

### 🔧 Requirements

- Python 3.10+
- OpenAI SDK (`openai>=1.24`)
- `python-dotenv`

Install dependencies:

```bash
pip install -r requirements.txt


Create a .env file with your OpenAI key:

ini
Copy
Edit
OPENAI_API_KEY=sk-...
▶️ Run the Bot
Save your test prompt and output in text files like this:

lua
Copy
Edit
prompt.txt
output.txt
Then run:

bash
Copy
Edit
python main.py
It will ask for the file paths and save the result to the examples/ folder.

🎯 Why This Exists
Prompt engineering is a real skill — and this tool demonstrates:

How to diagnose prompt failures

How to improve LLM interaction quality

How to wrap prompt logic in useful tooling

Built as a showcase project for applied LLM roles.

📁 Project Structure
bash
Copy
Edit
.
├── main.py                  # Core logic
├── .env                    # (ignored) your API key
├── prompt.txt              # Sample prompt input
├── output.txt              # Sample model output
├── examples/
│   └── casual_vs_formal_email.md  # Full example
├── .gitignore
├── requirements.txt
└── README.md
🧠 Future Ideas
Streamlit UI

Batch debugging mode

Option to choose between models

Prompt similarity scoring

