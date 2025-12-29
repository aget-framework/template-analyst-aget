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

---

## Specification

| Attribute | Value |
|-----------|-------|
| **Governed By** | [AGET_TEMPLATE_SPEC v3.1](https://github.com/aget-framework/aget/blob/main/specs/AGET_TEMPLATE_SPEC.md) |
| **Foundation** | [WORKER_TEMPLATE_SPEC v1.0](https://github.com/aget-framework/aget/blob/main/specs/WORKER_TEMPLATE_SPEC_v1.0.yaml) |
| **Archetype** | Analyst |
| **Extends** | Advisor |
| **Manifest Version** | 3.0 |
| **Contract Tests** | 9 tests |

### Key Capabilities

| ID | Capability | Pattern |
|----|------------|---------|
| CAP-001 | Wake Protocol | event-driven |
| CAP-009 | Wind Down Protocol | event-driven |
| CAP-020 | Version Configuration | ubiquitous |
| CAP-028 | Project Plan Pattern | event-driven |

Validate compliance: `pytest tests/ -v`

See: [Full specification](https://github.com/aget-framework/aget/tree/main/specs)

---

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
