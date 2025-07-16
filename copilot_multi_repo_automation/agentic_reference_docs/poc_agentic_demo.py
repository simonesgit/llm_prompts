#!/usr/bin/env python3
"""
Proof of Concept: Agentic AI Documentation Generator

A simplified demonstration of converting GitHub Copilot workflows to autonomous agentic AI
using LangGraph and simulated internal LLM integration.

This POC shows:
1. Repository scanning and analysis
2. Autonomous decision making
3. Content generation with quality control
4. LangGraph workflow orchestration
5. Simulated internal LLM integration

Usage:
    python poc_agentic_demo.py [workspace_path]
"""

import asyncio
import json
import os
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, TypedDict
from datetime import datetime
import time

# Simulated LangGraph implementation for POC
class StateGraph:
    """Simplified LangGraph StateGraph for POC"""
    
    def __init__(self, state_schema):
        self.state_schema = state_schema
        self.nodes = {}
        self.edges = {}
        self.conditional_edges = {}
        self.entry_point = None
    
    def add_node(self, name: str, func):
        self.nodes[name] = func
    
    def add_edge(self, from_node: str, to_node: str):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append(to_node)
    
    def add_conditional_edges(self, from_node: str, condition_func, edge_map: Dict[str, str]):
        self.conditional_edges[from_node] = (condition_func, edge_map)
    
    def set_entry_point(self, node: str):
        self.entry_point = node
    
    def compile(self):
        return CompiledGraph(self)

class CompiledGraph:
    """Compiled graph executor"""
    
    def __init__(self, graph: StateGraph):
        self.graph = graph
    
    async def ainvoke(self, initial_state: Dict) -> Dict:
        """Execute the graph asynchronously"""
        state = initial_state.copy()
        current_node = self.graph.entry_point
        
        while current_node and current_node != "END":
            print(f"\n🔄 Executing node: {current_node}")
            
            # Execute current node
            if current_node in self.graph.nodes:
                state = await self.graph.nodes[current_node](state)
            
            # Determine next node
            if current_node in self.graph.conditional_edges:
                condition_func, edge_map = self.graph.conditional_edges[current_node]
                next_key = condition_func(state)
                current_node = edge_map.get(next_key, "END")
            elif current_node in self.graph.edges:
                current_node = self.graph.edges[current_node][0]
            else:
                current_node = "END"
        
        return state

# Data structures
@dataclass
class RepositoryInfo:
    name: str
    path: str
    language: str
    size: int
    complexity: str
    documentation_status: str
    priority: int
    dependencies: List[str]

@dataclass
class LLMResponse:
    content: str
    confidence: float
    tokens_used: int
    model_used: str

class DocumentationState(TypedDict):
    repositories: List[RepositoryInfo]
    current_repo_index: int
    generated_docs: Dict[str, Dict[str, str]]
    quality_scores: Dict[str, float]
    workflow_status: str
    error_log: List[str]
    processing_stats: Dict[str, float]

