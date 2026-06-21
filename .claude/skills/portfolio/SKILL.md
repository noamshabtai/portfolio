---
name: portfolio
description: Guidance for working in the data & signal processing portfolio hub
  repo — its purpose, structure, GitHub Pages setup, the linked project repos,
  and how to register a new project repo. Use when editing this repo's site
  (docs/index.md), README, or adding/updating a linked project.
---

# Data & Signal Processing Portfolio

This repository is a landing page / hub linking to project repositories that
demonstrate data and signal processing development capabilities.

## Linked project repositories
- **[signal-processing](https://github.com/noamshabtai/signal-processing)** — Real-time signal processing framework with spatial audio demonstration. Technical docs (architecture, modules, dev setup) live in that repo's AGENT.md.
- **[data-processing](https://github.com/noamshabtai/data-processing)** — Data processing framework with finance demo (depends on signal-processing).

## Repository structure
```
portfolio/
├── docs/
│   ├── index.md      # Portfolio website (GitHub Pages)
│   └── _config.yml   # Jekyll configuration
├── README.md         # Repository overview
└── .gitignore
```

## GitHub Pages
- The site is served from `docs/index.md`, built with Jekyll via GitHub Pages.
- Live at: https://noamshabtai.github.io/portfolio/

## Adding a new project repository
When adding a new project repository to the portfolio:
1. Create the new repository.
2. Add a section for it in `docs/index.md`.
3. List it in `README.md`.
4. Add it to the "Linked project repositories" list above.
