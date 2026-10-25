# AI Prompt Audit Log

Outcome key: **Kept** = used as given, **Modified** = changed after review or testing, **Guidance** = advice only, no code or text kept.

| Date | User | File(s) affected | Prompt (summary) | Outcome | Notes |
|------|------|------------------|------------------|---------|-------|
| Oct 4 | ST | README.md, AGENTS.md, docs/usedPrompts.md | Asked for a GitHub repo structure and starter docs modeled on an example (scaffold description, AI disclaimer, governance rules, prompt log) | Modified | AI drafted the templates with blanks. Tool name, reviewer names, and team split had to be filled in by us. |
| Oct 4 | ST | none | Asked how to create the folder structure and push to GitHub, then confirmed the clone, add, push-to-main flow | Guidance | Git workflow steps only. |
| Oct 4 | JM | generator.py, app.py, tests/test_generator.py, requirements.txt | Build a basic QR generation feature with unit and integration tests for the PR | Modified | AI wrote the code and ran it in a sandbox: 18 tests passed, 99% coverage, confirmed on our machine. AI left debug=True in app.py, which review later flagged as High severity (see Oct 18-25 entry). |
| Oct 4  | ST | none | Hit a Visual Studio file-lock error (.vs folder) when committing and pushing | Guidance | Fix was adding .vs/ to .gitignore and untracking it. No code kept. |
| Oct 4  | ST | none | Hit "pytest is not recognized" in PowerShell | Guidance | Fix was running python -m pytest. Coverage then matched the AI's result. |
| Oct 4  | ST | none | Asked what the generation code does, and how QR generation and decoding work, including what the error-correction levels mean | Guidance | Learning only. Used to understand the code before the PR review. |
| Oct 18 | ST | scanner.py, app.py, frontend/index.html, tests/test_scanner.py, requirements.txt | Asked for help setting up an MVP to demo | Kept | AI added the decode endpoint, the demo page, and tests. Sandbox result: 27 tests passed, 99% coverage. Chose OpenCV over pyzbar to avoid Windows native-library setup. |
| Oct 18  | ST | generator.py | Hit ModuleNotFoundError for generator because the file was missing from the repo | Kept | Only the changed files had been re-sent. AI supplied generator.py again, unchanged. |
| Oct 18-25  | ST | app.py, tests/app.py (deleted) | Reviewer feedback: Flask debug mode (High) and a duplicate app.py in tests | Modified | AI-generated code caused the finding. Fixed so debug is off by default and only enabled with FLASK_DEBUG=1; server bound to 127.0.0.1. Duplicate file deleted by us. 27 tests still passed. |
| Oct 25 | JM | feature plan doc (Claude Doc) | Asked for a prioritized list of remaining features with a provisional schedule | Modified | AI drafted 7 features and a weekly schedule. We corrected the term end to Dec 8 and AI moved the feature freeze to Dec 2. Owners set to ST and JM by us. |
| Oct 25 | ST | requirements.txt | Asked to add version numbers, then to list only libraries actually used | Modified | AI pinned exact versions, then removed Werkzeug and Pillow (not imported directly). Tested in a clean virtual environment: 27 passed, 99%. |
| Oct 25 | ST | app.py | Asked whether debug was actually turned off | Guidance | AI checked the file: debug is controlled by FLASK_DEBUG and off by default. Offered an explicit debug=False option.
