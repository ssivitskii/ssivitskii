# Stepan Sivitskii

### Data Scientist · Applied Machine Learning

**Avito · Platform & Core** — Data Scientist, since October 2026.<br>
Previously **Yandex · International Search**. ITMO University, BSc 2024–2028 (expected).

[Email](mailto:ssivitskii@outlook.com) · [Telegram](https://t.me/ssivitskii) · [LinkedIn](https://www.linkedin.com/in/ssivitskiy)

## About

My public work explores **search and ranking, recommendation systems, tabular ML,
causal inference and scientific signals**. I care about meaningful baselines,
data leakage, reproducible experiments and understanding where models fail.
My software engineering background helps me turn experiments into usable tools.

## Experience

**Avito — Data Scientist**<br>
Platform & Core · **Oct 2026 — Present**

**Yandex — ML Developer Intern**<br>
Neural distribution group, International Search · **Jul 2026 — Oct 2026**

- Prepared data and reproducible experimental pipelines for RAG/LLM systems.
- Analyzed model quality and failure cases; automated evaluation experiments.

## Selected work

Each repository documents its data, evaluation protocol and limitations.
Public portfolio projects are separate from employers' internal systems.

| Project | What to look at |
| --- | --- |
| **[Marketplace Search & Ranking](https://github.com/ssivitskii/ds-bootcamp-avito)** | TF-IDF + fine-tuned RuBERT, hard-negative mining and gradient-boosted reranking. Query-group holdouts, ablations and error slices. |
| **[SpectraLab](https://github.com/ssivitskii/SpectraLab)** | Physical simulation, multi-label classification and synthetic-to-real evaluation. Grouped experiments and explicit separation of development, replay and independent validation. |
| **[Movie Recommender](https://github.com/ssivitskii/Movie-Recommender)** | MovieLens temporal benchmark: popularity, item similarity and sparse SVD; ranking metrics, coverage and cold/warm user slices. |
| **[ExperimentLab](https://github.com/ssivitskii/experiment-lab)** | Treatment effects, S/T-learners, uplift curves and validation-selected targeting policies. Explicit distinction between benchmark utility and assumed financial scenarios. |
| **[FraudGuard](https://github.com/ssivitskii/FraudGuard)** | Imbalanced classification, chronological transaction holdouts, average precision and review-budget metrics. |
| **[Code Review Evals](https://github.com/ssivitskii/code-review-evals)** | A curated executable bug/fix dataset and an LLM evaluation harness for findings, false positives, latency and provider usage. Live model benchmark results are not yet available. |

Also: [Cold-start Recommendation Lab](https://github.com/ssivitskii/cold-start-recsys)
provides a MIND evaluation pipeline and text/two-tower baselines; actual MIND
results await data access. [VibroLab](https://github.com/ssivitskii/VibroLab)
examines vibration classification and the gap between random-window and
operating-condition holdouts.

## Toolkit

**Modeling:** Python, NumPy, pandas, SciPy, scikit-learn, PyTorch,
Sentence Transformers.<br>
**Delivery:** FastAPI, Streamlit, PostgreSQL, Docker, GitHub Actions.

<details>
<summary><strong>Software engineering & open source</strong></summary>

**[Bon Voyage Travel](https://bonvoyagetravel.online)** — full-stack development
with ASP.NET Core, PostgreSQL and Angular: booking workflows, role-based access
and transaction-safe seat reservations, with integration and E2E coverage.

Selected contributions:

- [NethermindEth/dotnet-libp2p #302](https://github.com/NethermindEth/dotnet-libp2p/pull/302) — Kad-DHT frame limits and regression coverage.
- [microcks/microcks-testcontainers-dotnet #286](https://github.com/microcks/microcks-testcontainers-dotnet/pull/286) — ownership-aware Docker network disposal.
- [Azure/bicep #20357](https://github.com/Azure/bicep/pull/20357) — diagnostics for multi-document YAML streams.

</details>
