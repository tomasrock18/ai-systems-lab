# Stage 1 / Task 1 — Local Job Executor v0

## Context

Week 0 showed that the main immediate gap is the local execution model: asyncio Tasks, ownership, cancellation, bounded concurrency, cleanup and graceful shutdown.

Before adding databases, queues, networking or multiprocessing, build a local executor whose lifecycle guarantees can be explained and tested.

This is the first engineering task after the T0 baseline.

## Goal

Implement a small in-process asynchronous job executor in Python.

The task is not to reproduce Celery, a scheduler, or a production platform. The goal is to demonstrate correct ownership and lifecycle of concurrent work.

## Requirements

The executor must support:

1. Submission of multiple asynchronous jobs.
2. A configurable maximum number of concurrently running jobs.
3. A stable job identifier.
4. Observable job states covering at least:
   - pending;
   - running;
   - completed;
   - failed;
   - cancelled.
5. A way to inspect the current/result state of a submitted job.
6. Failure isolation: one job raising an exception must not terminate unrelated jobs or corrupt executor state.
7. Cancellation of an individual job.
8. Executor shutdown.
9. Once shutdown begins, new jobs must not be silently accepted as normal work.
10. After shutdown completes, the executor must not leave work that it owns running accidentally.
11. No busy waiting.
12. Resource/lifecycle ownership must be explicit in the implementation and explainable during review.

Use simulated I/O jobs such as sleeps; do not add real ML workloads yet.

## Shutdown semantics

Define the shutdown semantics yourself before implementing them.

At minimum document:

- what happens to pending jobs;
- what happens to running jobs;
- whether shutdown waits, cancels, or uses a timeout;
- what the caller can rely on after shutdown returns.

The implementation must match the documented contract.

## State model

Define allowed state transitions before coding.

The review will test invalid or adversarial transitions, for example cancellation racing with normal completion or shutdown.

Do not assume that a terminal result can safely be overwritten.

## Constraints

- Python 3.11+.
- In-process only.
- No persistence.
- No HTTP/API server.
- No multiprocessing worker pool.
- No external queue/broker.
- No Docker requirement.
- No Go implementation.
- No ML/GPU workload.
- Runtime implementation should use the Python standard library.
- Test dependencies such as pytest are allowed.
- Do not copy an existing executor implementation.

Do not add technology merely to make the project look more production-like.

## Acceptance criteria

The submission must include automated evidence for at least these cases:

1. The configured concurrency limit is never exceeded.
2. Several jobs can complete successfully.
3. One failed job does not prevent unrelated jobs from reaching their correct results.
4. A pending job can be cancelled and never starts executing.
5. A running job can be cancelled according to the documented contract.
6. Shutdown while work is active follows the documented shutdown contract.
7. Submission after shutdown begins is handled explicitly.
8. No executor-owned asyncio Tasks remain pending after completed shutdown.
9. Job state transitions remain internally consistent under the tested cancellation/failure cases.

Tests must verify behavior, not only execute code without assertions.

## Required design note

Before or alongside the implementation, add a short design note answering:

1. What objects/resources does the executor own?
2. Who owns each created asyncio Task?
3. What are the job-state invariants?
4. What exactly does cancellation mean in this implementation?
5. What exactly does shutdown guarantee?
6. What can shutdown NOT guarantee?
7. Where can races occur even on one event-loop thread?
8. Which failure modes are intentionally deferred to later stages?

Keep this concise. It is a reasoning artifact, not documentation for users.

## What not to use

Do not use:

- Celery;
- Dramatiq;
- RQ;
- RabbitMQ;
- Kafka;
- NATS;
- Redis;
- PostgreSQL;
- FastAPI background tasks;
- multiprocessing;
- Kubernetes;
- a copied worker-pool/executor implementation.

Do not introduce a lock/semaphore/queue/task-group merely because it appears in an example. Use a primitive only if you can explain the invariant/problem it enforces.

## Minimal just-in-time theory

Before implementation, use the official Python documentation to understand only the concepts needed here:

- coroutine vs asyncio Task;
- task creation and awaiting;
- task cancellation and CancelledError;
- event-loop suspension at await;
- cleanup with try/finally.

Do not turn this into a broad asyncio course before attempting the design.

## What to provide for review

Open a new PR containing:

- implementation;
- automated tests;
- design note;
- a short run/demo if useful;
- no unrelated refactoring.

In the PR description, include:

- the shutdown contract;
- the state-transition model;
- commands to run tests;
- one design decision you are uncertain about.

During review expect adversarial cases around cancellation, simultaneous completion, exceptions, shutdown and task leakage.
