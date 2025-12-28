# AGET Analyst Template

> **Data analysis and insight generation template**

Part of the [AGET Framework](https://github.com/aget-framework) v3.0.0.

## Archetype

**Analyst** - Transform data and information into actionable insights.

- **Extends**: advisor
- **Governance**: Balanced
- **Primary A-SDLC Phases**: 0 (Discovery), 1 (Specification), 4 (Validation)

## Key Capabilities

- Data analysis and visualization
- Trend identification and pattern recognition
- Report generation with evidence-based conclusions
- Quantitative and qualitative analysis

## Inviolable

```
INV-ANA-001: shall NOT present Analysis as Fact WITHOUT Evidence_Citation
```

## Quick Start

1. Clone this template
2. Run instantiation script (see [Getting Started](docs/GETTING_STARTED.md))
3. Configure for your analysis domain

## Structure

```
template-analyst-aget/
├── manifest.yaml          # Template configuration
├── governance/            # Charter, Mission, Scope
├── tests/                 # Contract tests
└── .aget/                 # 5D Composition Architecture
    ├── persona/           # D1: Identity
    ├── memory/            # D2: Knowledge
    ├── reasoning/         # D3: Decision-making
    ├── skills/            # D4: Capabilities
    └── context/           # D5: Relationships
```

## License

Apache License 2.0 - See [LICENSE](LICENSE)

---

*AGET Framework - AI discovers patterns, you describe intent*
