<div align="center">

[![](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1400&color=4ADECD&center=true&vCenter=true&width=680&height=40&lines=security+%26+infrastructure+tooling%2C+mostly+python.;building+an+agent+that+runs+the+whole+loop.;most+of+what+i+make+runs+at+home+and+stays+there.;the+long+game+is+autonomy.)](https://github.com/OneNobleSoul)

<br>

`security tooling` · `infrastructure` · `autonomous agents` · `python`

</div>

<br>

## ▚ about

I build security and infrastructure tooling, mostly in Python, and I'm
developing an autonomous agent to run the parts I'd rather not do by hand.
A few of the tools turned out useful enough to open up — they're below.
The agent is the long game, and it's getting close.

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

## ▚ J.A.R.V.I.S. (Inspired by a well-known superhero xD) — autonomous agent  `[ in development ]`

The long game: a self-hosted agent that runs the whole loop on its own
metal — scouts the target, writes and ships the code, researches what it
doesn't know, and rewrites its own internals when it finds a better way.
One operator, everything else delegated. It's close.

```
              _.-""""""-._
            .'  _.----._  '.       scout    ·  recon, triage, target mapping
           /   /        \   \      code     ·  build, patch, test, ship, redeploy
          |   |   .--.   |   |     research ·  reads the field, closes its own gaps
          |   |  ( () )  |   |     evolve   ·  rewrites & retrains its own core
          |   |   '--'   |   |     memory   ·  persistent recall across sessions
           \   \        /   /      swarm    ·  spawns sub-agents, delegates, reviews
            '.  '-.__.-'  .'       voice    ·  wake-word, realtime speech in and out
              '-._____.-'          watch    ·  proactive — acts before it's asked
```

```
  .-- J.A.R.V.I.S. // CORE SPEC ---------------------------------.
  | build ......... v0.9   ·   92%   [##################··]      |
  | architecture .. mixture-of-experts  ·  self-modifying core   |
  | params ........ 240B total / 22B active per token            |
  | context ....... 512K tokens  +  persistent long-term memory  |
  | senses ........ text · vision · voice (realtime STT/TTS)     |
  | runtime ....... own metal · offline-capable · sandboxed      |
  | interface ..... MCP-native · 40+ live tools · auto-skills    |
  '--------------------------------------------------------------'
```

Almost there, and already useful. Even before it's finished it closes tasks
end to end, lands flags in **CTFs**, and reports valid findings through
**bug-bounty** programs. Most of what it does never surfaces — private
tooling and work that stays on my own metal.

<!-- JARVIS:START -->
```
  .-- J.A.R.V.I.S. // TELEMETRY ---------------------------------------.
  | core .................... stable  mode ................ autonomous |
  | uptime .................... 322d  load ................... nominal |
  | scope ....... scout / code / r&d  self ................. improving |
  | directive ..... "shipping the parts you'd rather not do by hand."  |
  | last self-sync  2026-07-20 08:17 UTC                               |
  '--------------------------------------------------------------------'
```
<!-- JARVIS:END -->

<sub>the panel above is regenerated on its own — see <a href="gadget/telemetry.py">gadget/telemetry.py</a></sub>

<br>

---

<div align="center">
<sub>built and run in-house · most of it stays there</sub>
</div>
