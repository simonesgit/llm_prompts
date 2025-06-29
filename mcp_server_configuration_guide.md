# MCP Server Configuration Guide for VS Code with GitHub Copilot

This guide explains how to configure an SSE-based MCP (Model Context Protocol) server for GitHub Copilot in VS Code, with a focus on token authentication and Python implementation examples.

## Overview

The Model Context Protocol (MCP) allows VS Code to connect to external servers that provide tools and context for AI assistants like GitHub Copilot. This guide covers:

- Configuring MCP servers in VS Code
- Setting up SSE (Server-Sent Events) transport
- Token authentication for GitHub API access
- Python-based MCP server implementation

## Configuration Methods

### Current Limitation: Headers Property Not Supported

**Important Note**: As of VS Code 1.99.2, there is a known issue where the `headers` property is incorrectly flagged as invalid for SSE MCP servers, even though it should be supported according to the MCP specification.

### 1. Using VS Code Settings (Recommended)

Configure in `settings.json`:

```json
{
  "mcpServers": {
    "github-server": {
      "type": "sse",
      "url": "https://your-mcp-server.com/sse",
      "env": {
        "GITHUB_TOKEN": "${input:githubToken}"
      }
    }
  }
}
```

### 2. Alternative: Using `.vscode/mcp.json` (Current Working Configuration)

Create a `.vscode/mcp.json` file in your workspace:

```json
{
  "inputs": [
    {
      "id": "github-token",
      "type": "promptString",
      "description": "GitHub Personal Access Token",
      "password": true
    }
  ],
  "servers": {
    "github-server": {
      "type": "sse",
      "url": "http://localhost:3000/sse",
      "env": {
        "GITHUB_TOKEN": "${input:github-token}"
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
  "mcpServers": {
    "github-server": {
      "type": "sse",
      "url": "https://your-mcp-server.com/sse",
      "env": {
        "GITHUB_TOKEN": "${input:githubToken}"
      }
    }
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
  "mcpServers": {
    "github-server": {
      "type": "sse",
      "url": "http://localhost:8080/sse",
      "headers": {
        "Authorization": "Bearer ${env:GITHUB_TOKEN}",
        "X-API-Key": "${env:API_KEY}"
      }
    }
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
    # Extract GitHub token from headers
    auth_header = request.headers.get('Authorization', '')
    github_token = request.headers.get('X-GitHub-Token')
    
    # Try Bearer token format first
    if auth_header.startswith('Bearer '):
        github_token = auth_header[7:]  # Remove 'Bearer ' prefix
    
    response = web.StreamResponse(
        status=200,
        reason='OK',
        headers={
            'Content-Type': 'text/event-stream',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Authorization, Content-Type, X-GitHub-Token',
        }
    )
    
    await response.prepare(request)
    
    # Initialize server with token from headers or environment
    server = GitHubMCPServer()
    if github_token:
        server.github_token = github_token
    
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

### Corrected Token Flow (Based on Actual Testing)

1. **VS Code Startup**: VS Code loads your `settings.json` or `.vscode/mcp.json`
2. **Configuration Loading**: VS Code sees the MCP server configuration
3. **Environment Variable Resolution**: VS Code resolves variables like `${input:githubToken}` or `${env:GITHUB_TOKEN}`
4. **MCP Server Connection**: VS Code establishes SSE connection to your server
5. **HTTP Headers**: If configured, VS Code sends resolved tokens in HTTP headers:
   ```http
   GET /sse HTTP/1.1
   Authorization: Bearer ghp_actual_resolved_token_value
   X-GitHub-Token: ghp_actual_resolved_token_value
   ```
6. **Initialize Request**: VS Code sends `initialize` JSON-RPC request (WITHOUT environment variables):
   ```json
   {
     "method": "initialize",
     "params": {
       "protocolVersion": "2024-11-05",
       "capabilities": {...},
       "clientInfo": {...}
       // NO environment field
     }
   }
   ```
7. **Server Processing**: Your MCP server extracts token from headers or environment variables
8. **Tool Execution**: When tools are called, server uses the stored token for GitHub API requests

## Environment Variable Handling

**Important Update**: Based on actual testing, environment variables configured in VS Code are **NOT automatically sent** in the MCP `initialize` request. The `initialize` request only contains `protocolVersion`, `capabilities`, and `clientInfo`.

### Actual Initialize Request Format:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {...},
    "clientInfo": {...}
    // NO environment field here
  }
}
```