# Simulated Internal LLM Client
class SimulatedLLMClient:
    """Simulated internal LLM client for POC demonstration"""
    
    def __init__(self, base_url: str = "http://internal-llm.company.com"):
        self.base_url = base_url
        self.models = {
            "code-analysis": "Internal Code Analyzer v2.1",
            "documentation": "Internal Doc Generator v3.0",
            "quality-assessor": "Internal Quality Checker v1.5"
        }
        self.token_count = 0
    
    async def analyze_code(self, code_content: str, file_path: str) -> Dict:
        """Simulate code analysis"""
        await asyncio.sleep(0.5)  # Simulate processing time
        self.token_count += 150
        
        # Simulate intelligent analysis based on file extension and content
        file_ext = Path(file_path).suffix.lower()
        
        if file_ext == '.py':
            return {
                "purpose": "Python application with web framework integration",
                "dependencies": ["flask", "requests", "sqlalchemy"],
                "api_endpoints": ["/api/users", "/api/data"],
                "complexity": "Medium",
                "documentation_needs": ["README", "API Documentation", "Setup Guide"]
            }
        elif file_ext == '.js':
            return {
                "purpose": "JavaScript frontend application with React components",
                "dependencies": ["react", "axios", "lodash"],
                "api_endpoints": [],
                "complexity": "Simple",
                "documentation_needs": ["README", "Component Guide"]
            }
        else:
            return {
                "purpose": "General purpose application",
                "dependencies": [],
                "api_endpoints": [],
                "complexity": "Simple",
                "documentation_needs": ["README"]
            }
    
    async def generate_content(self, prompt: str, model: str = "documentation", **kwargs) -> LLMResponse:
        """Simulate content generation"""
        await asyncio.sleep(1.0)  # Simulate processing time
        tokens_used = len(prompt.split()) * 2  # Rough estimation
        self.token_count += tokens_used
        
        # Generate contextual content based on prompt keywords
        if "README" in prompt:
            content = self._generate_readme_content(prompt)
        elif "architecture" in prompt.lower():
            content = self._generate_architecture_content(prompt)
        elif "API" in prompt:
            content = self._generate_api_content(prompt)
        elif "quality" in prompt.lower() and "assess" in prompt.lower():
            content = self._generate_quality_score()
        else:
            content = self._generate_generic_content(prompt)
        
        return LLMResponse(
            content=content,
            confidence=0.85,
            tokens_used=tokens_used,
            model_used=self.models.get(model, "default-model")
        )
    
    def _generate_readme_content(self, prompt: str) -> str:
        """Generate README content"""
        return """# Project Documentation

## Overview
This project provides a comprehensive solution for automated documentation generation using advanced AI techniques.

## Features
- Automated repository scanning
- Intelligent content generation
- Quality assessment and improvement
- Cross-repository integration

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from agentic_docs import DocumentationGenerator

generator = DocumentationGenerator()
result = generator.process_workspace("/path/to/workspace")
```

## Configuration
Configure the system using environment variables:
- `LLM_BASE_URL`: Internal LLM farm endpoint
- `API_KEY`: Authentication key
- `QUALITY_THRESHOLD`: Minimum quality score (default: 0.8)

## Contributing
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
MIT License - see LICENSE file for details.
"""
    
    def _generate_architecture_content(self, prompt: str) -> str:
        """Generate architecture documentation"""
        return """# System Architecture

## Overview
The system follows a microservices architecture with autonomous agents handling different aspects of documentation generation.

## Core Components

### Repository Scanner Agent
- Discovers and analyzes code repositories
- Extracts metadata and dependencies
- Prioritizes repositories for processing

### Content Generation Agent
- Creates documentation using specialized LLM models
- Handles multiple document types (README, API, Architecture)
- Maintains consistency across repositories

### Quality Control Agent
- Assesses documentation quality
- Provides improvement suggestions
- Ensures professional standards

## Data Flow

```mermaid
graph TD
    A[Repository Scanner] --> B[Strategy Coordinator]
    B --> C[Content Generator]
    C --> D[Quality Controller]
    D --> E{Quality Gate}
    E -->|Pass| F[Cross Referencer]
    E -->|Improve| C
    F --> G[Documentation Publisher]
```

## Technology Stack
- **Orchestration**: LangGraph
- **AI Models**: Internal LLM Farm
- **Languages**: Python, TypeScript
- **Storage**: File System, Git

## Scalability Considerations
- Horizontal scaling through agent distribution
- Caching of analysis results
- Batch processing for large workspaces
- Incremental updates for changed repositories
"""
    
    def _generate_api_content(self, prompt: str) -> str:
        """Generate API documentation"""
        return """# API Documentation

## Base URL
```
http://localhost:8000/api/v1
```

## Authentication
All API requests require a valid API key in the header:
```
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### POST /repositories/scan
Scan a workspace for repositories.

**Request:**
```json
{
  "workspace_path": "/path/to/workspace",
  "include_patterns": ["*.py", "*.js"],
  "exclude_patterns": ["node_modules", "__pycache__"]
}
```

**Response:**
```json
{
  "repositories": [
    {
      "name": "my-project",
      "path": "/path/to/my-project",
      "language": "Python",
      "complexity": "Medium",
      "priority": 85
    }
  ],
  "total_count": 1
}
```

### POST /documentation/generate
Generate documentation for repositories.

**Request:**
```json
{
  "repository_ids": ["repo-1", "repo-2"],
  "document_types": ["README", "API", "Architecture"],
  "quality_threshold": 0.8
}
```

**Response:**
```json
{
  "job_id": "doc-job-123",
  "status": "processing",
  "estimated_completion": "2024-01-15T10:30:00Z"
}
```

### GET /jobs/{job_id}/status
Check documentation generation status.

**Response:**
```json
{
  "job_id": "doc-job-123",
  "status": "completed",
  "progress": 100,
  "results": {
    "repositories_processed": 2,
    "documents_generated": 6,
    "average_quality_score": 0.87
  }
}
```

## Error Codes
- `400`: Bad Request - Invalid parameters
- `401`: Unauthorized - Invalid API key
- `404`: Not Found - Resource not found
- `429`: Rate Limited - Too many requests
- `500`: Internal Error - Server error
"""
    
    def _generate_quality_score(self) -> str:
        """Generate quality assessment score"""
        import random
        score = round(random.uniform(0.7, 0.95), 2)
        return str(score)
    
    def _generate_generic_content(self, prompt: str) -> str:
        """Generate generic content"""
        return f"""# Generated Content

This content was generated based on the following analysis:

## Analysis Summary
The system has analyzed the provided context and generated appropriate documentation content.

## Key Points
- Automated content generation
- Context-aware responses
- Professional formatting
- Comprehensive coverage

## Next Steps
1. Review generated content
2. Apply quality improvements
3. Integrate with existing documentation
4. Deploy to production

*Generated by Internal LLM Farm at {datetime.now().isoformat()}*
"""

