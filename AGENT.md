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

## TODO: Portfolio Restructuring

Based on feedback from industry contacts, broaden the portfolio from pure "signal processing" to include "data processing" to appeal to a wider market.

### Tasks

1. **Restructure portfolio as a hub** ✅
   - Portfolio becomes a landing page linking to separate project repositories
   - `index.md` links to signal processing repo
   - Signal processing code moved to https://github.com/noamshabtai/signal-processing

2. **Signal processing repo** ✅
   - Moved `signal_processing/` to its own repository
   - Portfolio links to it as a demonstration project
   - CI/CD and branch protection configured

3. **Create data processing repo** (skipped for now)
   - New repository demonstrating data processing skills
   - First example: Stock Signal Analyzer
     - Apply signal processing techniques to financial time series
     - Filtering (trend extraction), FFT (cyclical patterns), wavelets (multi-scale)
     - Data pipeline: fetch data → feature extraction → ML model → dashboard
   - Shows overlap between signal processing expertise and data processing needs

4. **Update portfolio messaging** ✅
   - Updated title to "Data & Signal Processing Development Services"
   - Ready to add data processing projects when available
