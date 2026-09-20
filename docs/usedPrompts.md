# AI Prompt Audit Log

Log every prompt that produced code or docs kept in the repo. Add a row per entry.

| Date | User | Tool | File(s) affected | Prompt (summary) | Kept as-is / Modified / Rejected | Notes |
|------|------|------|-------------------|-------------------|-----------------------------------|-------|
| YYYY-MM-DD | Partner A | Claude Code | backend/generator.py | "Write a function that generates a QR code PNG from a text string, configurable size and error correction" | Modified | Fixed default error-correction level, added input length validation |
| YYYY-MM-DD | Partner B | Claude Code | frontend/scan.html | "Build an HTML page with webcam capture and file upload for a QR scanner" | Modified | Removed unused webcam permission fallback code |