### Alternative Approaches for Token Access:

#### Option 1: Direct Environment Access (Recommended)

The most reliable approach is to access environment variables directly in your server:

```python
import os

class GitHubMCPServer:
    def __init__(self):
        # Direct access to environment variables
        self.github_token = os.getenv('GITHUB_TOKEN')
        if not self.github_token:
            raise ValueError("GITHUB_TOKEN environment variable not set")
    
    async def initialize(self, params):
        # Token is already available from environment
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {"listChanged": True}},
            "serverInfo": {"name": "github-mcp-server", "version": "1.0.0"}
        }
```

**Setup**: Set the environment variable before starting VS Code:
```bash
export GITHUB_TOKEN="your_token_here"
code .
```

#### Option 2: VS Code Input Variables (Secure Prompting)

Use the `${input:github-token}` configuration as shown above. VS Code will securely prompt for the token when needed.

#### Option 3: HTTP Headers Authentication (Limited Support)

**Note**: Due to the current VS Code limitation where `headers` property is flagged as invalid for SSE MCP servers, this approach has limited support:

```json
{
  "mcpServers": {
    "github-server": {
      "type": "sse",
      "url": "https://your-mcp-server.com/sse",
      "headers": {
        "Authorization": "Bearer ${input:githubToken}",
        "X-GitHub-Token": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

Then extract from request headers:

```python
async def sse_handler(request):
    # Extract token from headers
    auth_header = request.headers.get('Authorization', '')
    github_token = request.headers.get('X-GitHub-Token')
    
    if auth_header.startswith('Bearer '):
        github_token = auth_header[7:]  # Remove 'Bearer ' prefix
    
    if not github_token:
        return web.Response(status=401, text="GitHub token required")
    
    # Store token for use in MCP server instance
    server = GitHubMCPServer(github_token)
    # ... rest of SSE handling
```

#### Option 4: Custom Authentication Tool

Implement a custom authentication tool that VS Code calls first:

```python
async def authenticate(self, params):
    """Custom authentication tool"""
    token = params.get("token")
    if not token:
        return {"error": "Token required"}
    
    self.github_token = token
    
    # Validate token
    if await self._validate_github_token(token):
        return {"content": [{"type": "text", "text": "Authentication successful"}]}
    else:
        return {"error": "Invalid GitHub token"}
```

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

## Current Status and Future Expectations

### Known Issues

1. **Headers Property Not Supported**: VS Code 1.99.2 incorrectly flags the `headers` property as invalid for SSE MCP servers
2. **Environment Variables Not Passed**: The MCP `initialize` request does not include environment variables

### Expected Resolution

The VS Code team has acknowledged the headers issue and it's expected to be resolved in future releases. Once fixed, the recommended configuration will be:

```json
{
  "servers": {
    "github-server": {
      "type": "sse",
      "url": "http://localhost:3000/sse",
      "headers": {
        "Authorization": "Bearer ${input:github-token}"
      }
    }
  }
}
```

## Troubleshooting

### Common Issues

1. **"Property headers is not allowed" error**: This is a known VS Code issue. Remove the `headers` property and use alternative authentication methods
2. **Token not found**: Ensure environment variable is set and VS Code can access it
3. **SSE connection fails**: Check server is running and endpoint is correct
4. **GitHub API errors**: Verify token has required scopes
5. **CORS issues**: Ensure server includes proper CORS headers

### Debug Tips

- Use VS Code Developer Tools to inspect network requests
- Add logging to your MCP server implementation
- Test server independently before integrating with VS Code
- Verify environment variables are properly set
- Check VS Code version compatibility (MCP support requires VS Code 1.99+)

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