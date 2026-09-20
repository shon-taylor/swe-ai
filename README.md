# QR Toolkit — Initial Scaffolding (Python Flask BE, HTML/JS FE)

This is the initial scaffolding of our SWE class project: a small web app that generates QR codes from text/URLs and decodes QR codes from an uploaded image or webcam feed. Backend is a lightweight Flask API wrapping the `qrcode` and `pyzbar` libraries; frontend is plain HTML/JS split into a generator page and a scanner page, so we could each own a side independently.

All architecture decisions in this scaffolding were made by us (human), based on our own reasoning about scope and split-ability — not AI-suggested. The class's focus is on using AI tools *within* the dev workflow, so the log below tracks where AI was used to generate/modify code, distinct from the decisions about what to build.

--------------------------------------------------------------------------------
AI CODE GENERATION DISCLAIMER & DETAILED LOG
--------------------------------------------------------------------------------

Notice: The code, configuration, and documentation files listed below were generated or modified with AI assistance (tool: _____ — e.g. Claude Code / Copilot / Cursor) under human direction and review. Every AI-assisted change was reviewed and, where needed, corrected before commit.

**Detailed Change Breakdown & AI Code Attribution:**

1. **Infrastructure & Environment Setup**
   - `.gitignore`: Standard Python/Node exclusions (`__pycache__/`, `venv/`, `node_modules/`, etc.)
   - `requirements.txt`: Pinned dependencies (`flask`, `qrcode`, `pyzbar`, `opencv-python` or `Pillow`)
   - `docs/architecture.md`: High-level description of the generator/scanner split and API contract

2. **Backend Development (Flask API)**
   - `backend/app.py`: Route definitions — `POST /api/generate`, `POST /api/decode`
   - `backend/generator.py`: Wraps `qrcode` library, handles size/error-correction params
   - `backend/scanner.py`: Wraps `pyzbar`/OpenCV decode logic, handles image upload parsing
   - `backend/tests/`: Unit tests for generate/decode round-trip

3. **Frontend Development (HTML/JS)**
   - `frontend/index.html` + `app.js`: Generator UI — text input, calls `/api/generate`, renders returned image
   - `frontend/scan.html`: Scanner UI — file upload or webcam capture, calls `/api/decode`, displays decoded text

4. **Governance & Audit Trails**
   - `AGENTS.md`: Rules for how we use AI tools on this project (attribution, review expectations)
   - `docs/usedPrompts.md`: Log of prompts used, timestamped, with reviewer initials

## Setup
1. `cd backend && pip install -r requirements.txt`
2. `python app.py` (defaults to `localhost:5000`)
3. Open `frontend/index.html` in a browser (or serve via `python -m http.server` from `frontend/`)

## Team split
- **Partner A**: Backend — generator route + logic, tests
- **Partner B**: Backend — scanner route + logic, frontend for both pages
  
*Still working on setting up team.