# Agentic AI Implementation
class AgenticDocumentationSystem:
    """Main agentic AI documentation system"""
    
    def __init__(self, workspace_path: str):
        self.workspace_path = Path(workspace_path)
        self.llm_client = SimulatedLLMClient()
        self.processing_stats = {
            "start_time": time.time(),
            "repositories_scanned": 0,
            "documents_generated": 0,
            "total_tokens_used": 0
        }
    
    def create_workflow(self) -> StateGraph:
        """Create the LangGraph workflow"""
        workflow = StateGraph(DocumentationState)
        
        # Add nodes
        workflow.add_node("scan_repositories", self.scan_repositories_node)
        workflow.add_node("analyze_strategy", self.analyze_strategy_node)
        workflow.add_node("generate_content", self.generate_content_node)
        workflow.add_node("assess_quality", self.assess_quality_node)
        workflow.add_node("improve_content", self.improve_content_node)
        workflow.add_node("finalize_docs", self.finalize_docs_node)
        
        # Define edges
        workflow.add_edge("scan_repositories", "analyze_strategy")
        workflow.add_edge("analyze_strategy", "generate_content")
        workflow.add_edge("generate_content", "assess_quality")
        
        # Conditional edges for quality control
        workflow.add_conditional_edges(
            "assess_quality",
            self.quality_gate_condition,
            {
                "improve": "improve_content",
                "next_repo": "generate_content",
                "finalize": "finalize_docs"
            }
        )
        
        workflow.add_edge("improve_content", "assess_quality")
        workflow.add_edge("finalize_docs", "END")
        
        workflow.set_entry_point("scan_repositories")
        return workflow.compile()
    
    async def scan_repositories_node(self, state: DocumentationState) -> DocumentationState:
        """Autonomous repository scanning and analysis"""
        print("🔍 Scanning workspace for repositories...")
        
        repositories = []
        
        # Scan workspace directory
        for item in self.workspace_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                if self._is_code_repository(item):
                    repo_info = await self._analyze_repository(item)
                    if repo_info:
                        repositories.append(repo_info)
                        self.processing_stats["repositories_scanned"] += 1
        
        # Sort by priority
        repositories.sort(key=lambda x: x.priority, reverse=True)
        
        state["repositories"] = repositories
        state["current_repo_index"] = 0
        state["generated_docs"] = {}
        state["quality_scores"] = {}
        state["workflow_status"] = "repositories_scanned"
        state["error_log"] = []
        state["processing_stats"] = self.processing_stats
        
        print(f"✅ Found {len(repositories)} repositories to process")
        for repo in repositories:
            print(f"   📁 {repo.name} ({repo.language}, Priority: {repo.priority})")
        
        return state
    
    async def analyze_strategy_node(self, state: DocumentationState) -> DocumentationState:
        """Autonomous strategy selection"""
        print("🧠 Analyzing optimal documentation strategy...")
        
        repositories = state["repositories"]
        
        # Analyze repository characteristics
        total_repos = len(repositories)
        languages = set(repo.language for repo in repositories)
        avg_complexity = sum(1 if repo.complexity == "Simple" else 2 if repo.complexity == "Medium" else 3 for repo in repositories) / total_repos
        
        strategy_prompt = f"""
        Analyze workspace with {total_repos} repositories using languages: {', '.join(languages)}.
        Average complexity: {avg_complexity:.1f}/3.0
        
        Select optimal documentation strategy:
        1. batch_processing - Group similar repositories
        2. priority_first - Process high-priority repositories first
        3. incremental - Build documentation incrementally
        
        Recommend strategy and processing order.
        """
        
        response = await self.llm_client.generate_content(
            strategy_prompt, 
            model="code-analysis"
        )
        
        state["documentation_strategy"] = response.content
        state["workflow_status"] = "strategy_selected"
        
        print(f"📋 Strategy selected: {response.content[:100]}...")
        return state
    
    async def generate_content_node(self, state: DocumentationState) -> DocumentationState:
        """Autonomous content generation"""
        repositories = state["repositories"]
        current_index = state["current_repo_index"]
        
        if current_index >= len(repositories):
            state["workflow_status"] = "all_repos_processed"
            return state
        
        current_repo = repositories[current_index]
        print(f"📝 Generating documentation for: {current_repo.name}")
        
        # Generate different types of documentation
        docs = {}
        
        # README documentation
        readme_prompt = f"""
        Generate comprehensive README documentation for:
        Repository: {current_repo.name}
        Language: {current_repo.language}
        Complexity: {current_repo.complexity}
        Dependencies: {', '.join(current_repo.dependencies)}
        
        Include installation, usage, and configuration sections.
        """
        
        readme_response = await self.llm_client.generate_content(
            readme_prompt, 
            model="documentation"
        )
        docs["README"] = readme_response.content
        
        # Architecture documentation for complex projects
        if current_repo.complexity in ["Medium", "Complex"]:
            arch_prompt = f"""
            Generate architecture documentation for {current_repo.name}.
            Focus on system design, components, and data flow.
            """
            
            arch_response = await self.llm_client.generate_content(
                arch_prompt, 
                model="documentation"
            )
            docs["Architecture"] = arch_response.content
        
        # API documentation if applicable
        if current_repo.dependencies and any("api" in dep.lower() or "flask" in dep.lower() or "express" in dep.lower() for dep in current_repo.dependencies):
            api_prompt = f"""
            Generate API documentation for {current_repo.name}.
            Include endpoints, authentication, and examples.
            """
            
            api_response = await self.llm_client.generate_content(
                api_prompt, 
                model="documentation"
            )
            docs["API"] = api_response.content
        
        state["generated_docs"][current_repo.name] = docs
        state["workflow_status"] = "content_generated"
        self.processing_stats["documents_generated"] += len(docs)
        self.processing_stats["total_tokens_used"] = self.llm_client.token_count
        
        print(f"✅ Generated {len(docs)} documents for {current_repo.name}")
        return state
    
    async def assess_quality_node(self, state: DocumentationState) -> DocumentationState:
        """Autonomous quality assessment"""
        repositories = state["repositories"]
        current_index = state["current_repo_index"]
        current_repo = repositories[current_index]
        
        print(f"🔍 Assessing quality for: {current_repo.name}")
        
        docs = state["generated_docs"][current_repo.name]
        
        # Assess quality using LLM
        quality_prompt = f"""
        Assess the quality of documentation for {current_repo.name}.
        
        Documents generated: {list(docs.keys())}
        Repository complexity: {current_repo.complexity}
        
        Rate overall quality from 0.0 to 1.0 considering:
        - Completeness
        - Clarity
        - Technical accuracy
        - Professional presentation
        
        Provide only the numeric score.
        """
        
        quality_response = await self.llm_client.generate_content(
            quality_prompt, 
            model="quality-assessor"
        )
        
        try:
            quality_score = float(quality_response.content.strip())
        except ValueError:
            quality_score = 0.75  # Default score
        
        state["quality_scores"][current_repo.name] = quality_score
        state["workflow_status"] = "quality_assessed"
        
        print(f"📊 Quality score: {quality_score:.2f}")
        return state
    
    def quality_gate_condition(self, state: DocumentationState) -> str:
        """Autonomous quality gate decision"""
        repositories = state["repositories"]
        current_index = state["current_repo_index"]
        
        if current_index >= len(repositories):
            return "finalize"
        
        current_repo = repositories[current_index]
        quality_score = state["quality_scores"].get(current_repo.name, 0)
        
        if quality_score >= 0.8:
            # High quality - move to next repository
            state["current_repo_index"] += 1
            if state["current_repo_index"] >= len(repositories):
                return "finalize"
            else:
                return "next_repo"
        elif quality_score >= 0.6:
            # Acceptable quality - move to next repository
            state["current_repo_index"] += 1
            if state["current_repo_index"] >= len(repositories):
                return "finalize"
            else:
                return "next_repo"
        else:
            # Needs improvement
            retry_count = state.get("retry_count", 0)
            if retry_count < 2:
                state["retry_count"] = retry_count + 1
                return "improve"
            else:
                # Skip after retries
                state["current_repo_index"] += 1
                state["retry_count"] = 0
                return "next_repo"
    
    async def improve_content_node(self, state: DocumentationState) -> DocumentationState:
        """Autonomous content improvement"""
        repositories = state["repositories"]
        current_index = state["current_repo_index"]
        current_repo = repositories[current_index]
        
        print(f"🔧 Improving documentation for: {current_repo.name}")
        
        docs = state["generated_docs"][current_repo.name]
        quality_score = state["quality_scores"][current_repo.name]
        
        # Improve each document
        improved_docs = {}
        for doc_type, content in docs.items():
            improve_prompt = f"""
            Improve this {doc_type} documentation (current quality: {quality_score:.2f}):
            
            {content}
            
            Focus on:
            - Adding missing information
            - Improving clarity
            - Better formatting
            - More practical examples
            """
            
            improved_response = await self.llm_client.generate_content(
                improve_prompt, 
                model="documentation"
            )
            improved_docs[doc_type] = improved_response.content
        
        state["generated_docs"][current_repo.name] = improved_docs
        state["workflow_status"] = "content_improved"
        
        print(f"✅ Improved documentation for {current_repo.name}")
        return state
    
    async def finalize_docs_node(self, state: DocumentationState) -> DocumentationState:
        """Finalize and save documentation"""
        print("📁 Finalizing documentation...")
        
        generated_docs = state["generated_docs"]
        quality_scores = state["quality_scores"]
        
        # Create output directory
        output_dir = self.workspace_path / "agentic_documentation"
        output_dir.mkdir(exist_ok=True)
        
        # Save documentation for each repository
        for repo_name, docs in generated_docs.items():
            repo_dir = output_dir / repo_name
            repo_dir.mkdir(exist_ok=True)
            
            for doc_type, content in docs.items():
                file_path = repo_dir / f"{doc_type}.md"
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
        
        # Create summary report
        await self._create_summary_report(state, output_dir)
        
        # Update processing stats
        self.processing_stats["end_time"] = time.time()
        self.processing_stats["total_duration"] = self.processing_stats["end_time"] - self.processing_stats["start_time"]
        
        state["workflow_status"] = "completed"
        state["processing_stats"] = self.processing_stats
        
        print(f"✅ Documentation saved to: {output_dir}")
        return state
    
    async def _create_summary_report(self, state: DocumentationState, output_dir: Path):
        """Create comprehensive summary report"""
        repositories = state["repositories"]
        generated_docs = state["generated_docs"]
        quality_scores = state["quality_scores"]
        stats = self.processing_stats
        
        report_content = f"""# Agentic Documentation Generation Report

**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary

- **Repositories Processed:** {len(generated_docs)}
- **Total Documents Generated:** {stats['documents_generated']}
- **Processing Time:** {stats.get('total_duration', 0):.2f} seconds
- **Average Quality Score:** {sum(quality_scores.values()) / len(quality_scores):.2f}
- **Total Tokens Used:** {stats['total_tokens_used']:,}

## Repository Analysis

| Repository | Language | Complexity | Documents | Quality Score |
|------------|----------|------------|-----------|---------------|
"""
        
        for repo in repositories:
            if repo.name in generated_docs:
                docs_count = len(generated_docs[repo.name])
                quality = quality_scores.get(repo.name, 0)
                report_content += f"| {repo.name} | {repo.language} | {repo.complexity} | {docs_count} | {quality:.2f} |\n"
        
        report_content += f"""

## Performance Metrics

- **Average Processing Time per Repository:** {stats.get('total_duration', 0) / max(1, len(generated_docs)):.2f} seconds
- **Documents per Second:** {stats['documents_generated'] / max(1, stats.get('total_duration', 1)):.2f}
- **Token Efficiency:** {stats['total_tokens_used'] / max(1, stats['documents_generated']):.0f} tokens per document

## Quality Distribution

"""
        
        # Quality distribution
        high_quality = sum(1 for score in quality_scores.values() if score >= 0.8)
        medium_quality = sum(1 for score in quality_scores.values() if 0.6 <= score < 0.8)
        low_quality = sum(1 for score in quality_scores.values() if score < 0.6)
        
        report_content += f"""- **High Quality (≥0.8):** {high_quality} repositories
- **Medium Quality (0.6-0.8):** {medium_quality} repositories
- **Low Quality (<0.6):** {low_quality} repositories

## Generated Documentation Structure

"""
        
        for repo_name, docs in generated_docs.items():
            report_content += f"""### {repo_name}
"""
            for doc_type in docs.keys():
                report_content += f"- {doc_type}.md\n"
            report_content += "\n"
        
        report_content += f"""
## Cost Analysis

- **Estimated LLM Cost:** ${stats['total_tokens_used'] * 0.0001:.2f}
- **Time Savings vs Manual:** {len(generated_docs) * 4:.1f} hours saved
- **ROI:** {(len(generated_docs) * 4 * 50) / max(1, stats['total_tokens_used'] * 0.0001):.0f}x

## Next Steps

1. Review generated documentation for accuracy
2. Customize content for specific requirements
3. Integrate with existing documentation systems
4. Set up automated updates for repository changes

---
*Generated by Agentic AI Documentation System*
"""
        
        # Save report
        report_path = output_dir / "generation_report.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
    
    def _is_code_repository(self, path: Path) -> bool:
        """Check if directory contains code"""
        code_indicators = [
            '.git', 'package.json', 'requirements.txt', 'go.mod', 
            'Cargo.toml', 'pom.xml', '.gitignore'
        ]
        
        # Check for repository indicators
        for indicator in code_indicators:
            if (path / indicator).exists():
                return True
        
        # Check for code files
        code_extensions = {'.py', '.js', '.ts', '.java', '.go', '.rs', '.cpp', '.c'}
        for file_path in path.rglob('*'):
            if file_path.suffix.lower() in code_extensions:
                return True
        
        return False
    
    async def _analyze_repository(self, repo_path: Path) -> Optional[RepositoryInfo]:
        """Analyze individual repository"""
        try:
            # Basic analysis
            language = self._detect_language(repo_path)
            size = self._calculate_size(repo_path)
            
            # Get code sample for LLM analysis
            code_sample = self._get_code_sample(repo_path)
            analysis = await self.llm_client.analyze_code(code_sample, str(repo_path))
            
            # Calculate priority
            complexity = analysis.get('complexity', 'Simple')
            doc_status = self._check_documentation(repo_path)
            priority = self._calculate_priority(size, complexity, doc_status)
            
            return RepositoryInfo(
                name=repo_path.name,
                path=str(repo_path),
                language=language,
                size=size,
                complexity=complexity,
                documentation_status=doc_status,
                priority=priority,
                dependencies=analysis.get('dependencies', [])
            )
        
        except Exception as e:
            print(f"⚠️  Error analyzing {repo_path.name}: {e}")
            return None
    
    def _detect_language(self, repo_path: Path) -> str:
        """Detect primary programming language"""
        language_map = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.java': 'Java',
            '.go': 'Go',
            '.rs': 'Rust',
            '.cpp': 'C++',
            '.c': 'C'
        }
        
        file_counts = {}
        for file_path in repo_path.rglob('*'):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                if ext in language_map:
                    lang = language_map[ext]
                    file_counts[lang] = file_counts.get(lang, 0) + 1
        
        return max(file_counts, key=file_counts.get) if file_counts else 'Unknown'
    
    def _calculate_size(self, repo_path: Path) -> int:
        """Calculate repository size in lines of code"""
        total_lines = 0
        code_extensions = {'.py', '.js', '.ts', '.java', '.go', '.rs', '.cpp', '.c'}
        
        for file_path in repo_path.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in code_extensions:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        total_lines += sum(1 for line in f if line.strip())
                except:
                    continue
        
        return total_lines
    
    def _get_code_sample(self, repo_path: Path) -> str:
        """Get representative code sample"""
        main_files = ['main.py', 'app.py', 'index.js', 'main.js', 'main.go']
        
        # Try main files first
        for main_file in main_files:
            main_path = repo_path / main_file
            if main_path.exists():
                try:
                    with open(main_path, 'r', encoding='utf-8', errors='ignore') as f:
                        return f.read()[:1000]
                except:
                    continue
        
        # Fallback to any code file
        code_extensions = {'.py', '.js', '.ts', '.java', '.go'}
        for file_path in repo_path.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in code_extensions:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        return f.read()[:1000]
                except:
                    continue
        
        return "# No code files found"
    
    def _check_documentation(self, repo_path: Path) -> str:
        """Check existing documentation status"""
        doc_files = ['README.md', 'README.rst', 'docs/', 'documentation/']
        
        existing = []
        for doc_file in doc_files:
            if (repo_path / doc_file).exists():
                existing.append(doc_file)
        
        if not existing:
            return "None"
        elif len(existing) == 1 and 'README' in existing[0]:
            return "Basic"
        else:
            return "Comprehensive"
    
    def _calculate_priority(self, size: int, complexity: str, doc_status: str) -> int:
        """Calculate processing priority"""
        score = 0
        
        # Size factor
        if size > 5000:
            score += 30
        elif size > 1000:
            score += 20
        else:
            score += 10
        
        # Complexity factor
        complexity_scores = {'Simple': 10, 'Medium': 20, 'Complex': 30}
        score += complexity_scores.get(complexity, 15)
        
        # Documentation gap factor
        doc_scores = {'None': 40, 'Basic': 20, 'Comprehensive': 5}
        score += doc_scores.get(doc_status, 15)
        
        return score

