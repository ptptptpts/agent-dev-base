# 📱 Mobile AI Development Base

This repository is a foundation for "Vibe Coding"—a seamless mobile development experience where you build products by simply creating GitHub Issues. All heavy lifting is handled by AI Agents in the cloud.

---

## 🚀 Step-by-Step Setup Guide

### Step 1: Duplicate the Repository
1. Click the **"Use this template"** button or **Duplicate** this repository to your own account.
2. Make sure the repository is **Public** if you want to use Vercel's free tier easily.

### Step 2: Configure GitHub Secrets (Essential)
To allow the AI Agent to work, you must provide an API Key.
1. Go to your repository's **Settings** tab.
2. On the left sidebar, click **Secrets and variables** > **Actions**.
3. Click the **New repository secret** button.
4. Set the **Name** to: `GEMINI_API_KEY`
5. Set the **Value** to your API key from [Google AI Studio](https://aistudio.google.com/).
6. Click **Add secret**.

### Step 3: Connect to Vercel (Highly Recommended)
Enable automatic preview deployments for every PR the AI creates.
1. Go to [Vercel.com](https://vercel.com) and log in.
2. Click **Add New** > **Project**.
3. Import this repository.
4. (Optional) Configure Environment Variables if your app requires them.
5. Click **Deploy**. Vercel will now automatically provide a preview URL for every Pull Request.

### Step 4: Define Your Project Goal
1. Open `project-config/project-goal.md`.
2. Edit the file to describe your app's mission, tech stack, and requirements.
   - *Tip: The AI will read this file every time it starts a task.*

### Step 5: Trigger the AI Bootstrap
1. Go to the **Issues** tab.
2. Click **New Issue** and choose the **"01-project-bootstrap"** template.
3. Click **Submit new issue**.
4. Wait for the **Issue-to-PR AI Agent** to trigger. It will automatically:
   - Read your goals.
   - Initialize the folder structure.
   - Create a Pull Request (PR).

---

## 📱 Mobile Workflow Tips
- **GitHub Mobile App**: Install the official GitHub app to create issues and review PRs on the go.
- **Vercel Previews**: Every PR created by the AI will have a Vercel preview link in the comments. Tap it to test the app immediately on your mobile browser.
- **Notifications**: Enable push notifications for PRs to know exactly when the AI has finished coding.

---

## 🛠 Project Structure
- `.github/`: CI/CD workflows and automation scripts.
- `project-config/`: Your project's "Source of Truth" (Goals & Build rules).
- `ai-context/`: Permanent guidelines for the AI to ensure high-quality code.

## ❓ Troubleshooting
- **Agent not running?**: Check the **Actions** tab to see if the workflow failed. Ensure `GEMINI_API_KEY` is correct.
- **Permission Error?**: Go to `Settings > Actions > General` and ensure "Workflow permissions" is set to **"Read and write permissions"**.

---
Happy Vibe Coding! 🚀
