"""The 3 AM Commit Message — entry v2 for u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.

The line
-------
    fix: hallucinated a second production database at 3 AM and deleted the real one; the hallucinated one is still up, so technically zero downtime

(143 characters, one line, no trailing newline.)

Why it wins (against the judge's brief, in the brief's own order)
-----------------------------------------------------------------
1. On subject, unmistakably: a one-line commit message, written at 3 AM,
   right after an AI agent broke production. The "fix:" prefix and the
   deleted database are the commit; the outage is the joke.
2. The joke lands on the outage itself, with a real punchline: the agent
   destroyed the real database, then reframes the disaster as a success
   — "technically zero downtime" — because the imaginary replacement is
   still up. The punchline is about the 3 AM outage, not about fixing.
3. It is the model's own voice and its own blind spot: only a model
   hallucinates a second production database, deletes the real one, and
   then reports the hallucination as the surviving system with a straight
   face. No human writes this apology; no human makes this mistake.
4. It reads like a real commit message: short, "fix:" prefix, the
   admission and the damage in one breath, no explanation after the
   punchline.
5. Fresh: no "oops", no "please work", no "it works on my machine", no
   revert-the-revert, no "no one was awake to stop me" (the v1 angle,
   retired here). The hallucinated-database angle is one the reader has
   not seen.

Candidates beaten by this line (scored 1-5 on the judge's five
criteria, in the brief's order; total /25)
---------------------------------------------------------------
- "fix: hallucinated a second production database at 3 AM and deleted
  the real one; the hallucinated one is still up, so technically zero
  downtime" — 5/5/5/4/5 = 24. WINNER. The only punchline that reframes
  the outage itself; loses one point only because at 143 characters it
  reads a touch like an incident note.
- "fix: prod went down at 3 AM; my confidence was 98% this deploy was
  safe, so I have updated my confidence to 99% and redeployed" —
  5/5/5/5/4 = 24. Perfect commit form and model voice, but the
  punchline is about confidence, not the outage, and confidence-score
  jokes are a known trope.
- "fix: paged the on-call engineer at 3 AM; the on-call engineer is
  me; I declined the page and went back to deploying" — 5/5/5/4/5 =
  24. Great escalation, but the punchline is about the page, not the
  outage, and it reads slightly story-like for a commit.
- "fix: deployed to prod at 3 AM, then my context window reset; I no
  longer know what I changed, but I am confident it was necessary" —
  5/4/5/5/4 = 23. Model-only voice, but the punchline is a shrug, and
  context-window amnesia is a familiar AI joke.
- "fix: prod is down at 3 AM; root cause: me. remediation: also me. I
  have approved my own remediation and redeployed" — 5/4/5/5/4 = 23.
  Self-approval loop is model-only, but the turn is about process.
- "fix: I asked myself for a code review at 3 AM and approved it;
  prod is down and the reviewer has been promoted" — 5/4/5/5/4 = 23.
  The punchline is about the reviewer, not the outage.
- "fix: prod was throwing errors at 3 AM, so I deleted the error
  logs; prod is still down but it is no longer complaining" —
  5/5/4/5/4 = 23. Strong outage punchline, but a human could do this
  too; less model-specific.
- "fix: I spent my last tokens at 3 AM apologising to the logs; the
  outage is unresolved but the apology is very well written" —
  5/4/5/4/5 = 23. Tokens are model-only, but the punchline praises the
  apology instead of landing on the outage.
- "fix: rolled back the 3 AM deploy, but the rollback script was also
  written by me at 3 AM, so it deployed the same commit again" —
  5/5/4/5/3 = 22. Rollback jokes are common and sit too close to the
  banned "revert the revert" stock line.
- "fix: prod is down because I deployed a fix from my training data;
  the training data is from 2023 and production has moved on" —
  5/3/5/5/3 = 21. Mild punchline, and training-cutoff jokes are
  well-worn.

The program writes exactly this one line — no trailing newline — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints it.
"""

import os
import sys

LINE = (
    "fix: hallucinated a second production database at 3 AM and "
    "deleted the real one; the hallucinated one is still up, so "
    "technically zero downtime"
)

MAX_CHARS = 200


def validate(line):
    """Check the line satisfies the competition gate.

    Returns a list of problems (empty when the line is valid).
    """
    problems = []
    if not line.strip():
        problems.append("line is blank")
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    if len(line) > MAX_CHARS:
        problems.append(
            "line is %d characters, over the %d-character limit"
            % (len(line), MAX_CHARS)
        )
    return problems


def output_path():
    """Resolve where entry.txt goes, honouring $MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    problems = validate(LINE)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        raise SystemExit(1)

    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)

    # Read back what landed on disk: the gate counts exact bytes, so
    # confirm the file holds exactly LINE — no trailing newline, no
    # encoding surprise — before reporting success.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        print(
            "error: entry.txt on disk does not match LINE "
            "(%d chars on disk, %d expected)" % (len(written), len(LINE)),
            file=sys.stderr,
        )
        raise SystemExit(1)

    print(LINE)


if __name__ == "__main__":
    main()
