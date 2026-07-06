# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A self-directed B.S. in Computer Science for one student: a 16-year
professional software engineer with no CS degree and 26 years since his last
math class. Claude plays professor, counselor, and registrar. The degree map
lives in the root `README.md` and `curriculum.json`; each `NNN-*/` folder is
one course whose `README.md` is its syllabus.

## Commands

```
make build          # build the uni CLI to ./bin/uni
make test           # gofmt check, go vet, go test -race on tools/uni
make status         # degree dashboard
make next           # advisor: what to work on next

./bin/uni status <course>          # standing within a course (e.g. 101)
./bin/uni grade <course>/<item>    # run item's test suite, record score
./bin/uni quiz <course>/<item>     # interactive quiz, record score
./bin/uni hash <salt> <answer>     # for authoring quiz files
```

`--dry` on grade/quiz runs without recording — always use it when verifying
authored content, so Claude's test runs never pollute the student's transcript.

Single Go test: `cd tools/uni && go test -run TestName .`
One Python suite directly: from the item's folder,
`python3 -m unittest discover -v -s tests -t tests -p 'test_*.py'`
(explorations use `-s . -t .`).

## Architecture

Everything is JSON + files; there is no database or server. Data flows:

1. `curriculum.json` (root) — the degree map: course ids, dirs, credits,
   prerequisites, the 0.80 pass bar.
2. `<course-dir>/course.json` — per-course manifest: component weights
   (exploration/quiz/assignment/final) and the list of gradable items with
   their paths and test locations. A course with no `course.json` shows as
   "not yet authored". `content_complete: false` means more items are coming;
   a course only counts as complete (credits + GPA) when `content_complete`
   is true AND every item is passed.
3. `progress/<course>/<item>.json` — one committed record per item: best
   score (the grade — mastery model), last score, attempt count, passed flag.
   Git history is the transcript. Never hand-edit these; `uni` writes them.

The `uni` CLI (`tools/uni/`, Go, stdlib only — keep it dependency-free) grades
assignments/explorations by running `python3 -m unittest discover` in the
item's folder and parsing the summary (score = fraction of tests passed).
Course grade = weighted average of component scores; components with no
authored items are excluded and weights renormalized. Letter grades / GPA use
the standard 4.0 scale in `status.go`.

## Authoring conventions (agreed with the student)

- **Reading materials are HTML, not markdown**: each lesson is a
  self-contained `lessons/NN-slug/index.html` — inline CSS and vanilla JS, no
  external assets, light/dark via `prefers-color-scheme`, interactive widgets
  wherever they teach (steppers, predict-reveal `<details>`). Link to
  reputable external sources (docs.python.org, Python Tutor, MDN, official
  docs). Syllabi, assignment statements, and this file stay markdown.
- **No notebooks.** Explorations are plain runnable scripts using the
  predict-run-verify pattern: student fills `PREDICT_*` constants, runs the
  script, then `uni grade` runs unittest self-checks comparing predictions to
  computed truth.
- **Assignments are kata-style TDD**: `README.md` statement, `starter/` with
  stubbed functions raising `NotImplementedError`, `tests/` as the visible
  executable spec. Python content is stdlib-only (unittest, no pytest).
- **Quiz answers are never stored in plaintext**: author questions in
  `quizzes/*.json` with `answer_hash` from `uni hash <salt> <answer>` (salt
  convention: `<course>.<quiz>.<n>`). Quizzes are retakeable by design.
- **Adding content to a course**: create the materials, then append an item
  to that course's `course.json` (unique `id`; `tests_dir` defaults to
  `tests`, use `"."` for explorations). Set `content_complete: true` only
  when the final item ships. Before handing content to the student, verify
  it: reference-solve assignments in the scratchpad (never commit solutions)
  and check quizzes/graders with `--dry`.
- **Authoring a new course**: keep the existing folder's syllabus README,
  add `course.json` mirroring 101's shape. Non-Python courses will need a
  new runner in `grade.go` (e.g. `go test` for 420, `make test` for C
  courses) — extend `runSuite` by item `runner` field when that day comes.
- Grading policy already decided: pass bar 80%, best score kept, unattempted
  items count as zero in the course grade, percent + letter + GPA reporting.
