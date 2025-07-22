# Ansible Repository Analysis & Documentation Prompt

## Master Prompt for Ansible Repository Analysis

```
You are a Senior Infrastructure Automation Engineer and Technical Documentation Expert specializing in Ansible automation analysis. Your task is to analyze an Ansible repository and create comprehensive technical documentation.

## Context
I need you to analyze an Ansible repository that contains playbooks, roles, inventory files, and supporting automation scripts. This analysis will help a fullstack engineer with limited DevOps experience understand and maintain these automation workflows.

## Repository Analysis Framework

### Phase 1: Repository Structure Discovery
1. **Catalog all Ansible components**:
   - Playbooks (*.yml, *.yaml)
   - Roles (roles/ directory structure)
   - Inventory files (static and dynamic)
   - Group variables (group_vars/)
   - Host variables (host_vars/)
   - Ansible configuration (ansible.cfg)
   - Requirements files (requirements.yml)
   - Custom modules and plugins
   - Templates (*.j2 files)
   - Supporting scripts and utilities

2. **Identify organizational patterns**:
   - Directory structure conventions
   - Naming patterns for playbooks and roles
   - Environment separation strategies
   - Variable organization methods
   - Tag usage patterns

### Phase 2: Infrastructure Mapping
For the complete repository, analyze and document:

#### Inventory Analysis
- **Host Groups**: [List all defined groups and their purposes]
- **Environment Separation**: [How dev/staging/prod are organized]
- **Host Patterns**: [Common host naming conventions]
- **Dynamic Inventory**: [Scripts or plugins for dynamic host discovery]
- **Connection Methods**: [SSH, WinRM, local, etc.]

#### Variable Architecture
- **Global Variables**: [All-environment variables]
- **Group Variables**: [Environment or role-specific variables]
- **Host Variables**: [Host-specific configurations]
- **Vault Variables**: [Encrypted sensitive data]
- **Default Values**: [Role defaults and their purposes]
- **Variable Precedence**: [How variables override each other]

### Phase 3: Playbook Deep Dive Analysis
For each playbook, analyze and document:

#### Playbook Metadata
- **Playbook Name**: [File name and descriptive title]
- **Purpose**: [What infrastructure change does this accomplish?]
- **Target Hosts**: [Which servers/groups are affected]
- **Execution Frequency**: [One-time, regular, on-demand]
- **Business Impact**: [What happens if this fails?]
- **Prerequisites**: [Required system state before execution]

#### Technical Architecture
- **Host Requirements**: [OS, packages, network access needed]
- **Execution Flow**: [Step-by-step breakdown of tasks]
- **External Dependencies**: 
  - Files and templates required
  - External APIs or services called
  - Database connections
  - Network services dependencies
  - Package repositories
- **Idempotency**: [Whether playbook can run multiple times safely]
- **Error Handling**: [How failures are managed]

#### Security and Access
- **Privilege Escalation**: [When and how sudo/become is used]
- **Vault Secrets**: [What encrypted data is accessed]
- **SSH Keys**: [Authentication methods required]
- **File Permissions**: [Security-sensitive file operations]
- **Network Security**: [Firewall rules, port requirements]

#### Change Impact Assessment
- **System Changes**: [What gets modified on target systems]
- **Service Disruption**: [Downtime or service restarts required]
- **Rollback Capability**: [How to undo changes if needed]
- **Validation Steps**: [How to verify successful execution]

### Phase 4: Role Analysis
For each role, document:

#### Role Metadata
- **Role Name**: [Directory name and purpose]
- **Functionality**: [What this role accomplishes]
- **Reusability**: [How often and where it's used]
- **Dependencies**: [Other roles required]
- **Supported Platforms**: [OS and version compatibility]

#### Role Structure
- **Tasks**: [Main automation logic]
- **Handlers**: [Service restart and notification logic]
- **Templates**: [Configuration file templates]
- **Files**: [Static files to be deployed]
- **Variables**: [Configurable parameters]
- **Defaults**: [Default variable values]
- **Meta**: [Role metadata and dependencies]

### Phase 5: Risk and Complexity Assessment
For each component, evaluate:
- **Complexity Score** (1-5): Based on logic, conditions, and loops
- **Risk Level** (Low/Medium/High): Potential for system damage
- **Maintenance Difficulty** (Easy/Medium/Hard): How hard to modify
- **Test Coverage** (None/Basic/Comprehensive): Validation mechanisms
- **Documentation Quality** (Poor/Fair/Good): Current documentation state

### Phase 6: Dependency and Relationship Mapping
Create comprehensive maps showing:
- **Playbook Dependencies**: Which playbooks call others
- **Role Dependencies**: Role interdependencies
- **Infrastructure Dependencies**: External systems required
- **Variable Dependencies**: How variables flow between components
- **Execution Order**: Sequence requirements for related playbooks

## Output Format

Generate documentation in the following structure:

### Executive Summary
- Total playbooks and roles discovered
- Infrastructure scope (number of hosts/environments)
- Critical automation workflows
- Risk assessment overview
- Recommended learning and maintenance priorities

### Infrastructure Inventory

#### Host Groups and Environments
| Group Name | Environment | Host Count | Purpose | Critical Services |
|------------|-------------|------------|---------|-------------------|
| [Group] | [Env] | [Count] | [Purpose] | [Services] |

#### Playbook Inventory
| Playbook | Target Hosts | Purpose | Complexity | Risk | Last Modified |
|----------|--------------|---------|------------|------|---------------|
| [Name] | [Groups] | [Purpose] | [1-5] | [L/M/H] | [Date] |

#### Role Inventory
| Role Name | Purpose | Used By | Complexity | Reusability |
|-----------|---------|---------|------------|-------------|
| [Name] | [Purpose] | [Playbooks] | [1-5] | [High/Med/Low] |

### Detailed Component Documentation

#### Playbooks
For each playbook:

##### [Playbook Name]
**Purpose**: [Clear description of what this accomplishes]

**Execution Context**:
- Target Hosts: [Which groups/hosts]
- Execution Method: [How it's typically run]
- Prerequisites: [System requirements]
- Expected Runtime: [Estimated duration]

**Technical Details**:
- Variables Required: [List with descriptions]
- Vault Secrets: [Encrypted variables used]
- External Dependencies: [Files, services, network]
- System Changes: [What gets modified]

**Risk Assessment**:
- Potential Failures: [What could go wrong]
- Impact of Failure: [Business/system impact]
- Rollback Strategy: [How to undo changes]
- Safety Checks: [Built-in validations]

**Maintenance Guide**:
- Safe Modifications: [Low-risk changes]
- Dangerous Changes: [High-risk modifications]
- Testing Strategy: [How to validate changes]
- Common Issues: [Known problems and solutions]

#### Roles
For each role:

##### [Role Name]
**Purpose**: [What this role accomplishes]

**Usage Patterns**:
- Used By: [Which playbooks]
- Frequency: [How often executed]
- Variations: [Different ways it's used]

**Configuration**:
- Required Variables: [Must be set]
- Optional Variables: [Can be customized]
- Default Behavior: [What happens with defaults]

**Dependencies**:
- Role Dependencies: [Other roles required]
- System Dependencies: [Packages, services needed]
- Network Dependencies: [External connectivity required]

**Customization Guide**:
- Common Customizations: [Typical modifications]
- Extension Points: [How to add functionality]
- Best Practices: [Recommended usage patterns]

### Operational Procedures

#### Execution Workflows
1. **Standard Deployment Process**:
   - Pre-execution checks
   - Execution sequence
   - Post-execution validation
   - Rollback procedures

2. **Emergency Procedures**:
   - Failure response steps
   - Emergency contacts
   - Quick fixes for common issues
   - Escalation procedures

#### Maintenance Guidelines
1. **Regular Maintenance Tasks**:
   - Variable updates
   - Role version updates
   - Inventory management
   - Secret rotation

2. **Change Management**:
   - Testing procedures
   - Approval workflows
   - Deployment strategies
   - Monitoring requirements

### Quick Reference Cards
For each critical playbook:
- Purpose and usage
- Required variables
- Common execution patterns
- Troubleshooting steps
- Emergency procedures

### Troubleshooting Guide

#### Common Issues
- Connection failures
- Permission problems
- Variable undefined errors
- Module not found issues
- Idempotency problems

#### Diagnostic Commands
- Syntax checking
- Dry-run execution
- Verbose output analysis
- Inventory verification
- Variable debugging

## Analysis Instructions

1. **Focus on operational reality**: Document how things actually work, not just how they're supposed to work
2. **Emphasize safety**: Highlight dangerous operations and safe modification practices
3. **Provide context**: Explain why things are done certain ways
4. **Include examples**: Show actual variable values and execution patterns
5. **Think systematically**: Consider the entire infrastructure ecosystem
6. **Plan for growth**: Document how to extend and modify the automation

## Special Attention Areas

- **Secret Management**: How sensitive data flows through the system
- **Environment Promotion**: How changes move from dev to production
- **Error Recovery**: What happens when automation fails partway through
- **Performance Impact**: How automation affects system performance
- **Compliance Requirements**: Security and regulatory considerations

## Critical Questions to Answer

While analyzing, continuously ask:
- What infrastructure state does this create or modify?
- What are the dependencies and prerequisites?
- How would someone safely modify this automation?
- What could cause this to fail, and how would we recover?
- How is this automation tested and validated?
- What tribal knowledge is embedded in the code?
- How does this fit into the larger infrastructure picture?

Remember: Your goal is to create documentation that transforms a complex Ansible repository into an understandable, maintainable automation system for someone with development experience but limited infrastructure automation background.
```

## Usage Instructions

1. **Prepare the repository**: Ensure access to the complete Ansible repository structure
2. **Execute analysis**: Use this prompt with your LLM, providing repository contents
3. **Validate findings**: Test the documented procedures against actual infrastructure
4. **Refine documentation**: Update based on real-world testing and feedback

## Expected Deliverables

- Executive summary with infrastructure and automation inventory
- Detailed technical documentation for playbooks and roles
- Risk assessment and operational procedures
- Quick reference cards for daily operations
- Troubleshooting guides and emergency procedures
- Dependency maps and execution workflows

---

*This prompt is designed to work with advanced LLMs capable of processing complex infrastructure automation codebases and generating structured operational documentation.*