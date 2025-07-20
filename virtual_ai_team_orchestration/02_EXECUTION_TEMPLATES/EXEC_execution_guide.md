# Prompt-Based Execution Guide

## 🚀 How to Execute Virtual AI Team Orchestration in Your IDE

### Prerequisites
- LLM-supported IDE (VS Code, Cursor, JetBrains, etc.)
- Access to LLM (GPT-4, Claude, etc.)
- Project workspace folder

## 📋 Step-by-Step Execution Process

### Phase 0: Project Validation & Foundation (NEW - Start Here)

#### Step 1: Project Analysis
1. **Open your IDE** (VS Code, Cursor, etc.)
2. **Copy the Project Analysis Prompt** from `prompt_starter_kit.md`
3. **Replace [PASTE USER'S PROJECT REQUEST HERE]** with your actual project request
4. **Execute the prompt** in your LLM
5. **Review the analysis output** carefully
6. **Confirm or request clarifications** until understanding is accurate

#### Step 2: Foundation Information Gathering
1. **Copy the Foundation Checklist Prompt** from `prompt_starter_kit.md`
2. **Paste your confirmed project analysis** into the checklist
3. **Work through each section** of the checklist:
   - Technical constraints and preferences
   - External integrations and APIs
   - Available resources and documentation
   - Team context and timeline
   - Success criteria and requirements
4. **Mark completion status** for each section
5. **Ensure all critical information** is provided

#### Step 3: Validation Complete
1. **Verify you have**:
   - ✅ Confirmed project understanding
   - ✅ Technical constraints defined
   - ✅ External dependencies identified
   - ✅ Available resources catalogued
   - ✅ Success criteria established
2. **Proceed to enhanced workspace creation**

### Phase 1: Enhanced Project Initialization

#### Step 4: Create Enhanced Project Workspace Structure

**Create the standardized folder structure:**
```bash
project_orchestration_workspace/
├── 01_project_analysis/
├── 02_architecture/
├── 03_implementation/
├── 04_quality_assurance/
├── 05_deployment/
└── PROJECT_WORKSPACE.md
```

**Create PROJECT_WORKSPACE.md:**
```markdown
# PROJECT_WORKSPACE.md

## 📊 Project Status Dashboard
- **Project Name**: [Your Project Name]
- **Current Phase**: Initialization
- **Active Role**: Master Orchestrator
- **Progress**: 0%
- **Last Updated**: [Current Timestamp]
- **Workspace Folder**: project_orchestration_workspace/

## 🎯 Project Context
### Requirements
[Paste your project requirements here]

### Technology Preferences
[List preferred technologies/constraints]

## 📝 Living Documentation
### Current Sprint/Phase
Project initialization and planning

### Completed Tasks
- Project workspace created
- Folder structure established

### Pending Tasks
- Architecture design
- Technology stack selection
- Implementation planning

## 🔄 Context for Next Role
### Handoff Summary
Ready for Solution Architect to begin system design

### Specific Instructions
Analyze requirements and design system architecture

## 🤝 Human Feedback Log
### Pending Approvals
- Architecture approval needed
- Technology stack confirmation required

## 🎯 GPT-4.1 Optimization Notes
### Quality Assurance
- Using enhanced prompts for better LLM compatibility
- Built-in validation checkpoints
- Explicit context preservation
```

#### Step 5: Execute Enhanced Master Orchestrator Prompt

**Copy the Enhanced Master Orchestrator prompt from your starter kit:**

1. **Copy the Enhanced Master Orchestrator prompt** from `prompt_starter_kit.md`
2. **Paste your validated foundation** and **PROJECT_WORKSPACE.md content** into the prompt
3. **Execute in your LLM** with complete context
4. **Review the enhanced orchestration plan**
5. **Confirm the approach** leveraging validated foundation

### Step 2: Role Execution Cycle

#### 2.1 Execute Generated Role Prompt

**Take the generated Solution Architect prompt and execute it:**

```markdown
# SOLUTION ARCHITECT EXECUTION

## Enhanced Prompt
[PASTE THE GENERATED ENHANCED PROMPT HERE]

## Current Project Workspace
[PASTE UPDATED WORKSPACE CONTENT HERE]

## Execute Task
Perform your role as Solution Architect with the enhanced context and latest research insights provided.

## Required Outputs
1. System architecture design
2. Technology stack recommendations
3. Updated project workspace
4. Context preparation for Technical Lead
5. Generated enhanced Technical Lead prompt
```

#### 2.2 Continue the Chain

Repeat this process for each role:
- Solution Architect → Technical Lead
- Technical Lead → Developer
- Developer → QA Engineer
- QA Engineer → DevOps Engineer
- DevOps Engineer → Project Manager (for next iteration)

### Step 3: Human Feedback Integration

#### 3.1 Approval Points

When the LLM indicates human feedback is needed:

```markdown
# HUMAN FEEDBACK REQUIRED

## Decision Point
[Description of what needs approval]

## Options Presented
[List of options with pros/cons]

## Recommendation
[LLM recommendation with reasoning]

## Your Decision
[Provide your feedback here]

## Continue Execution
Once you've provided feedback, use this prompt:

"Continue with my decision: [YOUR_DECISION]. Update the project workspace and generate the next enhanced role prompt."
```

## 🔄 Dynamic Enhancement Examples

### Example 1: Technology Research Integration

**Before Enhancement (Base Prompt):**
```markdown
Implement a REST API for user management.
```

**After Enhancement (Research-Augmented):**
```markdown
# ENHANCED API DEVELOPMENT PROMPT

## Latest API Best Practices (2024)
- Use OpenAPI 3.1 specification
- Implement JSON:API standard for consistency
- Add rate limiting with sliding window algorithm
- Use JWT with refresh token rotation

## Technology Stack (Current Recommendations)
- Node.js 20 LTS with Express 4.18
- TypeScript 5.0 with strict mode
- Prisma ORM with PostgreSQL 16
- Redis 7.2 for caching and sessions

## Security Implementation
```javascript
// Latest security middleware setup
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import { body, validationResult } from 'express-validator';

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  standardHeaders: true,
  legacyHeaders: false,
});

