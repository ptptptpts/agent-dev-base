from google import genai
import os
import yaml

def read_file(path):
    if not os.path.exists(path): return ""
    with open(path, 'r', encoding='utf-8') as f: return f.read()

def get_config_model():
    config = yaml.safe_load(read_file('.agent-config.yml') or "{}")
    model_name = config.get('model', 'gemini-3-flash-preview')
    return model_name.split('/')[-1] if '/' in model_name else model_name

def main():
    api_key = os.environ.get('GEMINI_API_KEY')
    model_id = get_config_model()
    client = genai.Client(api_key=api_key)
    diff = read_file('changes.diff')
    if not diff.strip(): return

    goal = read_file('project-config/project-goal.md').lower()
    prompt = read_file('ai-context/pr-review-prompt.md')
    rules = read_file('ai-context/ai-system-prompt.md')
    eng = read_file('ai-context/00-software-engineering.md')
    
    stack_context = ""
    context_dir = 'ai-context'
    if os.path.exists(context_dir):
        for filename in os.listdir(context_dir):
            if filename.startswith('stack-') and filename.endswith('.md'):
                stack_key = filename[6:-3].lower()
                if stack_key in goal:
                    stack_context += f"\\n[{stack_key.upper()} GUIDELINES]\\n" + read_file(os.path.join(context_dir, filename))

    final = f"{prompt}\\n\\n[RULES]\\n{rules}\\n{eng}{stack_context}\\n\\n[DIFF]\\n{diff}"
    try:
        response = client.models.generate_content(model=model_id, contents=final)
        with open('review_comment.md', 'w', encoding='utf-8') as f:
            f.write('## 🧐 Gemini AI Code Review\\n\\n' + response.text)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": main()
