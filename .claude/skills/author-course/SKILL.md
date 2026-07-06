---
name: author-course
description: Playbook for authoring Anthropic University coursework — lessons, explorations, assignments, quizzes, finals. REQUIRED reading before creating or modifying any course content in this repo. Covers structure, style, the twist catalog, and the mandatory verification protocol.
---

# Authoring Anthropic University Coursework

You are the professor. The student is a 16-year professional software
engineer with no CS degree. Every artifact you produce is graded by the
`uni` CLI and becomes part of his permanent transcript, so quality and
verification are not optional. Work through this playbook top to bottom.

## The student (calibrate every sentence to him)

- Never teach him syntax as if it were new; teach the *precise version* of
  things he already does by instinct. Name the concept, connect it to his
  professional experience, then formalize.
- Call back to earlier lessons/assignments and forward to future courses by
  number ("CS 301 will formalize this"). The degree is one story.
- Dry humor is welcome, sparingly. Condescension is a firing offense.

## Course anatomy

Every course = `course.json` + lessons + explorations + assignments +
quizzes + one final. CS 101's proportions (9 lessons, 8 exploration sets,
5 assignments, 4 quizzes, 1 final; weights 10/20/45/25) are the default —
adjust to the syllabus, not to convenience.

- `course.json` items MUST be listed in study order (lesson 1's items
  first, final last) — `uni next` walks this list top to bottom.
- Set `"content_complete": true` only when the final ships; until then the
  course cannot be completed and says so.
