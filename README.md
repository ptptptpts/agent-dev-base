# 📱 AI Development Base

A template for "Vibe Coding" where you can build products simply by creating GitHub Issues. All development processes are handled in the cloud (GitHub Actions), while you provide the vision and instructions.

## 🚀 Quick Start (3 Steps)

1. **Duplicate/Template**: Duplicate this repository to your new project.

2. **Configure**: Open `project-config/project-goal.md` and define your project's goals, tech stack, and core requirements.

3. **Bootstrap**: Go to the GitHub Issues tab, click **"New Issue"**, and select the **"01-project-bootstrap"** template to trigger the initial setup.

## 🛠 Structure & Roles

* **`.github/`**: Contains GitHub Actions workflows for the Cloud Agent and Issue templates.

* **`project-config/`**: **User Zone**. Manage project-specific goals (`project-goal.md`) and custom build/test requirements (`ci-cd-requirements.md`).

* **`ai-context/`**: **AI Knowledge Zone**. Contains the AI system prompt, general software engineering guidelines, and language-specific best practices.

* **`.agent-config.yml`**: Configures the Cloud Agent (e.g., Aider), specifying the LLM model and files to auto-load.

* **`.aiderignore`**: Protects core settings and sensitive files from being modified by the AI.

## 🤖 Workflow

1. **Create Issue**: User triggers a task via a mobile GitHub Issue.

2. **Agent Activation**: GitHub Actions triggers the AI Agent to write code.

3. **PR Generation**: The AI automatically creates a Pull Request once the task is complete.

4. **Review & Merge**: Verify the changes through the AI reviewer and merge. Vercel handles the deployment automatically.

Created with ❤️ for Mobile Developers.
