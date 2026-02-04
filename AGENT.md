# AI Agent Development Notes

This file contains notes and conventions for developing this project with the help of an AI agent.

# Data & Signal Processing Portfolio

## Project Overview
This repository serves as a landing page/hub linking to project repositories that demonstrate my data and signal processing development capabilities.

### Project Repositories
- **[signal-processing](https://github.com/noamshabtai/signal-processing)** - Real-time signal processing framework with spatial audio demonstration
- **[data-processing](https://github.com/noamshabtai/data-processing)** - Data processing framework with finance demo (depends on signal-processing)

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

### Data Processing Repository ✅
- Phase A: Extracted base_demo activator class in signal-processing (PR #3, #4)
- Phase B: Created data-processing repo with finance demo
  - data-fetcher: yfinance data retrieval
  - feature-extraction: trend and FFT extractors
  - model: LSTM PyTorch model
  - finance-demo: inherits from signal-processing base_demo
  - stock-analyzer: CLI entry point
- Repo: https://github.com/noamshabtai/data-processing

## Reference

### Data Processing Repository Plan (Completed)

Two-phase approach:
1. **Phase A**: Refactor signal-processing to extract a `DemoActivator` base class ✅
2. **Phase B**: Create data-processing repo that depends on signal-processing ✅

---

## Phase A: Refactor signal-processing (new branch)

### Goal
Extract a `DemoActivator` base class from `audio_demo.py` that can be inherited by both audio and finance demos.

### Branch: `feature/demo-base-class`

### TDD Approach - Tests First

#### Step 1: Write tests for the new DemoActivator base class
```python
# activator/tests/test_demo_base.py
def test_demo_activator_has_running_flag(kwargs_demo_base):
    """DemoActivator should have a running flag initialized to False"""

def test_demo_activator_stop_sets_running_false(kwargs_demo_base):
    """stop() should set running to False"""

def test_demo_activator_process_frame_calls_system_execute(kwargs_demo_base, mocker):
    """process_frame() should call system.execute() and return last output"""
```

#### Step 2: Write YAML config for demo base tests
```yaml
# activator/tests/config/demo_base.yaml
base:
  system:
    input_buffer:
      step_size: 10
      buffer_size: 50
      channel_shape: [1]
      dtype: float32

cases:
  - name: basic demo base
```

#### Step 3: Implement DemoActivator base class
```python
# activator/src/activator/demo_base.py
import abc
from . import base

class DemoActivator(base.Activator):
    """Base class for continuous/streaming demos (audio, finance, etc.)"""

    def __init__(self, activated_system, **kwargs):
        super().__init__(activated_system, **kwargs)
        self.running = False

    def process_frame(self, data):
        """Process one frame through the system, return last module's output."""
        self.system.execute(data)
        if self.system.outputs:
            output_key = list(self.system.outputs.keys())[-1]
            return self.system.outputs[output_key]
        return None

    def stop(self):
        """Stop the demo gracefully."""
        self.running = False

    @abc.abstractmethod
    def execute(self):
        """Run the demo. Subclasses implement their timing mechanism."""
        pass

    @abc.abstractmethod
    def cleanup(self):
        """Clean up resources."""
        pass
```

#### Step 4: Update audio_demo.py to inherit from DemoActivator
```python
# activator/src/activator/audio_demo.py
from . import demo_base  # Changed from base

class Activator(demo_base.DemoActivator):  # Changed parent
    def __init__(self, activated_system, **kwargs):
        super().__init__(activated_system, **kwargs)
        # ... rest stays the same

    def audio_callback(self, in_data, frame_count, time_info, status):
        # ...
        # Change: use self.process_frame() instead of direct system.execute()
        output_data = self.process_frame(data)
        # ...
```

#### Step 5: Verify existing audio_demo tests still pass

### Files to modify in signal-processing:
- `activator/src/activator/demo_base.py` (new)
- `activator/src/activator/audio_demo.py` (update inheritance)
- `activator/src/activator/__init__.py` (export demo_base)
- `activator/tests/config/demo_base.yaml` (new)
- `activator/tests/test_demo_base.py` (new)
- `activator/tests/conftest.py` (add demo_base fixture)

### Verification for Phase A:
```bash
cd ~/version_control/signal-processing
git checkout -b feature/demo-base-class
# Make changes
uv run pytest  # All tests pass including new ones
uv run pre-commit run --all-files
git commit
# Create PR, merge to main
```

---

## Phase B: Create data-processing repository

### data-processing depends on signal-processing
```toml
# pyproject.toml
[project]
dependencies = [
    "signal-processing @ git+https://github.com/noamshabtai/signal-processing.git",
]
```

### Repository Structure
```
data-processing/
├── .github/workflows/test.yml
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version              # 3.12
├── pyproject.toml               # Depends on signal-processing
├── uv.lock
├── AGENT.md
├── README.md
│
├── parametrize-tests/           # Copy from signal-processing (or depend on it)
│
├── data-fetcher/                # yfinance data retrieval
│   ├── pyproject.toml
│   ├── src/data_fetcher/
│   │   ├── __init__.py
│   │   └── fetcher.py
│   └── tests/
│       ├── config/fetcher.yaml
│       ├── conftest.py
│       └── test_fetcher.py
│
├── feature-extraction/          # Signal processing features for finance
│   ├── pyproject.toml
│   ├── src/feature_extraction/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── trend.py
│   │   ├── fft.py
│   │   ├── wavelet.py
│   │   └── pipeline.py
│   └── tests/
│
├── model/                       # PyTorch model
│   ├── pyproject.toml
│   ├── src/model/
│   │   ├── __init__.py
│   │   ├── lstm.py
│   │   ├── trainer.py
│   │   └── predictor.py
│   └── tests/
│
├── finance-demo/                # Finance demo inheriting from DemoActivator
│   ├── pyproject.toml
│   ├── src/finance_demo/
│   │   ├── __init__.py
│   │   ├── system.py            # StockAnalyzerSystem (uses signal-processing System)
│   │   └── demo.py              # FinanceDemoActivator (inherits DemoActivator)
│   └── tests/
│       ├── config/
│       │   └── finance_demo.yaml
│       ├── conftest.py
│       └── test_finance_demo.py
│
└── stock-analyzer/              # CLI entry point
    ├── pyproject.toml
    └── src/stock_analyzer/
        └── cli.py
```

### Finance Demo (inherits from signal-processing DemoActivator)
```python
# finance-demo/src/finance_demo/demo.py
from activator.demo_base import DemoActivator
import time

class FinanceDemoActivator(DemoActivator):
    """Polling-based demo for stock predictions."""

    def __init__(self, activated_system, **kwargs):
        super().__init__(activated_system, **kwargs)
        self.fetcher = StockDataFetcher(**kwargs["input"])
        self.poll_interval = kwargs.get("poll_interval", 60)

    def execute(self):
        """Polling loop - fetch latest data and predict."""
        self.running = True
        while self.running:
            frame = self.fetcher.fetch_latest()
            if frame is not None:
                prediction = self.process_frame(frame)  # Uses base class method
                if prediction is not None:
                    self._log_prediction(frame, prediction)
            time.sleep(self.poll_interval)
        self.completed = True

    def cleanup(self):
        self.running = False
        # Close any open connections

    def _log_prediction(self, frame, prediction):
        # Log to console with formatting
        pass
```

### System (uses signal-processing System base)
```python
# finance-demo/src/finance_demo/system.py
from system.system import System  # From signal-processing

class StockAnalyzerSystem(System):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.modules["features"] = FeaturePipeline(**kwargs["features"])
        self.modules["predictor"] = Predictor(**kwargs["predictor"])

    def connect(self, module):
        match module:
            case "features":
                self.inputs[module] = dict(data=self.input_buffer.get_window())
            case "predictor":
                self.inputs[module] = dict(features=self.outputs["features"])
```

### TDD Approach for Phase B

#### For each module, write tests FIRST:

1. **data-fetcher tests first:**
```yaml
# data-fetcher/tests/config/fetcher.yaml
base:
  symbol: AAPL
  period: 7d
  interval: 1h

cases:
  - name: fetch historical data
  - name: fetch latest single point
  - name: handle invalid symbol
    symbol: INVALID_SYMBOL_XYZ
    expect_error: true
```

```python
# data-fetcher/tests/test_fetcher.py
def test_fetch_historical_returns_dataframe(kwargs_fetcher):
    """Should return DataFrame with OHLCV columns"""

def test_fetch_historical_has_expected_columns(kwargs_fetcher):
    """DataFrame should have open, high, low, close, volume"""

def test_fetch_latest_returns_dict(kwargs_fetcher):
    """Should return dict with latest price data"""
```

2. **feature-extraction tests first:**
```python
# feature-extraction/tests/test_features.py
def test_trend_extractor_output_shape(kwargs_features):
    """TrendExtractor output dim should match expected"""

def test_fft_extractor_detects_periodic_signal(kwargs_features):
    """FFT should identify dominant frequency in synthetic periodic data"""

def test_pipeline_concatenates_all_features(kwargs_features):
    """Pipeline output should be concatenation of all extractors"""
```

3. **model tests first:**
```python
# model/tests/test_model.py
def test_lstm_forward_shape(kwargs_model):
    """LSTM output shape should be (batch, output_dim)"""

def test_trainer_reduces_loss(kwargs_model):
    """Training should reduce loss over epochs"""

def test_predictor_returns_numpy(kwargs_model):
    """Predictor should return numpy array"""
```

4. **finance-demo tests first:**
```python
# finance-demo/tests/test_finance_demo.py
def test_finance_demo_inherits_demo_activator(kwargs_finance_demo):
    """FinanceDemoActivator should be instance of DemoActivator"""

def test_finance_demo_uses_process_frame(kwargs_finance_demo, mocker):
    """Should use inherited process_frame() method"""

def test_finance_demo_stops_on_stop(kwargs_finance_demo):
    """stop() should set running=False and exit loop"""
```

---

## Implementation Order

### Phase A: signal-processing refactor
1. Create branch `feature/demo-base-class`
2. Write `test_demo_base.py` tests (TDD - tests first)
3. Write `demo_base.yaml` config
4. Implement `demo_base.py`
5. Update `audio_demo.py` to inherit from DemoActivator
6. Run all tests, verify nothing broke
7. PR and merge to main

### Phase B: data-processing repo
1. Create repo, set up workspace with signal-processing dependency
2. Copy parametrize-tests (or add as dependency)
3. Set up pre-commit, CI/CD

4. **data-fetcher (TDD)**
   - Write tests first
   - Write YAML config
   - Implement fetcher.py

5. **feature-extraction (TDD)**
   - Write tests first for each extractor
   - Implement base.py, trend.py, fft.py, wavelet.py, pipeline.py

6. **model (TDD)**
   - Write tests first
   - Implement lstm.py, trainer.py, predictor.py

7. **finance-demo (TDD)**
   - Write tests first
   - Implement system.py (inherits from signal-processing System)
   - Implement demo.py (inherits from signal-processing DemoActivator)

8. **stock-analyzer CLI**
   - Implement cli.py with train/predict commands

9. **Portfolio updates**
   - Update portfolio/AGENT.md, README.md, docs/index.md

---

## Verification

### Phase A:
```bash
cd ~/version_control/signal-processing
git checkout feature/demo-base-class
uv run pytest -v
uv run pre-commit run --all-files
# All tests pass, including new demo_base tests and existing audio_demo tests
```

### Phase B:
```bash
cd ~/version_control/data-processing
uv run pytest -v
uv run pre-commit run --all-files
uv run stock-analyzer train --symbol AAPL --period 1y --epochs 10 --output model.pt
uv run stock-analyzer predict --symbol AAPL --model model.pt --simulate
```
