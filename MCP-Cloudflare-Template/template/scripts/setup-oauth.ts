#!/usr/bin/env tsx

import { execSync } from 'node:child_process'
import { readFileSync, writeFileSync } from 'node:fs'

console.log('🔐 Setting up OAuth 2.1 infrastructure...')
console.log('')

const packageJson = JSON.parse(readFileSync('package.json', 'utf8'))
const projectName = packageJson.name

// Create KV namespaces for each environment
const environments = ['development', 'staging', 'production']
const kvIds: Record<string, string> = {}

console.log('Creating KV namespaces for OAuth client storage...')

for (const env of environments) {
    try {
        console.log(`📦 Creating KV namespace for ${env}...`)
        
        const namespaceName = `${projectName}-oauth-clients-${env}`
        const result = execSync(
            `wrangler kv namespace create "${namespaceName}"`,
            { encoding: 'utf8' }
        )
        
        // Extract KV namespace ID from wrangler output
        const match = result.match(/id = "([^"]+)"/)
        if (match) {
            kvIds[env] = match[1]
            console.log(`✅ ${env}: ${match[1]}`)
        } else {
            console.error(`❌ Failed to extract KV ID for ${env}`)
            continue
        }
    } catch (error) {
        console.error(`❌ Failed to create KV namespace for ${env}:`, error.message)
    }
}

console.log('')

// Update wrangler.toml with actual KV IDs
if (Object.keys(kvIds).length > 0) {
    console.log('📝 Updating wrangler.toml with KV namespace IDs...')
    
    let wranglerContent = readFileSync('wrangler.toml', 'utf8')
    
    // Replace placeholder IDs with actual ones
    if (kvIds.development) {
        wranglerContent = wranglerContent.replace(
            'REPLACE_WITH_DEV_KV_ID',
            kvIds.development
        )
    }
    if (kvIds.staging) {
        wranglerContent = wranglerContent.replace(
            'REPLACE_WITH_STAGING_KV_ID',
            kvIds.staging
        )
    }
    if (kvIds.production) {
        wranglerContent = wranglerContent.replace(
            'REPLACE_WITH_PRODUCTION_KV_ID',
            kvIds.production
        )
    }
    
    writeFileSync('wrangler.toml', wranglerContent)
    console.log('✅ wrangler.toml updated successfully')
} else {
    console.log('❌ No KV namespaces created successfully')
    process.exit(1)
}

console.log('')
console.log('🎉 OAuth 2.1 setup complete!')
console.log('')
console.log('Your MCP server now supports:')
console.log('  ✅ Dynamic Client Registration (DCR)')
console.log('  ✅ OAuth 2.1 compliant authentication')
console.log('  ✅ Multi-environment KV storage')
console.log('  ✅ Claude.ai connector compatibility')
console.log('')
console.log('Next steps:')
console.log('  1. Deploy: npm run deploy:development')
console.log('  2. Test: curl https://your-worker.workers.dev/.well-known/oauth-authorization-server')
console.log('  3. Add to Claude.ai with empty OAuth fields (DCR will handle it)')
console.log('')