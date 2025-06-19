# main.py

import os
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

SYSTEM_MESSAGE = """You are a prompt engineering assistant.
Your job is to help fix prompts that result in poor or confusing outputs from a language model.

For every example, analyze:
1. What went wrong in the original prompt
2. What kind of response it caused
3. How to fix the prompt
4. Suggest a revised prompt and explain why it's better

Be concise, practical, and helpful."""

def debug_prompt(bad_prompt, bad_output, model="gpt-4o"):
    messages = [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": f"""The following prompt was used:
---
{bad_prompt}
---

And the model gave this output:
---
{bad_output}
---

Please diagnose the issue, suggest an improved prompt, and explain the fix."""}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content

def main():
    print("🔍 Prompt Debugging Assistant (file input mode)")

    prompt_path = input("Enter path to the original prompt file: ").strip()
    output_path = input("Enter path to the bad output file: ").strip()

    with open(prompt_path, "r", encoding="utf-8") as f:
        bad_prompt = f.read()

    with open(output_path, "r", encoding="utf-8") as f:
        bad_output = f.read()

    result = debug_prompt(bad_prompt, bad_output)

    print("\n🧠 Debugging Analysis:\n")
    print(result)

    # Save result to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"examples/debug_{timestamp}.md"
    os.makedirs("examples", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Prompt Debugging Result\n\n")
        f.write(f"**Original Prompt:**\n```\n{bad_prompt}\n```\n\n")
        f.write(f"**Bad Output:**\n```\n{bad_output}\n```\n\n")
        f.write("**Analysis & Fix:**\n")
        f.write(result)

    print(f"\n📁 Saved result to: {filename}")


if __name__ == "__main__":
    main()
