#!/usr/bin/env python3
"""
PRD Agent - Automated Product Requirements Document Generator

This agent takes product input and generates comprehensive PRD documents.
"""

import json
import sys
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, field, asdict


@dataclass
class ProductInput:
    """Input structure for PRD generation"""
    product_name: str
    product_description: str
    target_audience: str
    problem_statement: str
    proposed_solution: str
    key_features: List[str] = field(default_factory=list)
    success_metrics: List[str] = field(default_factory=list)
    technical_requirements: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    timeline_weeks: Optional[int] = None
    budget: Optional[str] = None
    competitors: List[str] = field(default_factory=list)


@dataclass
class UserStory:
    """User story structure"""
    persona: str
    goal: str
    benefit: str

    def format(self) -> str:
        return f"As a **{self.persona}**, I want to **{self.goal}**, so that **{self.benefit}**."


class PRDAgent:
    """Agent for generating Product Requirements Documents"""

    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d")

    def generate_prd(self, product_input: ProductInput) -> str:
        """Generate a complete PRD from product input"""

        prd_sections = [
            self._generate_header(product_input),
            self._generate_executive_summary(product_input),
            self._generate_product_overview(product_input),
            self._generate_goals_and_objectives(product_input),
            self._generate_target_audience(product_input),
            self._generate_user_stories(product_input),
            self._generate_features_and_requirements(product_input),
            self._generate_technical_requirements(product_input),
            self._generate_success_metrics(product_input),
            self._generate_competitive_analysis(product_input),
            self._generate_timeline(product_input),
            self._generate_dependencies_and_risks(product_input),
            self._generate_appendix(product_input)
        ]

        return "\n\n".join(prd_sections)

    def _generate_header(self, input_data: ProductInput) -> str:
        """Generate PRD header"""
        return f"""# Product Requirements Document
## {input_data.product_name}

**Document Version:** 1.0
**Date:** {self.timestamp}
**Status:** Draft

---"""

    def _generate_executive_summary(self, input_data: ProductInput) -> str:
        """Generate executive summary section"""
        return f"""## 1. Executive Summary

{input_data.product_description}

This document outlines the product requirements for {input_data.product_name}, defining the scope, features, and technical specifications needed for successful development and launch."""

    def _generate_product_overview(self, input_data: ProductInput) -> str:
        """Generate product overview section"""
        return f"""## 2. Product Overview

### 2.1 Problem Statement
{input_data.problem_statement}

### 2.2 Proposed Solution
{input_data.proposed_solution}

### 2.3 Value Proposition
{input_data.product_name} addresses the identified problem by providing {input_data.proposed_solution.lower()}. This solution will benefit {input_data.target_audience} by delivering tangible value through the key features outlined in this document."""

    def _generate_goals_and_objectives(self, input_data: ProductInput) -> str:
        """Generate goals and objectives section"""
        objectives = []
        if input_data.success_metrics:
            objectives = [f"- {metric}" for metric in input_data.success_metrics[:3]]

        objectives_text = "\n".join(objectives) if objectives else "- To be defined based on stakeholder input"

        return f"""## 3. Goals and Objectives

### 3.1 Primary Goals
- Deliver a solution that effectively addresses: {input_data.problem_statement.lower()}
- Provide value to {input_data.target_audience}
- Achieve product-market fit within the target segment

### 3.2 Key Objectives
{objectives_text}"""

    def _generate_target_audience(self, input_data: ProductInput) -> str:
        """Generate target audience section"""
        return f"""## 4. Target Audience

### 4.1 Primary Users
{input_data.target_audience}

### 4.2 User Personas
The following personas represent our primary user segments:

**Persona 1: Primary User**
- **Demographics:** {input_data.target_audience}
- **Goals:** Solve the problem: {input_data.problem_statement.lower()}
- **Pain Points:** Current solutions are inadequate or non-existent
- **Technical Proficiency:** Varies (solution should accommodate all levels)"""

    def _generate_user_stories(self, input_data: ProductInput) -> str:
        """Generate user stories section"""
        # Auto-generate user stories based on features
        stories = []
        if input_data.key_features:
            for i, feature in enumerate(input_data.key_features[:5], 1):
                story = UserStory(
                    persona="User",
                    goal=f"use {feature.lower()}",
                    benefit=f"I can achieve my goals more effectively"
                )
                stories.append(f"{i}. {story.format()}")

        stories_text = "\n".join(stories) if stories else "1. As a **user**, I want to **use the product**, so that **I can solve my problem**."

        return f"""## 5. User Stories

{stories_text}"""

    def _generate_features_and_requirements(self, input_data: ProductInput) -> str:
        """Generate features and requirements section"""
        features_text = ""

        if input_data.key_features:
            for i, feature in enumerate(input_data.key_features, 1):
                features_text += f"""
### 5.{i} {feature}

**Priority:** High
**Description:** {feature} functionality to support user needs.
**Acceptance Criteria:**
- Feature is implemented and functional
- User can access and use the feature intuitively
- Feature meets performance and quality standards
"""
        else:
            features_text = "\n### 5.1 Core Features\nTo be defined based on product requirements."

        return f"""## 5. Features and Requirements

The following features are required for the MVP (Minimum Viable Product) release:
{features_text}"""

    def _generate_technical_requirements(self, input_data: ProductInput) -> str:
        """Generate technical requirements section"""
        tech_reqs = ""

        if input_data.technical_requirements:
            tech_reqs = "\n".join([f"- {req}" for req in input_data.technical_requirements])
        else:
            tech_reqs = """- Scalable architecture to support growth
- Secure authentication and authorization
- Responsive design for multiple device types
- API-first design for flexibility
- Automated testing and CI/CD pipeline"""

        return f"""## 6. Technical Requirements

### 6.1 System Requirements
{tech_reqs}

### 6.2 Performance Requirements
- Page load time: < 2 seconds
- API response time: < 200ms for 95th percentile
- System uptime: 99.9% availability
- Support for concurrent users as defined by success metrics

### 6.3 Security Requirements
- Data encryption at rest and in transit
- Regular security audits and penetration testing
- Compliance with relevant data protection regulations
- Secure authentication mechanisms"""

    def _generate_success_metrics(self, input_data: ProductInput) -> str:
        """Generate success metrics section"""
        metrics_text = ""

        if input_data.success_metrics:
            metrics_text = "\n".join([f"- {metric}" for metric in input_data.success_metrics])
        else:
            metrics_text = """- User adoption rate
- User engagement metrics
- User satisfaction (NPS score)
- Feature usage analytics
- Performance metrics (load time, uptime)"""

        return f"""## 7. Success Metrics

### 7.1 Key Performance Indicators (KPIs)
{metrics_text}

### 7.2 Measurement Strategy
- Implement analytics tracking from day one
- Regular review cycles (weekly/monthly)
- A/B testing for feature optimization
- User feedback collection and analysis"""

    def _generate_competitive_analysis(self, input_data: ProductInput) -> str:
        """Generate competitive analysis section"""
        competitors_text = ""

        if input_data.competitors:
            competitors_text = "\n".join([f"- {comp}" for comp in input_data.competitors])
        else:
            competitors_text = "- To be researched and documented"

        return f"""## 8. Competitive Analysis

### 8.1 Key Competitors
{competitors_text}

### 8.2 Competitive Advantages
- Unique value proposition: {input_data.proposed_solution}
- Focus on target audience needs: {input_data.target_audience}
- Differentiated feature set"""

    def _generate_timeline(self, input_data: ProductInput) -> str:
        """Generate timeline section"""
        if input_data.timeline_weeks:
            weeks = input_data.timeline_weeks
            phase1 = weeks // 4
            phase2 = weeks // 4
            phase3 = weeks // 4
            phase4 = weeks - (phase1 + phase2 + phase3)

            timeline_text = f"""
**Phase 1: Planning and Design** (Weeks 1-{phase1})
- Requirements finalization
- Technical architecture design
- UI/UX design

**Phase 2: Development** (Weeks {phase1+1}-{phase1+phase2})
- Core feature implementation
- Integration work
- Initial testing

**Phase 3: Testing and Refinement** (Weeks {phase1+phase2+1}-{phase1+phase2+phase3})
- Comprehensive testing
- Bug fixes
- Performance optimization

**Phase 4: Launch Preparation** (Weeks {phase1+phase2+phase3+1}-{weeks})
- Final QA
- Documentation
- Deployment and launch"""
        else:
            timeline_text = """
**Phase 1: Planning and Design** (TBD)
- Requirements finalization
- Technical architecture design
- UI/UX design

**Phase 2: Development** (TBD)
- Core feature implementation
- Integration work
- Initial testing

**Phase 3: Testing and Refinement** (TBD)
- Comprehensive testing
- Bug fixes
- Performance optimization

**Phase 4: Launch Preparation** (TBD)
- Final QA
- Documentation
- Deployment and launch"""

        budget_text = f"\n\n### 9.2 Budget\n{input_data.budget}" if input_data.budget else ""

        return f"""## 9. Timeline and Milestones

### 9.1 Project Timeline
{timeline_text}{budget_text}"""

    def _generate_dependencies_and_risks(self, input_data: ProductInput) -> str:
        """Generate dependencies and risks section"""
        deps_text = ""
        risks_text = ""

        if input_data.dependencies:
            deps_text = "\n".join([f"- {dep}" for dep in input_data.dependencies])
        else:
            deps_text = "- Third-party services and APIs\n- Infrastructure and hosting\n- Team resources and availability"

        if input_data.risks:
            risks_text = "\n".join([f"- **Risk:** {risk}\n  - **Mitigation:** To be defined" for risk in input_data.risks])
        else:
            risks_text = """- **Risk:** Technical complexity
  - **Mitigation:** Thorough planning and phased approach
- **Risk:** Resource constraints
  - **Mitigation:** Prioritization and scope management
- **Risk:** Market changes
  - **Mitigation:** Agile development and regular market validation"""

        return f"""## 10. Dependencies and Risks

### 10.1 Dependencies
{deps_text}

### 10.2 Risk Assessment
{risks_text}"""

    def _generate_appendix(self, input_data: ProductInput) -> str:
        """Generate appendix section"""
        return f"""## 11. Appendix

### 11.1 Glossary
- **PRD:** Product Requirements Document
- **MVP:** Minimum Viable Product
- **KPI:** Key Performance Indicator
- **API:** Application Programming Interface

### 11.2 References
- Product documentation (to be created)
- Technical specifications (to be created)
- User research data (to be gathered)

### 11.3 Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {self.timestamp} | PRD Agent | Initial document creation |

---

*This document was generated by PRD Agent - Automated Product Requirements Document Generator*"""


