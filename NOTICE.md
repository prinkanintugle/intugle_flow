# NOTICE

## Intugle Flow

Intugle Flow is a rebranded distribution of **Langflow** (https://github.com/langflow-ai/langflow),
an open-source visual builder for AI-powered agents and workflows, licensed under the MIT License.

---

## Original Work

- **Project:** Langflow
- **Copyright:** Copyright (c) 2024 Langflow (langflow-ai and contributors)
- **License:** MIT License (see `LICENSE`)
- **Upstream:** https://github.com/langflow-ai/langflow
- **Upstream release used:** Langflow 1.11.0
- **Website:** https://langflow.org

The MIT License requires that the original copyright notice and license text
be retained. Both are preserved unchanged in the `LICENSE` file at the root
of this repository.

---

## Modifications by the Intugle Flow project

The following changes have been made on top of Langflow 1.11.0:

1. Rebranding of user-visible product name from "Langflow" to "Intugle Flow" in:
   - `README.md`
   - `src/frontend/index.html` (browser tab title & meta)
   - `src/frontend/src/customization/config-constants.ts`
     (`APP_NAME`, `APP_DESCRIPTION`, related brand constants)
   - Selected frontend UI strings (welcome text, footer, "About" dialog copy)
   - Selected marketing/screenshot copy in this NOTICE and the top-level README.
2. Addition of this `NOTICE.md` file describing the derivative work.

Internal Python package names (`langflow`, `lfx`, `langflow-base`,
`langflow-stepflow`), CLI commands (`langflow run`), environment variable
prefixes (`LANGFLOW_*`), Alembic migration identifiers, Docker image names,
public API endpoints, on-disk database schemas, and the pip-published
distribution names have **not** been modified. This preserves compatibility
with the upstream project so operators can continue to consume upstream
security patches and bugfixes.

---

## Trademarks

"Langflow" is a name and mark owned by the original Langflow project and its
contributors. This distribution does not claim any rights over the "Langflow"
name or mark and only refers to the upstream project for the purpose of
attribution required by the MIT License.

"Intugle Flow" is used solely as a product name for this rebranded
distribution.

---

## Third-Party Software

Intugle Flow, like the upstream Langflow project, depends on a large number of
third-party open-source libraries. Each such library retains its own license,
which can be found either in the package metadata (e.g. `pyproject.toml`,
`uv.lock`, `package.json`) or in the source tree of the dependency itself.

---

## Contact

For questions about this rebranded distribution, please refer to the
maintainers of the Intugle Flow project.

For questions about the underlying Langflow platform, refer to the upstream
project at https://github.com/langflow-ai/langflow.
