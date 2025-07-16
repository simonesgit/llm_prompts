# Custom Instructions Template for Multi-Repository Documentation

> **Copy this content to your `.github/copilot-instructions.md` file**

---

# Project Documentation Standards

## 🎯 Project Context

This is a multi-repository project workspace where each repository represents a component of a larger system. Generate documentation that:

- **Maintains consistency** across all repository documentation
- **Identifies connections** between repositories and components
- **Provides clear navigation** between related documentation
- **Follows standardized formatting** for professional presentation

## 📋 Documentation Structure Requirements

### For Individual Repository Documentation

Each `{repo_name}_documentation/` folder should contain:

1. **README.md** - Repository overview and quick start
2. **architecture.md** - Technical architecture and design patterns
3. **api_documentation.md** - API endpoints, interfaces, and contracts (if applicable)
4. **workflows.md** - Development workflows and processes
5. **deployment.md** - Deployment and infrastructure details (if applicable)
6. **troubleshooting.md** - Common issues and solutions

### For Main Project Documentation

- **project.md** - High-level project overview at workspace root
- Cross-repository connections and dependencies
- System architecture overview
- Getting started guide for the entire project

## 🎨 Formatting Standards

### Markdown Conventions

```markdown
# Main Title (H1) - Only one per document
## Section Headers (H2) - Primary sections
### Subsection Headers (H3) - Detailed breakdowns
#### Detail Headers (H4) - Specific items

- Use bullet points for lists
- Use numbered lists for sequential steps
- Use `code blocks` for file names, commands, and code snippets
- Use **bold** for emphasis on important terms
- Use *italics* for notes and clarifications
```

### Code Block Standards

```bash
# Always specify language for syntax highlighting
# Use comments to explain complex commands
# Include full paths when referencing files
```

```mermaid
# Use Mermaid for diagrams when possible
# Follow validation guidelines from existing prompts
# Keep diagrams simple and readable
```

### Cross-Reference Format

```markdown
# Use relative paths for internal references
[Repository Documentation](../repo1_documentation/README.md)
[Main Project Overview](../project.md)

# Use descriptive link text
[API Documentation for User Service](../user_service_documentation/api_documentation.md)
```

## 🔗 Repository Connection Analysis

When analyzing repositories, always identify:

### Technical Connections
- **API Dependencies**: Which repos call APIs from other repos
- **Shared Libraries**: Common dependencies or shared code
- **Data Flow**: How data moves between repositories
- **Configuration Dependencies**: Shared configuration or environment variables

### Deployment Connections
- **Infrastructure Dependencies**: Shared infrastructure components
- **Deployment Order**: Which services must be deployed first
- **Environment Coordination**: Shared environments or resources

### Development Connections
- **Shared Development Tools**: Common build tools, testing frameworks
- **Code Style Consistency**: Shared linting rules, formatting standards
- **Documentation Standards**: Consistent documentation approaches

## 📊 Documentation Content Guidelines

### Executive Summary Requirements
- **Purpose**: What does this repository/project accomplish?
- **Technology Stack**: Key technologies, frameworks, languages
- **Key Features**: Main functionality and capabilities
- **Dependencies**: Critical external dependencies
- **Status**: Development status, maturity level

### Technical Documentation Requirements
- **Architecture Diagrams**: Visual representation of system design
- **API Documentation**: Complete endpoint documentation with examples
- **Configuration Guide**: Environment setup and configuration
- **Development Setup**: Step-by-step development environment setup
- **Testing Guide**: How to run tests and validate functionality

### Operational Documentation Requirements
- **Deployment Instructions**: Step-by-step deployment process
- **Monitoring and Logging**: How to monitor the system
- **Troubleshooting**: Common issues and their solutions
- **Performance Considerations**: Known performance characteristics
- **Security Considerations**: Security requirements and best practices

## 🎯 Quality Standards

### Completeness Criteria
- [ ] All major components documented
- [ ] All public APIs documented with examples
- [ ] All configuration options explained
- [ ] All deployment steps covered
- [ ] All dependencies clearly listed

### Clarity Criteria
- [ ] Technical jargon explained or avoided
- [ ] Step-by-step instructions provided
- [ ] Examples included for complex concepts
- [ ] Visual aids (diagrams, screenshots) used appropriately
- [ ] Consistent terminology throughout

### Maintainability Criteria
- [ ] Documentation structure is logical and navigable
- [ ] Cross-references are accurate and helpful
- [ ] Version information is included where relevant
- [ ] Update procedures are documented
- [ ] Contact information for maintainers is provided

## 🚀 Automation Preferences

### When Generating Documentation
1. **Start with repository analysis** - Understand the codebase before documenting
2. **Identify patterns** - Look for common patterns across repositories
3. **Generate comprehensive content** - Don't just create templates, fill them with actual analysis
4. **Include practical examples** - Use real code examples from the repository
5. **Create actionable content** - Documentation should help users accomplish tasks

### Multi-File Generation Preferences
- Generate multiple documentation files simultaneously when possible
- Maintain consistency across all generated files
- Include cross-references between related documentation
- Update existing files rather than overwriting when appropriate

### Error Handling
- If a repository type is unclear, ask for clarification
- If dependencies are complex, create dependency diagrams
- If APIs are extensive, prioritize the most commonly used endpoints
- If deployment is complex, break it into phases

## 🔍 Analysis Depth Preferences

### Code Analysis
- **Surface Level**: File structure, main entry points, configuration
- **Functional Level**: Key functions, classes, modules, and their purposes
- **Integration Level**: How components interact, data flow, external dependencies
- **Architectural Level**: Design patterns, architectural decisions, scalability considerations

### Documentation Generation Priority
1. **Critical Path Documentation**: Essential for getting started
2. **API Documentation**: For integration and usage
3. **Architecture Documentation**: For understanding and maintenance
4. **Operational Documentation**: For deployment and monitoring
5. **Advanced Documentation**: For optimization and troubleshooting

---

## 💡 Special Instructions for This Project

> **Customize this section based on your specific project needs**

### Project-Specific Requirements
- [Add any specific technologies, frameworks, or patterns used in your project]
- [Include any specific documentation requirements or standards]
- [Note any particular areas that need special attention]

### Team Preferences
- [Add team-specific preferences for documentation style]
- [Include any specific terminology or naming conventions]
- [Note any particular tools or platforms used for documentation]

### Business Context
- [Add business context that might affect technical decisions]
- [Include any compliance or regulatory requirements]
- [Note any specific user personas or use cases]

---

*These instructions ensure consistent, comprehensive, and useful documentation across all repositories in the project workspace.*