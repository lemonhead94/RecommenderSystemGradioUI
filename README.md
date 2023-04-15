# Recommender System Gradio Interface

## Local

### Installation

```bash
conda create -n py39 python=3.9
conda activate py39
python -m venv .venv && source .venv/bin/activate
poetry install
pre-commit install
```

### Launching the App

```bash
python recommender_ui/app.py
```

## Container Image

### Docker Build

```bash
docker build -t recommender_ui .
```

### Docker Run

```bash
docker run -it -p 7860:7860 recommender_ui
```