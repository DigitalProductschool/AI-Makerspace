# Creating Custom Providers

This template uses a provider pattern to support different APIs and services. Here's how to create your own provider.

## Provider Interface

Every provider must implement the `MCPProvider` interface:

```typescript
interface MCPProvider {
    name: string
    createAPI(env: Env): any
    createServerFactory(): MCPServerFactory
    getRequiredEnvVars(): string[]
}
```

## Creating a New Provider

### 1. Create Provider Directory
```bash
mkdir src/providers/your-service/
```

### 2. Create API Client (`api.ts`)
```typescript
export class YourServiceAPI {
    constructor(private apiKey: string) {}

    async yourMethod(): Promise<any> {
        // Implementation here
    }
}
```

### 3. Create Server Factory (`factory.ts`)
```typescript
import type { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { z } from 'zod'
import type { MCPServerFactory } from '../../types/runtime.js'
import type { YourServiceAPI } from './api.js'

export class YourServiceFactory implements MCPServerFactory {
    createServer(api: YourServiceAPI, serverName: string): McpServer {
        throw new Error('Use createMcpServer from registry.ts instead')
    }

    registerTools(server: McpServer, api: YourServiceAPI): void {
        server.tool(
            'your-tool',
            'Description of your tool',
            {
                param: z.string().describe('Parameter description'),
            },
            async ({ param }) => {
                const result = await api.yourMethod()
                return {
                    content: [{ type: 'text', text: JSON.stringify(result, null, 2) }],
                }
            },
        )
    }
}
```

### 4. Create Provider (`index.ts`)
```typescript
import type { MCPProvider, Env } from '../../types/runtime.js'
import { YourServiceAPI } from './api.js'
import { YourServiceFactory } from './factory.js'

export class YourServiceProvider implements MCPProvider {
    name = 'your-service'

    createAPI(env: Env): YourServiceAPI {
        if (!env.YOUR_SERVICE_API_KEY) {
            throw new Error('YOUR_SERVICE_API_KEY is required')
        }
        return new YourServiceAPI(env.YOUR_SERVICE_API_KEY)
    }

    createServerFactory(): YourServiceFactory {
        return new YourServiceFactory()
    }

    getRequiredEnvVars(): string[] {
        return ['YOUR_SERVICE_API_KEY']
    }
}

export const yourServiceProvider = new YourServiceProvider()
```

### 5. Update Worker to Use Your Provider
In `src/worker.ts`, replace the example provider:

```typescript
import { yourServiceProvider } from './providers/your-service/index.js'

// Replace this line:
// import { exampleProvider } from './providers/example/index.js'

// Update the validateConfig call:
const config = validateConfig(env, yourServiceProvider)

// Update the API and factory creation:
const api = yourServiceProvider.createAPI(env)
const serverFactory = yourServiceProvider.createServerFactory()

// Update the health endpoint response:
provider: yourServiceProvider.name,
```

### 6. Update Environment Types
In `src/types/runtime.ts`, add your environment variables:

```typescript
export interface Env {
    YOUR_SERVICE_API_KEY?: string
    // ... other vars
}
```

## Tool Best Practices

1. **Use Zod schemas** for parameter validation
2. **Return JSON arrays** for lists (not concatenated objects)
3. **Handle errors gracefully** with try/catch
4. **Add detailed descriptions** for tools and parameters
5. **Log tool registration** for debugging

## Provider Examples

Common types of providers that can be built with this template:

- **Task Management**: Project and task tracking systems
- **Communication**: Team messaging and collaboration platforms
- **Development**: Code repositories and CI/CD systems  
- **Content**: Document and knowledge management systems
- **Business**: CRM, analytics, and reporting platforms

Each provider follows the same pattern but connects to different APIs.