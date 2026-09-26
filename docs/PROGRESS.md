# Progress

Scale:

- 0 — practically unfamiliar
- 1 — know the basic terminology
- 2 — understand the basic mechanism
- 3 — used independently
- 4 — can design, debug, and reason about failures
- 5 — deep understanding of trade-offs and non-trivial failure modes

Levels must be supported by evidence from completed tasks, reviews, debugging, or production experience.

## T0 baseline — 2026-09-26

This matrix replaces the preliminary self/experience-based estimates recorded before Week 0.
Scores below are based on the Week 0 diagnostic evidence plus already-established commercial experience where noted.

| Skill | Level | Evidence / notes |
|---|---:|---|
| Python backend | 3 | 4+ years commercial backend experience; not the main subject of Week 0 |
| Python concurrency | 1 | Can recognize some async/thread use cases, but Task model, cancellation, ownership, lifecycle and race reasoning are not yet established |
| Processes / threads / async | 1 | Correct intuition for some CPU/process separation; execution models, GIL, synchronization and executor trade-offs need foundations |
| Linux | 1 | Practical operational familiarity and ability to use ps/proc/ss/lsof with reference material; process lifecycle, signals, FDs and diagnosis model are weak |
| Networking | 1 | Some packet/protocol experience and useful operational intuition; TCP connection model, layering, sockets and failure semantics need foundations |
| PostgreSQL | 1 | Commercial SQLAlchemy/PostgreSQL exposure and ability to reproduce lost updates; indexes, transactions, isolation, locks and pooling are not understood deeply |
| Distributed systems | 1 | Correctly recognizes timeout uncertainty and some race scenarios; delivery guarantees, idempotency, ownership, failure detection and recovery are mostly new |
| Reliability / fault tolerance | 1 | Can identify that failures matter, but liveness, retries, duplicate execution, backpressure and recovery guarantees are not yet modeled |
| Automated testing | 1 | Some prior pytest experience, but Week 0 did not demonstrate infrastructure-grade concurrency/failure testing |
| Go | 0 | Basic syntax partly recognizable; goroutines/channels and a small concurrent program could not yet be implemented independently |
| PyTorch | 0 | Not started |
| GPU architecture | 0 | Not started |
| CUDA | 0 | Not started |
| Inference systems | 0 | Not started |
| vLLM | 0 | Not started |
| Distributed ML | 0 | Not started |
| Kubernetes | 0 | Not started |

## Week 0 evidence summary

- Thread race experiment reproduced lost updates.
- asyncio bounded runner/cancellation task could not yet be implemented.
- Linux process/socket inspection was completed with reference material.
- Parent death / surviving child behavior was observed, but orphan vs zombie semantics were initially confused.
- Raw TCP client/server was implemented; accepted-socket vs listening-socket model was not yet understood.
- PostgreSQL concurrent read-modify-write reproduced a lost-update anomaly.
- HTTP timeout uncertainty was understood; queue ACK/redelivery and exactly/at-least/at-most-once semantics were not.
- Go concurrency primitives were effectively new.
- Mixed failure/debugging questions exposed major gaps in lifecycle, stale ownership, duplicate side effects, overload handling and bottleneck diagnosis.

## Review rule

A score should be increased only when there is concrete evidence.

Reading a book or watching a lecture does not by itself increase a skill level.
