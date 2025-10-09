import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import type { MCPServerFactory } from '../types/runtime.js'

// Build-time version injection - replaced during compilation
const VERSION = '1.0.0'

/**
 * Generic MCP server registry that uses provider factory pattern
 */
export function createMcpServer(serverFactory: MCPServerFactory, api: any, serverName: string): McpServer {
    const server = new McpServer({
        name: serverName,
        version: VERSION,
    })

    // Register tools using the provider factory
    serverFactory.registerTools(server, api)

    console.log('MCP server created successfully with provider tools')
    return server
}