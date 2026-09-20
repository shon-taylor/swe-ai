# AGENTS.md — AI Usage Rules for This Project

These are our team's ground rules for using AI coding tools on this repo, for the SWE class's AI-in-the-workflow requirement.

## Ground rules
1. **Architecture decisions are human-made.** AI can suggest structure, but we decide what goes where before asking it to generate code.
2. **Every AI-generated change gets reviewed before commit.** No pasting in code neither of us has read.
3. **Log every meaningful AI-assisted change** in `docs/usedPrompts.md` — what was asked, what tool, and a one-line note on what we kept/changed.
4. **Commit messages flag AI involvement** where relevant, e.g. `[AI-assisted] Add QR decode route` vs a plain commit for hand-written changes.
5. **Tests are written or reviewed by a human**, even if AI drafts the first pass — the assertions have to make sense to us, not just pass.

## Tools used
- Tool: _____ (e.g. Claude Code, GitHub Copilot, Cursor)
- Plan/access: _____

## Review responsibility
- Backend AI-assisted changes reviewed by: _____
- Frontend AI-assisted changes reviewed by: _____
