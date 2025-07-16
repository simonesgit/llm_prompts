# Automation Prompts for Multi-Repository Documentation Generation

> **Ready-to-use prompts for GitHub Copilot Chat and Multi-file Editing**

## 🎯 Usage Instructions

1. **Copy prompts exactly** as written (they're optimized for Copilot's latest features)
2. **Use @workspace** participant for full project context
3. **Enable multi-file editing** for prompts marked with 🔄
4. **Execute prompts in sequence** for best results
5. **Customize placeholders** in [brackets] as needed

---

## 📋 Phase 1: Project Discovery and Analysis

### 1.1 Initial Workspace Analysis

```
@workspace Analyze this multi-repository workspace and provide:

1. **Repository Inventory**: List all repositories with their primary purpose and technology stack
2. **Connection Analysis**: Identify technical dependencies, API connections, and data flow between repositories
3. **Architecture Overview**: Describe the overall system architecture and how repositories work together
4. **Documentation Gaps**: Identify what documentation currently exists and what's missing
5. **Recommended Documentation Structure**: Suggest the optimal documentation organization for this project

Format the response as a comprehensive analysis that will guide the documentation generation process.
```

### 1.2 Repository Classification

```
@workspace Classify each repository in this workspace by:

1. **Type**: (Frontend, Backend, API, Database, DevOps, Library, Tool, etc.)
2. **Technology Stack**: Primary languages, frameworks, and tools
3. **Complexity Level**: (Simple, Moderate, Complex) based on codebase size and architecture
4. **Documentation Priority**: (High, Medium, Low) based on importance to the overall system
5. **Integration Points**: How this repository connects to others

Create a summary table and recommend the documentation generation order.
```

---

## 🔄 Phase 2: Multi-File Documentation Generation

### 2.1 Create Documentation Structure (Multi-file Edit)

```
@workspace Using multi-file editing, create the complete documentation structure for this project:

1. **Create documentation folders** for each repository (format: {repo_name}_documentation/)
2. **Generate README.md** in each documentation folder with:
   - Repository overview and purpose
   - Technology stack and dependencies
   - Quick start guide
   - Links to detailed documentation

3. **Create main project.md** at workspace root with:
   - High-level project overview
   - Repository relationships and dependencies
   - System architecture summary
   - Getting started guide for the entire project

Ensure all files follow our custom instructions and include proper cross-references.
```

### 2.2 Generate Architecture Documentation (Multi-file Edit)

```
@workspace Using multi-file editing, create comprehensive architecture documentation:

1. **Generate architecture.md** for each repository containing:
   - System design and architectural patterns
   - Component relationships and data flow
   - Technology choices and rationale
   - Mermaid diagrams showing internal architecture

2. **Update project.md** with:
   - Overall system architecture diagram
   - Inter-repository communication patterns
   - Data flow across the entire system
   - Infrastructure and deployment architecture

Include proper Mermaid diagrams following validation guidelines from our existing prompts.
```

### 2.3 Generate API and Interface Documentation (Multi-file Edit)

```
@workspace Using multi-file editing, create API and interface documentation for repositories that expose APIs or interfaces:

1. **Generate api_documentation.md** for applicable repositories with:
   - Complete API endpoint documentation
   - Request/response examples
   - Authentication and authorization details
   - Error handling and status codes
   - SDK or client library information

2. **Generate integration_guide.md** in main documentation with:
   - How repositories communicate with each other
   - Shared interfaces and contracts
   - Integration patterns and best practices
   - Troubleshooting integration issues

Focus on practical examples and real usage scenarios.
```

---

## 🚀 Phase 3: Operational Documentation

### 3.1 Development and Deployment Workflows

```
@workspace Generate comprehensive workflow documentation:

1. **Create workflows.md** for each repository covering:
   - Development setup and environment configuration
   - Build and test processes
   - Code review and contribution guidelines
   - Release and deployment procedures

2. **Create deployment.md** for repositories with deployment requirements:
   - Infrastructure requirements
   - Deployment steps and automation
   - Environment configuration
   - Monitoring and health checks

3. **Update project.md** with:
   - Overall development workflow
   - Cross-repository development coordination
   - Release management across multiple repositories

Include actual commands and configuration examples from the codebase.
```

### 3.2 Troubleshooting and Maintenance

```
@workspace Create troubleshooting and maintenance documentation:

1. **Generate troubleshooting.md** for each repository with:
   - Common issues and their solutions
   - Debugging techniques and tools
   - Performance optimization tips
   - Error message explanations

2. **Create maintenance_guide.md** at project level with:
   - System health monitoring
   - Regular maintenance tasks
   - Backup and recovery procedures
   - Scaling considerations

Base solutions on actual code patterns and configurations found in the repositories.
```

---

## 🔗 Phase 4: Cross-Repository Integration

### 4.1 Dependency Mapping and Documentation

```
@workspace Analyze and document cross-repository dependencies:

1. **Create dependency_map.md** with:
   - Visual dependency graph using Mermaid
   - Detailed dependency analysis for each repository
   - Version compatibility requirements
   - Breaking change impact analysis

2. **Update each repository's README.md** with:
   - Dependencies on other repositories in this project
   - How this repository is used by others
   - Integration testing procedures

3. **Generate integration_testing.md** with:
   - End-to-end testing strategies
   - Cross-repository test scenarios
   - Continuous integration setup

Include actual dependency versions and configuration examples.
```