# Main execution
async def main():
    """Main execution function"""
    print("🚀 Agentic AI Documentation Generator - Proof of Concept")
    print("=" * 60)
    
    # Get workspace path
    workspace_path = sys.argv[1] if len(sys.argv) > 1 else "."
    workspace_path = Path(workspace_path).resolve()
    
    print(f"📁 Workspace: {workspace_path}")
    print(f"🤖 LLM: Simulated Internal LLM Farm")
    print(f"🔧 Framework: LangGraph (Simulated)")
    print()
    
    # Initialize system
    system = AgenticDocumentationSystem(workspace_path)
    
    # Create and execute workflow
    workflow = system.create_workflow()
    
    initial_state = {
        "repositories": [],
        "current_repo_index": 0,
        "generated_docs": {},
        "quality_scores": {},
        "workflow_status": "initialized",
        "error_log": [],
        "processing_stats": {}
    }
    
    print("🔄 Executing agentic workflow...")
    print()
    
    try:
        final_state = await workflow.ainvoke(initial_state)
        
        # Display results
        print()
        print("🎉 Workflow Completed Successfully!")
        print("=" * 40)
        
        stats = final_state["processing_stats"]
        quality_scores = final_state["quality_scores"]
        
        print(f"📊 Repositories Processed: {stats.get('repositories_scanned', 0)}")
        print(f"📝 Documents Generated: {stats.get('documents_generated', 0)}")
        print(f"⏱️  Total Processing Time: {stats.get('total_duration', 0):.2f} seconds")
        print(f"🎯 Average Quality Score: {sum(quality_scores.values()) / len(quality_scores):.2f}" if quality_scores else "🎯 Average Quality Score: N/A")
        print(f"🔤 Total Tokens Used: {stats.get('total_tokens_used', 0):,}")
        
        if quality_scores:
            print("\n📈 Quality Scores by Repository:")
            for repo, score in quality_scores.items():
                emoji = "🟢" if score >= 0.8 else "🟡" if score >= 0.6 else "🔴"
                print(f"   {emoji} {repo}: {score:.2f}")
        
        output_dir = workspace_path / "agentic_documentation"
        print(f"\n📁 Documentation saved to: {output_dir}")
        print(f"📋 Summary report: {output_dir / 'generation_report.md'}")
        
        # Calculate ROI
        manual_hours = stats.get('repositories_scanned', 0) * 4
        automated_hours = stats.get('total_duration', 0) / 3600
        time_saved = manual_hours - automated_hours
        cost_savings = time_saved * 50  # $50/hour
        llm_cost = stats.get('total_tokens_used', 0) * 0.0001
        roi = cost_savings / max(llm_cost, 0.01)
        
        print(f"\n💰 ROI Analysis:")
        print(f"   ⏰ Time Saved: {time_saved:.1f} hours")
        print(f"   💵 Cost Savings: ${cost_savings:.2f}")
        print(f"   🤖 LLM Cost: ${llm_cost:.2f}")
        print(f"   📈 ROI: {roi:.0f}x")
        
    except Exception as e:
        print(f"❌ Workflow failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())