# Greenfield #4 Task Checklist

This document lists the 150 tasks defined in `greenfield_plan_4_150_tasks.csv` with checkboxes so progress can be tracked directly in the repository.

- **Total tasks:** 150
- **Source file:** `greenfield_plan_4_150_tasks.csv`

## TCB & Loader (micro-runtime) (Epic G0)

- [ ] **Loader — G0-01** — Task `5D87D2CD`
  - **Area:** Runtime  |  **Owner:** LLL-Runtime  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'loader' for TCB & Loader (micro-runtime) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `loader.rs_or_wasm`, `loader_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Module-Signature-Verify — G0-02** — Task `2C9C95E4`
  - **Area:** Runtime  |  **Owner:** LLL-Engine  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'module-signature-verify' for TCB & Loader (micro-runtime) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `module-signature-verify.rs_or_wasm`, `module-signature-verify_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Capabilities-Enforce — G0-03** — Task `C08BC26A`
  - **Area:** Runtime  |  **Owner:** LLL-Compiler  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'capabilities-enforce' for TCB & Loader (micro-runtime) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `capabilities-enforce.rs_or_wasm`, `capabilities-enforce_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Abi-Hostcalls — G0-04** — Task `2335833E`
  - **Area:** Runtime  |  **Owner:** LLL-Policy  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'abi-hostcalls' for TCB & Loader (micro-runtime) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `abi-hostcalls.rs_or_wasm`, `abi-hostcalls_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Io-Adapters — G0-05** — Task `FA59C9D0`
  - **Area:** Runtime  |  **Owner:** LLL-Infra  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'io-adapters' for TCB & Loader (micro-runtime) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `io-adapters.rs_or_wasm`, `io-adapters_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Lifecycle-Hooks — G0-06** — Task `FAEB7BC9`
  - **Area:** Runtime  |  **Owner:** LLL-Finance  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'lifecycle-hooks' for TCB & Loader (micro-runtime) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `lifecycle-hooks.rs_or_wasm`, `lifecycle-hooks_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Panic-Strategy — G0-07** — Task `98442E83`
  - **Area:** Runtime  |  **Owner:** LLL-Fed  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'panic-strategy' for TCB & Loader (micro-runtime) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `panic-strategy.rs_or_wasm`, `panic-strategy_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Metrics-Bootstrap — G0-08** — Task `7C7CB27D`
  - **Area:** Runtime  |  **Owner:** LLL-Engine  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'metrics-bootstrap' for TCB & Loader (micro-runtime) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `metrics-bootstrap.rs_or_wasm`, `metrics-bootstrap_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413


## .lll Grammar & IR (EBNF, SSA/DFG+FSM) (Epic G1)

- [ ] **Ebnf-Spec — G1-01** — Task `2962122B`
  - **Area:** Compiler  |  **Owner:** LLL-QA  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'ebnf-spec' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `ebnf-spec.rs_or_wasm`, `ebnf-spec_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Parser — G1-02** — Task `CB9C9B3C`
  - **Area:** Compiler  |  **Owner:** LLL-QA  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'parser' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `parser.rs_or_wasm`, `parser_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Typechecker — G1-03** — Task `85C66F75`
  - **Area:** Compiler  |  **Owner:** LLL-Finance  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'typechecker' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `typechecker.rs_or_wasm`, `typechecker_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Ir-Ssa — G1-04** — Task `C65F2FAD`
  - **Area:** Compiler  |  **Owner:** LLL-Runtime  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'ir-ssa' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `ir-ssa.rs_or_wasm`, `ir-ssa_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Fsm-Normalizer — G1-05** — Task `906AE2DD`
  - **Area:** Compiler  |  **Owner:** LLL-Fed  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'fsm-normalizer' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `fsm-normalizer.rs_or_wasm`, `fsm-normalizer_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Effect-System — G1-06** — Task `E15FAA35`
  - **Area:** Compiler  |  **Owner:** LLL-QA  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'effect-system' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `effect-system.rs_or_wasm`, `effect-system_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Error-Model — G1-07** — Task `67D470D3`
  - **Area:** Compiler  |  **Owner:** LLL-Docs  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'error-model' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `error-model.rs_or_wasm`, `error-model_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Policy-Nodes — G1-08** — Task `5EBE922A`
  - **Area:** Compiler  |  **Owner:** LLL-Policy  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'policy-nodes' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `policy-nodes.rs_or_wasm`, `policy-nodes_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Guard-Ir — G1-09** — Task `23CABB3D`
  - **Area:** Compiler  |  **Owner:** LLL-Fed  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'guard-ir' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `guard-ir.rs_or_wasm`, `guard-ir_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Router-Ir — G1-10** — Task `C70C8C7E`
  - **Area:** Compiler  |  **Owner:** LLL-Docs  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'router-ir' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `router-ir.rs_or_wasm`, `router-ir_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Enzyme-Ir — G1-11** — Task `930D8A57`
  - **Area:** Compiler  |  **Owner:** LLL-Docs  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'enzyme-ir' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `enzyme-ir.rs_or_wasm`, `enzyme-ir_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Api-Ir — G1-12** — Task `0C5B805A`
  - **Area:** Compiler  |  **Owner:** LLL-Engine  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'api-ir' for .lll Grammar & IR (EBNF, SSA/DFG+FSM) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `api-ir.rs_or_wasm`, `api-ir_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413


