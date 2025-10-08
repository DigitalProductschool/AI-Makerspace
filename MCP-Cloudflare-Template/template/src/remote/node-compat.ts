// node-compat.ts — Minimal Node.js req/res shims for Cloudflare Workers

type Listener = (...args: unknown[]) => void

export interface NodeReq {
    method: string
    url: string
    headers: Record<string, string>
    httpVersion: string
    httpVersionMajor: number
    httpVersionMinor: number
    complete: boolean
    readable: boolean
    socket: null
    connection: null
    on: Listener
    once: Listener
    off: Listener
    addListener: Listener
    removeListener: Listener
    emit: Listener
}

export interface NodeRes {
    statusCode: number
    statusMessage: string
    headersSent: boolean
    finished: boolean
    writable: boolean
    writableEnded: boolean
    socket: null
    connection: null
    setHeader: (name: string, value: string | string[]) => void
    getHeader: (name: string) => string | undefined
    removeHeader: (name: string) => void
    writeHead: (
        code: number,
        msgOrHeaders?: string | Record<string, string>,
        headersMaybe?: Record<string, string>,
    ) => NodeRes
    write: (chunk?: string | Uint8Array) => boolean
    end: (chunk?: string | Uint8Array) => NodeRes
    flushHeaders: () => void
    setTimeout: (ms?: number, cb?: () => void) => NodeRes
    on: (...args: unknown[]) => NodeRes
    once: (...args: unknown[]) => NodeRes
    emit: (...args: unknown[]) => boolean
    removeListener: (...args: unknown[]) => NodeRes
    addListener: (...args: unknown[]) => NodeRes
}

export function createNodeMocks(request: Request) {
    const url = new URL(request.url)
    const headers: Record<string, string> = {}
    request.headers.forEach((value, key) => {
        headers[key.toLowerCase()] = value
    })

    const req: NodeReq = {
        method: request.method,
        url: url.pathname + url.search,
        headers,
        httpVersion: '1.1',
        httpVersionMajor: 1,
        httpVersionMinor: 1,
        complete: true,
        readable: false,
        socket: null,
        connection: null,
        // No-op event methods (SDK won't rely on streaming from req in this code path)
        on() {},
        once() {},
        off() {},
        addListener() {},
        removeListener() {},
        emit() {},
    }

    let _statusCode = 200
    let _statusMessage = 'OK'
    let _headersSent = false
    const headerMap = new Map<string, string>()
    const chunks: Uint8Array[] = []

    const enc = new TextEncoder()

    const res: NodeRes = {
        get statusCode() {
            return _statusCode
        },
        set statusCode(v: number) {
            _statusCode = v
        },
        get statusMessage() {
            return _statusMessage
        },
        set statusMessage(v: string) {
            _statusMessage = v
        },
        get headersSent() {
            return _headersSent
        },
        set headersSent(_v: boolean) {
            _headersSent = _v
        },
        finished: false,
        writable: true,
        writableEnded: false,
        socket: null,
        connection: null,

        setHeader(name, value) {
            headerMap.set(String(name), Array.isArray(value) ? value.join(', ') : String(value))
        },
        getHeader(name) {
            return headerMap.get(String(name))
        },
        removeHeader(name) {
            headerMap.delete(String(name))
        },

        writeHead(code, msgOrHeaders?, headersMaybe?) {
            _statusCode = code
            const headersArg = typeof msgOrHeaders === 'object' ? msgOrHeaders : headersMaybe
            if (typeof msgOrHeaders === 'string') _statusMessage = msgOrHeaders
            if (headersArg) {
                for (const [k, v] of Object.entries(headersArg)) {
                    res.setHeader(k, String(v))
                }
            }
            _headersSent = true
            return res
        },

        write(chunk) {
            if (chunk == null) return true
            chunks.push(typeof chunk === 'string' ? enc.encode(chunk) : chunk)
            return true
        },

        end(chunk?) {
            if (chunk) res.write(chunk)
            res.finished = true
            res.writable = false
            res.writableEnded = true
            resolveDone() // signal "response ready"
            return res
        },

        flushHeaders() {
            _headersSent = true
        },

        setTimeout() {
            return res
        },

        // Event emitter methods
        on() {
            return res
        },
        once() {
            return res
        },
        emit() {
            return true
        },
        removeListener() {
            return res
        },
        addListener() {
            return res
        },
    }

    let resolveDone!: () => void
    const done = new Promise<void>((resolve) => {
        resolveDone = resolve
    })

    async function toResponse(): Promise<Response> {
        await done // wait for res.end()
        const body = chunks.length ? new Blob(chunks as any[]) : null
        const h = new Headers()
        for (const [k, v] of headerMap) h.set(k, v)
        return new Response(body, { status: _statusCode, statusText: _statusMessage, headers: h })
    }

    return { req, res, toResponse }
}