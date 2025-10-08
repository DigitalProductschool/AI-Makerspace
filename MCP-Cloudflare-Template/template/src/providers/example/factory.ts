import type { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { z } from 'zod'
import type { MCPServerFactory } from '../../types/runtime.js'
import type { ExampleAPI } from './api.js'

export class ExampleServerFactory implements MCPServerFactory {
    createServer(api: ExampleAPI, serverName: string): McpServer {
        // The server creation is handled by the generic registry
        // This method exists for interface compliance but actual creation
        // happens in the registry with proper version injection
        throw new Error('Use createMcpServer from registry.ts instead')
    }

    registerTools(server: McpServer, api: ExampleAPI): void {
        // Ping tool - simple connectivity test
        server.tool(
            'ping',
            'Test connectivity to the service',
            {},
            async () => {
                const result = await api.ping()
                return {
                    content: [{ type: 'text', text: JSON.stringify(result, null, 2) }],
                }
            },
        )

        // Echo tool - text processing example
        server.tool(
            'echo',
            'Echo back text with metadata',
            {
                text: z.string().describe('Text to echo back'),
            },
            async ({ text }) => {
                const result = await api.echo(text)
                return {
                    content: [{ type: 'text', text: JSON.stringify(result, null, 2) }],
                }
            },
        )

        // Status tool - service information
        server.tool(
            'get-status',
            'Get service status and information',
            {},
            async () => {
                const result = await api.getStatus()
                return {
                    content: [{ type: 'text', text: JSON.stringify(result, null, 2) }],
                }
            },
        )

        console.log('Example provider tools registered: ping, echo, get-status')
    }
}