## Optimizer & Partial Evaluation (Epic G2)

- [ ] **Partial-Eval — G2-01** — Task `773FF42E`
  - **Area:** Compiler  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'partial-eval' for Optimizer & Partial Evaluation with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `partial-eval.rs_or_wasm`, `partial-eval_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Dead-Branch-Elim — G2-02** — Task `2201FCF0`
  - **Area:** Compiler  |  **Owner:** LLL-Runtime  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'dead-branch-elim' for Optimizer & Partial Evaluation with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `dead-branch-elim.rs_or_wasm`, `dead-branch-elim_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Const-Folding — G2-03** — Task `5930C038`
  - **Area:** Compiler  |  **Owner:** LLL-Policy  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'const-folding' for Optimizer & Partial Evaluation with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `const-folding.rs_or_wasm`, `const-folding_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Guard-Specialization — G2-04** — Task `FA445559`
  - **Area:** Compiler  |  **Owner:** LLL-Docs  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'guard-specialization' for Optimizer & Partial Evaluation with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `guard-specialization.rs_or_wasm`, `guard-specialization_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Policy-Inlining — G2-05** — Task `36659CC2`
  - **Area:** Compiler  |  **Owner:** LLL-Fed  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'policy-inlining' for Optimizer & Partial Evaluation with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `policy-inlining.rs_or_wasm`, `policy-inlining_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Shape-Prop — G2-06** — Task `9DDA0A48`
  - **Area:** Compiler  |  **Owner:** LLL-Policy  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'shape-prop' for Optimizer & Partial Evaluation with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `shape-prop.rs_or_wasm`, `shape-prop_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Idempotency-Proofs — G2-07** — Task `B7B04797`
  - **Area:** Compiler  |  **Owner:** LLL-Infra  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'idempotency-proofs' for Optimizer & Partial Evaluation with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `idempotency-proofs.rs_or_wasm`, `idempotency-proofs_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Layout-Planner — G2-08** — Task `E900D57D`
  - **Area:** Compiler  |  **Owner:** LLL-Policy  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'layout-planner' for Optimizer & Partial Evaluation with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `layout-planner.rs_or_wasm`, `layout-planner_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Index-Planner — G2-09** — Task `BE8AFAB7`
  - **Area:** Compiler  |  **Owner:** LLL-QA  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'index-planner' for Optimizer & Partial Evaluation with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `index-planner.rs_or_wasm`, `index-planner_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Cost-Model — G2-10** — Task `CF73863D`
  - **Area:** Compiler  |  **Owner:** LLL-Compiler  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'cost-model' for Optimizer & Partial Evaluation with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `cost-model.rs_or_wasm`, `cost-model_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** None
  - **Created at:** 2025-10-04T18:34:41.528413


## AOT Backends (WASM, Rust/C) (Epic G3)

- [ ] **Wasm-Backend — G3-01** — Task `731AE533`
  - **Area:** Compiler  |  **Owner:** LLL-Finance  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'wasm-backend' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `wasm-backend.rs_or_wasm`, `wasm-backend_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Rustgen-Backend — G3-02** — Task `9F9F050B`
  - **Area:** Compiler  |  **Owner:** LLL-Finance  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'rustgen-backend' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `rustgen-backend.rs_or_wasm`, `rustgen-backend_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Jit-Linker — G3-03** — Task `E7154A3E`
  - **Area:** Compiler  |  **Owner:** LLL-Fed  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'jit-linker' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `jit-linker.rs_or_wasm`, `jit-linker_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Aot-Cache — G3-04** — Task `37C6A943`
  - **Area:** Compiler  |  **Owner:** LLL-Fed  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'aot-cache' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `aot-cache.rs_or_wasm`, `aot-cache_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Rtlib-Min — G3-05** — Task `E5E46F07`
  - **Area:** Compiler  |  **Owner:** LLL-Engine  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'rtlib-min' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `rtlib-min.rs_or_wasm`, `rtlib-min_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Vectorized-Json — G3-06** — Task `6658D9B6`
  - **Area:** Compiler  |  **Owner:** LLL-Engine  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'vectorized-json' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `vectorized-json.rs_or_wasm`, `vectorized-json_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Simd-Validate — G3-07** — Task `C6D71CAC`
  - **Area:** Compiler  |  **Owner:** LLL-QA  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'simd-validate' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `simd-validate.rs_or_wasm`, `simd-validate_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Event-Batching — G3-08** — Task `9E017EFA`
  - **Area:** Compiler  |  **Owner:** LLL-Fed  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'event-batching' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `event-batching.rs_or_wasm`, `event-batching_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Lock-Free-Queues — G3-09** — Task `9F328F49`
  - **Area:** Compiler  |  **Owner:** LLL-QA  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'lock-free-queues' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `lock-free-queues.rs_or_wasm`, `lock-free-queues_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Ring-Buffers — G3-10** — Task `81CAFC49`
  - **Area:** Compiler  |  **Owner:** LLL-Compiler  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'ring-buffers' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `ring-buffers.rs_or_wasm`, `ring-buffers_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Arena-Alloc — G3-11** — Task `07CFCB55`
  - **Area:** Compiler  |  **Owner:** LLL-Fed  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'arena-alloc' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `arena-alloc.rs_or_wasm`, `arena-alloc_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Zero-Copy-Pipeline — G3-12** — Task `73165535`
  - **Area:** Compiler  |  **Owner:** LLL-Engine  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'zero-copy-pipeline' for AOT Backends (WASM, Rust/C) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `zero-copy-pipeline.rs_or_wasm`, `zero-copy-pipeline_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Determinism & Sandbox (Epic G4)

