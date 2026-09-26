# Learning Log

Short records of meaningful learning iterations.

## 2026-09-23 — T0

### Context

Started the ML Infrastructure / AI Systems learning project.

### Current direction

Transition from Middle Python Backend Developer toward ML Infrastructure / AI Systems engineering.

### Primary learning method

Theory -> engineering task -> independent implementation -> code review -> fixes -> defense -> next task.

### Main project

Build a Mini AI Compute Platform and gradually use Glyph as a real ML workload.

### Immediate next step

Run Stage 0 baseline diagnostics before implementing the first substantial component.

---

## 2026-09-26 — Week 0 baseline diagnostics complete

**Built**
- Thread race-condition experiment.
- Linux parent/child process experiment and process/socket inspection.
- Minimal TCP client/server.
- PostgreSQL concurrent counter experiment reproducing lost updates.
- Initial Go syntax/concurrency diagnostic.

**Learned**
- Successful repeated runs do not prove concurrency correctness.
- Operational familiarity is stronger than the underlying execution/system models.
- HTTP timeout does not determine whether a remote side effect happened.

**Mistakes / weak spots**
- Confused asyncio Task with thread and overestimated the protection provided by the GIL.
- Cancellation, task ownership, cleanup and graceful shutdown are not yet understood.
- Orphan vs zombie process semantics were confused.
- TCP listener/accepted connection/ephemeral port model is weak.
- PostgreSQL transactions, isolation, row locking, indexes and pooling are weak.
- Delivery guarantees, ACK/redelivery, idempotency, stale ownership and recovery are mostly new.
- Overload/backpressure and performance diagnosis need foundations.
- Go concurrency primitives are new.

**What is clear now**
- Python backend experience is real, but infrastructure/system fundamentals must be rebuilt from first principles where evidence is weak.
- The next stage should focus on local execution and lifecycle correctness rather than adding distributed technologies.

**What is still unclear**
- Precise coroutine/Task/thread/process execution models.
- How cancellation propagates and how owned work is cleaned up.
- How to state and enforce invariants under concurrency.
- How to diagnose resource saturation/queueing from system evidence.
- How persistent/distributed ownership will later survive crashes.

### Immediate next step

Stage 1 — Execution model and local job executor.

---

## Entry template

### YYYY-MM-DD — Task name

**Built**
-

**Learned**
-

**Mistakes / weak spots**
-

**What is clear now**
-

**What is still unclear**
-
