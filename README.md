# Vibeit - PRD Agent

An automated Product Requirements Document (PRD) generator that transforms product ideas into comprehensive, structured PRD documents.

## Overview

The PRD Agent helps product managers, founders, and development teams quickly create professional PRD documents from basic product inputs. It automates the process of structuring requirements, generating user stories, and organizing technical specifications.

## Features

- **Interactive Mode**: Guided input through command-line prompts
- **JSON Input**: Batch processing from structured JSON files
- **Comprehensive PRDs**: Generates complete documents with all standard PRD sections
- **Customizable**: Flexible input format supporting various levels of detail
- **Professional Output**: Clean, well-structured Markdown documents

## Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Vibeit
```

2. Make the script executable (optional):
```bash
chmod +x prd_agent.py
```

## Usage

### Interactive Mode

Run the agent without arguments for interactive input:

```bash
python prd_agent.py
```

You'll be prompted to enter:
- Product name and description
- Target audience
- Problem statement and proposed solution
- Key features
- Success metrics
- Technical requirements
- Timeline and budget
- Competitors, dependencies, and risks

### JSON Input Mode

Create a JSON file with your product details and pass it as an argument:

```bash
python prd_agent.py example_input.json
```

### JSON Format

```json
{
  "product_name": "Your Product Name",
  "product_description": "Brief description of your product",
  "target_audience": "Who will use this product",
  "problem_statement": "What problem does this solve",
  "proposed_solution": "How does your product solve it",
  "key_features": ["Feature 1", "Feature 2", "Feature 3"],
  "success_metrics": ["Metric 1", "Metric 2"],
  "technical_requirements": ["Requirement 1", "Requirement 2"],
  "dependencies": ["Dependency 1"],
  "risks": ["Risk 1"],
  "timeline_weeks": 12,
  "budget": "$50,000",
  "competitors": ["Competitor 1", "Competitor 2"]
}
```

**Note:** All fields except `product_name`, `product_description`, `target_audience`, `problem_statement`, and `proposed_solution` are optional.

### Help

```bash
python prd_agent.py --help
```

## Output

The agent generates a Markdown file named `PRD_<ProductName>_<Date>.md` containing:

1. **Executive Summary** - High-level overview
2. **Product Overview** - Problem statement and solution
3. **Goals and Objectives** - What you aim to achieve
4. **Target Audience** - User personas and demographics
5. **User Stories** - Feature-based user stories
6. **Features and Requirements** - Detailed feature specifications
7. **Technical Requirements** - System, performance, and security requirements
8. **Success Metrics** - KPIs and measurement strategy
9. **Competitive Analysis** - Market positioning
10. **Timeline and Milestones** - Project phases and budget
11. **Dependencies and Risks** - External factors and mitigation strategies
12. **Appendix** - Glossary, references, and document history

## Example

An example input file (`example_input.json`) is provided. Generate a sample PRD:

```bash
python prd_agent.py example_input.json
```

This creates a complete PRD for "TaskFlow Pro", a task management platform.

## Use Cases

- **Startups**: Quickly document product ideas for investors or development teams
- **Product Managers**: Standardize PRD creation across projects
- **Development Teams**: Clarify requirements before starting development
- **Educators**: Teach product management and requirements gathering
- **Consultants**: Accelerate client deliverables

## Customization

The PRD Agent can be extended or customized:

- **Templates**: Modify section generators in `PRDAgent` class
- **Additional Fields**: Extend `ProductInput` dataclass
- **Output Formats**: Add exporters for PDF, HTML, or other formats
- **AI Integration**: Add LLM-based content enhancement

## Project Structure

```
Vibeit/
├── prd_agent.py          # Main PRD generator
├── example_input.json    # Example input file
├── README.md             # This file
└── PRD_*.md             # Generated PRD documents
```

## Contributing

Contributions are welcome! Areas for enhancement:

- Additional PRD templates for different industries
- PDF/HTML export functionality
- AI-powered content suggestions
- Web-based UI
- Version control for PRD iterations

## License

MIT License - Feel free to use and modify as needed.

## Support

For issues or questions, please open an issue in the repository.

---

**PRD Agent** - Transforming product ideas into actionable requirements documents.