- [ ] **Deterministic-Clock — G4-01** — Task `6103D852`
  - **Area:** Security  |  **Owner:** LLL-Policy  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'deterministic-clock' for Determinism & Sandbox with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `deterministic-clock.rs_or_wasm`, `deterministic-clock_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Seeded-Rand — G4-02** — Task `A29D2163`
  - **Area:** Security  |  **Owner:** LLL-Runtime  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'seeded-rand' for Determinism & Sandbox with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `seeded-rand.rs_or_wasm`, `seeded-rand_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Capability-Tokens — G4-03** — Task `DD5ECB4C`
  - **Area:** Security  |  **Owner:** LLL-Fed  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'capability-tokens' for Determinism & Sandbox with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `capability-tokens.rs_or_wasm`, `capability-tokens_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Sandbox-Limits — G4-04** — Task `89E751BE`
  - **Area:** Security  |  **Owner:** LLL-Infra  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'sandbox-limits' for Determinism & Sandbox with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `sandbox-limits.rs_or_wasm`, `sandbox-limits_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Side-Effect-Gates — G4-05** — Task `109F471F`
  - **Area:** Security  |  **Owner:** LLL-Infra  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'side-effect-gates' for Determinism & Sandbox with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `side-effect-gates.rs_or_wasm`, `side-effect-gates_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Provenance-Core — G4-06** — Task `2AC7ED5A`
  - **Area:** Security  |  **Owner:** LLL-Runtime  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'provenance-core' for Determinism & Sandbox with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `provenance-core.rs_or_wasm`, `provenance-core_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Audit-Worm — G4-07** — Task `56EA9D35`
  - **Area:** Security  |  **Owner:** LLL-Runtime  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'audit-worm' for Determinism & Sandbox with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `audit-worm.rs_or_wasm`, `audit-worm_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Threat-Model — G4-08** — Task `16E1810C`
  - **Area:** Security  |  **Owner:** LLL-Runtime  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'threat-model' for Determinism & Sandbox with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `threat-model.rs_or_wasm`, `threat-model_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Fuzz-Contracts — G4-09** — Task `CD8054CE`
  - **Area:** Security  |  **Owner:** LLL-QA  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'fuzz-contracts' for Determinism & Sandbox with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `fuzz-contracts.rs_or_wasm`, `fuzz-contracts_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Ingress Kernel (eBPF/XDP optional) (Epic G5)

- [ ] **Ebpf-Filter — G5-01** — Task `108BCAEB`
  - **Area:** Ingress  |  **Owner:** LLL-QA  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'ebpf-filter' for Ingress Kernel (eBPF/XDP optional) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `ebpf-filter.rs_or_wasm`, `ebpf-filter_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Xdp-Normalizer — G5-02** — Task `FF37FDAC`
  - **Area:** Ingress  |  **Owner:** LLL-Runtime  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'xdp-normalizer' for Ingress Kernel (eBPF/XDP optional) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `xdp-normalizer.rs_or_wasm`, `xdp-normalizer_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Early-Tenant-Mark — G5-03** — Task `B367B5D5`
  - **Area:** Ingress  |  **Owner:** LLL-Docs  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'early-tenant-mark' for Ingress Kernel (eBPF/XDP optional) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `early-tenant-mark.rs_or_wasm`, `early-tenant-mark_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Sig-Precheck — G5-04** — Task `EEDAEF6A`
  - **Area:** Ingress  |  **Owner:** LLL-Compiler  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'sig-precheck' for Ingress Kernel (eBPF/XDP optional) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `sig-precheck.rs_or_wasm`, `sig-precheck_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Payload-Sampler — G5-05** — Task `0BFF4265`
  - **Area:** Ingress  |  **Owner:** LLL-Engine  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'payload-sampler' for Ingress Kernel (eBPF/XDP optional) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `payload-sampler.rs_or_wasm`, `payload-sampler_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Lossy-Guard — G5-06** — Task `B599B16E`
  - **Area:** Ingress  |  **Owner:** LLL-Runtime  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'lossy-guard' for Ingress Kernel (eBPF/XDP optional) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `lossy-guard.rs_or_wasm`, `lossy-guard_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Drop-Policies — G5-07** — Task `B4B877D4`
  - **Area:** Ingress  |  **Owner:** LLL-Policy  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'drop-policies' for Ingress Kernel (eBPF/XDP optional) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `drop-policies.rs_or_wasm`, `drop-policies_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Kernel-Metrics — G5-08** — Task `A18C777E`
  - **Area:** Ingress  |  **Owner:** LLL-Compiler  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'kernel-metrics' for Ingress Kernel (eBPF/XDP optional) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `kernel-metrics.rs_or_wasm`, `kernel-metrics_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Routers/Policies/Workflows in .lll (Epic G6)

- [ ] **Router.Lll — G6-01** — Task `2F8B0E85`
  - **Area:** Rules  |  **Owner:** LLL-Policy  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'router.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `router.lll.lll`, `router.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Policy.Lll — G6-02** — Task `2B589D35`
  - **Area:** Rules  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'policy.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `policy.lll.lll`, `policy.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Workflow.Lll — G6-03** — Task `54509748`
  - **Area:** Rules  |  **Owner:** LLL-Fed  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'workflow.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `workflow.lll.lll`, `workflow.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Enzyme.Lll — G6-04** — Task `1A7D1FE6`
  - **Area:** Rules  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'enzyme.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `enzyme.lll.lll`, `enzyme.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Api.Lll — G6-05** — Task `59573352`
  - **Area:** Rules  |  **Owner:** LLL-Runtime  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'api.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `api.lll.lll`, `api.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Validator.Lll — G6-06** — Task `9A3CC10D`
  - **Area:** Rules  |  **Owner:** LLL-Fed  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'validator.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `validator.lll.lll`, `validator.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Normalizer.Lll — G6-07** — Task `917AE3FC`
  - **Area:** Rules  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'normalizer.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `normalizer.lll.lll`, `normalizer.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Rate-Limit.Lll — G6-08** — Task `919EBE9B`
  - **Area:** Rules  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'rate-limit.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `rate-limit.lll.lll`, `rate-limit.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Dedup.Lll — G6-09** — Task `7A98717C`
  - **Area:** Rules  |  **Owner:** LLL-Docs  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'dedup.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `dedup.lll.lll`, `dedup.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Retry.Lll — G6-10** — Task `EA56F688`
  - **Area:** Rules  |  **Owner:** LLL-Docs  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'retry.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `retry.lll.lll`, `retry.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Saga.Lll — G6-11** — Task `F54FF4F5`
  - **Area:** Rules  |  **Owner:** LLL-Compiler  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'saga.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `saga.lll.lll`, `saga.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Quorum.Lll — G6-12** — Task `FCC126A3`
  - **Area:** Rules  |  **Owner:** LLL-Runtime  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'quorum.lll' for Routers/Policies/Workflows in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `quorum.lll.lll`, `quorum.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Banking/Wallet & Receipts in .lll (Epic G7)

- [ ] **Wallet.Lll — G7-01** — Task `6C1303FD`
  - **Area:** Finance  |  **Owner:** LLL-Compiler  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'wallet.lll' for Banking/Wallet & Receipts in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `wallet.lll.lll`, `wallet.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Limits.Lll — G7-02** — Task `8DD3BAB4`
  - **Area:** Finance  |  **Owner:** LLL-Runtime  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'limits.lll' for Banking/Wallet & Receipts in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `limits.lll.lll`, `limits.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Receipts.Lll — G7-03** — Task `82E5DEB6`
  - **Area:** Finance  |  **Owner:** LLL-QA  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'receipts.lll' for Banking/Wallet & Receipts in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `receipts.lll.lll`, `receipts.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Dual-Approval.Lll — G7-04** — Task `23D08CC7`
  - **Area:** Finance  |  **Owner:** LLL-Engine  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'dual-approval.lll' for Banking/Wallet & Receipts in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `dual-approval.lll.lll`, `dual-approval.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Alerts.Lll — G7-05** — Task `3F204BDA`
  - **Area:** Finance  |  **Owner:** LLL-Compiler  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'alerts.lll' for Banking/Wallet & Receipts in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `alerts.lll.lll`, `alerts.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Reconcile.Lll — G7-06** — Task `0FD3621E`
  - **Area:** Finance  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'reconcile.lll' for Banking/Wallet & Receipts in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `reconcile.lll.lll`, `reconcile.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Freeze.Lll — G7-07** — Task `7EF5DE7A`
  - **Area:** Finance  |  **Owner:** LLL-Docs  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'freeze.lll' for Banking/Wallet & Receipts in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `freeze.lll.lll`, `freeze.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Fees.Lll — G7-08** — Task `906721A0`
  - **Area:** Finance  |  **Owner:** LLL-Engine  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'fees.lll' for Banking/Wallet & Receipts in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `fees.lll.lll`, `fees.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Chargeback.Lll — G7-09** — Task `E2055111`
  - **Area:** Finance  |  **Owner:** LLL-Compiler  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'chargeback.lll' for Banking/Wallet & Receipts in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `chargeback.lll.lll`, `chargeback.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Statements.Lll — G7-10** — Task `86B26826`
  - **Area:** Finance  |  **Owner:** LLL-Policy  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'statements.lll' for Banking/Wallet & Receipts in .lll with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `statements.lll.lll`, `statements.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Ledger & Columnar Indexing (Epic G8)

- [ ] **Ledger-Append — G8-01** — Task `5F260A5C`
  - **Area:** Storage  |  **Owner:** LLL-Compiler  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'ledger-append' for Ledger & Columnar Indexing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `ledger-append.rs_or_wasm`, `ledger-append_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Columnar-Layout — G8-02** — Task `DBE5404E`
  - **Area:** Storage  |  **Owner:** LLL-Docs  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'columnar-layout' for Ledger & Columnar Indexing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `columnar-layout.rs_or_wasm`, `columnar-layout_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Arrow-Export — G8-03** — Task `38093B85`
  - **Area:** Storage  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'arrow-export' for Ledger & Columnar Indexing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `arrow-export.rs_or_wasm`, `arrow-export_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Fts-Index — G8-04** — Task `C32F5D67`
  - **Area:** Storage  |  **Owner:** LLL-Engine  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'fts-index' for Ledger & Columnar Indexing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `fts-index.rs_or_wasm`, `fts-index_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Perfect-Hash — G8-05** — Task `282B129B`
  - **Area:** Storage  |  **Owner:** LLL-Fed  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'perfect-hash' for Ledger & Columnar Indexing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `perfect-hash.rs_or_wasm`, `perfect-hash_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Bloom-Filters — G8-06** — Task `9165572D`
  - **Area:** Storage  |  **Owner:** LLL-Docs  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'bloom-filters' for Ledger & Columnar Indexing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `bloom-filters.rs_or_wasm`, `bloom-filters_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Hotset-Cache — G8-07** — Task `4BC195EF`
  - **Area:** Storage  |  **Owner:** LLL-Docs  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'hotset-cache' for Ledger & Columnar Indexing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `hotset-cache.rs_or_wasm`, `hotset-cache_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Snapshot-Writer — G8-08** — Task `77E1A1E1`
  - **Area:** Storage  |  **Owner:** LLL-Finance  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'snapshot-writer' for Ledger & Columnar Indexing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `snapshot-writer.rs_or_wasm`, `snapshot-writer_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Restore-Engine — G8-09** — Task `A9ED4A8D`
  - **Area:** Storage  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'restore-engine' for Ledger & Columnar Indexing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `restore-engine.rs_or_wasm`, `restore-engine_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Checksums — G8-10** — Task `D5553AC0`
  - **Area:** Storage  |  **Owner:** LLL-QA  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'checksums' for Ledger & Columnar Indexing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `checksums.rs_or_wasm`, `checksums_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Federation & Privacy (Epic G9)

- [ ] **Sync-Policy.Lll — G9-01** — Task `5791E0ED`
  - **Area:** Federation  |  **Owner:** LLL-Policy  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'sync-policy.lll' for Federation & Privacy with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `sync-policy.lll.lll`, `sync-policy.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Privacy-Redaction.Lll — G9-02** — Task `02F507C8`
  - **Area:** Federation  |  **Owner:** LLL-Finance  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'privacy-redaction.lll' for Federation & Privacy with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `privacy-redaction.lll.lll`, `privacy-redaction.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Pull-Push.Lll — G9-03** — Task `76BBEEF2`
  - **Area:** Federation  |  **Owner:** LLL-Policy  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'pull-push.lll' for Federation & Privacy with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `pull-push.lll.lll`, `pull-push.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Leases.Lll — G9-04** — Task `1862BDAE`
  - **Area:** Federation  |  **Owner:** LLL-Runtime  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'leases.lll' for Federation & Privacy with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `leases.lll.lll`, `leases.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Conflict-Resolve.Lll — G9-05** — Task `BBEE89D8`
  - **Area:** Federation  |  **Owner:** LLL-Engine  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'conflict-resolve.lll' for Federation & Privacy with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `conflict-resolve.lll.lll`, `conflict-resolve.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Cross-Sign.Lll — G9-06** — Task `C2A5A6BA`
  - **Area:** Federation  |  **Owner:** LLL-QA  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'cross-sign.lll' for Federation & Privacy with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `cross-sign.lll.lll`, `cross-sign.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Tenant-Filters.Lll — G9-07** — Task `2CBED710`
  - **Area:** Federation  |  **Owner:** LLL-Engine  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'tenant-filters.lll' for Federation & Privacy with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `tenant-filters.lll.lll`, `tenant-filters.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Federation-Metrics.Lll — G9-08** — Task `227C1A18`
  - **Area:** Federation  |  **Owner:** LLL-Infra  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'federation-metrics.lll' for Federation & Privacy with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `federation-metrics.lll.lll`, `federation-metrics.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Quota.Lll — G9-09** — Task `EEB1B3A6`
  - **Area:** Federation  |  **Owner:** LLL-Policy  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'quota.lll' for Federation & Privacy with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `quota.lll.lll`, `quota.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Observability & Trace Synthesis (Epic G10)