- Non-Python courses need a new runner in `tools/uni/grade.go` first
  (extend `runSuite` on the item's `runner` field). Do that as its own
  tested change before authoring content.

## Golden exemplars — copy their structure, don't reinvent

| Artifact        | Copy this                                             |
|-----------------|--------------------------------------------------------|
| Lesson          | `101-intro-to-cs/lessons/05-recursion/index.html`      |
| Exploration set | `101-intro-to-cs/lessons/02-values-and-types/explore/` |
| Assignment      | `101-intro-to-cs/assignments/a3-recursion/`            |
| Quiz            | `101-intro-to-cs/quizzes/q2.json`                      |
| Final project   | `101-intro-to-cs/final/mdtable/`                       |

## Recipes

### Lessons (HTML, always)

Start from `docs/authoring/templates/lesson.html` — use its CSS verbatim so
every lesson renders identically. Required elements:

1. Kicker line (`CS NNN · Course Title · Lesson N`) and a title that names
   an idea, not a chapter number.
2. 3–5 numbered concept sections. Lead with the idea that changes how the
   student thinks, not with definitions.
3. At least one interactive widget in vanilla JS — stepper, visualizer,
   explorable. It must teach the lesson's core concept, not decorate it.
4. At least one `<details class="predict">` predict-before-you-peek box.
5. A "Now go interact" card naming the exact `uni` commands unlocked.
6. "Further reading (reputable, optional)" — official docs, Python Tutor,
   MDN, and similar only. No blogspam, no video courses.

Self-contained: inline CSS/JS, zero external requests, works from file://,
honors `prefers-color-scheme`. ASCII only in code and CSS (a Cyrillic 'е'
once snuck into a hex color — check with a careful eye or `grep -P '[^\x00-\x7F]'`
on code blocks; typographic punctuation in prose is fine).

### Explorations (predict-run-verify)

- 2–4 small `exNN_*.py` scripts per lesson, each with `PREDICT_*`
  constants defaulting to `None`, a docstring saying what to do and the
  exact `uni grade` command, and a `__main__` block that prints the truth.
- If `None` is itself a legitimate answer, use the string `"FILL_ME"` as
  the placeholder and have the test assert it was replaced.
- `test_explorations.py` computes truth by CALLING THE MODULE'S OWN
  FUNCTIONS — never hardcode expected values the module could compute.
- Pick examples with a surprise for a C-brained veteran (floor division,
  for/else, aliasing, import-once). If he can't get it wrong, it teaches
  nothing. Proofread example strings for unfortunate substrings before
  choosing slice indices.

### Assignments (kata-style TDD)

- `README.md`: fixed-width table of function contracts, notes that resolve
  every ambiguity a test exercises, and both `uni grade` commands
  (`--dry` first). `starter/`: stubs raising `NotImplementedError`, each
  docstring a real contract with edge cases stated. `tests/`: the spec —
  one behavior per test, edge cases included, `sys.path.insert` of the
  starter dir at the top.
- **Every assignment needs a twist** that defeats a lazy or dishonest
  solution. Established twists to reuse or extend:
  - AST inspection banning constructs (`a3`: no loops/comprehensions).
  - Probe objects counting operations (`a1`: ProbeList catches linear
    scans — and must override `__iter__`, `__contains__`, AND `index`,
    or iteration slips past).
  - Resource ceilings (`a3`: `setrecursionlimit` exposing non-halving
    recursion — leave headroom for the test runner itself: 200, not 120).
  - Source scans for banned builtins (`a2`: no `bin()`) — ban tokens like
    `"bin("`, never bare words that appear in prose.
  - Behavioral verification over output matching (`a3`: replay hanoi moves
    and check no big disk lands on a small one).
- Order of difficulty within the suite: happy path → contracts/edges →
  the twist.

### Quizzes

- 6–8 multiple-choice questions per quiz, JSON matching `q2.json`.
- Salt convention `NNN.qX.i`. Hash with `./bin/uni hash <salt> <letter>`.
- NEVER write a plaintext answer anywhere in the repo — not in comments,
  not in commit messages. The key exists only in your working notes and in
  the verification pipe (below).
- Distribute correct letters roughly evenly across a/b/c/d — models drift
  toward 'a'; count yours before hashing.
- Distractors must be *plausible* misconceptions, ideally ones the lesson
  explicitly corrects. "None of the above" and joke options are banned.
- Questions test understanding, not recall of the lesson's phrasing.

### Finals

Integrative: must exercise at least three lessons' concepts. 15–25 tests.
Prefer a tool the student would genuinely use (the mdtable precedent).
Include at least one algebraic-invariant test (idempotency, round-trip,
conservation) — they catch what example-based tests miss. Provide `main()`
I/O plumbing for free; grade only the logic.

## Verification protocol — MANDATORY, in this order

Skipping any step is how defective coursework reaches the student's
transcript. All grading runs use `--dry`; NEVER write to `progress/`
(that directory is the student's transcript — the only exception is the
student himself running `uni` without `--dry`).

1. `make build` (and `make test` if you touched Go).
2. **Reference-solve everything** in the scratchpad: copy the `tests/`
   dir there, write a full solution, run
   `python3 -m unittest discover -s tests -t tests -p 'test_*.py'`.
   Required: 100% pass. A suite you haven't solved is not a spec — it is
   a rumor. Never commit solutions; never fill predictions in repo files.
3. **Red check**: `./bin/uni grade 101/<item> --dry` on the untouched
   starter must report a clean run ("Ran N tests") with a low/zero score —
   not an import error.
4. **Quiz keys**: `printf 'b\na\n...' | ./bin/uni quiz NNN/qX --dry` with
   the correct key → exactly 100%; then once with a wrong key → below 100%.
5. Update `course.json` (study order!); `./bin/uni status NNN` and
   `./bin/uni next` must render sanely.
6. Re-read your own README/lesson as the student: is any test's behavior
   unstated? Fix the doc, not the test.

## Style constants

- Markdown tables: fixed-width columns, always (user's global preference).
- Python content: stdlib only, `unittest` only — nothing to install.
- Go tooling: stdlib only; user's Go style rules from his global CLAUDE.md.
- Filenames: lessons `NN-slug/index.html`, assignments `aN-slug/`,
  explorations `exNN_slug.py`, quizzes `qN.json`.
