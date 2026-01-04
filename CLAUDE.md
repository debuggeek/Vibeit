# CLAUDE.md - AI Assistant Guide for Vibeit

> **Last Updated**: 2026-01-04
>
> **Project Status**: Multi-Project Repository - Projects Directory Established

This document serves as a comprehensive guide for AI assistants working on the Vibeit codebase. It explains the project structure, development workflows, coding conventions, and best practices.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Current State](#current-state)
3. [Repository Structure](#repository-structure)
4. [Development Workflow](#development-workflow)
5. [Coding Conventions](#coding-conventions)
6. [Git Workflow](#git-workflow)
7. [Testing Guidelines](#testing-guidelines)
8. [Documentation Standards](#documentation-standards)
9. [AI Assistant Guidelines](#ai-assistant-guidelines)
10. [Custom Agents](#custom-agents)
11. [Future Roadmap](#future-roadmap)

---

## Project Overview

### About Vibeit

**Project Name**: Vibeit
**Description**: A collection of vibe-related projects for testing and experimentation
**Repository**: debuggeek/Vibeit
**Purpose**: Multi-project repository housing various vibe-coated test projects

### Repository Type

**Type**: Multi-Project Repository

Vibeit serves as a container repository for multiple independent projects. Each project in the `projects/` directory:
- Is self-contained with its own tech stack and dependencies
- Focuses on specific testing goals or experimental concepts
- Has its own documentation and setup instructions
- Can use different frameworks and technologies

### Tech Stack

**Status**: Varies by project

Each project in the `projects/` directory may use different technologies. When adding a new project, document its tech stack in the project's own README.md:
- Frontend framework (React, Vue, Svelte, etc.)
- Backend framework (Node.js, Python, Go, etc.)
- Database (PostgreSQL, MongoDB, etc.)
- Build tools (Vite, Webpack, etc.)
- Testing frameworks (Jest, Vitest, Pytest, etc.)

---

## Current State

### Repository Status

- **Initialization Date**: January 4, 2026
- **Current Branch**: `claude/add-projects-directory-67f3p`
- **Repository Type**: Multi-project container
- **Projects**: 0 (directory structure established)

### What Exists

```
/home/user/Vibeit/
├── .claude/           # Claude Code configuration
│   └── agents/        # Custom Claude agents
│       └── prd-generator.md  # PRD generation agent
├── .git/              # Git repository metadata
├── projects/          # Container for vibe-related test projects
│   └── README.md      # Guide for the projects directory
├── README.md          # Repository overview and documentation
└── CLAUDE.md          # This file - AI assistant guide
```

### Adding New Projects

When adding a new project to the `projects/` directory:

1. Create a new subdirectory under `projects/` with a descriptive name
2. Initialize the project with its own tech stack and dependencies
3. Include a comprehensive README.md explaining:
   - Project purpose and goals
   - Tech stack and dependencies
   - Setup and installation instructions
   - Usage and testing instructions
4. Add project-specific configuration files (.gitignore, package.json, etc.)
5. Document the project in the main README.md if applicable

Each project should be self-contained and independent.

---

## Repository Structure

### Current Structure

Vibeit is organized as a multi-project container repository:

```
Vibeit/
├── .claude/              # Claude Code configuration
│   └── agents/           # Custom Claude agents (available globally)
│       └── prd-generator.md  # PRD generation agent
├── .github/              # GitHub workflows and templates (if needed)
│   └── workflows/        # CI/CD workflows
├── projects/             # Container for all vibe-related projects
│   ├── README.md         # Guide for the projects directory
│   ├── project-1/        # Individual project (self-contained)
│   │   ├── src/          # Project source code
│   │   ├── tests/        # Project tests
│   │   ├── README.md     # Project documentation
│   │   └── ...           # Project-specific files
│   ├── project-2/        # Another independent project
│   │   └── ...
│   └── ...               # Additional projects
├── README.md             # Repository overview
└── CLAUDE.md             # This file - AI assistant guide
```

### Project-Level Structure

Each project in the `projects/` directory should follow this general pattern:

```
projects/project-name/
├── src/                  # Source code (structure varies by project type)
├── tests/                # Test files
│   ├── unit/            # Unit tests
│   ├── integration/     # Integration tests
│   └── e2e/             # End-to-end tests (if applicable)
├── docs/                 # Project-specific documentation (if needed)
├── .gitignore           # Project-specific ignore rules
├── package.json          # Dependencies (Node.js projects)
├── requirements.txt      # Dependencies (Python projects)
├── README.md             # Project documentation
└── ...                   # Other project-specific files
```

**Note**: Each project's structure will vary based on its tech stack and requirements. The above is a guideline, not a strict requirement.

---

## Development Workflow

### Working with Projects

Since Vibeit is a multi-project repository, the development workflow is project-specific:

1. **Navigate to the project directory**: `cd projects/project-name`
2. **Follow project-specific setup**: Refer to the project's README.md
3. **Work within the project context**: Each project is self-contained

### Setting Up a New Project

When creating a new project in the `projects/` directory:

1. Create the project directory: `mkdir projects/project-name`
2. Initialize the project with your chosen tech stack
3. Create a comprehensive README.md documenting:
   - Prerequisites (Node.js version, Python version, etc.)
   - Installation steps
   - Environment variables required
   - Database setup (if applicable)
   - Running the development server
   - Building for production
   - Testing instructions
4. Add project-specific configuration files
5. Update the main repository README.md if needed

### Common Project Commands

Commands will vary by project. Each project's README.md should document its specific commands. Examples:

**Node.js Project:**
```bash
cd projects/project-name
npm install          # Install dependencies
npm run dev          # Start development server
npm run build        # Build for production
npm run test         # Run tests
npm run lint         # Lint code
```

**Python Project:**
```bash
cd projects/project-name
pip install -r requirements.txt  # Install dependencies
python main.py                    # Run the application
pytest                            # Run tests
```

---

## Coding Conventions

### General Principles

Until specific conventions are established, follow these general principles:

1. **Consistency**: Follow existing patterns in the codebase
2. **Clarity**: Write self-documenting code with clear variable and function names
3. **Simplicity**: Avoid over-engineering; implement what's needed
4. **DRY**: Don't Repeat Yourself - extract reusable logic
5. **YAGNI**: You Aren't Gonna Need It - don't add speculative features

### Naming Conventions

**To Be Established**: Document naming conventions for:
- Files and directories
- Variables and constants
- Functions and methods
- Classes and interfaces
- CSS/styling conventions

### Code Style

**To Be Established**: Once linting tools are configured, document:
- Indentation (spaces vs tabs, size)
- Quote style (single vs double)
- Semicolon usage
- Line length limits
- Import ordering
- Comment style

### Project-Specific Patterns

**To Be Documented**: As the codebase grows, document:
- State management patterns
- API calling conventions
- Error handling approach
- Logging practices
- Component composition patterns
- File organization rules

---

## Git Workflow

### Branch Naming Convention

Follow this pattern for branch names:
- `main` or `master` - Production-ready code
- `develop` - Integration branch (if using Gitflow)
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `hotfix/description` - Urgent production fixes
- `claude/description-sessionId` - AI assistant development branches

### Commit Message Guidelines

Write clear, descriptive commit messages:

```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples**:
```
feat: add user authentication system

fix: resolve null pointer exception in user service

docs: update API documentation for v2 endpoints

refactor: simplify database connection logic
```

### Pull Request Guidelines

When creating pull requests:
1. Provide a clear title and description
2. Reference related issues (e.g., "Fixes #123")
3. Include test plan or testing instructions
4. Ensure all tests pass
5. Request reviews from appropriate team members

---

## Testing Guidelines

### Testing Philosophy

**To Be Established**: Document testing approach:
- Unit test coverage expectations
- Integration testing strategy
- E2E testing approach
- Test file naming and location conventions

### Writing Tests

**To Be Documented**: Once testing framework is set up:
- Test structure and organization
- Mocking and stubbing practices
- Test data management
- Assertion style

---

## Documentation Standards

### Code Comments

- Write comments for complex logic or non-obvious decisions
- Avoid redundant comments that just restate the code
- Keep comments up-to-date with code changes
- Use JSDoc/docstrings for public APIs

### README Updates

Keep the README.md current with:
- Project description and purpose
- Setup and installation instructions
- Usage examples
- Contribution guidelines
- License information

### CLAUDE.md Maintenance

This file should be updated when:
- Project tech stack is established
- New coding conventions are adopted
- Development workflow changes
- New architectural patterns are introduced
- Testing strategy evolves

---

## AI Assistant Guidelines

### Best Practices for AI Assistants

When working on this codebase, AI assistants should:

1. **Read Before Writing**
   - Always read existing files before making changes
   - Understand current patterns before adding new code
   - Check for existing implementations before creating new ones

2. **Maintain Consistency**
   - Follow established naming conventions
   - Match existing code style
   - Use the same libraries and patterns already in use

3. **Avoid Over-Engineering**
   - Implement only what's requested
   - Don't add unnecessary features or abstractions
   - Keep solutions simple and focused
   - Don't add error handling for impossible scenarios

4. **Security Awareness**
   - Watch for common vulnerabilities (XSS, SQL injection, etc.)
   - Validate user input at system boundaries
   - Follow security best practices for the tech stack
   - Don't commit secrets or sensitive data

5. **Testing**
   - Write or update tests for new functionality
   - Ensure existing tests pass
   - Follow project testing conventions

6. **Documentation**
   - Update relevant documentation when making changes
   - Add comments for complex logic
   - Keep CLAUDE.md current with new patterns

7. **Git Practices**
   - Write clear commit messages
   - Work on appropriate branches (usually `claude/*` branches)
   - Push to the correct branch
   - Don't force push to shared branches

8. **Communication**
   - Use direct, concise language
   - Focus on technical accuracy
   - Ask for clarification when requirements are unclear
   - Provide context for significant decisions

### What NOT to Do

- ❌ Don't create files unnecessarily - prefer editing existing files
- ❌ Don't add emojis unless explicitly requested
- ❌ Don't make changes to code you haven't read
- ❌ Don't add features beyond what was requested
- ❌ Don't create abstraction layers for one-time operations
- ❌ Don't add backwards-compatibility hacks
- ❌ Don't commit broken code or failing tests
- ❌ Don't modify configuration without understanding impact
- ❌ Don't use generic variable names or magic numbers

### Exploration and Planning

For complex tasks:
1. Explore the codebase first to understand existing patterns
2. Plan the implementation approach
3. Break down large tasks into smaller steps
4. Use TodoWrite to track progress
5. Implement changes incrementally
6. Test thoroughly before committing

---

## Custom Agents

### Available Agents

The repository includes custom Claude agents in the `.claude/agents/` directory that are available across all projects.

#### PRD Generator (`prd-generator`)

**Purpose**: Generates comprehensive Product Requirements Documents from simple product ideas or prompts.

**Location**: `.claude/agents/prd-generator.md`

**Capabilities**:
- Transforms simple product ideas into detailed PRDs
- Creates well-structured documentation with all essential sections
- Asks clarifying questions when needed
- Outputs professional, developer-ready specifications

**What It Generates**:
- Executive Summary
- Product Overview (vision, goals, target audience)
- Functional & Non-functional Requirements
- User Stories with Acceptance Criteria
- Technical Considerations (tech stack, integrations, data model)
- User Experience (flows, screens, interactions)
- Success Metrics & KPIs
- Timeline & Milestones
- Risk Assessment & Mitigation
- Open Questions & Assumptions

**How to Use**:

In Claude Code, you can invoke this agent by asking Claude to use it:

```
"Use the prd-generator agent to create a PRD for [your product idea]"
```

**Example**:
```
"Use the prd-generator agent to create a PRD for a mobile app that helps
users track their daily water intake with reminders and goals"
```

The agent will:
1. Analyze your prompt
2. Ask clarifying questions if needed
3. Generate a comprehensive PRD document
4. Create/use the appropriate project directory in `projects/`
5. Save the PRD as `PRD.md` in the project directory

**Output**: Markdown file saved in `projects/[project-name]/PRD.md`

**Example Output Locations**:
- `projects/fitness-tracker/PRD.md`
- `projects/water-intake-app/PRD.md`
- `projects/chrome-extension-blocker/PRD.md`

#### PRD to Architecture (`prd-to-architecture`)

**Purpose**: Converts Product Requirements Documents (PRDs) into comprehensive architectural specifications.

**Location**: `.claude/agents/prd-to-architecture.md`

**Capabilities**:
- Analyzes existing PRD documents
- Translates business requirements into technical architecture
- Makes informed technology stack decisions
- Creates detailed system design specifications
- Documents architectural decisions and trade-offs

**What It Generates**:
- Executive Summary & Key Architectural Decisions
- System Architecture Overview (patterns, components, data flow)
- Component Architecture (detailed breakdown, interfaces, dependencies)
- Data Architecture (database design, schemas, ERDs, caching)
- API Design (endpoints, authentication, request/response formats)
- Technology Stack (frontend, backend, database, infrastructure)
- Security Architecture (authentication, authorization, encryption)
- Integration Architecture (external services, APIs, webhooks)
- Infrastructure & Deployment Architecture
- Performance & Scalability Architecture
- Observability & Monitoring Strategy
- Development Workflow & CI/CD
- Migration & Deployment Strategy
- Technical Debt & Future Considerations

**How to Use**:

In Claude Code, you can invoke this agent by providing a PRD file path or project name:

```
"Use the prd-to-architecture agent to convert projects/fitness-tracker/PRD.md into an architecture spec"
```

Or:

```
"Create an architecture specification for the water-intake-app project"
```

The agent will:
1. Read the existing PRD document
2. Analyze functional and non-functional requirements
3. Make architectural decisions based on requirements
4. Generate a comprehensive architecture specification
5. Save the architecture spec as `ARCHITECTURE.md` in the same project directory

**Output**: Markdown file saved in `projects/[project-name]/ARCHITECTURE.md`

**Example Output Locations**:
- `projects/fitness-tracker/ARCHITECTURE.md`
- `projects/water-intake-app/docs/ARCHITECTURE.md`
- `projects/chrome-extension-blocker/ARCHITECTURE.md`

**Workflow Integration**:

This agent works seamlessly with the PRD Generator agent:
1. Use `prd-generator` to create a PRD from a product idea
2. Use `prd-to-architecture` to convert the PRD into technical specifications
3. Development team has both business requirements and technical architecture

#### Task Breakdown (`task-breakdown`)

**Purpose**: Converts architectural specifications into discrete, actionable development tasks organized in a task management system.

**Location**: `.claude/agents/task-breakdown.md`

**Capabilities**:
- Analyzes ARCHITECTURE.md files
- Breaks down architecture into actionable development tasks
- Creates individual task markdown files with clear structure
- Organizes tasks by category and dependency order
- Generates comprehensive task index and progress tracking
- Provides task management workflow

**What It Generates**:

For each project, creates:
- `Tasks/` directory with `Uncompleted/` and `Completed/` subdirectories
- Individual task markdown files (e.g., `001-setup-project.md`, `002-configure-db.md`)
- `Tasks/README.md` with task index and progress tracking
- Tasks organized by category:
  - Setup & Infrastructure (001-020)
  - Backend Development (021-100)
  - Frontend Development (101-200)
  - Integration (201-250)
  - Testing (251-300)
  - Documentation (301-320)
  - Deployment (321-350)

**Task File Structure**:

Each task markdown file includes:
- Status checkboxes (Not Started / In Progress / Completed)
- Priority level (High / Medium / Low)
- Clear description of what needs to be done
- Related architecture sections
- Dependencies on other tasks
- Acceptance criteria (measurable outcomes)
- Technical implementation notes
- Files to create/modify
- Testing requirements
- Estimated complexity
- References to ARCHITECTURE.md and PRD.md

**How to Use**:

In Claude Code, you can invoke this agent by providing an architecture file or project name:

```
"Use the task-breakdown agent to create tasks from projects/fitness-tracker/ARCHITECTURE.md"
```

Or:

```
"Break down the architecture for the water-intake-app project into tasks"
```

The agent will:
1. Read the ARCHITECTURE.md file
2. Optionally read PRD.md for additional context
3. Analyze components, features, and requirements
4. Break down into discrete, actionable tasks
5. Create task files in `Tasks/Uncompleted/`
6. Generate task index in `Tasks/README.md`
7. Provide summary report

**Output**: Task markdown files in `projects/[project-name]/Tasks/Uncompleted/`

**Example Directory Structure After Running**:
```
projects/fitness-tracker/
├── ARCHITECTURE.md
├── PRD.md
└── Tasks/
    ├── README.md              # Task index and progress tracking
    ├── Uncompleted/
    │   ├── 001-setup-project-structure.md
    │   ├── 002-configure-database.md
    │   ├── 003-implement-user-model.md
    │   ├── 021-create-auth-endpoints.md
    │   ├── 101-create-login-page.md
    │   └── ...
    └── Completed/
        └── (tasks moved here when finished)
```

**Task Management Workflow**:

1. **Starting a Task**:
   - Open task file in `Tasks/Uncompleted/`
   - Check dependencies are completed
   - Update status to "In Progress"
   - Implement according to acceptance criteria

2. **Completing a Task**:
   - Verify all acceptance criteria are met
   - Update status to "Completed"
   - Move file from `Tasks/Uncompleted/` to `Tasks/Completed/`
   - Update `Tasks/README.md` progress tracking

3. **Tracking Progress**:
   - View `Tasks/README.md` for complete task list
   - Track progress by category
   - See dependencies and task relationships

**Workflow Integration**:

This agent completes the full project planning workflow:
1. Use `prd-generator` to create PRD from product idea
2. Use `prd-to-architecture` to convert PRD into technical architecture
3. Use `task-breakdown` to convert architecture into actionable tasks
4. Development team has: business requirements, technical architecture, AND implementation task list

**Example Task Output**:

A task file (`001-setup-project-structure.md`) might look like:

```markdown
# Task 001: Setup Project Structure

## Status
- [x] Not Started
- [ ] In Progress
- [ ] Completed

## Priority
High

## Description
Initialize the project structure with necessary directories,
configuration files, and development tools.

## Acceptance Criteria
- [ ] Project directory structure created
- [ ] Package manager initialized (package.json created)
- [ ] TypeScript configured with tsconfig.json
- [ ] ESLint and Prettier configured
- [ ] Git repository initialized with .gitignore
- [ ] README.md created with setup instructions

## Dependencies
None (first task)

## Files to Create/Modify
- `package.json` - Project dependencies and scripts
- `tsconfig.json` - TypeScript configuration
- `.eslintrc.js` - ESLint configuration
- `.prettierrc` - Prettier configuration
- `.gitignore` - Git ignore rules
- `README.md` - Project documentation
```

### Adding New Agents

To create additional custom agents:

1. Create a new file in `.claude/agents/` with a `.md` extension
2. Add YAML frontmatter with configuration:
   ```yaml
   ---
   name: agent-name
   description: Brief description of what the agent does
   model: sonnet  # or haiku, opus
   tools:
     - Write
     - Read
     - Glob
     - Grep
   ---
   ```
3. Write the agent's system prompt below the frontmatter
4. Document the agent in this section of CLAUDE.md

**Available Tools for Agents**:
- `Write` - Create new files
- `Read` - Read existing files
- `Glob` - Find files by pattern
- `Grep` - Search file contents
- `Edit` - Modify existing files
- `Bash` - Run shell commands
- `WebFetch` - Fetch web content
- `WebSearch` - Search the web

---

## Future Roadmap

### Immediate Next Steps

1. **Add First Project**: Create the first vibe-related project in `projects/`
2. **Establish Project Template**: Create a template or guide for adding new projects
3. **Set Up Repository-Level CI/CD**: Configure workflows that can handle multiple projects (if needed)
4. **Create Shared Resources**: Add any shared utilities or resources used across projects (if applicable)
5. **Document Project Guidelines**: Refine guidelines for project structure and conventions

### Growing the Repository

As projects are added:

1. **For Each New Project**:
   - Choose appropriate tech stack for the project's goals
   - Initialize with package manager and dependencies
   - Set up project-specific linting, formatting, and testing
   - Document thoroughly in the project's README.md
   - Add project-level CI/CD if needed

2. **Repository-Level Considerations**:
   - Keep the main README.md updated with project list (if beneficial)
   - Maintain consistent Git workflow across projects
   - Share learnings and patterns between projects
   - Consider shared tooling or utilities if multiple projects need them

### Areas to Document as Projects Grow

For individual projects, document:
- **Architecture Decisions**: Major architectural choices and rationale
- **API Design**: Endpoints, authentication, data formats (if applicable)
- **Database Schema**: Data models and relationships (if applicable)
- **Deployment Process**: How to deploy the specific project
- **Troubleshooting Guide**: Common issues and solutions
- **Performance Considerations**: Optimization strategies and benchmarks

For the repository level, document:
- **Project Selection Criteria**: What makes a good Vibeit project
- **Shared Patterns**: Common patterns emerging across projects
- **Cross-Project Learnings**: Insights gained from experiments

---

## Getting Help

### Resources

**To Be Added**: Links to:
- Project documentation
- Team communication channels
- Issue tracker
- Contributing guidelines
- Code of conduct

### Updating This Document

This document should evolve with the project. When making updates:

1. Keep information current and accurate
2. Remove outdated sections
3. Add new sections as the project grows
4. Update the "Last Updated" date at the top
5. Commit changes with a clear message

---

## Appendix

### Repository Setup Checklist

Repository-level setup (completed):

- [x] Create `projects/` directory structure
- [x] Create `projects/README.md` with guidelines
- [x] Update main README.md with repository overview
- [x] Update CLAUDE.md with multi-project structure
- [x] Create `.claude/agents/` directory for custom agents
- [x] Add PRD Generator agent (`prd-generator.md`)

### New Project Initialization Checklist

When adding a new project to `projects/`, complete these tasks:

**Project Setup:**
- [ ] Create project directory: `projects/project-name/`
- [ ] Choose and document tech stack in project README
- [ ] Initialize package manager (npm, pip, cargo, etc.)
- [ ] Set up project directory structure
- [ ] Create comprehensive project README.md

**Development Tools:**
- [ ] Configure linting tools (ESLint, Pylint, etc.)
- [ ] Configure code formatting (Prettier, Black, etc.)
- [ ] Set up testing framework (Jest, Pytest, etc.)
- [ ] Configure TypeScript (if applicable)
- [ ] Set up build tools (Vite, Webpack, etc.)
- [ ] Create project-specific .gitignore file

**Project Configuration:**
- [ ] Set up pre-commit hooks (if needed)
- [ ] Configure project-level CI/CD (if needed)
- [ ] Document environment variables
- [ ] Add project to main README.md (if beneficial)

**Documentation:**
- [ ] Write clear project purpose and goals
- [ ] Document setup and installation steps
- [ ] Document usage and testing instructions
- [ ] Add troubleshooting section (if applicable)

### Glossary

**To Be Added**: Define project-specific terms and acronyms as they emerge.

---

**Document Version**: 1.0
**Created By**: Claude (AI Assistant)
**Last Updated**: 2026-01-04

This is a living document. Keep it updated as the project evolves.
