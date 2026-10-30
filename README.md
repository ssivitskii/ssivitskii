<a id="top"></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img alt="Stepan Sivitskii — Data Scientist at Avito · Platform & Core | Automated Moderation" src="assets/header-light.svg" width="100%">
</picture>

<p align="center">
  <a href="#user-content-about">About</a> &nbsp;·&nbsp;
  <a href="#user-content-current-focus">Focus</a> &nbsp;·&nbsp;
  <a href="#user-content-selected-work">Projects</a> &nbsp;·&nbsp;
  <a href="#user-content-open-source">Open source</a> &nbsp;·&nbsp;
  <a href="#user-content-mlds-stack">Stack</a> &nbsp;·&nbsp;
  <a href="#user-content-contact">Contact</a>
</p>

## About

I work as a **Data Scientist at Avito**, in **Platform & Core | Automated Moderation**.
My public projects explore search, ranking, classification and scientific ML — with
an emphasis on meaningful baselines, careful validation and understanding model failures.

Previously **ML Developer Intern at Yandex · International Search**, working on
RAG/LLM experiments and evaluation. **ITMO University**, BSc 2024–2028 (expected).

## Current focus

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/focus/dark-mobile.svg">
  <source media="(max-width: 600px)" srcset="assets/focus/light-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/focus/dark.svg">
  <img src="assets/focus/light.svg" width="100%" alt="Current focus — At work: Automated Moderation at Avito, Platform &amp; Core. Public projects: Search &amp; Ranking. Research: Scientific ML, atomic spectra and instrument shift.">
</picture>

## Selected work

<a href="https://github.com/ssivitskii/ds-bootcamp-avito">
  <picture>
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/projects/search-dark-mobile.svg">
    <source media="(max-width: 600px)" srcset="assets/projects/search-light-mobile.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/projects/search-dark.svg">
    <img src="assets/projects/search-light.svg" width="100%" alt="Search &amp; Ranking: 0.861 Recall@50. 0.804 baseline · +5.69 percentage points. First dense model · 1,200 held-out queries. Later adaptive runs are reported separately.">
  </picture>
</a>

<a href="https://github.com/ssivitskii/FraudGuard">
  <picture>
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ssivitskii/ssivitskii/3069b01207f59c029362dc8cbac5a33532bd28a6/assets/projects/fraud-dark-mobile.svg">
    <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/ssivitskii/ssivitskii/3069b01207f59c029362dc8cbac5a33532bd28a6/assets/projects/fraud-light-mobile.svg">
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ssivitskii/ssivitskii/3069b01207f59c029362dc8cbac5a33532bd28a6/assets/projects/fraud-dark.svg">
    <img src="https://raw.githubusercontent.com/ssivitskii/ssivitskii/3069b01207f59c029362dc8cbac5a33532bd28a6/assets/projects/fraud-light.svg" width="100%" alt="FraudGuard: 0.6634 average precision on the Elliptic test versus 0.6337 for the local baseline. Offline AML on completed Bitcoin graph snapshots, test steps 40–49. At a 1% review budget on the labelled cohort, all variants find 112 of 636 illicit cases.">
  </picture>
</a>

<a href="https://github.com/ssivitskii/SpectraLab">
  <picture>
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/projects/spectra-dark-mobile.svg">
    <source media="(max-width: 600px)" srcset="assets/projects/spectra-light-mobile.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/projects/spectra-dark.svg">
    <img src="assets/projects/spectra-light.svg" width="100%" alt="SpectraLab: 0.994 Micro-F1 at 0.75 nm synthetic drift. 0.493 baseline · five matched seeds. Controlled synthetic study. Transfer to real instruments is evaluated separately.">
  </picture>
</a>

<a href="https://github.com/ssivitskii/Movie-Recommender">
  <picture>
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/projects/movies-dark-mobile.svg">
    <source media="(max-width: 600px)" srcset="assets/projects/movies-light-mobile.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/projects/movies-dark.svg">
    <img src="assets/projects/movies-light.svg" width="100%" alt="Movie Recommender: 17.0% Catalog coverage@10 · sparse SVD. NDCG@10 0.277 · MovieLens 100K. Future-time holdout. Single-split offline results; no claim of online engagement lift.">
  </picture>
</a>

Evaluation details: [Search & Ranking](https://github.com/ssivitskii/ds-bootcamp-avito/blob/main/docs/experiment-log.md) · [FraudGuard · Elliptic](https://github.com/ssivitskii/FraudGuard/blob/main/reports/elliptic.json) · [SpectraLab](https://github.com/ssivitskii/SpectraLab/blob/main/docs/line_classifier_v1.md) · [Movie Recommender](https://github.com/ssivitskii/Movie-Recommender/blob/main/reports/temporal_ml100k.json).

**More experiments** · [ExperimentLab](https://github.com/ssivitskii/experiment-lab)
— causal inference and uplift; exploratory Criteo pilot ·
[Code Review Evals](https://github.com/ssivitskii/code-review-evals)
— executable fixtures and LLM evaluation; live model benchmark pending ·
[VibroLab](https://github.com/ssivitskii/VibroLab)
— vibration classification under operating-condition shift.

## Open source

[DoubleML #422](https://github.com/DoubleML/doubleml-for-py/pull/422)
— fixed cluster fold counts with externally supplied sample splits.
**Merged on October 30, 2026.**

<a id="toolkit"></a>

## ML/DS stack

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/stack/dark-mobile.svg">
  <source media="(max-width: 600px)" srcset="assets/stack/light-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack/dark.svg">
  <img src="assets/stack/light.svg" width="100%" alt="ML/DS stack: Python, NumPy, pandas, SciPy, scikit-learn, PyTorch, Hugging Face, Plotly, FastAPI, Streamlit, PostgreSQL and Docker.">
</picture>

**NLP** · Transformers · Sentence Transformers.<br>
**Visualization** · Matplotlib · Seaborn.<br>
**Development** · Git · GitHub Actions · pytest.

<sub>Public projects are personal work. Reported results belong to the linked datasets and evaluation protocols.</sub>

## Contributions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ssivitskii/ssivitskii/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ssivitskii/ssivitskii/output/github-snake.svg">
  <img alt="Animated snake following my GitHub contribution calendar" src="https://raw.githubusercontent.com/ssivitskii/ssivitskii/output/github-snake.svg" width="100%">
</picture>

<sub>Updated daily · <a href="https://github.com/Platane/snk">Snake animation by Platane</a></sub>


## Contact

<a href="mailto:ssivitskii@outlook.com">
  <picture>
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/contact/dark-mobile.svg">
    <source media="(max-width: 600px)" srcset="assets/contact/light-mobile.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/contact/dark.svg">
    <img src="assets/contact/light.svg" width="100%" alt="Contact Stepan Sivitskii — ML research, open source and project ideas. Email ssivitskii@outlook.com.">
  </picture>
</a>

<p align="center">
  <a href="mailto:ssivitskii@outlook.com">Email</a> &nbsp;·&nbsp;
  <a href="https://t.me/ssivitskii">Telegram</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/ssivitskiy">LinkedIn</a>
</p>

<p align="center"><a href="#user-content-top">Back to top ↑</a></p>
