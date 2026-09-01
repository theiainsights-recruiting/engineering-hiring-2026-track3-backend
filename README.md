# Theia Insights — technical interview (backend / API)

Welcome. This repo is used during the 60-minute technical interview. You'll
have received this link on the call — nothing needs doing in advance.

## Get set up (about 2 minutes)

You need Python 3.10+. In your usual environment, or a fresh one:

```
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cd exercise
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs — if you see the API docs page,
you're ready.

## The format

- **Part A (~25 minutes):** your interviewer will send you a pull request
  link in this repo. Review it as you would a colleague's PR and talk your
  interviewer through it. It's a reading exercise — the `api/` folder is the
  service the PR belongs to; you don't need to run it.
- **Part B (~25 minutes):** open `exercise/TASK.md` and take it from there.

Worth knowing:

- Use whatever tools you'd normally use, including AI assistants — we're
  interested in how you work.
- Think out loud, and say your assumptions as you make them.
- Finishing is not the goal.
