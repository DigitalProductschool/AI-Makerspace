# Cloudflare MCP Template Usage

## Quick Start

1. **Copy template files to your project:**
   ```bash
   cp -r template/* your-mcp-project/
   cd your-mcp-project/
   ```

2. **Replace template variables:**
   ```bash
   # Replace {{PROJECT_NAME}} in package.json.template and wrangler.toml.template
   sed 's/{{PROJECT_NAME}}/your-project-name/g' package.json.template > package.json
   sed 's/{{PROJECT_NAME}}/your-project-name/g' wrangler.toml.template > wrangler.toml
   ```

3. **Install dependencies:**
   ```bash
   npm install
   ```

4. **Set up OAuth 2.1 infrastructure:**
   ```bash
   npm run setup-oauth
   # Creates KV namespaces for OAuth client storage across all environments
   ```

5. **Test the example provider:**
   ```bash
   npm run dev
   # Server runs at http://localhost:8787
   ```

6. **Configure your provider:**
   - Edit `src/providers/your-provider/` 
   - Implement `MCPServerFactory` interface
   - Add tools and API client
   - Update `src/worker.ts` to use your provider

7. **Deploy:**
   ```bash
   # Set required secrets (if needed by your provider)
   wrangler secret put API_KEY --env development
   
   # Deploy
   npm run deploy:development
   ```

## Testing

### Local Development
```bash
npm run dev
```

### Test MCP endpoints
```bash
# Health check
curl http://localhost:8787/

# Test OAuth 2.1 metadata
curl http://localhost:8787/.well-known/oauth-authorization-server

# Initialize MCP (note: requires proper MCP headers) 
curl -X POST http://localhost:8787/ \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "MCP-Protocol-Version: 2024-11-05" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0.0"}}}'

# List tools
curl -X POST http://localhost:8787/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "MCP-Protocol-Version: 2024-11-05" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'

# Call example tool
curl -X POST http://localhost:8787/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "MCP-Protocol-Version: 2024-11-05" \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"ping","arguments":{}}}'
```

## Integration with Claude

### Claude Desktop
Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "your-project": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/client-fetch",
        "https://your-project.your-account.workers.dev"
      ]
    }
  }
}
```

### Claude.ai Web/Mobile Connector
Use the "Add Custom Connector" option with:
- **Server URL**: `https://your-project.your-account.workers.dev`
- **OAuth Client ID**: Leave empty (uses Dynamic Client Registration)
- **OAuth Client Secret**: Leave empty (uses Dynamic Client Registration)

**OAuth 2.1 Features:**
- Automatic client registration via `/register` endpoint
- No manual OAuth setup required
- Secure credential storage in Cloudflare KV
- MCP specification compliant authentication

## Next Steps

See [PROVIDERS.md](PROVIDERS.md) for creating custom providers.