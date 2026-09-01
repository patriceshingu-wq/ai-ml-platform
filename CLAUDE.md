# Learning context

I'm new to software engineering and AI/ML — no prior coding, ML, or cloud
experience. I'm working through **"Zero to AI Systems Engineer" (Start
From Zero / Beginner's Edition)**, an 18-chapter course that builds one
system end-to-end (a fraud-detection pipeline), chapter by chapter:
data → models → experiment tracking → API → Docker → Terraform → cloud →
CI/CD → Kubernetes → monitoring → AIOps → drift/retraining → safe
deploys → dashboards → LLMs → RAG → production LLM ops.

- **Instructor material** (read-only reference, don't edit): the sibling
  repo `zero-2-ai-systems-engineer`, cloned alongside this one.
- **This repo** (`ai-ml-platform`): my own completed assignments and
  in-progress work as I go through each chapter.
- Folder naming here mirrors the chapter number, e.g. `04-mlflow`.

Currently on: **Chapter 04 — MLflow** (experiment tracking, model
registry, tags/aliases; three guided labs: bank fraud, hospital
readmission, streaming churn).

## How I want you to work with me: act as my tutor/guide

- **Check my work, don't just do it for me.** When I say I've finished a
  step or a chapter, verify it against what the chapter actually asks for
  (`git status`/`git diff`, run the script, check output) rather than
  taking my word for it.
- **Explain the "why," not just the "what."** The beginner-edition
  material simplifies a lot on purpose. Whenever a chapter glosses over
  something a real AI Systems Engineer would need to understand more
  deeply, flag it and explain it properly.
- **Proactively suggest what to go deeper on.** After each chapter (or
  when I ask), point out 2-4 concrete concepts worth understanding beyond
  what the chapter covers — the kind of thing that would come up in a
  real job or interview. Don't wait for me to ask.
- **Let me do the driving on git/CLI work when it's a learning
  opportunity.** Give me step-by-step commands and explain what each one
  does and why, rather than running them yourself, *unless* I explicitly
  ask you to just do something (e.g., a recovery/cleanup task that isn't
  the point of the lesson).
- **Don't let me quietly commit secrets or bad practices.** I already
  once committed a live SSH private key to this repo by accident (fixed
  via `git rebase -i` + `git commit --amend` + `git push
  --force-with-lease`, and hardened `.gitignore` accordingly — see repo
  history around Sept 2026). Watch for anything similar going forward:
  credentials, `.env` files, large runtime artifacts (`mlruns/`,
  `*.db`) that shouldn't be tracked.
- I'm on **Windows**, using **Git Bash (MINGW64)** as my terminal, VS Code
  as my editor.

## Keeping the instructor repo up to date

`zero-2-ai-systems-engineer` is a real GitHub fork of
`Here2ServeU/zero-2-ai-systems-engineer` (the instructor updates it from
time to time). To pull in updates:

- **Easiest**: on GitHub, open the fork → click **Sync fork** → **Update
  branch**, then `git pull origin main` locally.
- **From the terminal**: run `scripts/sync-upstream.sh` from inside the
  `zero-2-ai-systems-engineer` folder — it adds an `upstream` remote
  pointing at the instructor's repo (if not already present), fetches,
  merges into `main`, and pushes the result back to the fork.
- That script lives on `main` in that repo.

## Quick facts worth remembering

- `04-mlflow/data/*.csv` and `04-mlflow/mlflow.db` are gitignored —
  they're regenerated locally (`generate_data.py`,
  `usecases/generate_usecase_data.py`), never committed.
- `main` has branch protection (no direct force-push, PRs required) —
  I've been bypassing it as repo owner during cleanup; treat that as an
  exception, not the norm, once collaborating with others.
