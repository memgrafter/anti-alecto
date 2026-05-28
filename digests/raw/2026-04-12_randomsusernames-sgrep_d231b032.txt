<p align="center">
  <h1 align="center">sgrep</h1>
  <p align="center">
    <strong>Semantic grep for the AI era</strong><br>
    Natural language code search powered by Rust
  </p>
</p>

<p align="center">
  <a href="https://crates.io/crates/searchgrep"><img src="https://img.shields.io/crates/v/searchgrep.svg" alt="Crates.io"></a>
  <a href="https://github.com/RandomsUsernames/sgrep/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://github.com/RandomsUsernames/sgrep/releases"><img src="https://img.shields.io/github/v/release/RandomsUsernames/sgrep" alt="GitHub release"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/rust-%23000000.svg?style=flat&logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/MCP-Compatible-green" alt="MCP Compatible">
  <img src="https://img.shields.io/badge/Apple%20Silicon-Optimized-black" alt="Apple Silicon">
</p>

---

Search your codebase using natural language. Ask questions like *"where are authentication errors handled"* or *"database connection pooling logic"* and get instant results.

```bash
# Install
brew install RandomsUsernames/sgrep/sgrep

# Index & Search
sgrep index .
sgrep search "error handling for API requests"
```

## Why sgrep?

| Traditional grep | sgrep |
|-----------------|------------|
| `grep -r "error"` finds literal matches | Finds code by *meaning* |
| Requires knowing exact terms | Use natural language |
| Misses synonyms and related code | Understands context |
| No AI integration | Works with Claude, Cursor, etc. |

## Installation

### Homebrew (macOS)

```bash
brew tap RandomsUsernames/sgrep
brew install sgrep
```

### Cargo (crates.io)

```bash
cargo install searchgrep
```

### From Source

```bash
git clone https://github.com/RandomsUsernames/sgrep.git
cd sgrep
cargo install --path .
```

## Quick Start

```bash
# 1. Index your codebase
sgrep index .

# 2. Search with natural language
sgrep search "authentication middleware"

# 3. Get AI-powered answers
sgrep ask "how does the login flow work"

# 4. View codebase structure
sgrep map
```

## Features

### Semantic Search
Find code by meaning, not just keywords. The query *"handle user login"* will find authentication code even if it doesn't contain those exact words.

```bash
sgrep search "database connection pooling"
sgrep search "where are errors logged" --content
```

### AI Answers
Get synthesized answers about your codebase using GPT.

```bash
sgrep ask "explain the authentication flow"
sgrep ask "what testing framework is used"
```

### Codebase Map
Get a structural overview of your code - functions, classes, and their relationships.

```bash
sgrep map              # Full codebase map
sgrep map src/         # Specific directory
```

### MCP Server
Integrates directly with Claude Code, Cursor, and other MCP-compatible tools.

```bash
sgrep setup   # Interactive setup for AI tools
```

### Multiple Search Modes

| Mode | Flag | Best For |
|------|------|----------|
| Balanced | *(default)* | General search |
| Code | `--code` | Code-specific queries |
| Hybrid | `--hybrid` | Best quality (slower) |

## AI Tool Integration

### Claude Code / Cursor / Continue

```bash
sgrep setup  # Interactive MCP setup
```

Or manually add to your MCP config:

```json
{
  "mcpServers": {
    "sgrep": {
      "command": "sgrep",
      "args": ["mcp-server"]
    }
  }
}
```

### Skills (Claude, Gemini CLI, OpenCode)

```bash
sgrep skill         # Interactive setup
sgrep skill claude  # Claude only
sgrep skill all     # All tools
```

## Commands

| Command | Description |
|---------|-------------|
| `sgrep index <path>` | Index a directory |
| `sgrep search <query>` | Semantic search |
| `sgrep ask <question>` | AI-powered Q&A |
| `sgrep map [path]` | Codebase structure map |
| `sgrep setup` | Configure MCP for AI tools |
| `sgrep skill [tool]` | Install as skill |
| `sgrep status` | Show index status |
| `sgrep config` | Configure settings |

### Search Options

```bash
sgrep search "query" [options]

  -m, --max-results <n>   Max results (default: 10)
  -c, --content           Show code snippets
  -a, --answer            Generate AI answer
  --code                  Code-optimized model
  --hybrid                Best quality (BGE + CodeRankEmbed)
```

## How It Works

1. **Index** - Files are chunked and converted to vector embeddings locally using BGE or CodeRankEmbed
2. **Store** - Embeddings cached in `~/.sgrep/`
3. **Search** - Your query is embedded and compared using cosine similarity
4. **Rank** - Results sorted by semantic relevance
5. **Answer** - Optionally, top results sent to GPT for synthesis

## Performance

- **Apple Silicon** - Uses Accelerate framework for fast inference
- **Local Models** - No API calls needed for search
- **Indexing** - ~100 files/minute
- **Search** - ~2s (single model), ~3.5s (hybrid)

## Configuration

```bash
sgrep config --api-key sk-...   # Set OpenAI key (for answers)
sgrep config --show             # Show config
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | For `--answer` and `ask` commands |
| `OPENAI_BASE_URL` | Custom API endpoint |

### Ignore Files

sgrep respects `.gitignore` and `.sgrepignore`.

## Examples

```bash
# Find auth code
sgrep search "user authentication and sessions"

# With code preview
sgrep search "database queries" --content

# Best quality search
sgrep search --hybrid "vector embeddings"

# Architecture overview
sgrep ask "what's the project architecture"

# View structure
sgrep map src/
```

## Contributing

Contributions welcome! Please open an issue or PR.

## License

[MIT](LICENSE)

## Troubleshooting

### MCP "Transport closed" or "Client is not connected" Errors

Some MCP clients (Codex CLI, Gemini CLI) have stdio transport issues with direct Rust binaries. Use the included Node.js wrapper:

**Codex CLI** (`~/.codex/config.toml`):
```toml
[mcp_servers.searchgrep]
command = "node"
args = ["/path/to/scripts/mcp-wrapper.js"]
startup_timeout_sec = 60
```

**Gemini CLI** (`~/.gemini/settings.json`):
```json
{
  "mcpServers": {
    "searchgrep": {
      "command": "node",
      "args": ["/path/to/scripts/mcp-wrapper.js"]
    }
  }
}
```

You can also copy the wrapper to a convenient location:
```bash
cp scripts/mcp-wrapper.js ~/.local/bin/
# Then use: node ~/.local/bin/mcp-wrapper.js
```

### MCP Server Timeout

For slow-starting servers, increase the timeout in your client config:

**Codex**: Add `startup_timeout_sec = 60` to the server config  
**Claude Code**: Timeouts are usually sufficient by default
