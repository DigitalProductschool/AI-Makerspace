import type { AppConfig, Env, MCPProvider } from '../types/runtime.js'

export function validateConfig(env: Env, provider?: MCPProvider): AppConfig {
    const serverName = env.MCP_SERVER_NAME
    if (!serverName) {
        throw new Error('Missing required environment variable: MCP_SERVER_NAME')
    }

    // Check provider-specific required environment variables
    if (provider) {
        const requiredVars = provider.getRequiredEnvVars()
        for (const varName of requiredVars) {
            if (!env[varName as keyof Env]) {
                throw new Error(`Missing required environment variable: ${varName}`)
            }
        }
    }

    // WebSocket disabled by default (can be enabled with ENABLE_WS=true)
    const enableWebSocket = env.ENABLE_WS === 'true'
    const corsOrigins = env.CORS_ORIGINS ? env.CORS_ORIGINS.split(',') : ['*']

    return {
        serverName,
        enableWebSocket,
        corsOrigins,
        bearerToken: env.BEARER_TOKEN,
        apiKey: env.API_KEY,
    }
}