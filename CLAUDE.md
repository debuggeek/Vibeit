# CLAUDE.md - AI Assistant Guide for Vibeit

> **Last Updated**: 2026-01-04
>
> **Project Status**: Greenfield - Initial Development Phase

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
10. [Future Roadmap](#future-roadmap)

---

## Project Overview

### About Vibeit

**Project Name**: Vibeit
**Description**: Fir vibing
**Repository**: debuggeek/Vibeit

### Tech Stack

**Status**: To be determined during initial setup

When the tech stack is established, document here:
- Frontend framework (React, Vue, Svelte, etc.)
- Backend framework (Node.js, Python, Go, etc.)
- Database (PostgreSQL, MongoDB, etc.)
- Build tools (Vite, Webpack, etc.)
- Testing frameworks (Jest, Vitest, Pytest, etc.)

---

## Current State

### Repository Status

- **Initialization Date**: January 4, 2026
- **Current Branch**: `claude/add-claude-documentation-Yye2a`
- **Commits**: 1 (Initial commit)
- **Code Files**: 0
- **Configuration Files**: 0

### What Exists

```
/home/user/Vibeit/
├── .git/           # Git repository metadata
├── README.md       # Basic project description
└── CLAUDE.md       # This file
```

### What Needs to Be Created

This is a greenfield project. The following components need to be established:

- [ ] Project initialization (package.json or equivalent)
- [ ] Directory structure (src/, tests/, docs/, etc.)
- [ ] Core dependencies and tooling
- [ ] Development environment setup
- [ ] Linting and formatting configuration
- [ ] Testing framework setup
- [ ] CI/CD pipeline configuration
- [ ] Documentation structure

---

## Repository Structure

### Recommended Structure (To Be Implemented)

Once the project type is determined, establish a clear directory structure. Example for a typical web application:

```
Vibeit/
├── .github/              # GitHub workflows and templates
│   └── workflows/        # CI/CD workflows
├── src/                  # Source code
│   ├── components/       # Reusable components
│   ├── pages/           # Page components
│   ├── services/        # Business logic and API calls
│   ├── utils/           # Utility functions
│   ├── types/           # TypeScript type definitions
│   ├── config/          # Configuration files
│   └── assets/          # Static assets
├── tests/               # Test files
│   ├── unit/           # Unit tests
│   ├── integration/    # Integration tests
│   └── e2e/            # End-to-end tests
├── docs/                # Additional documentation
├── public/              # Public assets (if web app)
├── scripts/             # Build and utility scripts
├── .gitignore          # Git ignore rules
├── package.json         # Dependencies and scripts (if Node.js)
├── tsconfig.json        # TypeScript configuration (if applicable)
├── README.md            # Project overview
└── CLAUDE.md            # This file
```

---

## Development Workflow

### Setting Up the Development Environment

**To Be Documented**: Once the project is initialized, document:

1. Prerequisites (Node.js version, Python version, etc.)
2. Installation steps
3. Environment variables required
4. Database setup (if applicable)
5. Running the development server
6. Building for production

### Common Commands

**To Be Documented**: Common commands will be added here, such as:

```bash
# Example (adjust based on actual project setup)
npm install          # Install dependencies
npm run dev          # Start development server
npm run build        # Build for production
npm run test         # Run tests
npm run lint         # Lint code
npm run format       # Format code
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

## Future Roadmap

### Immediate Next Steps

1. **Determine Project Type**: Decide what Vibeit will be (web app, mobile app, API, etc.)
2. **Choose Tech Stack**: Select frameworks, languages, and tools
3. **Initialize Project**: Set up package manager and basic structure
4. **Configure Development Tools**: Set up linting, formatting, testing
5. **Establish Conventions**: Define coding standards and patterns
6. **Set Up CI/CD**: Configure automated testing and deployment
7. **Update Documentation**: Expand this file as decisions are made

### Areas to Document as Project Grows

- **Architecture Decisions**: Document major architectural choices and rationale
- **API Design**: If building an API, document endpoints, authentication, etc.
- **Database Schema**: Document data models and relationships
- **Deployment Process**: Document how to deploy to staging/production
- **Troubleshooting Guide**: Common issues and solutions
- **Performance Considerations**: Optimization strategies and benchmarks

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

### Project Initialization Checklist

When setting up the project, complete these tasks and document results above:

- [ ] Choose and document tech stack
- [ ] Initialize package manager (npm, pip, cargo, etc.)
- [ ] Set up directory structure
- [ ] Configure linting tools (ESLint, Pylint, etc.)
- [ ] Configure code formatting (Prettier, Black, etc.)
- [ ] Set up testing framework (Jest, Pytest, etc.)
- [ ] Configure TypeScript (if applicable)
- [ ] Set up build tools (Vite, Webpack, etc.)
- [ ] Create .gitignore file
- [ ] Set up pre-commit hooks (Husky, pre-commit, etc.)
- [ ] Configure CI/CD (GitHub Actions, etc.)
- [ ] Document environment variables
- [ ] Create contributing guidelines
- [ ] Add license file
- [ ] Update README.md with setup instructions
- [ ] Update this CLAUDE.md with specific conventions

### Glossary

**To Be Added**: Define project-specific terms and acronyms as they emerge.

---

**Document Version**: 1.0
**Created By**: Claude (AI Assistant)
**Last Updated**: 2026-01-04

This is a living document. Keep it updated as the project evolves.
