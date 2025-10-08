#!/usr/bin/env tsx

import { execSync } from 'node:child_process'
import { readFileSync } from 'node:fs'

// Professional deployment tracking
const packageJson = JSON.parse(readFileSync('package.json', 'utf8'))
const gitHash = execSync('git rev-parse --short HEAD', { encoding: 'utf8' }).trim()
const timestamp = new Date().toISOString()

// Determine deployment environment (default to development)
const deployEnv = process.argv[2] || process.env.DEPLOY_ENV || 'development'

// Build version with metadata for traceability (not displayed prominently)
const buildVersion = `${packageJson.version}+${gitHash}`

console.log('Deploying MCP Server...')
console.log(`Environment: ${deployEnv}`)
console.log(`Version: ${buildVersion}`)
console.log(`Build: ${timestamp}`)
console.log('')

// Determine wrangler environment
const wranglerEnv =
    deployEnv === 'production' ? 'production' : deployEnv === 'staging' ? 'staging' : 'development'
const endpoint =
    deployEnv === 'production'
        ? `https://${packageJson.name}.your-account.workers.dev`
        : deployEnv === 'staging'
          ? `https://${packageJson.name}-staging.your-account.workers.dev`
          : `https://${packageJson.name}-dev.your-account.workers.dev`

// Deploy with stable server name from wrangler.toml
try {
    const _result = execSync(`wrangler deploy --env=${wranglerEnv}`, {
        encoding: 'utf8',
        stdio: 'inherit',
    })

    console.log('')
    console.log('Deployment successful!')
    console.log(`Endpoint: ${endpoint}`)

    // Show stable server name based on environment
    const stableServerName =
        deployEnv === 'production'
            ? packageJson.name
            : deployEnv === 'staging'
              ? `${packageJson.name}-staging`
              : `${packageJson.name}-dev`
    console.log(`MCP Server Name: ${stableServerName}`)
    console.log('')
    console.log('Use this stable name in Claude:')
    console.log(`   ${stableServerName}`)
    console.log('')
    console.log('Build tracking:')
    console.log(`   Version: ${buildVersion}`)
    console.log(`   Deployed: ${timestamp}`)
} catch (error) {
    console.error('Deployment failed:', error.message)
    process.exit(1)
}