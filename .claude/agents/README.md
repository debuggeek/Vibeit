# Custom Claude Agents

This directory contains custom Claude agents that are available globally across all projects in the Vibeit repository.

## What Are Custom Agents?

Custom agents are specialized AI assistants with specific system prompts and capabilities designed for particular tasks. They're built on the Claude Agent SDK and can be invoked within Claude Code to perform focused operations.

## Available Agents

### 1. PRD Generator (`prd-generator`)

**File**: `prd-generator.md`

**Purpose**: Generates comprehensive Product Requirements Documents from simple product ideas.

**Use Cases**:
- Quickly document new product ideas
- Create structured specifications for development teams
- Explore and flesh out feature concepts
- Standardize PRD format across projects

**Example Usage**:

In Claude Code, ask:
```
Use the prd-generator agent to create a PRD for a fitness tracking app
that gamifies workouts with achievements and social features
```

Or:
```
I need a PRD for a Chrome extension that blocks distracting websites
during work hours. Use the prd-generator agent.
```

**What You Get**:
- Executive summary with problem/solution
- Detailed functional and non-functional requirements
- User stories with acceptance criteria
- Technical architecture suggestions
- Success metrics and KPIs
- Risk assessment
- Timeline and milestones
- PRD saved as markdown file in `projects/[project-name]/PRD.md`

**Output Location**: The agent automatically creates/uses the appropriate project directory and saves the PRD there.

## How to Use Agents

### Method 1: Direct Request
Simply ask Claude Code to use a specific agent:
```
"Use the [agent-name] agent to [task description]"
```

### Method 2: Natural Language
Describe what you want and mention the agent:
```
"Can you use prd-generator to create documentation for [product idea]?"
```

## Agent Capabilities

Each agent has access to specific tools:

- **Write**: Create new files
- **Read**: Read existing files
- **Glob**: Find files by pattern
- **Grep**: Search file contents
- **Edit**: Modify existing files
- **Bash**: Run shell commands (if enabled)
- **WebFetch**: Fetch web content (if enabled)
- **WebSearch**: Search the web (if enabled)

Check each agent's YAML frontmatter to see which tools it can use.

## Creating Your Own Agents

Want to add a new custom agent? Here's how:

### 1. Create the Agent File

Create a new `.md` file in this directory:
```bash
touch .claude/agents/my-agent.md
```

### 2. Add YAML Frontmatter

Start with configuration:
```yaml
---
name: my-agent
description: Brief description of what this agent does
model: sonnet  # or haiku, opus
tools:
  - Write
  - Read
  - Glob
  - Grep
---
```

### 3. Write the System Prompt

Below the frontmatter, write detailed instructions:
```markdown
You are a [role] specialized in [task].

## Your Task
[Detailed description of what the agent should do]

## Guidelines
- [Guideline 1]
- [Guideline 2]

## Output Format
[How results should be structured]
```

### 4. Document the Agent

Add your agent to:
- This README.md (under "Available Agents")
- `/CLAUDE.md` (in the "Custom Agents" section)

### 5. Test It

Try using your agent to ensure it works as expected.

## Tips for Creating Effective Agents

1. **Be Specific**: Clear, detailed system prompts produce better results
2. **Define Output Format**: Specify exactly what format you want (Markdown, JSON, etc.)
3. **Include Examples**: Show the agent what good output looks like
4. **Set Boundaries**: Explain what the agent should NOT do
5. **Choose Tools Wisely**: Only grant access to tools the agent needs
6. **Use Appropriate Models**:
   - `haiku`: Fast, cost-effective for simple tasks
   - `sonnet`: Balanced performance for most tasks (default)
   - `opus`: Maximum capability for complex tasks

## Agent Best Practices

- **Single Responsibility**: Each agent should do one thing well
- **Reusable**: Design agents for multiple use cases, not one-off tasks
- **Well-Documented**: Include clear descriptions and usage examples
- **Tested**: Verify agents work before committing
- **Maintained**: Update agents as requirements evolve

## Examples of Good Agent Ideas

- **Code Reviewer**: Reviews code for bugs, style issues, security vulnerabilities
- **API Documentation Generator**: Creates API docs from code comments
- **Test Generator**: Writes unit tests for existing code
- **Changelog Creator**: Generates changelogs from git commits
- **Database Schema Designer**: Creates database schemas from requirements
- **Component Generator**: Scaffolds React/Vue components with boilerplate
- **Error Investigator**: Analyzes error logs and suggests fixes
- **Performance Analyzer**: Reviews code for performance bottlenecks

## Need Help?

- Check the [Claude Agent SDK documentation](https://platform.claude.com/docs/en/agent-sdk/overview)
- See examples in this directory
- Refer to `/CLAUDE.md` for repository guidelines

---

**Note**: Agents in this directory are available to all projects in the repository. For project-specific agents, create a `.claude/agents/` directory within the project.
