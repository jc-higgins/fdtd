# fdtd
Python Library for use in fdtd.

Taking inspiration from [Electromagnetic Simulation Using the FDTD Method](https://lshoshia.science.tsu.ge/fdtd/Dennissullivan-fixed.pdf). 

## Setup

This project uses [UV](https://docs.astral.sh/uv/) for dependency management and virtual environment handling.

### Prerequisites

- Python 3.12 or higher
- UV package manager (install from [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fdtd
   ```

2. **Create and activate virtual environment**
   ```bash
   uv venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies in editable mode**
   ```bash
   uv pip install -e .
   ```

4. **Install development dependencies (optional)**
   ```bash
   uv pip install -e ".[dev]"
   ```

### Running the Application

After setup, you can run the FDTD application:

```bash
python main.py
```

Or using the module directly:

```bash
python -m fdtd.main
```

### Development

- The main entrypoint is in `fdtd/main.py`
- The graphical application entry point is in `fdtd/qt_app.py`
- The FDTD grid implementation is in `fdtd/grid.py`

