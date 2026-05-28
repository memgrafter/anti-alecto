---
url: https://docs.swarms.world/en/latest/swarms/install/install/
title: Swarms install docs
scraped_at: '2026-04-25T05:14:13Z'
word_count: 470
raw_file: raw/2026-04-25_swarms-install-docs_1aeacf8f.txt
tldr: Swarms install docs show multiple ways to set up the project in a Python 3.10+ environment—via pip, UV, Poetry, Anaconda, Docker, Kubernetes, and CI/CD pipelines—with a strong emphasis on reproducible deployments and the Rust implementation link at the end.
key_quote: Docker is an excellent option for creating isolated and reproducible environments, suitable for both development and production.
durability: medium
content_type: mixed
density: medium
originality: primary
reference_style: refer-back
scrape_quality: partial
people:
- kyegomez
tools:
- pip
- uv
- Poetry
- Anaconda
- Docker
- Kubernetes
- GitHub Actions
- Jenkins
- pytest
- git
libraries:
- swarm-models
- swarms
companies: []
tags:
- python-installation
- deployment
- containerization
- ci-cd
- reproducible-environments
---

### TL;DR
Swarms install docs show multiple ways to set up the project in a Python 3.10+ environment—via pip, UV, Poetry, Anaconda, Docker, Kubernetes, and CI/CD pipelines—with a strong emphasis on reproducible deployments and the Rust implementation link at the end.

### Key Quote
“Docker is an excellent option for creating isolated and reproducible environments, suitable for both development and production.”

### Summary
- **What this page is:** An installation guide for the Swarms project, covering prerequisites and several environment/deployment options.
- **Prerequisites:**
  - Python **3.10 or higher**
  - `pip >= 21.0`
  - `git` for cloning the repository
- **Simple installation:**
  - The docs say the simplest method is installing with **pip**
  - They also recommend **UV** for faster installs and better dependency resolution
  - **Poetry** is mentioned as a more robust dependency/environment management tool
- **Environment/setup options mentioned:**
  - **Clone repository** and navigate to the root directory
  - **Set up and activate a Python environment**
  - **Install Swarms**
  - Separate paths are listed for **headless install** and **desktop install**
- **Anaconda option:**
  - Create and activate an **Anaconda** environment
  - Clone the repository
  - Install Swarms
  - Separate headless and desktop install steps are again referenced
- **Docker installation:**
  - Recommended as an isolated, reproducible environment for development and production
  - The page mentions:
    - pulling a Docker image
    - running a container
    - building and running a custom image
  - The included Dockerfile snippet uses:
    - `FROM python:3.11-slim`
    - environment variables like `PYTHONDONTWRITEBYTECODE=1`, `PYTHONUNBUFFERED=1`, `WORKSPACE_DIR="agent_workspace"`, and `OPENAI_API_KEY="your_swarm_api_key_here"`
    - system packages: `build-essential`, `gcc`, `g++`, `gfortran`
    - `pip3 install -U swarm-models`
    - `pip3 install -U swarms`
- **Kubernetes:**
  - Briefly notes Kubernetes as a way to deploy, scale, and manage containerized applications
  - Mentions:
    - creating a **Deployment YAML**
    - applying the deployment
    - exposing the deployment
- **CI/CD integration:**
  - Says integrating Swarms into CI/CD enables automated testing and deployment
  - **GitHub Actions** example:
    - runs on push and pull request to `main`
    - checks out code
    - sets up Python 3.10
    - creates a virtualenv
    - installs the project with `pip install -e .`
    - runs `pytest`
  - **Jenkins** example:
    - clones `https://github.com/kyegomez/swarms.git`
    - creates a virtualenv
    - upgrades pip
    - installs editable dependencies with `pip install -e .`
    - runs `pytest`
- **Rust:**
  - The page closes by pointing to the **Rust implementation of Swarms** and says to get started with the docs there

### Assessment
This is a **reference / tutorial** page with **medium durability**: the installation patterns are fairly reusable, but specific commands, package versions, and setup recommendations may change as Swarms evolves. The content is **mixed** because it combines install guidance, deployment examples, and CI/CD snippets. Density is **medium**: there are useful concrete details, but the scrape appears incomplete and somewhat fragmented—several sections read like headings or placeholders without full step-by-step commands, and some code blocks/formatting may be missing. It looks like **primary documentation** from the project rather than commentary or synthesis. Best used as a **refer-back** page for installation options and deployment workflow reminders rather than deep study.
