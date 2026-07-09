<div align="center">

# Unterwegs

**Security-minded software engineer — Python, automation & self-hosted AI.**

*Always on the move. Rarely seen. Usually building.*

<br>

![Python](https://img.shields.io/badge/Python-1a1a1a?style=for-the-badge&logo=python&logoColor=3776AB)
![TypeScript](https://img.shields.io/badge/TypeScript-1a1a1a?style=for-the-badge&logo=typescript&logoColor=3178C6)
![FastAPI](https://img.shields.io/badge/FastAPI-1a1a1a?style=for-the-badge&logo=fastapi&logoColor=009688)
![Docker](https://img.shields.io/badge/Docker-1a1a1a?style=for-the-badge&logo=docker&logoColor=2496ED)
![Linux](https://img.shields.io/badge/Linux-1a1a1a?style=for-the-badge&logo=linux&logoColor=FCC624)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-1a1a1a?style=for-the-badge&logo=githubactions&logoColor=2088FF)

</div>

<br>

## What I do

- 🔐 **Security first.** I build tools that assume the worst — and verify it. If it isn't auditable, it isn't finished.
- 🤖 **Self-hosted AI.** Persistent, tool-using agents with long-term memory, scheduling and skills — running on my own metal, not someone else's cloud.
- 🧰 **Small, sharp tools.** Dependency-free CLIs, honest error messages, tests that actually test. A linter should pass its own lint.
- 🕶️ **Privacy by default.** Most of my work lives in private repositories. The interesting parts tend to surface eventually.

## Open tools

Utilities I built for my own workflow years ago and never stopped using. I've
rewritten each one from scratch — proper tests, CI, no loose ends — and opened
them up in case they save someone else the same afternoon.

| Project | Status | About |
|---|---|---|
| **repolens** | 🟢 Public | A dependency-free Python CLI that audits any repository against open-source best practices — and audits itself in CI on every push. |
| **hookrelay** | 🟢 Public | A tiny self-hosted webhook relay. Match inbound hooks, verify the HMAC, template a message and fan it out to Slack, Discord, ntfy or any URL. Stdlib-only. Grew out of the glue I ran to route my own alerts. |
| **certwatch** | 🟢 Public | TLS certificate expiry monitor for the terminal. Watches a list of hosts, sorts worst-first, exits non-zero for cron. Started life as a one-line script I leaned on for years. |
| **mcpwarden** | 🟢 Public | A security auditor for local MCP servers. Static config scan, live tool inspection over a minimal stdio client, and a lockfile model that flags rug-pulls when a server's tools change under you. |

## Currently below the waterline

| Project | Status | About |
|---|---|---|
| **A rather intelligent system** | 🟠 Testing | Self-hosted agent platform: FastAPI core, persistent memory, background learning, self-updating. It wrote parts of its own deploy pipeline. |
| **VaultComm** | 🟠 Testing | A secure, anonymous, European-built communication platform. |

## Principles

> Build it like you'll be the one who has to break it.

- Boring technology, exciting results.
- Every dependency is a liability with a changelog.
- Automate the second time, not the tenth.

---

<div align="center">
<sub>No socials. No newsletter. If it matters, it ships.</sub>
</div>