- [ ] **Metrics-Map.Lll — G10-01** — Task `A446523A`
  - **Area:** Observability  |  **Owner:** LLL-Engine  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'metrics-map.lll' for Observability & Trace Synthesis with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `metrics-map.lll.lll`, `metrics-map.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Trace-Links.Lll — G10-02** — Task `4F68013E`
  - **Area:** Observability  |  **Owner:** LLL-Fed  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'trace-links.lll' for Observability & Trace Synthesis with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `trace-links.lll.lll`, `trace-links.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Delta_S-Hist.Lll — G10-03** — Task `BC6C8E5B`
  - **Area:** Observability  |  **Owner:** LLL-Finance  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'delta_s-hist.lll' for Observability & Trace Synthesis with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `delta_s-hist.lll.lll`, `delta_s-hist.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Error-Rate.Lll — G10-04** — Task `C97162B2`
  - **Area:** Observability  |  **Owner:** LLL-QA  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'error-rate.lll' for Observability & Trace Synthesis with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `error-rate.lll.lll`, `error-rate.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Lag-Alarms.Lll — G10-05** — Task `FB823391`
  - **Area:** Observability  |  **Owner:** LLL-Engine  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'lag-alarms.lll' for Observability & Trace Synthesis with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `lag-alarms.lll.lll`, `lag-alarms.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Thresholds.Lll — G10-06** — Task `045CBA3E`
  - **Area:** Observability  |  **Owner:** LLL-QA  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'thresholds.lll' for Observability & Trace Synthesis with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `thresholds.lll.lll`, `thresholds.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Sampling.Lll — G10-07** — Task `15261131`
  - **Area:** Observability  |  **Owner:** LLL-Policy  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'sampling.lll' for Observability & Trace Synthesis with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `sampling.lll.lll`, `sampling.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Export-Prom.Lll — G10-08** — Task `0A46D6A3`
  - **Area:** Observability  |  **Owner:** LLL-Infra  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'export-prom.lll' for Observability & Trace Synthesis with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `export-prom.lll.lll`, `export-prom.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Exports & Compliance (Epic G11)

