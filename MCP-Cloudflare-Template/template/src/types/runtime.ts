// Runtime types for Cloudflare Workers MCP template

// Cloudflare Workers KV types
interface KVNamespace {
    get(
        key: string,
        options?: { type: 'text' | 'json' | 'arrayBuffer' | 'stream' },
    ): Promise<string | null>
    put(
        key: string,
        value: string | ArrayBuffer | ArrayBufferView | ReadableStream,
        options?: any,
    ): Promise<void>
    delete(key: string): Promise<void>
    list(options?: any): Promise<{ keys: { name: string }[] }>
}

export interface Env {
    API_KEY?: string // Provider-specific API key
    BEARER_TOKEN?: string
    MCP_SERVER_NAME?: string
    ENABLE_WS?: string
    CORS_ORIGINS?: string
    OAUTH_CLIENTS: KVNamespace // OAuth 2.1 client credential storage
    // Add other provider-specific env vars as needed
}

export interface RequestContext {
    reqId: string
    url: URL
    env: Env
}

export interface AppConfig {
    serverName: string
    enableWebSocket: boolean
    corsOrigins: string[]
    bearerToken?: string
    apiKey?: string
    // Provider-specific config will extend this
}

// Provider interfaces
export interface MCPServerFactory {
    createServer(api: any, serverName: string): any // McpServer instance
    registerTools(server: any, api: any): void
}

export interface MCPProvider {
    name: string
    createAPI(env: Env): any
    createServerFactory(): MCPServerFactory
    getRequiredEnvVars(): string[]
}