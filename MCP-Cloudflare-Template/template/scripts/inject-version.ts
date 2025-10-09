#!/usr/bin/env tsx

import { readFileSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'

// Read package.json version
const packageJson = JSON.parse(readFileSync('package.json', 'utf8'))
const version = packageJson.version

// Read registry.ts file
const registryPath = join('src', 'core', 'registry.ts')
let content = readFileSync(registryPath, 'utf8')

// Replace __VERSION__ placeholder with actual version
content = content.replace('__VERSION__', version)

// Write back to file
writeFileSync(registryPath, content)

console.log(`Version injected: ${version}`)