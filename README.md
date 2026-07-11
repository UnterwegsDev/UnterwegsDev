<div align="center">

<br>

```
        ▄▄▄▄▄▄▄▄▄
      ▄█░░░░░░░░░█▄
     █░░░▄▄░░░▄▄░░░█        no name. no face. no pattern.
     █░░░▀▀░░░▀▀░░░█        only output.
      ▀█░░░░▄░░░░░█▀
        ▀▀█░░░█▀▀
           ▀▀▀
```

[![](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&pause=1400&color=4ADECD&center=true&vCenter=true&width=680&height=40&lines=access+is+a+privilege%2C+not+a+right.;i+read+the+source+before+i+trust+the+badge.;the+quiet+ones+ship+the+exploits.;if+you+can+profile+me+from+this%2C+i+failed.)](https://github.com/OneNobleSoul)

<br>

`security research` · `offensive tooling` · `self-hosted systems` · `autonomous agents`

</div>

<br>

## ▚ whoami

A red-teamer's job is to think like the adversary and leave nothing behind.
So this profile does the same: no stats, no streaks, no activity graph on
display, no follower count, no location. If you can build a profile of me
from this page, then I have already lost.

The public repositories below are the parts I chose to surface. The rest
stays where it belongs.

<br>

## ▚ surfaced

Small, sharp tools. Dependency-light, tested, no loose ends.

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

## ▚ J.A.R.V.I.S. — autonomous agent  `[ in development ]`

The long game. A self-hosted agent meant to run the whole loop on its own
metal: **scout** the target, **write** and ship the code, **research** what
it doesn't know, and **rewrite its own internals** when it finds a better
way. One operator, everything else delegated.

```
              _.-""""""-._
            .'  _.----._  '.
           /   /        \   \
          |   |   .--.   |   |          scout    ·  recon, triage, mapping
          |   |  ( () )  |   |          code     ·  build, patch, ship, test
          |   |   '--'   |   |          research ·  read the field, close gaps
           \   \        /   /           evolve   ·  improve its own model + code
            '.  '-.__.-'  .'
              '-._____.-'                one operator. everything delegated.
```

Not vaporware. Even mid-build it already carries real weight — closing
tasks end to end, landing flags in **CTFs**, and reporting valid findings
through **bug-bounty** programs. Most of what it does never surfaces:
private tooling and development that stays on my own metal.

<!-- JARVIS:START -->
```
  .-- J.A.R.V.I.S. // TELEMETRY ---------------------------------------.
  | core .................... stable  mode ................ autonomous |
  | uptime .................... 313d  load ................... nominal |
  | scope ....... scout / code / r&d  self ................. improving |
  | directive ..... "read the source before you trust the badge."      |
  | last self-sync  2026-07-11 11:26 UTC                               |
  '--------------------------------------------------------------------'
```
<!-- JARVIS:END -->

<sub>the panel above is regenerated on its own — see <a href="gadget/telemetry.py">gadget/telemetry.py</a></sub>

<br>

## ▚ below the waterline

Most of what I build never surfaces. It runs on my own metal, answers to no
cloud, and keeps its own counsel.

<br>

## ▚ doctrine

```
› assume compromise. verify everything. trust nothing you did not read.
› boring technology, quiet results.
› every dependency is a liability with a changelog.
› if it isn't auditable, it isn't finished.
› leave no pattern.
```

<br>

---

<div align="center">
<sub>no socials · no newsletter · no forwarding address</sub>
</div>
