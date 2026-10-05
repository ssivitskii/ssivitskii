<h1 align="center">Stepan Sivitskii</h1>

<p align="center">
  <strong>Software Developer · .NET Backend Focus</strong><br>
  Backend systems, concurrent workflows, and full-stack products — currently focused on C# / .NET.
</p>

<p align="center">
  <a href="mailto:ssivitskii@outlook.com"><img alt="Email" src="https://img.shields.io/badge/Email-ssivitskii%40outlook.com-0A66C2?style=flat-square&logo=microsoftoutlook&logoColor=white"></a>
  <a href="https://t.me/ssivitskii"><img alt="Telegram" src="https://img.shields.io/badge/Telegram-@ssivitskii-26A5E4?style=flat-square&logo=telegram&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/ssivitskiy"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-ssivitskiy-0A66C2?style=flat-square&logo=linkedin&logoColor=white"></a>
</p>

## About

I am a software developer and ITMO University student, currently focused on backend development with C# / .NET. I build systems where correctness matters: transactional updates, idempotent operations, concurrent processing, authorization, and integration testing.

My main stack is **C# / .NET, ASP.NET Core, EF Core, PostgreSQL, and Docker**. I also work with **Go, Java, C++, Python, and TypeScript**, build full-stack products with Angular, and have practical experience with RAG/LLM experimentation from an ML internship at Yandex.

## Experience

**Yandex — ML Developer Intern** · Jul 2026 - Oct 2026<br>
Neural distribution group, international search

- Prepared data and reproducible experimental pipelines for RAG/LLM systems.
- Analyzed model quality and failure cases and automated experiments.

**[Bon Voyage Travel](https://bonvoyagetravel.online) — Full-stack Developer (.NET / Angular)**

- Built a passenger transportation platform with an ASP.NET Core 10 API, EF Core/PostgreSQL, an Angular 22 public site, and a CRM.
- Implemented Identity, RBAC, audit, routes, trips, fleet and seat layouts, fares, search, seat holds, and booking workflows.
- Protected bookings from race conditions with PostgreSQL transactions and locking, covered by concurrent integration and E2E scenarios.

## Selected projects

| Project | Engineering focus |
|---|---|
| **[Bank Account Management API](https://github.com/ssivitskii/BankAccountManagement)** | ASP.NET Core banking API with atomic transfers, PostgreSQL row-level locking, idempotency, JWT/ownership authorization, and Testcontainers integration tests. |
| **[Notification Routing Service](https://github.com/ssivitskii/NotificationRoutingService)** | Asynchronous delivery through bounded `Channel<T>` and `BackgroundService`, with retries, dead letters, idempotency keys, and webhooks. |
| **[FileFlow CLI](https://github.com/ssivitskii/FileFlow)** | Safe filesystem operations with immutable plans, `--dry-run`, a JSONL journal, transaction-scoped trash, conflict-aware undo, and SHA-256 duplicate detection. |
| **[Bon Voyage](https://github.com/ssivitskii/BonVoyage)** | Full-stack transportation and booking system built as a .NET 10 modular monolith with Angular 22 public and CRM applications. |

## Open-source contributions

- **[NethermindEth/dotnet-libp2p #302](https://github.com/NethermindEth/dotnet-libp2p/pull/302)** — merged: enforced Kad-DHT request/response size limits, rejected oversized and overflowing frames, and added regression coverage.
- **[microcks/microcks-testcontainers-dotnet #286](https://github.com/microcks/microcks-testcontainers-dotnet/pull/286)** — merged: fixed ownership-aware Docker network disposal and covered both internal and caller-owned network paths.
- **[Azure/bicep #20357](https://github.com/Azure/bicep/pull/20357)** — open, awaiting maintainer review: added a dedicated diagnostic and regression tests for multi-document YAML streams.

## Technical toolkit

| Area | Technologies |
|---|---|
| Languages | C#, Go, Java, C++, Python, TypeScript |
| Backend | C#, .NET 9/10, ASP.NET Core Web API, EF Core, LINQ, dependency injection, `BackgroundService`, `IHttpClientFactory` |
| Data | PostgreSQL, SQL, Redis, Npgsql, migrations, transactions, isolation and row-level locking |
| Testing | xUnit, WebApplicationFactory, Testcontainers, Playwright, unit/integration/E2E testing |
| API & security | REST, OpenAPI, JWT/cookie authentication, RBAC, ownership authorization, idempotency, Problem Details |
| Delivery | Docker, Docker Compose, GitHub Actions, CI/CD, structured logging, health checks |
| Frontend | Angular, TypeScript, RxJS, Reactive Forms |

## Education

**ITMO University** · 2024 - 2028 (expected)<br>
BSc, Information Systems and Technologies

<p align="center">
  <a href="https://github.com/ssivitskii?tab=repositories"><strong>Explore all repositories</strong></a>
  &nbsp;·&nbsp;
  <a href="mailto:ssivitskii@outlook.com"><strong>Get in touch</strong></a>
</p>