- [ ] **Export-Ndjson.Lll — G11-01** — Task `1AD28D01`
  - **Area:** Egress  |  **Owner:** LLL-Infra  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'export-ndjson.lll' for Exports & Compliance with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `export-ndjson.lll.lll`, `export-ndjson.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Export-Saft.Lll — G11-02** — Task `7D93D449`
  - **Area:** Egress  |  **Owner:** LLL-Infra  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'export-saft.lll' for Exports & Compliance with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `export-saft.lll.lll`, `export-saft.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Export-Csv.Lll — G11-03** — Task `756FE014`
  - **Area:** Egress  |  **Owner:** LLL-Fed  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'export-csv.lll' for Exports & Compliance with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `export-csv.lll.lll`, `export-csv.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Package-Sign.Lll — G11-04** — Task `781F59DC`
  - **Area:** Egress  |  **Owner:** LLL-Engine  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'package-sign.lll' for Exports & Compliance with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `package-sign.lll.lll`, `package-sign.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Egress-Api.Lll — G11-05** — Task `8A7AA797`
  - **Area:** Egress  |  **Owner:** LLL-Compiler  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'egress-api.lll' for Exports & Compliance with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `egress-api.lll.lll`, `egress-api.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Validator-Ext.Lll — G11-06** — Task `34D2ADA6`
  - **Area:** Egress  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'validator-ext.lll' for Exports & Compliance with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `validator-ext.lll.lll`, `validator-ext.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Catalog.Lll — G11-07** — Task `669E2FC0`
  - **Area:** Egress  |  **Owner:** LLL-QA  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'catalog.lll' for Exports & Compliance with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `catalog.lll.lll`, `catalog.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Retention-Manifest.Lll — G11-08** — Task `4196A813`
  - **Area:** Egress  |  **Owner:** LLL-Infra  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'retention-manifest.lll' for Exports & Compliance with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `retention-manifest.lll.lll`, `retention-manifest.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## UI Bindings & Hot-reload (Epic G12)

