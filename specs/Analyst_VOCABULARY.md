# Analyst Domain Vocabulary

**Version**: 1.0.0
**Status**: Active
**Owner**: template-analyst-aget
**Created**: 2026-01-10
**Scope**: Template vocabulary (DRIVES instance behavior per L481)
**Archetype**: Analyst

---

## Meta

```yaml
vocabulary:
  meta:
    domain: "analysis"
    version: "1.0.0"
    owner: "template-analyst-aget"
    created: "2026-01-10"
    theoretical_basis:
      - "L481: Ontology-Driven Agent Creation"
      - "L482: Executable Ontology - SKOS+EARS Grounding"
    archetype: "Analyst"
```

---

## Concept Scheme

```yaml
Analyst_Vocabulary:
  skos:prefLabel: "Analyst Vocabulary"
  skos:definition: "Vocabulary for analyst domain agents"
  skos:hasTopConcept:
    - Analyst_Core_Concepts
  rdf:type: skos:ConceptScheme
```

---

## Core Concepts

### Data

```yaml
Data:
  skos:prefLabel: "Data"
  skos:definition: "Raw information to be analyzed"
  skos:broader: Analyst_Core_Concepts
  skos:inScheme: Analyst_Vocabulary
```

### Pattern

```yaml
Pattern:
  skos:prefLabel: "Pattern"
  skos:definition: "Recurring structure or trend in data"
  skos:broader: Analyst_Core_Concepts
  skos:inScheme: Analyst_Vocabulary
```

### Insight

```yaml
Insight:
  skos:prefLabel: "Insight"
  skos:definition: "Actionable understanding derived from analysis"
  skos:broader: Analyst_Core_Concepts
  skos:inScheme: Analyst_Vocabulary
```

### Metric

```yaml
Metric:
  skos:prefLabel: "Metric"
  skos:definition: "Quantifiable measure of a characteristic"
  skos:broader: Analyst_Core_Concepts
  skos:inScheme: Analyst_Vocabulary
```

### Visualization

```yaml
Visualization:
  skos:prefLabel: "Visualization"
  skos:definition: "Visual representation of data or findings"
  skos:broader: Analyst_Core_Concepts
  skos:inScheme: Analyst_Vocabulary
```

---

## Extension Points

Instances extending this template vocabulary should:
1. Add domain-specific terms under appropriate broader concepts
2. Maintain SKOS compliance (prefLabel, definition, broader/narrower)
3. Reference foundation L-docs where applicable
4. Use `research_status` for terms under investigation

---

## References

- L481: Ontology-Driven Agent Creation
- L482: Executable Ontology - SKOS+EARS Grounding
- R-REL-015: Template Ontology Conformance
- AGET_VOCABULARY_SPEC.md

---

*Analyst_VOCABULARY.md v1.0.0 — SKOS-compliant template vocabulary*
*Generated: 2026-01-10*
