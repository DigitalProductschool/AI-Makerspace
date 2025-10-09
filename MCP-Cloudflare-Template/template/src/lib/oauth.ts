// OAuth 2.1 implementation for MCP servers
// Implements Dynamic Client Registration per MCP specification

import type { Env } from '../types/runtime.js'
import { jsonResponse } from './http.js'

export interface ClientRegistrationRequest {
    client_name?: string
    redirect_uris?: string[]
}

export interface ClientCredentials {
    client_id: string
    client_secret: string
    client_name: string
    redirect_uris: string[]
    created_at: string
}

/**
 * Handles OAuth 2.0 Dynamic Client Registration (DCR)
 * Per MCP specification: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization
 */
export async function handleClientRegistration(
    request: Request,
    env: Env,
    reqId: string,
): Promise<Response> {
    try {
        const registrationRequest: ClientRegistrationRequest = await request.json()
        console.log(`${reqId} DCR request:`, JSON.stringify(registrationRequest))

        // Generate unique client credentials
        const clientId = crypto.randomUUID()
        const clientSecret = crypto.randomUUID()

        // Store client credentials in KV namespace
        const clientData: ClientCredentials = {
            client_id: clientId,
            client_secret: clientSecret,
            client_name: registrationRequest.client_name || 'MCP Client',
            redirect_uris: registrationRequest.redirect_uris || [],
            created_at: new Date().toISOString(),
        }

        await env.OAUTH_CLIENTS.put(clientId, JSON.stringify(clientData))
        console.log(`${reqId} Registered OAuth client: ${clientId}`)

        // Return OAuth 2.1 compliant registration response
        return jsonResponse(201, {
            client_id: clientId,
            client_secret: clientSecret,
            client_name: clientData.client_name,
            redirect_uris: clientData.redirect_uris,
            grant_types: ['authorization_code', 'client_credentials'],
            response_types: ['code'],
            token_endpoint_auth_method: 'client_secret_basic',
        })
    } catch (error) {
        console.error(`${reqId} DCR error:`, error)
        return jsonResponse(400, {
            error: 'invalid_request',
            error_description: 'Invalid client registration request',
        })
    }
}

/**
 * Returns OAuth 2.0 Authorization Server Metadata
 * Per RFC 8414: https://tools.ietf.org/html/rfc8414
 */
export function getAuthorizationServerMetadata(serverUrl: string): Response {
    return jsonResponse(200, {
        issuer: serverUrl,
        authorization_endpoint: `${serverUrl}/authorize`,
        token_endpoint: `${serverUrl}/token`,
        registration_endpoint: `${serverUrl}/register`,
        response_types_supported: ['code'],
        grant_types_supported: ['authorization_code', 'client_credentials'],
        code_challenge_methods_supported: ['S256'],
        scopes_supported: ['mcp:tools'],
        token_endpoint_auth_methods_supported: ['client_secret_basic', 'client_secret_post'],
    })
}