# AI Agent Development Notes

This file contains notes and conventions for developing this project with the help of an AI agent.

# Data & Signal Processing Portfolio

## Project Overview
This repository serves as a landing page/hub linking to project repositories that demonstrate my data and signal processing development capabilities.

### Project Repositories
- **[signal-processing](https://github.com/noamshabtai/signal-processing)** - Real-time signal processing framework with spatial audio demonstration

For technical documentation about the signal processing framework (architecture, modules, development setup, etc.), see the AGENT.md in that repository.

## Repository Structure

```
portfolio/
├── docs/
│   ├── index.md      # Portfolio website (GitHub Pages)
│   └── _config.yml   # Jekyll configuration
├── README.md         # Repository overview
├── AGENT.md          # This file
└── .gitignore
```

## Development Notes

### GitHub Pages
- The portfolio website is served from `docs/index.md`
- Uses Jekyll with GitHub Pages
- Live at: https://noamshabtai.github.io/portfolio/

### Adding New Project Repositories
When adding a new project repository to the portfolio:
1. Create the new repository
2. Update `docs/index.md` to add a section for the new project
3. Update `README.md` to list the new repository
4. Update this file's "Project Repositories" section

## Completed Work

### Portfolio Restructuring ✅
- Restructured portfolio as a hub linking to separate project repositories
- Signal processing code moved to https://github.com/noamshabtai/signal-processing
- CI/CD and branch protection configured on signal-processing repo
- Updated portfolio title to "Data & Signal Processing Development Services"

## Next Steps

### 1. Create data processing repo (when ready)
- New repository demonstrating data processing skills
- First example: Stock Signal Analyzer
  - Apply signal processing techniques to financial time series
  - Filtering (trend extraction), FFT (cyclical patterns), wavelets (multi-scale)
  - Data pipeline: fetch data → feature extraction → ML model → dashboard
- Shows overlap between signal processing expertise and data processing needs
- When created, add to portfolio:
  - Update `docs/index.md` with new section
  - Update `README.md` project list
  - Update this file's "Project Repositories" section
