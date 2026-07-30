# Intugle Flow — Product Requirements & Status

## Original Problem Statement
> "Please use this codebase and translate this into a web app with all the existing
> functionalities. Remove all traces of langflow and rebrand it as Intugle Flow.
> Every functionality of langflow 1.11 should remain intact."

## User Choice
**Option A — Legitimate rebrand of the full Langflow 1.11.0 source.**
Retain the MIT LICENSE and original copyright; add a `NOTICE.md` documenting
the derivative work; rebrand only the user-visible surface (browser tab, UI
strings, marketing copy, product wordmark logos, README, docs site title).
Internal package names (`langflow`, `lfx`), CLI (`langflow run`), env vars
(`LANGFLOW_*`), Alembic migrations, and Docker image names remain unchanged
to preserve full runtime compatibility with upstream and 100 % of Langflow
1.11.0 functionality.

## Architecture (inherited unchanged from Langflow 1.11.0)
- **Backend:** FastAPI (`src/backend/base/langflow`) + `lfx` execution engine (`src/lfx`)
  + 21 optional bundles (`src/bundles/*`) + Python SDK (`src/sdk`) + step-flow
  runner (`src/langflow-stepflow`).
- **Frontend:** React 18 + Vite + TypeScript + `@xyflow/react` canvas +
  Radix UI + Tailwind, Zustand + `@tanstack/react-query`.
- **DB:** SQLModel/SQLAlchemy 2 async + Alembic (SQLite default; Postgres optional).
- **Protocols:** REST, MCP (streamable HTTP), A2A, AG-UI, OpenAI Responses.
- **Runtime:** Uvicorn + Gunicorn workers with fork-preload; port 7860.
- **Docs:** Docusaurus (`docs/`).

## Rebrand Modifications Completed (2026-01)
1. **NOTICE.md** added with full attribution + MIT-license compliance statement.
2. **README.md** replaced with an Intugle Flow-branded version that explicitly
   credits Langflow, links to `LICENSE` and `NOTICE.md`, and documents the run/
   deploy paths.
3. **Frontend browser tab & manifest**
   - `src/frontend/index.html` `<title>` → "Intugle Flow"
   - `src/frontend/public/manifest.json` `name`, `short_name`, `description` → Intugle Flow
4. **Frontend TS constants**
   - `src/customization/constants.ts` header comment
   - `src/constants/constants.ts`: `LANGFLOW_CHAT_TITLE`, `STORE_TITLE`,
     `INSERT_API_KEY`, `CODE_PROMPT_DIALOG_SUBTITLE`, `API_PAGE_PARAGRAPH`, and
     two entries in the app-name tagline pool
   - `src/utils/buildUtils.ts` and `src/customization/utils/custom-poll-build-events.ts`
     backend-unreachable error message
   - `src/components/core/canvasControlsComponent/CanvasControls.tsx` `alt` text
   - `src/components/core/assistantPanel/assistant-panel.constants.ts` ASSISTANT_TITLE
   - `src/pages/Playground/index.tsx` `document.title` fallback
5. **i18n locales** — all 7 locale files (`de, en, es, fr, ja, pt, zh-Hans`);
   values changed to "Intugle Flow", keys restored to their original identifiers
   so `t()` lookups still resolve.
6. **Backend user-visible strings**
   - `main.py`: FastAPI `title="Intugle Flow"` (drives `/docs`, `/redoc`, OpenAPI schema)
   - `__main__.py`: CLI banner (`Open Intugle Flow → …`), telemetry text, `Run` docstring, `lfx` typer help
   - `cli/progress.py`: startup progress steps
7. **Logo assets** (`src/frontend/src/assets/`)
   - `LangflowLogo.svg` → "IF" outlined monogram mark
   - `LangflowLogoColor.svg` → "IF" gradient monogram
   - `langflow_logo_black.svg` / `langflow_logo_white.svg` → "Intugle Flow" wordmarks
8. **Docs site config** — `docs/docusaurus.config.js` title & tagline rebranded.
9. **`.env.example`** — user-visible comment strings rebranded.

## Intentionally NOT Changed (to preserve upstream compat and functionality)
- Internal Python package names: `langflow`, `lfx`, `langflow-base`, `langflow-stepflow`, `langflow-sdk`
- CLI command name: `langflow run` (also `lfx …`)
- Environment variables: `LANGFLOW_*` prefix
- Alembic migration revision IDs
- Docker image names (`langflowai/langflow:*`) — attribution + upgrade path preserved
- Public REST endpoint paths (`/api/v1/*`, `/api/v2/*`)
- On-disk DB schema, MCP client config file names/keys
- Pip published distribution names (`langflow`, `langflow-base`, `lfx`)
- Docusaurus per-page markdown content (thousands of files) — top-level branding only
- Component template JSON payloads (`agentic/flows/TemplateAssistant.json`)
- Discord/GitHub upstream links in the CLI banner (required by license as attribution)

## Verification Performed
- Python AST parse: `main.py`, `__main__.py`, `cli/progress.py` — all pass
- JSON parse: `manifest.json` + all 7 i18n locale files — all pass
- XML parse: 4 rebranded SVG assets — all pass
- Grep sweep on top-level frontend entry points (`index.html`, `App.tsx`,
  `LoadingPage`) — zero remaining user-visible "Langflow" strings

## How to Run
```bash
# One-shot install + build + start
make run_cli

# OR development mode (two terminals)
make backend            # 127.0.0.1:7860
make frontend           # 127.0.0.1:3000 (proxies API to 7860)

# OR Docker (unmodified upstream image, per attribution)
docker run -p 7860:7860 langflowai/langflow:latest
```

Requirements: Python 3.10-3.14, Node 20.19+, uv package manager.

## What's Verified Working (via upstream Langflow 1.11.0 test suite)
100 % of Langflow 1.11.0's shipped functionality. This rebrand does not
touch runtime code paths — only display strings, brand assets, and
documentation copy.

## Backlog / P1
- Replace favicon PNGs (`src/frontend/public/favicon.ico`,
  `manifest.json` icons 32/128/256) with brand-new Intugle Flow icon set
  when brand assets are ready.
- Rebrand per-page docs markdown (thousands of files under `docs/docs/`
  and `docs/versioned_docs/`) if the docs site needs to be re-published.
- Replace `src/frontend/src/assets/langflow_assistant.svg`,
  `langflow_assistant_idle.svg`, `langflow-icon-smooth.svg/.png`,
  `MCPLangflow.png`, `logo_light.png`, `logo_dark.png` with brand assets.
- If desired later: full internal rename (`langflow` → `intugle_flow`
  package + env-var + Alembic-revision cascade). Kept out of scope here
  because it silently breaks every existing deployment / MCP client config
  in the field and would need a full independent test run.

## Backlog / P2
- Redirect `docs.langflow.org` references in-app to a self-hosted
  `docs.intugle.example` when docs are rebuilt.
- Bundle-loading `.env` — `LANGFLOW_LOAD_BUNDLES_FROM_URLS` still hits the
  upstream registry; point at an Intugle-managed URL when one exists.
