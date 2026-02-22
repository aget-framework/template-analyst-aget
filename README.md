# Template: Analyst Agent

> Transform data into insights with analysis and reporting capabilities

**Version**: v3.6.0 | **Archetype**: Analyst | **Skills**: 2 specialized + 14 universal

---

## Why Analyst?

The Analyst archetype turns **data into actionable insights**. Unlike generic data tools, analyst agents provide:

- **Pattern discovery** — Identify trends, anomalies, and correlations across datasets
- **Structured reporting** — Generate audience-appropriate reports with metrics and visualizations
- **Evidence-based conclusions** — Ground insights in data, not speculation

**For evaluators**: If you need an AI that can analyze data methodically and communicate findings clearly to different audiences, the Analyst archetype brings analytical rigor to your workflow.

---

## Skills

Analyst agents come with **2 archetype-specific skills** plus the universal AGET skills.

### Archetype Skills

| Skill | Description |
|-------|-------------|
| **aget-analyze-data** | Analyze datasets to discover patterns, trends, and anomalies. Profiles data quality, computes statistics, and generates actionable insights. |
| **aget-generate-report** | Generate structured reports tailored to audience (executive, technical, operational). Includes metrics, findings, and recommendations. |

### Universal Skills

All AGET agents include session management, knowledge capture, and health monitoring:

- `aget-wake-up` / `aget-wind-down` — Session lifecycle
- `aget-create-project` / `aget-review-project` — Project management
- `aget-record-lesson` / `aget-capture-observation` — Learning capture
- `aget-check-health` / `aget-check-kb` / `aget-check-evolution` — Health monitoring
- `aget-propose-skill` / `aget-create-skill` — Skill development
- `aget-save-state` / `aget-file-issue` — State and issue management

---

## Ontology

Analyst agents use a **formal vocabulary** of 7 concepts organized into 3 clusters:

| Cluster | Concepts |
|---------|----------|
| **Data Analysis** | Dataset, Analysis, Pattern |
| **Metrics** | Metric, Trend, Anomaly |
| **Reporting** | Report |

This vocabulary enables precise communication about analytical work.

See: [`ontology/ONTOLOGY_analyst.yaml`](ontology/ONTOLOGY_analyst.yaml)

---

## Quick Start

```bash
# 1. Clone the template
git clone https://github.com/aget-framework/template-analyst-aget.git my-analyst-agent
cd my-analyst-agent

# 2. Configure identity
# Edit .aget/version.json:
#   "agent_name": "my-analyst-agent"
#   "domain": "your-domain"

# 3. Verify setup
python3 -m pytest tests/ -v
# Expected: All tests passing
```

### Try the Skills

```bash
# In Claude Code CLI
/aget-analyze-data       # Analyze a dataset
/aget-generate-report    # Create a structured report
```

---

## What Makes Analyst Different

| Aspect | Generic Data Tool | Analyst Agent |
|--------|------------------|---------------|
| **Data profiling** | Schema inspection | Quality assessment with completeness scores |
| **Pattern detection** | Manual queries | Automated trend and anomaly identification |
| **Reporting** | Raw exports | Audience-tailored reports with context |
| **Vocabulary** | Ad-hoc | Formal ontology (Dataset, Metric, Trend) |

---

## Framework Specification

| Attribute | Value |
|-----------|-------|
| **Framework** | [AGET v3.6.0](https://github.com/aget-framework/aget) |
| **Archetype** | Analyst |
| **Skills** | 16 total (2 archetype + 14 universal) |
| **Ontology** | 7 concepts, 3 clusters |
| **License** | Apache 2.0 |

---

## Learn More

- **[AGET Framework](https://github.com/aget-framework/aget)** — Core framework documentation
- **[Archetype Guide](https://github.com/aget-framework/aget/blob/main/docs/GETTING_STARTED.md)** — All 12 archetypes explained
- **[Getting Started](https://github.com/aget-framework/aget/blob/main/docs/GETTING_STARTED.md)** — Full onboarding guide

---

## Related Archetypes

| Archetype | Best For |
|-----------|----------|
| **[Researcher](https://github.com/aget-framework/template-researcher-aget)** | Literature search and knowledge synthesis |
| **[Advisor](https://github.com/aget-framework/template-advisor-aget)** | Risk assessment and recommendations |
| **[Developer](https://github.com/aget-framework/template-developer-aget)** | Code analysis and quality metrics |

---

**AGET Framework** | Apache 2.0 | [Issues](https://github.com/aget-framework/template-analyst-aget/issues)
