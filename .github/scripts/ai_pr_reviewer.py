from google import genai
import os
import yaml

def read_file(path):
    if not os.path.exists(path):
        return ""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def get_config_model():
    \"\"\"Extract model name from .agent-config.yml\"\"\"
    config_content = read_file('.agent-config.yml')
    if not config_content:
        return "gemini-1.5-pro"
    
    try:
        config = yaml.safe_load(config_content)
        model_name = config.get('model', 'gemini-3-flash-preview')
        if '/' in model_name:
            return model_name.split('/')[-1]
        return model_name
    except Exception:
        return "gemini-3-flash-preview"

def main():
    api_key = os.environ.get('GEMINI_API_KEY')
    model_id = get_config_model()
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found.")
        return

    client = genai.Client(api_key=api_key)

    diff_content = read_file('changes.diff')
    if not diff_content.strip():
        print("No changes found in diff.")
        return

    prompt_template = read_file('ai-context/pr-review-prompt.md')
    system_rules = read_file('ai-context/ai-system-prompt.md')
    
    final_prompt = f'''
{prompt_template}

[AI_SYSTEM_RULES]
{system_rules}

[DIFF_CONTENT]
{diff_content}
'''

    try:
        response = client.models.generate_content(
            model=model_id,
            contents=final_prompt
        )
        
        with open('review_comment.md', 'w', encoding='utf-8') as f:
            f.write('## 🧐 Gemini AI Code Review\\n\\n')
            f.write(response.text)
            
    except Exception as e:
        print(f"Error during AI generation: {e}")

if __name__ == "__main__":
    main()
