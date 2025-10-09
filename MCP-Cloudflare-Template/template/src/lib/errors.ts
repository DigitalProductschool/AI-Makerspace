// Error handling utilities for MCP template

export class AppError extends Error {
    constructor(
        message: string,
        public status: number = 500,
        public code: string = 'INTERNAL_ERROR',
    ) {
        super(message)
        this.name = 'AppError'
    }
}

export function errorToResponse(error: unknown, reqId: string): Response {
    console.error(`${reqId} Error:`, error)

    if (error instanceof AppError) {
        return new Response(
            JSON.stringify({
                jsonrpc: '2.0',
                error: {
                    code: -32603,
                    message: error.message,
                    data: error.code,
                },
                id: null,
            }),
            {
                status: error.status,
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                },
            },
        )
    }

    const message = error instanceof Error ? error.message : 'Unknown error'
    return new Response(
        JSON.stringify({
            jsonrpc: '2.0',
            error: {
                code: -32603,
                message: 'Internal error',
                data: message,
            },
            id: null,
        }),
        {
            status: 500,
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            },
        },
    )
}