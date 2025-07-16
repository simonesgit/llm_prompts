# Setup Guide: GitHub Copilot Multi-Repository Documentation Automation

## 🎯 Prerequisites

### Required Software
- **VS Code** (latest version)
- **GitHub Copilot Extension** (v1.100+) <mcreference link="https://github.blog/changelog/2025-05-08-github-copilot-in-vs-code-april-release-v1-100/" index="5">5</mcreference>
- **GitHub Copilot Pro/Business** subscription (for multi-file editing features)

### Required Features
- ✅ Multi-file editing (preview feature)
- ✅ @workspace participant
- ✅ Custom instructions support
- ✅ Enhanced workspace symbols

## 📁 Step 1: Workspace Preparation

### 1.1 Organize Repository Structure

```bash
# Your workspace should look like this:
workspace_root/
├── repo1/           # Your first repository
├── repo2/           # Your second repository
├── repo3/           # Your third repository
└── ...
```

### 1.2 Open Workspace in VS Code

```bash
# Open the entire workspace
code /path/to/your/workspace_root
```

### 1.3 Verify Copilot Features

1. **Check Multi-file Editing**:
   - Open Command Palette (`Cmd+Shift+P`)
   - Search for "Copilot: Start Multi-file Edit"
   - Ensure the command is available

2. **Test @workspace Participant**:
   - Open Copilot Chat (`Ctrl+Alt+I`)
   - Type `@workspace` and verify autocomplete

## 🔧 Step 2: Configure Custom Instructions

### 2.1 Create Custom Instructions File

```bash
# Create .github directory at workspace root
mkdir -p .github

# Create custom instructions file
touch .github/copilot-instructions.md
```

### 2.2 Add Project-Specific Instructions

Copy the content from [`custom_instructions.md`](./custom_instructions.md) into your `.github/copilot-instructions.md` file.

### 2.3 Verify Custom Instructions

1. Restart VS Code
2. Open Copilot Chat
3. Ask: `@workspace What are the custom instructions for this project?`
4. Verify Copilot acknowledges your custom instructions

## 📋 Step 3: Initialize Documentation Structure

### 3.1 Create Documentation Folders

Run this in your workspace root:

```bash
# Create documentation folders for each repository
for repo in */; do
    if [ -d "$repo" ] && [ "$repo" != ".*" ]; then
        repo_name=$(basename "$repo")
        mkdir -p "${repo_name}_documentation"
        echo "Created documentation folder for $repo_name"
    fi
done
```

### 3.2 Verify Structure

Your workspace should now look like:

```
workspace_root/
├── repo1/
├── repo1_documentation/     # ← New
├── repo2/
├── repo2_documentation/     # ← New
├── repo3/
├── repo3_documentation/     # ← New
└── .github/
    └── copilot-instructions.md
```

## 🚀 Step 4: Enable Advanced Features

### 4.1 Enable Multi-file Editing Preview

1. Open VS Code Settings (`Cmd+,`)
2. Search for "copilot preview"
3. Enable:
   - `github.copilot.editor.enableMultiFileEdit`
   - `github.copilot.chat.enableMultiFileEdit`

### 4.2 Configure Workspace Context

1. Open Settings
2. Search for "copilot workspace"
3. Ensure these are enabled:
   - `github.copilot.advanced.workspaceContext`
   - `github.copilot.advanced.symbolLinks`

### 4.3 Optimize Performance

```json
// Add to workspace settings (.vscode/settings.json)
{
    "github.copilot.advanced.length": 10000,
    "github.copilot.advanced.inlineSuggestCount": 5,
    "github.copilot.chat.localeOverride": "en",
    "github.copilot.editor.enableAutoCompletions": true
}
```

## 🔍 Step 5: Test Setup

### 5.1 Basic Workspace Test

1. Open Copilot Chat
2. Run: `@workspace Analyze the structure of this multi-repository project`
3. Verify Copilot can see all repositories

### 5.2 Multi-file Editing Test

1. Start multi-file edit session:
   - Command Palette → "Copilot: Start Multi-file Edit"
2. Prompt: "Create a basic README.md file in each documentation folder"
3. Verify files are created across multiple folders

### 5.3 Custom Instructions Test

1. Ask: `@workspace Generate documentation following our project standards`
2. Verify output follows your custom instructions format

## ⚡ Step 6: Performance Optimization

### 6.1 Workspace Indexing

```bash
# Ensure proper file indexing
# Add to .vscode/settings.json
{
    "files.watcherExclude": {
        "**/node_modules/**": true,
        "**/.git/**": true,
        "**/dist/**": true,
        "**/build/**": true
    },
    "search.exclude": {
        "**/node_modules": true,
        "**/dist": true,
        "**/build": true
    }
}
```

### 6.2 Memory Management

For large workspaces:

```json
{
    "github.copilot.advanced.debug.overrideEngine": "gpt-4",
    "github.copilot.advanced.debug.useNodeRuntime": true,
    "typescript.preferences.includePackageJsonAutoImports": "off"
}
```

## 🔧 Troubleshooting

### Common Issues

1. **@workspace not working**:
   - Restart VS Code
   - Check Copilot subscription status
   - Verify workspace is properly opened (not individual folders)

2. **Multi-file editing unavailable**:
   - Update Copilot extension to latest version
   - Enable preview features in settings
   - Check subscription includes preview features

3. **Custom instructions ignored**:
   - Verify file location: `.github/copilot-instructions.md`
   - Check file format (must be Markdown)
   - Restart VS Code after changes

4. **Performance issues**:
   - Exclude large directories from indexing
   - Close unnecessary files/tabs
   - Restart VS Code periodically

### Verification Commands

```bash
# Check Copilot status
code --list-extensions | grep copilot

# Verify workspace structure
find . -maxdepth 2 -type d | sort

# Check custom instructions
cat .github/copilot-instructions.md
```

## ✅ Setup Complete

Once setup is complete, proceed to:
1. [`automation_prompts.md`](./automation_prompts.md) - Execute documentation generation
2. [`workflow_automation.md`](./workflow_automation.md) - Advanced automation techniques

---

**Next Step**: [Automation Prompts →](./automation_prompts.md)