- [ ] **Ws-Topics.Lll — G12-01** — Task `348B6AFE`
  - **Area:** UI  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'ws-topics.lll' for UI Bindings & Hot-reload with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `ws-topics.lll.lll`, `ws-topics.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Panel-Bindings.Lll — G12-02** — Task `F279DB76`
  - **Area:** UI  |  **Owner:** LLL-Finance  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'panel-bindings.lll' for UI Bindings & Hot-reload with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `panel-bindings.lll.lll`, `panel-bindings.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Hot-Reload-Ui.Lll — G12-03** — Task `0B2EAE81`
  - **Area:** UI  |  **Owner:** LLL-Engine  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'hot-reload-ui.lll' for UI Bindings & Hot-reload with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `hot-reload-ui.lll.lll`, `hot-reload-ui.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **A11Y.Lll — G12-04** — Task `27A2502E`
  - **Area:** UI  |  **Owner:** LLL-Policy  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'a11y.lll' for UI Bindings & Hot-reload with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `a11y.lll.lll`, `a11y.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Offline-Cache.Lll — G12-05** — Task `A88BDC0C`
  - **Area:** UI  |  **Owner:** LLL-Engine  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'offline-cache.lll' for UI Bindings & Hot-reload with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `offline-cache.lll.lll`, `offline-cache.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Fts-Search.Lll — G12-06** — Task `668E2454`
  - **Area:** UI  |  **Owner:** LLL-Finance  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'fts-search.lll' for UI Bindings & Hot-reload with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `fts-search.lll.lll`, `fts-search.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Theme.Lll — G12-07** — Task `71C1C1E9`
  - **Area:** UI  |  **Owner:** LLL-Runtime  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'theme.lll' for UI Bindings & Hot-reload with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `theme.lll.lll`, `theme.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Ui-Tests.Lll — G12-08** — Task `F70DC1F0`
  - **Area:** UI  |  **Owner:** LLL-Runtime  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'ui-tests.lll' for UI Bindings & Hot-reload with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `ui-tests.lll.lll`, `ui-tests.lll_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Bench Suite & Shadow-Run (Epic G13)