def interactive_mode():
    """Interactive mode for gathering product input"""
    print("=== PRD Agent - Interactive Mode ===\n")

    product_name = input("Product Name: ").strip()
    product_description = input("Product Description (brief): ").strip()
    target_audience = input("Target Audience: ").strip()
    problem_statement = input("Problem Statement: ").strip()
    proposed_solution = input("Proposed Solution: ").strip()

    print("\nKey Features (enter one per line, empty line to finish):")
    key_features = []
    while True:
        feature = input(f"  Feature {len(key_features) + 1}: ").strip()
        if not feature:
            break
        key_features.append(feature)

    print("\nSuccess Metrics (enter one per line, empty line to finish):")
    success_metrics = []
    while True:
        metric = input(f"  Metric {len(success_metrics) + 1}: ").strip()
        if not metric:
            break
        success_metrics.append(metric)

    print("\nTechnical Requirements (enter one per line, empty line to finish):")
    technical_requirements = []
    while True:
        req = input(f"  Requirement {len(technical_requirements) + 1}: ").strip()
        if not req:
            break
        technical_requirements.append(req)

    timeline = input("\nEstimated Timeline (in weeks, or press Enter to skip): ").strip()
    timeline_weeks = int(timeline) if timeline.isdigit() else None

    budget = input("Budget (or press Enter to skip): ").strip() or None

    print("\nCompetitors (enter one per line, empty line to finish):")
    competitors = []
    while True:
        comp = input(f"  Competitor {len(competitors) + 1}: ").strip()
        if not comp:
            break
        competitors.append(comp)

    print("\nDependencies (enter one per line, empty line to finish):")
    dependencies = []
    while True:
        dep = input(f"  Dependency {len(dependencies) + 1}: ").strip()
        if not dep:
            break
        dependencies.append(dep)

    print("\nRisks (enter one per line, empty line to finish):")
    risks = []
    while True:
        risk = input(f"  Risk {len(risks) + 1}: ").strip()
        if not risk:
            break
        risks.append(risk)

    return ProductInput(
        product_name=product_name,
        product_description=product_description,
        target_audience=target_audience,
        problem_statement=problem_statement,
        proposed_solution=proposed_solution,
        key_features=key_features,
        success_metrics=success_metrics,
        technical_requirements=technical_requirements,
        dependencies=dependencies,
        risks=risks,
        timeline_weeks=timeline_weeks,
        budget=budget,
        competitors=competitors
    )