### 4.2 Data Flow and Communication Documentation

```
@workspace Document data flow and communication patterns:

1. **Create data_flow.md** with:
   - System-wide data flow diagrams
   - Data transformation points
   - Data storage and persistence patterns
   - Data security and privacy considerations

2. **Generate communication_patterns.md** with:
   - Inter-service communication protocols
   - Message formats and schemas
   - Event-driven architecture patterns
   - Synchronous vs asynchronous communication

Use Mermaid sequence diagrams and flowcharts to visualize complex interactions.
```

---

## 📊 Phase 5: Advanced Documentation

### 5.1 Performance and Scalability Documentation

```
@workspace Create performance and scalability documentation:

1. **Generate performance.md** for each repository with:
   - Performance characteristics and benchmarks
   - Bottlenecks and optimization opportunities
   - Resource requirements and scaling patterns
   - Monitoring and alerting setup

2. **Create scalability_guide.md** at project level with:
   - System-wide scaling strategies
   - Load balancing and distribution patterns
   - Database scaling considerations
   - Infrastructure scaling automation

Include actual performance metrics and configuration examples where available.
```

### 5.2 Security and Compliance Documentation

```
@workspace Generate security and compliance documentation:

1. **Create security.md** for each repository with:
   - Security requirements and implementations
   - Authentication and authorization patterns
   - Data protection and encryption
   - Security testing and validation

2. **Generate compliance_guide.md** at project level with:
   - Regulatory compliance requirements
   - Audit trails and logging
   - Data governance policies
   - Security incident response procedures

Focus on practical implementation details and actual security configurations.
```

---

## 🔍 Phase 6: Validation and Enhancement

### 6.1 Documentation Quality Review

```
@workspace Review and enhance the generated documentation:

1. **Validate completeness**: Check that all repositories have comprehensive documentation
2. **Verify accuracy**: Ensure technical details match the actual codebase
3. **Check consistency**: Confirm formatting and style consistency across all documents
4. **Test cross-references**: Verify all internal links work correctly
5. **Identify gaps**: Find any missing documentation or unclear sections

Provide a summary report with specific recommendations for improvements.
```

### 6.2 Documentation Navigation and Index

```
@workspace Create navigation aids and documentation index:

1. **Update project.md** with:
   - Complete table of contents for all documentation
   - Quick navigation links to key documents
   - Documentation maintenance guidelines

2. **Create DOCUMENTATION_INDEX.md** with:
   - Searchable index of all documentation topics
   - Cross-reference matrix showing relationships
   - Documentation update procedures

3. **Add navigation sections** to each repository's README.md with links to related documentation

Ensure the documentation is easily discoverable and navigable.
```

---

## 🎯 Specialized Prompts

### For Large Workspaces (10+ Repositories)

```
@workspace This workspace has many repositories. Let's process them in batches:

1. **Batch 1**: Analyze and document the [3-5] most critical repositories first
2. **Batch 2**: Process the [next 3-5] repositories with medium priority
3. **Batch 3**: Handle remaining repositories and create cross-references

Start with Batch 1 and focus on [specify repository names or types].
```

### For Microservices Architecture

```
@workspace This appears to be a microservices architecture. Create specialized documentation:

1. **Service catalog**: Complete inventory of all microservices
2. **API gateway documentation**: Central API management and routing
3. **Service mesh documentation**: Inter-service communication patterns
4. **Distributed tracing**: Request flow across services
5. **Circuit breaker patterns**: Fault tolerance and resilience

Focus on service discovery, load balancing, and failure handling patterns.
```

### For DevOps-Heavy Projects

```
@workspace This project has significant DevOps components. Create infrastructure-focused documentation:

1. **Infrastructure as Code**: Document all IaC templates and configurations
2. **CI/CD pipelines**: Complete pipeline documentation with flow diagrams
3. **Environment management**: Development, staging, and production environments
4. **Monitoring and observability**: Logging, metrics, and alerting setup
5. **Disaster recovery**: Backup, restore, and business continuity procedures

Include actual pipeline configurations and infrastructure diagrams.
```

---

## 💡 Tips for Optimal Results

### Before Running Prompts
- ✅ Ensure all repositories are accessible in the workspace
- ✅ Verify custom instructions are properly configured
- ✅ Enable multi-file editing preview features
- ✅ Close unnecessary files to improve performance

### During Execution
- 🔄 Use multi-file editing for prompts marked with 🔄
- ⏱️ Allow time for Copilot to analyze large workspaces
- 📝 Review and refine generated content before proceeding
- 🔗 Verify cross-references and links are accurate

### After Generation
- ✅ Run validation prompts to ensure quality
- 📋 Use the validation checklist for comprehensive review
- 🔄 Iterate on any sections that need improvement
- 📚 Keep documentation updated as code evolves

---

**Next Step**: [Workflow Automation →](./workflow_automation.md)