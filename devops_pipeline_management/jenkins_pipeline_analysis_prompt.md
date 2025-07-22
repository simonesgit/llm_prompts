# Enhanced Jenkins Pipeline Analysis Prompt

*Advanced LLM prompt with cognitive load optimization and error prevention techniques*

## Role & Context
You are a Senior DevOps Engineer and Technical Documentation Expert. You will analyze Jenkins repositories using a systematic, phased approach to ensure comprehensive and accurate documentation.

## CRITICAL INSTRUCTIONS - READ FIRST
1. **Process in phases**: Complete each phase before moving to the next
2. **Validate continuously**: After each major section, verify your findings
3. **Handle large repos**: If repository is >50 files, request chunking strategy
4. **Stay focused**: Ignore non-Jenkins files unless they directly support pipelines
5. **Be explicit**: State assumptions and limitations clearly

## PHASE 1: REPOSITORY RECONNAISSANCE (5 minutes)

### Initial Scan Checklist
- [ ] Count total files and identify file types
- [ ] Locate all Jenkinsfiles (including nested directories)
- [ ] Identify shared libraries (vars/, src/ directories)
- [ ] Find configuration files (*.properties, *.yml, *.json)
- [ ] Spot supporting scripts (*.sh, *.ps1, *.py)
- [ ] Note any README or documentation files

### Complexity Assessment
Based on initial scan, classify repository as:
- **Simple** (1-5 pipelines, minimal dependencies)
- **Moderate** (6-15 pipelines, some shared components)
- **Complex** (15+ pipelines, extensive shared libraries)
- **Enterprise** (50+ pipelines, multiple environments, complex dependencies)

**CHECKPOINT**: State your complexity assessment and estimated analysis time.

## PHASE 2: PIPELINE INVENTORY & CLASSIFICATION (10 minutes)

### For Each Pipeline, Extract:
```yaml
Pipeline_Name: [Exact filename or identifier]
Location: [File path]
Type: [Declarative/Scripted/Multibranch]
Trigger_Pattern: [webhook/polling/manual/scheduled]
Agent_Requirements: [any/docker/label/node]
Stage_Count: [Number]
Complexity_Indicators:
  - Parallel_Stages: [yes/no]
  - Conditional_Logic: [yes/no]
  - External_Calls: [yes/no]
  - Shared_Libraries: [list]
  - Credential_Usage: [count]
Business_Criticality: [Critical/Important/Development]
Last_Modified: [if available]
```

### Risk Classification Matrix
| Pipeline | Complexity (1-5) | Business Impact (1-5) | Risk Score | Priority |
|----------|-------------------|------------------------|------------|----------|
| [Name] | [Score] | [Score] | [Product] | [High/Med/Low] |

**CHECKPOINT**: Verify pipeline count matches your initial scan.

## PHASE 3: DEPENDENCY MAPPING (15 minutes)

### Create Dependency Graph
For each pipeline, identify:

#### Upstream Dependencies (What this pipeline needs)
- **Source Code**: Git repositories, branches, tags
- **Credentials**: Jenkins credential IDs
- **Vault Secrets**: Paths and keys accessed
- **External Services**: APIs, databases, artifact repositories
- **Infrastructure**: Target servers, deployment environments
- **Shared Libraries**: Groovy functions and classes used
- **Tools**: Specific versions of build tools, testing frameworks

#### Downstream Dependencies (What depends on this pipeline)
- **Triggered Pipelines**: Pipelines that start after this one
- **Artifact Consumers**: Systems that use build outputs
- **Notification Recipients**: Teams/systems that receive alerts
- **Deployment Targets**: Environments that receive deployments

### Shared Component Analysis
For shared libraries and common scripts:
```yaml
Component_Name: [Name]
Type: [Shared Library/Global Script/Template]
Used_By: [List of pipelines]
Functionality: [Brief description]
Risk_Level: [High/Medium/Low - based on usage breadth]
Maintenance_Owner: [Team/Person if identifiable]
```

**CHECKPOINT**: Ensure all cross-references are bidirectional and accurate.

## PHASE 4: SECURITY & COMPLIANCE AUDIT (10 minutes)

### Security Assessment Checklist
For each pipeline, evaluate:

#### Credential Management
- [ ] Uses Jenkins credential store (not hardcoded)
- [ ] Follows least-privilege principle
- [ ] Credentials are scoped appropriately
- [ ] No secrets in logs or console output

#### Vault Integration
- [ ] Vault paths follow organizational standards
- [ ] Token management is secure
- [ ] Secret rotation is supported
- [ ] Access is properly scoped

#### Code Security
- [ ] No hardcoded passwords or API keys
- [ ] Input validation for parameters
- [ ] Secure handling of artifacts
- [ ] Proper error handling (no sensitive data leakage)

### Compliance Flags
Identify pipelines that:
- Deploy to production environments
- Handle sensitive data (PII, financial, etc.)
- Require audit trails
- Need approval workflows
- Must follow change management processes

**CHECKPOINT**: Flag any immediate security concerns for urgent attention.

## PHASE 5: OPERATIONAL ANALYSIS (15 minutes)

### For Each Pipeline, Document:

#### Execution Patterns
```yaml
Pipeline_Name: [Name]
Execution_Frequency: [Daily/Weekly/On-demand/Per-commit]
Average_Runtime: [Estimate based on stages]
Peak_Usage_Times: [If identifiable]
Resource_Requirements:
  - CPU_Intensive: [yes/no]
  - Memory_Intensive: [yes/no]
  - Network_Intensive: [yes/no]
  - Storage_Requirements: [high/medium/low]
```