def load_from_json(json_file: str) -> ProductInput:
    """Load product input from JSON file"""
    with open(json_file, 'r') as f:
        data = json.load(f)
    return ProductInput(**data)


def main():
    """Main entry point for PRD Agent"""
    print("PRD Agent - Product Requirements Document Generator\n")

    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print("""Usage:
    python prd_agent.py                    # Interactive mode
    python prd_agent.py input.json         # Load from JSON file
    python prd_agent.py --help             # Show this help message

JSON Input Format:
{
    "product_name": "Product Name",
    "product_description": "Brief description",
    "target_audience": "Target users",
    "problem_statement": "Problem to solve",
    "proposed_solution": "Solution approach",
    "key_features": ["Feature 1", "Feature 2"],
    "success_metrics": ["Metric 1", "Metric 2"],
    "technical_requirements": ["Req 1", "Req 2"],
    "dependencies": ["Dep 1"],
    "risks": ["Risk 1"],
    "timeline_weeks": 12,
    "budget": "$50,000",
    "competitors": ["Competitor 1"]
}
""")
            return

        # Load from JSON file
        json_file = sys.argv[1]
        try:
            product_input = load_from_json(json_file)
            print(f"Loaded product input from: {json_file}\n")
        except FileNotFoundError:
            print(f"Error: File '{json_file}' not found.")
            return
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in file '{json_file}'.")
            return
        except Exception as e:
            print(f"Error loading file: {e}")
            return
    else:
        # Interactive mode
        product_input = interactive_mode()

    # Generate PRD
    print("\n=== Generating PRD ===\n")
    agent = PRDAgent()
    prd_content = agent.generate_prd(product_input)

    # Save to file
    output_filename = f"PRD_{product_input.product_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.md"
    with open(output_filename, 'w') as f:
        f.write(prd_content)

    print(f"✓ PRD generated successfully!")
    print(f"✓ Saved to: {output_filename}")
    print(f"\nPreview:\n{'-' * 80}")
    # Show first 50 lines of the PRD
    lines = prd_content.split('\n')
    preview_lines = min(50, len(lines))
    print('\n'.join(lines[:preview_lines]))
    if len(lines) > preview_lines:
        print(f"\n... ({len(lines) - preview_lines} more lines)")
    print('-' * 80)


if __name__ == "__main__":
    main()
