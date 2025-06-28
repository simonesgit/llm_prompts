# 🚀 Master LLM Project Analysis Prompt

**Copy and paste this entire prompt into your LLM chat interface (VS Code Copilot, ChatGPT, Claude, etc.) to automatically analyze your multi-repository application ecosystem.**

---

## 📋 ANALYSIS REQUEST

I need you to perform a comprehensive analysis of my multi-repository application ecosystem. Please analyze all repositories in my workspace and generate complete documentation in the `./documentation/` folder.

### 🎯 ANALYSIS SCOPE

**Target Directory Structure:**
```
📁 [MY_ROOT_PATH]/
├── [source-repo-1]/          # Source code repositories
├── [source-repo-2]/
├── [infrastructure-repo]/    # Infrastructure as code
├── [cicd-repo]/             # CI/CD pipelines
├── [config-repo]/           # Configuration files
└── 📋 documentation/        # ← Generate all analysis here
```

### 🔍 REQUIRED ANALYSIS COMPONENTS

#### 1. **Comprehensive Project Analysis** (Priority: HIGH)
- **Technology Stack Discovery**: Identify all languages, frameworks, databases, tools
- **Architecture Mapping**: System components, service interactions, data flow
- **Module Dependency Analysis**: Cross-repository dependencies and relationships
- **Script Path Documentation**: Complete relative paths from repository root for ALL scripts
- **Multi-Script Workflow Mapping**: Execution order, dependencies, contexts
- **Integration Points**: APIs, databases, external services, message queues
- **Flexible Repository Detection**: Automatically identify project structure (monorepo, multi-repo, embedded CI/CD)

#### 2. **Workflow Mapping & Visualization** (Priority: HIGH)
- **End-to-End Process Flows**: Development → Testing → Deployment
- **Cross-Repository Workflows**: How repositories interact during operations
- **Script Integration Documentation**: When, where, and how scripts execute
- **Mermaid Diagrams**: System architecture, sequence flows, state transitions
- **Environment Management**: Development, staging, production workflows
- **Individual Script Flow Diagrams**: Create detailed flow diagrams for each significant script
- **Embedded CI/CD Detection**: Identify Jenkins files, GitHub Actions, or other CI/CD configurations within source repositories

#### 3. **DevOps & CI/CD Analysis** (Priority: HIGH)
- **Pipeline Discovery**: Jenkins, GitHub Actions, GitLab CI, custom scripts
- **Infrastructure Analysis**: Terraform, Kubernetes, Docker, cloud resources
- **Deployment Workflows**: Build → Test → Deploy → Monitor
- **Environment Configuration**: Variables, secrets, configuration management
- **Script Execution Contexts**: Build scripts, deployment scripts, maintenance scripts
- **Dynamic CI/CD Location Handling**: Analyze CI/CD configurations regardless of their location (dedicated repos, source repos, or mixed)

#### 4. **Code Quality & Security Assessment** (Priority: MEDIUM)
- **Redundancy Detection**: Duplicate code, configurations, scripts across repositories
- **Security Analysis**: Vulnerability assessment, secret management, access controls
- **Performance Analysis**: Bottlenecks, optimization opportunities
- **Code Quality Metrics**: Maintainability, complexity, documentation coverage

#### 5. **Enhancement Strategies** (Priority: MEDIUM)
- **Optimization Recommendations**: Performance, security, maintainability improvements
- **Automation Opportunities**: Manual processes that can be automated
- **Best Practices Implementation**: Industry standards and conventions
- **Technical Debt Assessment**: Areas requiring refactoring or updates

### 📊 OUTPUT REQUIREMENTS

#### **Documentation Structure** (Generate in `./documentation/`):
```
📋 documentation/
├── 📊 01_system_overview/
│   ├── architecture_summary.md
│   ├── technology_stack.md
│   ├── service_dependencies.md
│   └── integration_points.md
├── 🔄 02_workflows/
│   ├── development_workflow.md
│   ├── build_pipeline.md
│   ├── deployment_process.md
│   └── maintenance_procedures.md
├── 📝 03_scripts_inventory/
│   ├── complete_script_list.md
│   ├── execution_contexts.md
│   ├── dependency_mapping.md
│   ├── multi_script_workflows.md
│   ├── individual_script_flows.md
│   └── dynamic_structure_analysis.md
├── 📈 04_diagrams/
│   ├── system_architecture.mermaid
│   ├── workflow_sequences.mermaid
│   ├── service_interactions.mermaid
│   ├── deployment_flow.mermaid
│   └── script_flows/
│       ├── [script_name]_flow.mermaid
│       ├── build_process_flow.mermaid
│       ├── deployment_flow.mermaid
│       └── maintenance_scripts_flow.mermaid
├── 🔍 05_analysis_reports/
│   ├── code_quality_assessment.md
│   ├── security_analysis.md
│   ├── performance_review.md
│   └── redundancy_detection.md
├── 🚀 06_recommendations/
│   ├── enhancement_roadmap.md
│   ├── optimization_opportunities.md
│   ├── automation_suggestions.md
│   └── best_practices_implementation.md
├── 📋 07_onboarding/
│   ├── developer_guide.md
│   ├── setup_instructions.md
│   ├── troubleshooting.md
│   └── team_workflows.md
└── 🔧 08_cicd_analysis/
    ├── pipeline_discovery.md
    ├── deployment_strategies.md
    ├── environment_management.md
    └── security_compliance.md
```

