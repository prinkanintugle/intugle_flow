<!-- markdownlint-disable MD030 -->

<h1 align="center">Intugle Flow</h1>

<p align="center">
  <em>A powerful platform for building and deploying AI-powered agents and workflows.</em>
</p>

---

## About

**Intugle Flow** is a distribution of the open-source **Langflow** platform, rebranded and packaged for the Intugle ecosystem. It provides both a visual authoring experience and a built-in API and MCP server that turns every workflow into a tool that can be integrated into applications built on any framework or stack.

Intugle Flow ships with batteries included and supports all major LLMs, vector databases, and a growing library of AI tools.

> Intugle Flow is a derivative work of **[Langflow](https://github.com/langflow-ai/langflow)** (Copyright © 2024 Langflow contributors), licensed under the MIT License. The original `LICENSE` file is preserved unchanged at the root of this repository. See [`NOTICE.md`](./NOTICE.md) for the full attribution and a complete list of modifications made in this distribution.

---

## ✨ Highlights

- **Visual builder interface** to quickly get started and iterate.
- **Source code access** lets you customize any component using Python.
- **Interactive playground** to immediately test and refine your flows with step-by-step control.
- **Multi-agent orchestration** with conversation management and retrieval.
- **Deploy as an API** or export as JSON for Python apps.
- **Deploy as an MCP server** and turn your flows into tools for MCP clients.
- **Observability** with LangSmith, LangFuse, and other integrations.
- **Enterprise-ready** security and scalability.

---

## ⚡️ Quickstart

Intugle Flow retains 100% of the runtime, API, and CLI behavior of upstream Langflow 1.11. All standard install and run methods work unchanged.

### Requirements

- **Python** 3.10 – 3.14
- **Node.js** 20.19 or newer, and **npm** 10.9 or newer (for building the frontend from source)
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** — Python package manager (recommended)

### Option 1 — Run from source (recommended for this repo)

From the repository root:

```bash
make run_cli
```

This installs backend and frontend dependencies, builds the frontend, and starts the app.

Once running, open **http://127.0.0.1:7860** in your browser.

### Option 2 — Development mode with hot reload

In two separate terminals:

```bash
# Terminal 1 — backend
make backend
```

```bash
# Terminal 2 — frontend
make frontend
```

Backend runs on `http://127.0.0.1:7860`, frontend dev server on `http://127.0.0.1:3000` with an API proxy.

### Option 3 — Docker

The underlying container images are the upstream Langflow images:

```bash
docker run -p 7860:7860 langflowai/langflow:latest
```

Available at http://localhost:7860/.

### Option 4 — Install as a Python package

```bash
uv pip install langflow -U
uv run langflow run
```

> ℹ️ The published pip package name and CLI command remain `langflow` (and `langflow run`) to preserve upstream compatibility, security patch upgrade paths, and MCP client configurations already deployed in the field. Only the user-visible product name has been changed to Intugle Flow.

---

## 🧭 Repository Layout

```
.
├── src/
│   ├── backend/            # FastAPI application (langflow-base package)
│   ├── frontend/           # React + Vite + xyflow visual canvas UI
│   ├── lfx/                # Core execution engine (graph runtime, components)
│   ├── bundles/            # 21 vendor-specific integration bundles
│   ├── sdk/                # Python SDK
│   └── langflow-stepflow/  # Step-by-step flow execution
├── docs/                   # Docusaurus documentation site
├── deploy/                 # docker-compose + observability
├── docker/                 # Dockerfiles (dev, base, ep, cdk, render, ...)
├── scripts/                # Utility scripts
├── DESIGN.md               # Full design system spec
├── DEVELOPMENT.md          # Contributor setup guide
├── LICENSE                 # MIT License (upstream Langflow, preserved)
├── NOTICE.md               # Attribution + list of modifications
└── README.md               # This file
```

---

## 🛡️ Security

For security information, see [`SECURITY.md`](./SECURITY.md).

## 🚀 Deployment

Intugle Flow can be deployed to all major cloud providers using the standard Langflow deployment paths (Docker, Render, Kubernetes, IBM watsonx, AWS, etc.). See the [Docker deployment guide](https://docs.langflow.org/deployment-docker) for reference.

## 📄 License

MIT License — see [`LICENSE`](./LICENSE). Intugle Flow is a derivative work of Langflow; see [`NOTICE.md`](./NOTICE.md) for full attribution.

## 👋 Contributing to the upstream project

If you'd like to contribute improvements that should benefit the whole community, we encourage you to send them upstream to the original Langflow project: https://github.com/langflow-ai/langflow

## ❤️ Credits

Intugle Flow stands entirely on the shoulders of the **Langflow** project and its contributors — thank you.

[![langflow contributors](https://contrib.rocks/image?repo=langflow-ai/langflow)](https://github.com/langflow-ai/langflow/graphs/contributors)