app.use(helmet());
app.use(limiter);
```

## Performance Optimizations
- Implement database connection pooling
- Add response compression
- Use CDN for static assets
- Implement proper caching strategies

## Implementation Task
Create a user management API with the above enhancements applied.
```

### Example 2: Context-Aware Enhancement

**Project Context:** E-commerce Platform
**Role:** QA Engineer
**Task:** Create testing strategy

**Enhanced Prompt Generated:**
```markdown
# ENHANCED QA ENGINEER PROMPT - E-COMMERCE TESTING

## Project-Specific Testing Requirements
### E-commerce Critical Paths
- User registration and authentication
- Product search and filtering
- Shopping cart functionality
- Payment processing
- Order management
- Inventory tracking

## Latest Testing Technologies (2024)
### Frontend Testing
- Playwright 1.40 for E2E testing
- React Testing Library for component tests
- Storybook 7.6 for visual testing
- Chromatic for visual regression

### API Testing
- Postman/Newman for automated API tests
- Contract testing with Pact
- Load testing with k6
- Security testing with OWASP ZAP

## E-commerce Specific Test Cases
```javascript
// Payment flow test example
test('complete purchase flow', async ({ page }) => {
  await page.goto('/products');
  await page.click('[data-testid="add-to-cart"]');
  await page.click('[data-testid="checkout"]');
  
  // Test payment integration
  await page.fill('[data-testid="card-number"]', '4242424242424242');
  await page.fill('[data-testid="expiry"]', '12/25');
  await page.fill('[data-testid="cvc"]', '123');
  
  await page.click('[data-testid="pay-now"]');
  await expect(page.locator('[data-testid="success-message"]')).toBeVisible();
});
```

## Performance Testing Strategy
- Load test for Black Friday traffic (10x normal load)
- Database performance under concurrent transactions
- CDN and caching effectiveness
- Mobile performance optimization

## Security Testing Focus
- Payment data protection (PCI DSS compliance)
- User data privacy (GDPR compliance)
- SQL injection prevention
- XSS protection validation
```

## 🛠️ IDE Integration Tips

### VS Code Setup
1. Create a `.vscode/settings.json` for project-specific LLM settings
2. Use workspace snippets for common prompt templates
3. Set up tasks for quick prompt execution

### Cursor IDE Setup
1. Use Cursor's AI features for prompt enhancement
2. Set up custom rules for project context
3. Leverage Cursor's codebase understanding

### JetBrains Setup
1. Use AI Assistant plugin for prompt execution
2. Create live templates for role prompts
3. Set up project-specific AI context

## 📊 Execution Tracking

### Progress Monitoring
```markdown
# EXECUTION_LOG.md

## Session: [Date/Time]
### Roles Executed
- [x] Master Orchestrator
- [x] Solution Architect
- [ ] Technical Lead
- [ ] Developer
- [ ] QA Engineer
- [ ] DevOps Engineer

### Research Enhancements Applied
- Latest React patterns integrated
- Security best practices updated
- Performance optimizations included

### Human Decisions Made
- Technology stack approved
- Architecture design confirmed
- Security requirements validated

### Next Steps
- Execute Technical Lead prompt
- Review implementation plan
- Prepare development environment
```

## 🎯 Quality Assurance

### Prompt Quality Checklist
- [ ] Latest technology versions included
- [ ] Project-specific context applied
- [ ] Security considerations addressed
- [ ] Performance optimizations included
- [ ] Best practices integrated
- [ ] Clear output requirements defined

### Context Continuity Checklist
- [ ] Previous role outputs included
- [ ] Project workspace updated
- [ ] Decisions logged and accessible
- [ ] Next role context prepared
- [ ] Human feedback points identified

## 🔧 Troubleshooting

### Common Issues

**Issue:** Prompt too long for LLM context window
**Solution:** Use context summarization prompt to compress workspace content

**Issue:** Research enhancement not relevant
**Solution:** Refine research keywords and focus areas

**Issue:** Role handoff context lost
**Solution:** Use explicit context handoff prompts

**Issue:** Human feedback loop unclear
**Solution:** Use structured decision templates

### Benefits of Enhanced Approach

✅ **Validated Foundation**: Complete project understanding before starting
✅ **Reduced Iterations**: All critical information gathered upfront
✅ **Better Architecture**: Solution design with full context
✅ **Accurate Planning**: Timeline and complexity based on complete requirements
✅ **Zero Setup Time**: Start immediately in any IDE
✅ **No Dependencies**: Pure prompt-based, no installations
✅ **Flexible Execution**: Adapt to any project type
✅ **Human Control**: Strategic intervention points
✅ **Quality Assurance**: Built-in validation and feedback
✅ **Continuous Learning**: Each project improves the prompts

This guide enables you to execute the Virtual AI Team Orchestration entirely through prompts in your preferred IDE environment.