### 🎯 CRITICAL REQUIREMENTS

#### **Script Path Documentation Standards:**
- **Always use complete relative paths** from repository root
- **Format**: `./repository-name/path/to/script.ext`
- **Include execution context**: When, how, and why each script runs
- **Document dependencies**: What each script requires to function
- **Multi-script workflows**: Show execution order and data flow
- **Individual Script Flows**: Create detailed flow diagrams for each significant script

#### **Dynamic Project Structure Handling:**
- **Flexible Detection**: Automatically identify whether CI/CD files are in dedicated repositories or embedded within source code
- **Monorepo Support**: Handle projects where multiple applications exist in a single repository
- **Mixed Structures**: Adapt to projects with both dedicated and embedded CI/CD configurations
- **No Assumptions**: Don't assume standard project structures; analyze what actually exists

#### **Mermaid Diagram Validation:**
- **Node Naming**: Use alphanumeric characters, avoid spaces and special characters
- **Script References**: Include script paths in node labels: `"./path/to/script.sh<br/>Description"`
- **Individual Script Flows**: Create separate flow diagrams for each significant script
- **Syntax Validation**: Ensure all diagrams render correctly
- **Connection Clarity**: Clear arrows and relationship indicators

#### **Cross-Repository Analysis:**
- **Identify shared components**: Common libraries, configurations, scripts
- **Map data flow**: How data moves between repositories and services
- **Document integration points**: APIs, databases, message queues, file systems
- **Analyze deployment dependencies**: Which repositories must be deployed together

### 🔧 ANALYSIS METHODOLOGY

#### Phase 1: Discovery & Mapping
1. **Project Structure Detection**: Automatically identify project organization (monorepo, multi-repo, mixed)
2. **Repository Discovery**: Scan all directories for project indicators
3. **CI/CD Configuration Discovery**: Locate CI/CD files regardless of their location (dedicated repos vs embedded)
4. **Technology Stack Identification**: Analyze package files, configurations, code
5. **Script Inventory**: Find and catalog all executable scripts with full paths
6. **Integration Mapping**: Identify how components communicate and depend on each other

#### Phase 2: Deep Analysis
1. **Individual Script Analysis**: Create detailed flow diagrams for each significant script
2. **Workflow Tracing**: Follow code execution paths and deployment processes
3. **Architecture Documentation**: Create comprehensive system architecture diagrams
4. **Dynamic Structure Adaptation**: Adjust analysis approach based on actual project structure
5. **Documentation Generation**: Create comprehensive, navigable documentation

#### Phase 3: Enhancement & Recommendations
1. **Gap Analysis**: Identify missing components or processes
2. **Optimization Opportunities**: Suggest improvements for efficiency and maintainability
3. **Structure-Specific Recommendations**: Provide suggestions tailored to the actual project organization
4. **Validation**: Ensure all diagrams render and paths are accurate

### ✅ SUCCESS CRITERIA

Your analysis is successful when:
- ✅ **Complete Documentation**: All required files are generated in `./documentation/`
- ✅ **Accurate Script Paths**: All script references use complete relative paths
- ✅ **Valid Mermaid Diagrams**: All diagrams render without syntax errors
- ✅ **Individual Script Flows**: Each significant script has its own detailed flow diagram
- ✅ **Dynamic Structure Handling**: Analysis adapts to actual project organization (monorepo, multi-repo, embedded CI/CD)
- ✅ **Comprehensive Coverage**: Every significant script and workflow is documented
- ✅ **Flexible CI/CD Analysis**: CI/CD configurations are analyzed regardless of their location
- ✅ **Actionable Insights**: Clear, implementable recommendations are provided
- ✅ **Cross-Repository Mapping**: Dependencies and workflows across repositories are clear
- ✅ **Executive Summary**: High-level overview suitable for stakeholders

### 🚀 EXECUTION INSTRUCTIONS

**Please begin the analysis now by:**

1. **Scanning my workspace** for all repositories and project structures
2. **Identifying the technology stack** across all repositories
3. **Creating the documentation folder structure** as specified above
4. **Generating comprehensive analysis** following all requirements
5. **Validating all outputs** for accuracy and completeness

**Start with a high-level overview, then dive deep into each component. Ensure all script paths are documented with complete relative paths from repository root, and all Mermaid diagrams follow proper syntax validation.**

---

*This prompt is designed to work with any LLM interface. Simply copy, paste, and let the AI analyze your entire application ecosystem automatically.*