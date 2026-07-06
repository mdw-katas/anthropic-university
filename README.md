# Anthropic University — Bachelor of Science in Computer Science

A complete CS bachelor's curriculum designed for a working software engineer
(16 years of professional experience, no formal CS degree, 26 years since the
last math class). General education is waived; math is included because it is
load-bearing for the CS coursework.

## Design Notes

- **Math track:** Lighter, CS-focused — a foundations refresher instead of the
  full calculus sequence, then discrete math, linear algebra, and
  probability/statistics.
- **Intro courses included:** The 101/102 sequence is kept for completeness and
  vocabulary; a professional can move through it quickly.
- **Languages:** Traditional per-subject choices — C for systems and
  architecture, Python for AI/ML, a functional language in the programming
  languages course. The goal is learning-by-unfamiliarity.
- **Elective tracks:** Compilers & languages, distributed systems, and AI &
  machine learning (two courses).

## Course Catalog

| Course                            | Title                                  | Prerequisites      |
|-----------------------------------|----------------------------------------|--------------------|
| [101](101-intro-to-cs/)           | Introduction to Computer Science       | none               |
| [102](102-program-design/)        | Program Design and Abstraction         | 101                |
| [110](110-math-foundations/)      | Mathematical Foundations               | none               |
| [120](120-discrete-mathematics/)  | Discrete Mathematics                   | 110                |
| [201](201-data-structures/)       | Data Structures                        | 102, 120           |
| [210](210-computer-architecture/) | Computer Organization and Architecture | 102                |
| [220](220-systems-programming/)   | Systems Programming in C and Unix      | 210                |
| [240](240-linear-algebra/)        | Linear Algebra                         | 110                |
| [301](301-algorithms/)            | Design and Analysis of Algorithms      | 201                |
| [310](310-operating-systems/)     | Operating Systems                      | 220                |
| [320](320-computer-networks/)     | Computer Networks                      | 220                |
| [330](330-databases/)             | Database Systems                       | 201                |
| [340](340-programming-languages/) | Programming Languages                  | 201                |
| [350](350-software-engineering/)  | Software Engineering                   | 201                |
| [360](360-probability-statistics/)| Probability and Statistics             | 110                |
| [370](370-theory-of-computation/) | Theory of Computation                  | 120                |
| [410](410-compilers/)             | Compiler Construction                  | 340, 370           |
| [420](420-distributed-systems/)   | Distributed Systems                    | 310, 320           |
| [430](430-machine-learning/)      | Machine Learning                       | 240, 360           |
| [440](440-deep-learning/)         | Deep Learning and Large Language Models| 430                |
| [490](490-capstone/)              | Senior Capstone Project                | senior standing    |

## Suggested Sequence (eight semesters)

| Semester | Courses            |
|----------|--------------------|
| 1        | 101, 110           |
| 2        | 102, 120           |
| 3        | 201, 210, 240      |
| 4        | 220, 301, 360      |
| 5        | 310, 330, 340      |
| 6        | 320, 350, 370      |
| 7        | 410, 420, 430      |
| 8        | 440, 490           |

Each course folder contains a `README.md` syllabus. Readings, assignments,
quizzes, and exams will be added later, course by course.
