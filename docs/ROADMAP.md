# Roadmap

This repository is the practical backbone of the ML Infrastructure / AI Systems learning project.

The roadmap is skill-gated rather than calendar-gated: a stage is considered complete only when the required skills are demonstrated in code, review, debugging, and explanation.

## Stages

- [x] Stage 0 — Baseline diagnostics
- [ ] Stage 1 — Execution model and local job executor
- [ ] Stage 2 — Worker architecture and process lifecycle
- [ ] Stage 3 — Distributed scheduler and persistent state
- [ ] Stage 4 — Reliability: retries, idempotency, leases, heartbeats, recovery
- [ ] Stage 5 — Observability, load testing, backpressure, admission control
- [ ] Stage 6 — ML workloads: VAD, ASR, PyTorch fundamentals
- [ ] Stage 7 — GPU fundamentals, profiling, CUDA basics
- [ ] Stage 8 — Inference systems and model serving
- [ ] Stage 9 — vLLM, batching, GPU scheduling
- [ ] Stage 10 — Distributed ML
- [ ] Stage 11 — Kubernetes and GPU infrastructure
- [ ] Stage 12 — Production hardening, portfolio, interviews

## Current stage — Stage 1

### Purpose

Build a correct mental and implementation model for local concurrency before introducing persistence, distributed scheduling, queues or ML workloads.

### Skills to demonstrate

- distinguish coroutine, Task, thread and process;
- reason about shared mutable state and race conditions;
- establish explicit ownership of background work;
- implement bounded concurrency;
- handle exceptions without losing unrelated work;
- implement cancellation propagation and cleanup;
- perform graceful shutdown with no owned work left running accidentally;
- write automated tests for lifecycle and failure behavior;
- explain invariants and guarantees rather than relying on repeated successful runs.

### Exit criteria

Stage 1 is complete only when the learner can:

1. implement and defend a local concurrent job executor;
2. explain who owns every running unit of work;
3. demonstrate bounded concurrency with tests;
4. cancel individual jobs and the executor without leaking owned tasks;
5. handle job failures without corrupting executor state;
6. shut down gracefully and explain what is and is not guaranteed;
7. identify race/lifecycle failure modes under adversarial review;
8. diagnose at least one intentionally injected concurrency bug.

### Explicitly deferred

Do not add these merely to make the project look more production-like:

- PostgreSQL persistence;
- HTTP/FastAPI API;
- RabbitMQ/Kafka/NATS/Redis queues;
- multiprocessing worker pool;
- distributed scheduler;
- Docker/Kubernetes;
- Go rewrite;
- ML/GPU workloads.

They will be introduced when the engineering problem requires them.

## Applied workload

Glyph will gradually become a real client of the compute platform.

Target pipeline:

`audio -> VAD -> ASR -> language/LLM analysis -> metrics -> report`

Product features that do not contribute to ML infrastructure learning should not distract from the core curriculum.
