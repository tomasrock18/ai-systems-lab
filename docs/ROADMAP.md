# Roadmap

This repository is the practical backbone of the ML Infrastructure / AI Systems learning project.

The roadmap is skill-gated rather than calendar-gated: a stage is considered complete only when the required skills are demonstrated in code, review, debugging, and explanation.

## Stages

- [ ] Stage 0 — Baseline diagnostics
- [ ] Stage 1 — Local job executor
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

## Applied workload

Glyph will gradually become a real client of the compute platform.

Target pipeline:

`audio -> VAD -> ASR -> language/LLM analysis -> metrics -> report`

Product features that do not contribute to ML infrastructure learning should not distract from the core curriculum.