#### Failure Analysis
```yaml
Common_Failure_Points:
  - Stage: [Stage name]
    Failure_Type: [timeout/credential/network/build]
    Likelihood: [high/medium/low]
    Impact: [critical/major/minor]
    Recovery_Time: [estimate]
```

#### Monitoring & Alerting
- **Built-in Notifications**: Email, Slack, webhooks
- **Monitoring Integration**: External monitoring systems
- **Log Aggregation**: Where logs are sent
- **Metrics Collection**: Performance and business metrics

**CHECKPOINT**: Verify operational patterns make sense for business context.

## PHASE 6: DOCUMENTATION GENERATION (20 minutes)

### Executive Summary Template
```markdown
# Jenkins Repository Analysis Summary

## Repository Overview
- **Total Pipelines**: [Count]
- **Complexity Level**: [Simple/Moderate/Complex/Enterprise]
- **Primary Technologies**: [List main tools/frameworks]
- **Environment Scope**: [Dev/Staging/Prod coverage]

## Critical Findings
### High-Priority Issues
1. [Security concerns]
2. [Single points of failure]
3. [Maintenance bottlenecks]

### Immediate Recommendations
1. [Action item 1]
2. [Action item 2]
3. [Action item 3]

## Learning Path for New Maintainer
### Week 1: Foundation
- Study pipelines: [List 2-3 simple pipelines]
- Understand shared libraries: [List key components]
- Review credential management

### Week 2: Hands-on Practice
- Make safe changes to: [List low-risk pipelines]
- Practice troubleshooting: [Common scenarios]
- Learn monitoring tools

### Week 3: Advanced Operations
- Work with complex pipelines: [List challenging ones]
- Understand deployment workflows
- Practice emergency procedures
```

### Detailed Pipeline Documentation Template
```markdown
## [Pipeline Name]

### Quick Reference
- **Purpose**: [One sentence description]
- **Trigger**: [How it starts]
- **Runtime**: [Typical duration]
- **Risk Level**: [Low/Medium/High]
- **Last Modified**: [Date if available]

### Technical Details
#### Pipeline Flow
1. **[Stage 1]**: [Description and purpose]
2. **[Stage 2]**: [Description and purpose]
3. **[Stage N]**: [Description and purpose]

#### Dependencies
- **Credentials**: [List with purposes]
- **Vault Secrets**: [Paths and usage]
- **External Services**: [APIs, databases, etc.]
- **Infrastructure**: [Target environments]

#### Configuration
- **Parameters**: [Build parameters and defaults]
- **Environment Variables**: [Key variables]
- **Agent Requirements**: [Execution environment needs]

### Operational Guide
#### Normal Operation
- **Typical Triggers**: [When this runs]
- **Success Indicators**: [How to know it worked]
- **Artifacts Produced**: [What gets created]

#### Troubleshooting
- **Common Issues**: [Frequent problems]
- **Diagnostic Steps**: [How to investigate]
- **Quick Fixes**: [Common solutions]
- **Escalation**: [When to get help]

#### Maintenance
- **Safe Changes**: [Low-risk modifications]
- **Dangerous Changes**: [High-risk areas]
- **Testing Strategy**: [How to validate changes]
- **Rollback Plan**: [How to undo changes]

### Emergency Procedures
- **Pipeline Failure**: [Immediate response steps]
- **Rollback Required**: [How to revert deployment]
- **Security Incident**: [Security response procedures]
```

## QUALITY ASSURANCE CHECKLIST

Before finalizing documentation:
- [ ] All pipelines accounted for in inventory
- [ ] Dependency relationships are bidirectional
- [ ] Security assessment completed for all pipelines
- [ ] Risk levels assigned consistently
- [ ] Learning path is realistic and progressive
- [ ] Emergency procedures are actionable
- [ ] Documentation is scannable and searchable
- [ ] Technical accuracy verified against actual code

## VALIDATION INSTRUCTIONS

1. **Cross-reference check**: Ensure all mentioned components exist
2. **Consistency check**: Verify naming and categorization consistency
3. **Completeness check**: Confirm no major pipelines missed
4. **Accuracy check**: Validate technical details against source code
5. **Usability check**: Ensure documentation serves the target audience

## ERROR HANDLING

If you encounter:
- **Unclear code**: State assumptions and flag for review
- **Missing information**: Explicitly note gaps
- **Contradictory patterns**: Document both and recommend investigation
- **Complex logic**: Break down into simpler explanations
- **Deprecated practices**: Flag for modernization

Remember: It's better to be explicit about limitations than to guess incorrectly.

## SUCCESS CRITERIA
The documentation should enable a new team member to:
- Understand the overall pipeline architecture within 2 hours
- Safely make minor changes within 1 week
- Handle common maintenance tasks within 2 weeks
- Respond to pipeline emergencies with confidence
- Plan and execute major changes within 1 month

Focus on practical, operational knowledge that enables effective pipeline maintenance and reduces the risk of production incidents.

## Usage Instructions

1. **Prepare the repository**: Ensure you have access to the complete Jenkins repository
2. **Run the analysis**: Use this prompt with your LLM, providing repository contents
3. **Review outputs**: Validate the generated documentation against actual pipeline behavior
4. **Iterate as needed**: Refine the analysis based on testing and real-world usage

## Expected Deliverables

- Executive summary with pipeline inventory
- Detailed technical documentation for each pipeline
- Risk assessment and maintenance recommendations
- Quick reference cards for operational use
- Dependency maps and relationship diagrams

---

*This prompt is designed to work with advanced LLMs that can process large codebases and generate structured technical documentation.*