- [ ] **Bench-Ingress — G13-01** — Task `2D2B2C21`
  - **Area:** QA/Perf  |  **Owner:** LLL-Finance  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'bench-ingress' for Bench Suite & Shadow-Run with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `bench-ingress.rs_or_wasm`, `bench-ingress_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Bench-Ledger — G13-02** — Task `CA0F9870`
  - **Area:** QA/Perf  |  **Owner:** LLL-Runtime  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'bench-ledger' for Bench Suite & Shadow-Run with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `bench-ledger.rs_or_wasm`, `bench-ledger_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Bench-Workflow — G13-03** — Task `4D2A4B95`
  - **Area:** QA/Perf  |  **Owner:** LLL-Docs  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'bench-workflow' for Bench Suite & Shadow-Run with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `bench-workflow.rs_or_wasm`, `bench-workflow_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Bench-Receipts — G13-04** — Task `7A4E93A3`
  - **Area:** QA/Perf  |  **Owner:** LLL-QA  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'bench-receipts' for Bench Suite & Shadow-Run with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `bench-receipts.rs_or_wasm`, `bench-receipts_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Bench-Query — G13-05** — Task `E1B6051E`
  - **Area:** QA/Perf  |  **Owner:** LLL-Engine  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'bench-query' for Bench Suite & Shadow-Run with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `bench-query.rs_or_wasm`, `bench-query_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Shadow-Runner — G13-06** — Task `EF7EFA93`
  - **Area:** QA/Perf  |  **Owner:** LLL-Compiler  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'shadow-runner' for Bench Suite & Shadow-Run with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `shadow-runner.rs_or_wasm`, `shadow-runner_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Corpus-Gen — G13-07** — Task `C6F548EA`
  - **Area:** QA/Perf  |  **Owner:** LLL-Infra  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'corpus-gen' for Bench Suite & Shadow-Run with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `corpus-gen.rs_or_wasm`, `corpus-gen_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Perf-Regression — G13-08** — Task `8EE89173`
  - **Area:** QA/Perf  |  **Owner:** LLL-Finance  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'perf-regression' for Bench Suite & Shadow-Run with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `perf-regression.rs_or_wasm`, `perf-regression_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Pgo-Cycle — G13-09** — Task `3DB593FC`
  - **Area:** QA/Perf  |  **Owner:** LLL-Engine  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'pgo-cycle' for Bench Suite & Shadow-Run with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `pgo-cycle.rs_or_wasm`, `pgo-cycle_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Dashboards — G13-10** — Task `940DDFFA`
  - **Area:** QA/Perf  |  **Owner:** LLL-Engine  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'dashboards' for Bench Suite & Shadow-Run with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `dashboards.rs_or_wasm`, `dashboards_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Supply Chain & Signing (Epic G14)

