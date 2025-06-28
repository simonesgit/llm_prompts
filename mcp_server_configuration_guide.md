# MCP Server Configuration Guide for VS Code with GitHub Copilot

This guide explains how to configure an SSE-based MCP (Model Context Protocol) server for GitHub Copilot in VS Code, with a focus on token authentication and Python implementation examples.

## Overview

The Model Context Protocol (MCP) allows VS Code to connect to external servers that provide tools and context for AI assistants like GitHub Copilot. This guide covers:

- Configuring MCP servers in VS Code
- Setting up SSE (Server-Sent Events) transport
- Token authentication for GitHub API access
- Python-based MCP server implementation

## Configuration Methods

### 1. Using `.vscode/mcp.json` (Recommended)

Create a `.vscode/mcp.json` file in your workspace:

```json
{
  "servers": {
    "github-mcp-server": {
      "command": "python",
      "args": ["/path/to/your/mcp_server.py"],
      "transport": "sse",
      "endpoint": "http://localhost:8080/sse",
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

### 2. Using VS Code Settings

Alternatively, configure in `settings.json`:

```json
{
  "mcp.servers": {
    "github-mcp-server": {
      "command": "python",
      "args": ["/path/to/your/mcp_server.py"],
      "transport": "sse",
      "endpoint": "http://localhost:8080/sse",
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

## Token Authentication Options

### Option 1: Environment Variables (Recommended)

**Configuration:**
```json
{
  "env": {
    "GITHUB_TOKEN": "${env:GITHUB_TOKEN}"
  }
}
```

**Setup:**
1. Set the environment variable in your shell:
   ```bash
   export GITHUB_TOKEN="ghp_your_token_here"
   ```

2. Or add to your `.env` file:
   ```
   GITHUB_TOKEN=ghp_your_token_here
   ```

### Option 2: VS Code Input Variables

**Configuration:**
```json
{
  "env": {
    "GITHUB_TOKEN": "${input:githubToken}"
  },
  "inputs": [
    {
      "id": "githubToken",
      "type": "password",
      "description": "Enter your GitHub Personal Access Token"
    }
  ]
}
```

### Option 3: HTTP Headers

**Configuration:**
```json
{
  "transport": "sse",
  "endpoint": "http://localhost:8080/sse",
  "headers": {
    "Authorization": "Bearer ${env:GITHUB_TOKEN}",
    "X-API-Key": "${env:API_KEY}"
  }
}
```

## Python MCP Server Implementation

### Basic SSE Server Structure

```python
#!/usr/bin/env python3
import os
import json
import asyncio
from aiohttp import web, ClientSession
from aiohttp.web_response import Response
import logging

class GitHubMCPServer:
    def __init__(self):
        self.github_token = None
        self.tools = {
            "create_issue": self.create_issue,
            "list_repositories": self.list_repositories,
            "get_file_content": self.get_file_content
        }
        
    async def initialize(self, params):
        """Handle MCP initialization request"""
        # Extract GitHub token from environment or initialization params
        self.github_token = (
            params.get("environment", {}).get("GITHUB_TOKEN") or
            os.getenv("GITHUB_TOKEN")
        )
        
        if not self.github_token:
            raise ValueError("GitHub token not provided")
            
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {
                    "listChanged": True
                }
            },
            "serverInfo": {
                "name": "github-mcp-server",
                "version": "1.0.0"
            }
        }
    
    async def list_tools(self):
        """Return available tools"""
        return {
            "tools": [
                {
                    "name": "create_issue",
                    "description": "Create a new GitHub issue",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "owner": {"type": "string"},
                            "repo": {"type": "string"},
                            "title": {"type": "string"},
                            "body": {"type": "string"}
                        },
                        "required": ["owner", "repo", "title"]
                    }
                },
                {
                    "name": "list_repositories",
                    "description": "List user repositories",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "username": {"type": "string"}
                        }
                    }
                }
            ]
        }
    
    async def create_issue(self, params):
        """Create a GitHub issue using the provided token"""
        owner = params["owner"]
        repo = params["repo"]
        title = params["title"]
        body = params.get("body", "")
        
        headers = {
            "Authorization": f"Bearer {self.github_token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "MCP-GitHub-Server/1.0"
        }
        
        payload = {
            "title": title,
            "body": body
        }
        
        async with ClientSession() as session:
            url = f"https://api.github.com/repos/{owner}/{repo}/issues"
            async with session.post(url, headers=headers, json=payload) as response:
                if response.status == 201:
                    issue_data = await response.json()
                    return {
                        "content": [{
                            "type": "text",
                            "text": f"Successfully created issue #{issue_data['number']}: {issue_data['html_url']}"
                        }]
                    }
                else:
                    error_text = await response.text()
                    return {
                        "content": [{
                            "type": "text",
                            "text": f"Failed to create issue: {response.status} - {error_text}"
                        }],
                        "isError": True
                    }
    
    async def list_repositories(self, params):
        """List repositories for a user"""
        username = params.get("username", "user")
        
        headers = {
            "Authorization": f"Bearer {self.github_token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "MCP-GitHub-Server/1.0"
        }
        
        async with ClientSession() as session:
            url = f"https://api.github.com/users/{username}/repos"
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    repos = await response.json()
                    repo_list = "\n".join([f"- {repo['name']}: {repo['html_url']}" for repo in repos[:10]])
                    return {
                        "content": [{
                            "type": "text",
                            "text": f"Repositories for {username}:\n{repo_list}"
                        }]
                    }
                else:
                    error_text = await response.text()
                    return {
                        "content": [{
                            "type": "text",
                            "text": f"Failed to fetch repositories: {response.status} - {error_text}"
                        }],
                        "isError": True
                    }

# SSE endpoint handler
async def sse_handler(request):
    """Handle SSE connections from VS Code"""
    response = web.StreamResponse(
        status=200,
        reason='OK',
        headers={
            'Content-Type': 'text/event-stream',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Authorization, Content-Type',
        }
    )
    
    await response.prepare(request)
    
    server = GitHubMCPServer()
    
    try:
        async for line in request.stream():
            if line:
                try:
                    message = json.loads(line.decode())
                    method = message.get("method")
                    params = message.get("params", {})
                    msg_id = message.get("id")
                    
                    if method == "initialize":
                        result = await server.initialize(params)
                    elif method == "tools/list":
                        result = await server.list_tools()
                    elif method == "tools/call":
                        tool_name = params.get("name")
                        tool_params = params.get("arguments", {})
                        if tool_name in server.tools:
                            result = await server.tools[tool_name](tool_params)
                        else:
                            result = {"error": f"Unknown tool: {tool_name}"}
                    else:
                        result = {"error": f"Unknown method: {method}"}
                    
                    # Send response
                    response_msg = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": result
                    }
                    
                    await response.write(f"data: {json.dumps(response_msg)}\n\n".encode())
                    
                except json.JSONDecodeError:
                    error_msg = {
                        "jsonrpc": "2.0",
                        "error": {"code": -32700, "message": "Parse error"}
                    }
                    await response.write(f"data: {json.dumps(error_msg)}\n\n".encode())
                    
    except Exception as e:
        logging.error(f"SSE handler error: {e}")
    
    return response

# Web application setup
app = web.Application()
app.router.add_post('/sse', sse_handler)
app.router.add_get('/sse', sse_handler)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, host='localhost', port=8080)
```

### Alternative: Direct Environment Access

```python
import os

class GitHubMCPServer:
    def __init__(self):
        # Direct environment variable access
        self.github_token = os.getenv('GITHUB_TOKEN')
        if not self.github_token:
            raise ValueError("GITHUB_TOKEN environment variable not set")
    
    async def make_github_request(self, method, url, **kwargs):
        """Helper method for GitHub API requests"""
        headers = kwargs.get('headers', {})
        headers.update({
            'Authorization': f'Bearer {self.github_token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'MCP-GitHub-Server/1.0'
        })
        kwargs['headers'] = headers
        
        async with ClientSession() as session:
            async with session.request(method, url, **kwargs) as response:
                return response, await response.json() if response.content_type == 'application/json' else await response.text()
```

## Token Flow Timeline

1. **VS Code Startup**: VS Code loads MCP configuration from `.vscode/mcp.json` or `settings.json`
2. **Environment Resolution**: VS Code resolves `${env:GITHUB_TOKEN}` from environment variables
3. **Server Connection**: VS Code initiates SSE connection to the MCP server endpoint
4. **Initialize Request**: VS Code sends MCP `initialize` request with resolved environment variables
5. **Token Processing**: MCP server receives and stores the GitHub token for API calls
6. **Tool Execution**: When tools are called, the server uses the stored token for GitHub API requests

## Security Best Practices

### Token Management
- **Never hardcode tokens** in configuration files
- Use environment variables or VS Code input variables
- Validate tokens on server startup
- Handle token expiration gracefully
- Log authentication failures (without exposing tokens)

### Server Security
```python
class SecureGitHubMCPServer:
    def __init__(self):
        self.github_token = None
        self._validate_environment()
    
    def _validate_environment(self):
        """Validate required environment variables"""
        required_vars = ['GITHUB_TOKEN']
        missing = [var for var in required_vars if not os.getenv(var)]
        if missing:
            raise ValueError(f"Missing required environment variables: {missing}")
    
    def _validate_token(self, token):
        """Validate GitHub token format"""
        if not token or not token.startswith(('ghp_', 'github_pat_')):
            raise ValueError("Invalid GitHub token format")
        return token
    
    async def initialize(self, params):
        """Secure initialization with token validation"""
        token = (
            params.get("environment", {}).get("GITHUB_TOKEN") or
            os.getenv("GITHUB_TOKEN")
        )
        
        self.github_token = self._validate_token(token)
        
        # Test token validity
        await self._test_github_connection()
        
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {"listChanged": True}},
            "serverInfo": {"name": "github-mcp-server", "version": "1.0.0"}
        }
    
    async def _test_github_connection(self):
        """Test GitHub API connection"""
        headers = {
            "Authorization": f"Bearer {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        async with ClientSession() as session:
            async with session.get("https://api.github.com/user", headers=headers) as response:
                if response.status != 200:
                    raise ValueError(f"GitHub token validation failed: {response.status}")
```

## Required GitHub Token Scopes

For different operations, your GitHub Personal Access Token needs specific scopes:

- **Repository access**: `repo` (for private repos) or `public_repo` (for public repos only)
- **Issue management**: `repo` or `public_repo`
- **Pull requests**: `repo` or `public_repo`
- **User information**: `user:read`
- **Organization access**: `read:org`

## Troubleshooting

### Common Issues

1. **Token not found**: Ensure environment variable is set and VS Code can access it
2. **SSE connection fails**: Check server is running and endpoint is correct
3. **GitHub API errors**: Verify token has required scopes
4. **CORS issues**: Ensure server includes proper CORS headers

### Debug Configuration

```json
{
  "servers": {
    "github-mcp-server": {
      "command": "python",
      "args": ["/path/to/your/mcp_server.py", "--debug"],
      "transport": "sse",
      "endpoint": "http://localhost:8080/sse",
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}",
        "LOG_LEVEL": "DEBUG"
      }
    }
  }
}
```

## Alternative: Using mcp-proxy

For complex setups, consider using `mcp-proxy` to bridge different transports:

```bash
# Install mcp-proxy
npm install -g @mcp/proxy

# Run with environment variables
GITHUB_TOKEN=your_token mcp-proxy --sse --port 8080 --target stdio://python mcp_server.py
```

## Conclusion

This guide provides a comprehensive approach to configuring SSE-based MCP servers for GitHub Copilot in VS Code using Python. The key points are:

- Use environment variables for secure token management
- Implement proper token validation and error handling
- Follow security best practices
- Test your configuration thoroughly

For production use, consider implementing additional features like token refresh, rate limiting, and comprehensive logging.