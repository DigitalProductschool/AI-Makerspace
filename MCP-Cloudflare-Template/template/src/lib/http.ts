// HTTP utilities for Cloudflare Workers MCP template

export function corsHeaders(origins: string[] = ['*']): Record<string, string> {
    return {
        'Access-Control-Allow-Origin': origins[0], // Use first origin or *
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers':
            'Authorization, Content-Type, MCP-Protocol-Version, Mcp-Session-Id',
        'Access-Control-Expose-Headers': 'MCP-Protocol-Version, Mcp-Session-Id',
        'Access-Control-Max-Age': '86400',
        Vary: 'Origin',
    }
}

export function jsonResponse(
    status: number,
    data: unknown,
    headers?: Record<string, string>,
): Response {
    return new Response(JSON.stringify(data), {
        status,
        headers: {
            'Content-Type': 'application/json',
            ...corsHeaders(),
            ...headers,
        },
    })
}

export function textResponse(
    status: number,
    body: string,
    headers?: Record<string, string>,
): Response {
    return new Response(body, {
        status,
        headers: {
            ...corsHeaders(),
            ...headers,
        },
    })
}