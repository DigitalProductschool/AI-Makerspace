import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js'
import { AppError } from '../lib/errors.js'
import { createNodeMocks } from '../remote/node-compat.js'
import type { AppConfig, RequestContext, MCPServerFactory } from '../types/runtime.js'

export async function handleHttpMcp(
    request: Request,
    ctx: RequestContext,
    config: AppConfig,
    serverFactory: MCPServerFactory,
    api: any,
): Promise<Response> {
    const { reqId } = ctx

    // Bearer token auth check
    if (config.bearerToken) {
        const auth = request.headers.get('Authorization')
        if (!auth || !auth.startsWith('Bearer ') || auth.slice(7) !== config.bearerToken) {
            throw new AppError('Unauthorized', 401, 'AUTH_REQUIRED')
        }
    }

    console.log(`${reqId} MCP request: ${request.method}`)

    // Create MCP server using the registry
    const { createMcpServer } = await import('../core/registry.js')
    const server = createMcpServer(serverFactory, api, config.serverName)

    // Create official MCP Streamable HTTP transport (stateless mode)
    const transport = new StreamableHTTPServerTransport({
        sessionIdGenerator: undefined,
        enableJsonResponse: true,
    })

    // Connect server to transport
    await server.connect(transport)
    console.log(`${reqId} MCP server connected to transport`)

    if (!server.isConnected) {
        throw new AppError('MCP server failed to connect to transport', 500, 'TRANSPORT_ERROR')
    }

    // Create Node.js-compatible request/response mocks
    const { req, res, toResponse } = createNodeMocks(request)

    // Get request body for POST requests
    const body = request.method === 'POST' ? await request.json() : undefined

    // Log request details
    if (body && typeof body === 'object' && 'method' in body) {
        console.log(`${reqId} MCP ${body.method} id=${(body as any).id || 'null'}`)
        console.log(`${reqId} REQUEST: ${JSON.stringify(body)}`)
        console.log(`${reqId} Server name: ${config.serverName}`)
    }

    // Handle request with timeout
    try {
        console.log(`${reqId} Starting transport.handleRequest`)
        const timeoutPromise = new Promise((_, reject) =>
            setTimeout(() => reject(new Error('Transport timeout after 30s')), 30000),
        )

        await Promise.race([transport.handleRequest(req as any, res as any, body), timeoutPromise])

        console.log(`${reqId} Transport.handleRequest completed`)
    } catch (transportError) {
        console.error(`${reqId} Transport error:`, transportError)
        throw new AppError(
            `MCP transport error: ${transportError instanceof Error ? transportError.message : 'Unknown transport error'}`,
            500,
            'TRANSPORT_ERROR',
        )
    }

    // Convert to Response and add CORS headers
    const response = await toResponse()
    const responseText = await response.text()
    console.log(`${reqId} RESPONSE: ${responseText}`)

    return new Response(responseText, {
        status: response.status,
        statusText: response.statusText,
        headers: response.headers,
    })
}