// Example API client for demonstration purposes
// Replace this with your actual API client

export class ExampleAPI {
    constructor(private apiKey?: string) {}

    async ping(): Promise<{ message: string; timestamp: string; authenticated: boolean }> {
        return {
            message: 'pong',
            timestamp: new Date().toISOString(),
            authenticated: !!this.apiKey,
        }
    }

    async echo(text: string): Promise<{ echo: string; length: number }> {
        return {
            echo: text,
            length: text.length,
        }
    }

    async getStatus(): Promise<{ status: string; version: string; uptime: number }> {
        return {
            status: 'ok',
            version: '1.0.0',
            uptime: Date.now(),
        }
    }
}