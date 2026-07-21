<div align="center">

[![](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1400&color=4ADECD&center=true&vCenter=true&width=680&height=40&lines=security+%26+infrastructure+tooling%2C+mostly+python.;a+private+messenger+on+a+real+mix+network.;post-quantum+crypto%2C+zero-knowledge+servers.;most+of+what+i+make+runs+at+home+and+stays+there.)](https://github.com/OneNobleSoul)

<br>

`security tooling` · `mix networks` · `post-quantum crypto` · `python`

</div>

<br>

## ▚ about

I build security and infrastructure tooling, mostly in Python. My main
project right now is **NobleChat** — a private messenger that runs over a
real mix network with hybrid post-quantum encryption. A few smaller tools
turned out useful enough to open up; they're below. Most of what I make
runs at home and stays there.

<br>

## ▚ noblechat  ·  flagship

> Private messaging over a real mix network with hybrid post-quantum
> encryption. End-to-end encrypted in the browser — the server never sees
> content and can't tell a real message from cover traffic.

```
  .-- NobleChat // SPEC ------------------------------------------.
  | transport ..... Sphinx mix network  ·  or the public Nym net  |
  | crypto ........ X25519 + ML-KEM-768  ·  Ed25519 + ML-DSA-65   |
  | server ........ zero-knowledge  ·  opaque onion packets only  |
  | delivery ...... accounts · multi-device · offline · at-rest   |
  | chat .......... 1:1 & groups · files · calls · reactions      |
  | clients ....... PWA · desktop · android  ·  self-hostable     |
  | license ....... AGPL-3.0                                      |
  '--------------------------------------------------------------'
```

A layered mix network moves every message as a constant-size onion packet
with Poisson mixing and cover traffic — each node only ever learns its own
hop. Keys are generated on your device and never leave it. Voice and video
calls run over WebRTC, signalled end to end.

→ **[github.com/OneNobleSoul/noblechat](https://github.com/OneNobleSoul/noblechat)** &nbsp;·&nbsp; working project · no independent audit yet

<br>

## ▚ open tools

Small, focused tools. Dependency-light, tested, no loose ends.

```
  ┌─[ mcpwarden ]─· security · python · cli

     auditor for local MCP servers. static config scan, live tool
     inspection over a minimal stdio client, and a lockfile model
     that flags rug-pulls when a server's tools shift under you.
  ╵

  ┌─[ repolens ]─· hygiene · python · zero-dep

     audits any repository against open-source hygiene and scores
     it 0-100. gates itself in CI on every push with --min-score.
  ╵

  ┌─[ hookrelay ]─· plumbing · python · stdlib-only

     tiny self-hosted webhook relay. match, verify the HMAC,
     template, fan out to slack / discord / ntfy / anywhere.
  ╵

  ┌─[ certwatch ]─· monitoring · python · zero-dep

     TLS expiry monitor for the terminal. worst-first, exits
     non-zero for cron, no dependencies to rot.
  ╵
```

<br>

---

<div align="center">
<sub>built and run in-house · most of it stays there</sub>
</div>
