# Claude Code Tips for MCP Template

This file provides guidance for Claude Code when working with this Cloudflare MCP template.

## Project Overview

This is a reusable template for creating Cloudflare Workers that serve Model Context Protocol (MCP) servers. The template provides a provider plugin system to support different APIs and services.

## Development Commands

### Build and Setup
- `npm run build` - Build TypeScript and inject version
- `npm run build-tsc` - Compile TypeScript only  
- `npm run inject-version` - Inject package.json version into code

### Deployment
- `npm run deploy:development` - Deploy to development environment
- `npm run deploy:staging` - Deploy to staging environment
- `npm run deploy:production` - Deploy to production environment

### Development
- `npm run dev` - Start local development server with wrangler
- `npm run format` - Format code (requires biome.json setup)

## Architecture

### Core Structure
- **Entry point**: `src/worker.ts` - Generic worker that loads providers
- **Provider system**: `src/providers/` - Pluggable API integrations
- **Transport layer**: `src/transport/` - HTTP/WebSocket MCP transport
- **Configuration**: `src/config/` - Environment validation
- **Utilities**: `src/lib/` - HTTP helpers and error handling

### Provider Pattern
Each provider implements:
1. `MCPProvider` interface - Main provider class
2. `MCPServerFactory` - Tool registration logic  
3. API client - Service-specific API wrapper
4. Required environment variables

### Key Components
- **Generic Worker**: Loads any provider via plugin system
- **Stable Naming**: Environment-specific server names
- **Professional Deployment**: SemVer tracking with git metadata
- **Build-time Version Injection**: No runtime file system access needed

## Environment Configuration

### Required Variables
- `MCP_SERVER_NAME` - Stable server name (set in wrangler.toml)
- Provider-specific API keys (varies by provider, example provider has none)

### Optional Variables  
- `BEARER_TOKEN` - Additional authentication
- `ENABLE_WS` - Enable WebSocket support (set to "true" to enable, default: false)
- `CORS_ORIGINS` - Comma-separated allowed origins (default: *)

### Environment Separation
- **Development**: `your-project-dev` 
- **Staging**: `your-project-staging`
- **Production**: `your-project`

## Creating New Providers

1. **Create provider directory**: `src/providers/your-service/`
2. **Implement interfaces**: API client, server factory, provider class
3. **Update worker.ts**: Import and use your provider
4. **Add environment types**: Update `src/types/runtime.ts`
5. **Test locally**: `npm run dev`

## Best Practices

- **Follow provider pattern** - Don't modify core transport/config
- **Use Zod schemas** for tool parameter validation
- **Return proper JSON** - Arrays for lists, objects for single items
- **Handle errors gracefully** - Use AppError for known errors
- **Professional naming** - Stable server names per environment
- **Version management** - Use build-time injection, not runtime reading

## Testing

### Local Testing
```bash
npm run dev
curl http://localhost:8787/  # Health check
```

### MCP Testing
```bash
# Initialize
curl -X POST http://localhost:8787/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test"}}}'

# List tools  
curl -X POST http://localhost:8787/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
```

## Common Issues

- **Missing environment variables** - Check wrangler.toml and secrets
- **Transport timeout** - Usually missing required env vars
- **Tool registration fails** - Check provider factory implementation
- **CORS issues** - Verify CORS_ORIGINS configuration