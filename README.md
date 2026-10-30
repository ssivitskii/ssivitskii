<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img alt="Stepan Sivitskii — Data Scientist at Avito · Platform & Core | Automated Moderation" src="assets/header-light.svg" width="100%">
</picture>

<p align="center">
  <a href="mailto:ssivitskii@outlook.com">Email</a> &nbsp;·&nbsp;
  <a href="https://t.me/ssivitskii">Telegram</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/ssivitskiy">LinkedIn</a>
</p>

I work as a **Data Scientist at Avito**, in **Platform & Core | Automated Moderation**.
My public projects explore search, ranking, classification and scientific ML — with
an emphasis on meaningful baselines, careful validation and understanding model failures.

Previously **ML Developer Intern at Yandex · International Search**, working on
RAG/LLM experiments and evaluation. **ITMO University**, BSc 2024–2028 (expected).

## Selected work

<table>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/ssivitskii/ds-bootcamp-avito">Search &amp; Ranking</a></h3>
<p>TF-IDF + RuBERT retrieval, hard-negative mining and learned reranking.</p>
<p><strong>Recall@50: 0.804 → 0.861</strong> for the first dense version on the same reserved holdout. Later adaptive experiments are documented separately.</p>
<p><a href="https://github.com/ssivitskii/ds-bootcamp-avito/blob/main/docs/experiment-log.md">Read the experiments →</a></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/ssivitskii/FraudGuard">FraudGuard</a></h3>
<p>Imbalanced classification with chronological validation and an explicit review budget.</p>
<p><strong>87.0% recall at a 1% review budget</strong> on the held-out ULB split; average precision 0.751. Frozen model selection and recorded provenance.</p>
<p><a href="https://github.com/ssivitskii/FraudGuard/blob/main/reports/creditcard.json">Inspect the measured report →</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/ssivitskii/SpectraLab">SpectraLab</a></h3>
<p>Scientific ML for atomic spectra: physical simulation, line features and synthetic-to-real transfer.</p>
<p><strong>Micro-F1 0.994 vs 0.493</strong> under a controlled synthetic wavelength shift of 0.75 nm. External measurement studies expose transfer limits.</p>
<p><a href="https://github.com/ssivitskii/SpectraLab/blob/main/docs/line_classifier_v1.md">Read the study →</a></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/ssivitskii/Movie-Recommender">Movie Recommender</a></h3>
<p>Temporal MovieLens benchmark: popularity, item similarity and sparse SVD.</p>
<p><strong>Ranking, coverage and cold-start slices</strong> on future interactions. User-bootstrap intervals make the uncertainty visible.</p>
<p><a href="https://github.com/ssivitskii/Movie-Recommender/blob/main/reports/temporal_ml100k.json">Explore the benchmark →</a></p>
</td>
</tr>
</table>

**More experiments** · [ExperimentLab](https://github.com/ssivitskii/experiment-lab)
— causal inference and uplift; exploratory Criteo pilot ·
[Code Review Evals](https://github.com/ssivitskii/code-review-evals)
— executable fixtures and LLM evaluation; live model benchmark pending ·
[VibroLab](https://github.com/ssivitskii/VibroLab)
— vibration classification under operating-condition shift.

## Open source

[DoubleML #422](https://github.com/DoubleML/doubleml-for-py/pull/422)
— proposed fix for cluster fold counts with externally supplied sample splits.
Pull request open as of October 2026.

## Toolkit

**ML & data** · Python, NumPy, pandas, SciPy, scikit-learn, PyTorch, Sentence Transformers.<br>
**Delivery** · FastAPI, Streamlit, PostgreSQL, Docker, GitHub Actions.

<sub>Public projects are personal work. Reported results belong to the linked datasets and evaluation protocols.</sub>

## Contributions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ssivitskii/ssivitskii/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ssivitskii/ssivitskii/output/github-snake.svg">
  <img alt="Animated snake following my GitHub contribution calendar" src="https://raw.githubusercontent.com/ssivitskii/ssivitskii/output/github-snake.svg" width="100%">
</picture>

<sub>Updated daily · <a href="https://github.com/Platane/snk">Snake animation by Platane</a></sub>
