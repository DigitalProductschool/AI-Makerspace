# Cloudflare MCP Template

A reusable template for creating **Cloudflare Workers** that serve **Model Context Protocol (MCP)** servers with a **provider plugin system**.

## 🚀 Quick Start

```bash
# Clone this template repository
git clone https://github.com/mahmoudfazeli/cloudflare-mcp-template.git
cd cloudflare-mcp-template

# Copy template files to your new project directory
mkdir ../your-mcp-project
cp -r template/* ../your-mcp-project/
cd ../your-mcp-project/

# Set up for your project  
sed 's/{{PROJECT_NAME}}/your-project-name/g' package.json.template > package.json
sed 's/{{PROJECT_NAME}}/your-project-name/g' wrangler.toml.template > wrangler.toml

# Install dependencies
npm install

# Set up OAuth 2.1 infrastructure (creates KV namespaces)
npm run setup-oauth

# Test locally
npm run dev
```

Visit http://localhost:8787/ to see the running server with example tools.

## 🎯 What You Get

### 🔌 **Provider Plugin System**
- **Easy API Integration**: Connect to any REST API or service
- **Example Provider**: Working ping/echo/status tools out of the box
- **Clean Interfaces**: `MCPProvider` and `MCPServerFactory` patterns

### 🏗️ **Production-Ready Architecture** 
- **Modular Design**: Reusable transport, config, error handling
- **Stable Naming**: Environment-specific server names (`project-dev`, `project-staging`, `project`)
- **Professional Deployment**: SemVer tracking with git metadata
- **TypeScript Strict**: Full type safety and validation

### 📋 **Complete Setup**
- **Build Scripts**: Version injection, TypeScript compilation
- **Documentation**: Usage guides and provider creation
- **Testing**: curl examples and local development
- **CORS & Auth**: Production security features

## 📁 Template Structure

```
template/
├── src/
│   ├── worker.ts              # Generic worker entry point
│   ├── transport/             # MCP transport layer
│   │   └── http.ts           # Streamable HTTP transport
│   ├── lib/                   # Utilities
│   │   ├── http.ts           # CORS, JSON responses
│   │   ├── errors.ts         # Error handling & mapping
│   │   └── oauth.ts          # OAuth 2.1 with DCR
│   ├── config/               # Configuration
│   │   └── index.ts          # Environment validation
│   ├── core/                 # MCP Server
│   │   └── registry.ts       # Generic server factory
│   ├── types/                # TypeScript types
│   │   └── runtime.ts        # Env, Provider interfaces
│   ├── remote/               # Compatibility layer
│   │   └── node-compat.ts    # Node.js compatibility shims
│   └── providers/example/    # Example provider
│       ├── index.ts          # Provider implementation
│       ├── factory.ts        # Tool registration
│       └── api.ts            # API client
├── scripts/                  # Build & deployment
│   ├── deploy.ts            # Environment-aware deployment
│   ├── inject-version.ts    # Build-time version injection
│   └── setup-oauth.ts       # OAuth 2.1 KV namespace setup
├── docs/                    # Documentation
│   ├── USAGE.md            # Quick start guide
│   ├── PROVIDERS.md        # How to create providers
│   └── CLAUDE.md           # Claude Code integration tips
├── package.json.template   # Template package.json
├── wrangler.toml.template  # Template wrangler config
└── tsconfig.json          # TypeScript configuration
```

## 🔧 Creating a Provider

1. **Create provider directory**: `src/providers/your-service/`
2. **Implement API client**: Connect to your service's REST API
3. **Create server factory**: Register MCP tools using Zod schemas  
4. **Update worker.ts**: Import and use your provider
5. **Test locally**: `npm run dev` and curl the endpoints

See [docs/PROVIDERS.md](template/docs/PROVIDERS.md) for detailed instructions.

## 🌍 Environment Setup

The template supports three environments with stable naming:

- **Development**: `your-project-dev` 
- **Staging**: `your-project-staging`
- **Production**: `your-project`

Deploy with:
```bash
npm run deploy:development
npm run deploy:staging  
npm run deploy:production
```

## 📖 Documentation

- **[USAGE.md](template/docs/USAGE.md)** - Quick start and testing
- **[PROVIDERS.md](template/docs/PROVIDERS.md)** - Creating custom providers
- **[CLAUDE.md](template/docs/CLAUDE.md)** - Claude Code integration

## ✨ Features

### MCP Protocol Support
- ✅ **Initialize** - Server info with stable naming
- ✅ **Tools/List** - Dynamic tool discovery  
- ✅ **Tools/Call** - Parameterized tool execution
- ✅ **Error Handling** - Proper JSON-RPC error responses

### OAuth 2.1 Authentication
- ✅ **Dynamic Client Registration** - No manual OAuth setup needed
- ✅ **MCP Specification Compliant** - Follows official auth standards
- ✅ **Secure Credential Storage** - KV namespace isolation per environment
- ✅ **Claude.ai Compatible** - Works with web/mobile connectors out-of-the-box

### Cloudflare Workers Optimized
- ✅ **Stateless Transport** - No session persistence needed
- ✅ **Node.js Compatibility** - Shims for MCP SDK
- ✅ **Build-time Version** - No runtime file system access
- ✅ **Professional Deployment** - Git metadata tracking
- ✅ **Multi-Environment Setup** - Development/staging/production ready

### Claude Integration Ready
- ✅ **WebSocket Support** - Optional for Claude web UI
- ✅ **CORS Headers** - Proper cross-origin handling
- ✅ **Stable URLs** - No connector reconfiguration needed
- ✅ **OAuth 2.1 DCR** - Leave OAuth fields empty, authentication handled automatically

## 🎯 Use Cases

This template can be used to create MCP servers for various types of services:

- **Task Management** - Projects, tasks, and workflows
- **Team Communication** - Messages, channels, and notifications  
- **Development Tools** - Code repositories, issues, and CI/CD
- **Content Management** - Documents, notes, and knowledge bases
- **Business Applications** - CRM, analytics, and reporting tools

Each provider follows the same pattern but connects to different APIs.

## 📄 License

MIT License - See template files for details.