- [ ] **Key-Mgmt — G14-01** — Task `742A282D`
  - **Area:** SupplyChain  |  **Owner:** LLL-Policy  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'key-mgmt' for Supply Chain & Signing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `key-mgmt.rs_or_wasm`, `key-mgmt_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Supply-Sign — G14-02** — Task `8762A3BB`
  - **Area:** SupplyChain  |  **Owner:** LLL-Finance  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'supply-sign' for Supply Chain & Signing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `supply-sign.rs_or_wasm`, `supply-sign_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Verify-On-Load — G14-03** — Task `CE195497`
  - **Area:** SupplyChain  |  **Owner:** LLL-QA  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'verify-on-load' for Supply Chain & Signing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `verify-on-load.rs_or_wasm`, `verify-on-load_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Attest-Manifest — G14-04** — Task `4B3790B6`
  - **Area:** SupplyChain  |  **Owner:** LLL-Fed  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'attest-manifest' for Supply Chain & Signing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `attest-manifest.rs_or_wasm`, `attest-manifest_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Sbom — G14-05** — Task `23C52E06`
  - **Area:** SupplyChain  |  **Owner:** LLL-Infra  |  **Complexity:** 5  |  **Status:** Planned
  - **Description:** Build 'sbom' for Supply Chain & Signing with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `sbom.rs_or_wasm`, `sbom_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Profiles & Packaging (Epic G15)

- [ ] **Profiles.Dev — G15-01** — Task `02750AF9`
  - **Area:** Deploy  |  **Owner:** LLL-Runtime  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'profiles.dev' for Profiles & Packaging with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `profiles.dev.rs_or_wasm`, `profiles.dev_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Profiles.Single — G15-02** — Task `17B3F437`
  - **Area:** Deploy  |  **Owner:** LLL-Docs  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'profiles.single' for Profiles & Packaging with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `profiles.single.rs_or_wasm`, `profiles.single_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Profiles.Federated — G15-03** — Task `EF6B6B14`
  - **Area:** Deploy  |  **Owner:** LLL-Engine  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'profiles.federated' for Profiles & Packaging with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `profiles.federated.rs_or_wasm`, `profiles.federated_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Packaging — G15-04** — Task `457E9F0E`
  - **Area:** Deploy  |  **Owner:** LLL-Finance  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'packaging' for Profiles & Packaging with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `packaging.rs_or_wasm`, `packaging_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Upgrade-Protocol — G15-05** — Task `93D614AC`
  - **Area:** Deploy  |  **Owner:** LLL-Runtime  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'upgrade-protocol' for Profiles & Packaging with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `upgrade-protocol.rs_or_wasm`, `upgrade-protocol_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413


## Ops & Resilience (snapshots/restore) (Epic G16)

- [ ] **Disaster-Recovery — G16-01** — Task `81D37449`
  - **Area:** Ops  |  **Owner:** LLL-Finance  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'disaster-recovery' for Ops & Resilience (snapshots/restore) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `disaster-recovery.rs_or_wasm`, `disaster-recovery_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Watchdog — G16-02** — Task `4AD870BD`
  - **Area:** Ops  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'watchdog' for Ops & Resilience (snapshots/restore) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `watchdog.rs_or_wasm`, `watchdog_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Kill-Switches — G16-03** — Task `390CD711`
  - **Area:** Ops  |  **Owner:** LLL-Finance  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'kill-switches' for Ops & Resilience (snapshots/restore) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `kill-switches.rs_or_wasm`, `kill-switches_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Runbooks — G16-04** — Task `920D5B90`
  - **Area:** Ops  |  **Owner:** LLL-Docs  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'runbooks' for Ops & Resilience (snapshots/restore) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `runbooks.rs_or_wasm`, `runbooks_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Oncall — G16-05** — Task `283046F7`
  - **Area:** Ops  |  **Owner:** LLL-Finance  |  **Complexity:** 3  |  **Status:** Planned
  - **Description:** Build 'oncall' for Ops & Resilience (snapshots/restore) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `oncall.rs_or_wasm`, `oncall_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413

- [ ] **Budget-Alarms — G16-06** — Task `443FBD0E`
  - **Area:** Ops  |  **Owner:** LLL-Compiler  |  **Complexity:** 4  |  **Status:** Planned
  - **Description:** Build 'budget-alarms' for Ops & Resilience (snapshots/restore) with .lll-as-source-of-truth; generate AOT where possible; no business logic in TCB.
  - **Expected outputs:** `budget-alarms.rs_or_wasm`, `budget-alarms_tests.lll`
  - **Acceptance criteria:** `Reproducible builds; deterministic semantics`, `Meets target SLO/throughput for epic`, `Shadow-run parity with interpreter (where applicable)`
  - **Dependencies:** `5D87D2CD,2C9C95E4,C08BC26A,2962122B,CB9C9B3C,85C66F75,773FF42E,2201FCF0,5930C038`
  - **Created at:** 2025-10-04T18:34:41.528413
