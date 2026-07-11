Security and infra tooling, mostly Python, built for my own use. The ones
that turned out useful enough to share are public:

- **[mcpwarden](https://github.com/OneNobleSoul/mcpwarden)** - security scanner for local MCP servers: config audit, live tool inspection, lockfile pinning to catch rug pulls
- **[repolens](https://github.com/OneNobleSoul/repolens)** - audits a repo against OSS best practices, works as a CI gate (`--min-score`)
- **[hookrelay](https://github.com/OneNobleSoul/hookrelay)** - small self-hosted webhook relay, stdlib only
- **[certwatch](https://github.com/OneNobleSoul/certwatch)** - TLS expiry checks for the terminal and cron

No dependency gets in unless it earns its keep. The rest of what I build
runs at home and stays there.
