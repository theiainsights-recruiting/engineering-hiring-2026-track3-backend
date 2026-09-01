# Task: classification lookup endpoint

Starter repo: a FastAPI app skeleton (`main.py`), a small dataset
(`data.json`) and an entitlements table (`entitlements.py`).

`data.json` maps companies to their classifications across the five TIIC
levels (sector, industry, sub_industry, major_theme, micro_theme).
`entitlements.py` maps API keys to the levels each customer may see.

**Implement:**

```
GET /companies/{company_id}/classifications?level=<optional>
```

- Authenticate via the `X-API-Key` header.
- Return the company's classifications, restricted to the levels the caller
  is entitled to. `level` filters to one level (if entitled).
- Choose appropriate status codes for: missing/unknown key, unknown company,
  a level the caller isn't entitled to. Be ready to justify each choice.

Run it with `uvicorn main:app --reload` and hit it however you like
(curl, httpie, the /docs page).

Notes:

- Use whatever tools you'd normally use, including AI assistants.
- Finishing is not the goal.
