import type { MCPProvider, Env } from '../../types/runtime.js'
import { ExampleAPI } from './api.js'
import { ExampleServerFactory } from './factory.js'

export class ExampleProvider implements MCPProvider {
    name = 'example'

    createAPI(env: Env): ExampleAPI {
        return new ExampleAPI(env.API_KEY)
    }

    createServerFactory(): ExampleServerFactory {
        return new ExampleServerFactory()
    }

    getRequiredEnvVars(): string[] {
        // API_KEY is optional for the example provider
        return []
    }
}

// Export the provider instance
export const exampleProvider = new ExampleProvider()