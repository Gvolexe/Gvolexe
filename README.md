<p align="center">
  <img src="assets/profile-banner.svg" alt="Gvol: hosting infrastructure, networks and automation. AS218429." width="100%">
</p>

# 💫 About Me:
🛠️ I work at [Novacloud](https://novacloud-hosting.com), [Galenius Nodes](https://www.galeniusnodes.com/) and [MellonLab](https://mellonlab.org/)<br>
🌍 I run [AS218429](https://bgp.tools/as/218429), my own network<br>
🖥️ I focus on hosting infrastructure, networks and automation<br>
🎓 I am currently studying Business Administration


## 🌐 Socials:
[![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:gvol@nexusystems.org) [![Novacloud](https://img.shields.io/badge/Novacloud-novacloud--hosting.com-89b4fa?labelColor=1e1e2e)](https://novacloud-hosting.com) [![Galenius Nodes](https://img.shields.io/badge/Galenius%20Nodes-galeniusnodes.com-cba6f7?labelColor=1e1e2e)](https://www.galeniusnodes.com/) [![MellonLab](https://img.shields.io/badge/MellonLab-mellonlab.org-a6e3a1?labelColor=1e1e2e)](https://mellonlab.org/) [![AS218429](https://img.shields.io/badge/bgp.tools-AS218429-fab387?labelColor=1e1e2e)](https://bgp.tools/as/218429)

# 💻 Tech Stack:
<p>
  <img src="assets/icons/cards/c.svg" width="88" height="100" alt="C" title="C">
  <img src="assets/icons/cards/csharp.svg" width="88" height="100" alt="C#" title="C#">
  <img src="assets/icons/cards/go.svg" width="88" height="100" alt="Go" title="Go">
  <img src="assets/icons/cards/javascript.svg" width="88" height="100" alt="JavaScript" title="JavaScript">
  <img src="assets/icons/cards/java.svg" width="88" height="100" alt="Java" title="Java">
  <img src="assets/icons/cards/rust.svg" width="88" height="100" alt="Rust" title="Rust">
  <img src="assets/icons/cards/zig.svg" width="88" height="100" alt="Zig" title="Zig">
  <img src="assets/icons/cards/php.svg" width="88" height="100" alt="PHP" title="PHP">
  <img src="assets/icons/cards/python.svg" width="88" height="100" alt="Python" title="Python">
</p>

## 🏗️ Infrastructure:
<p>
  <img src="assets/icons/cards/linux.svg" width="88" height="100" alt="Linux" title="Linux">
  <img src="assets/icons/cards/proxmox.svg" width="88" height="100" alt="Proxmox VE" title="Proxmox VE">
  <img src="assets/icons/cards/ansible.svg" width="88" height="100" alt="Ansible" title="Ansible">
  <img src="assets/icons/cards/bash.svg" width="88" height="100" alt="Shell &amp; SSH" title="Shell &amp; SSH">
  <img src="assets/icons/cards/cloudflareworkers.svg" width="88" height="100" alt="Cloudflare Workers" title="Cloudflare Workers">
  <img src="assets/icons/cards/githubactions.svg" width="88" height="100" alt="GitHub Actions" title="GitHub Actions">
</p>

🖥️ Proxmox VE clusters and VMs, provisioned with Ansible, with guest IP pools and bridged networking<br>
☁️ Cloudflare Workers host the geofeed and network website; GitHub Actions validates and deploys the geofeed

**🌍 [AS218429](https://bgp.tools/as/218429) · my network**<br>
![BGP](https://img.shields.io/badge/BGP-fab387) ![IPv4](https://img.shields.io/badge/IPv4-fab387) ![IPv6](https://img.shields.io/badge/IPv6-fab387)<br>
Backbone for Ruxora and Galenius Nodes, announced over BGP on IPv4 and IPv6

**🧭 DNS & addressing**<br>
[![Technitium DNS](https://img.shields.io/badge/Technitium-DNS-89dceb?labelColor=1e1e2e)](https://technitium.com/dns/) [![RIPE reverse DNS](https://img.shields.io/badge/RIPE-reverse%20DNS-89dceb?labelColor=1e1e2e)](https://www.ripe.net/)<br>
Authoritative and reverse zones on Technitium, with reverse DNS delegated through RIPE

**🛠️ Network & server tools**<br>
[![syncgeo](https://img.shields.io/badge/syncgeo-geofeed%20workbench-f9e2af?labelColor=1e1e2e)](https://github.com/ASN218429/scripts) [![geofeed, RFC 8805](https://img.shields.io/badge/geofeed-RFC%208805-f9e2af?labelColor=1e1e2e)](https://github.com/ASN218429/geofeed) [![RIPEstat prefix data](https://img.shields.io/badge/RIPEstat-prefix%20data-f9e2af?labelColor=1e1e2e)](https://stat.ripe.net/AS218429) [![GvolTools](https://img.shields.io/badge/GvolTools-server%20CLI-f9e2af?labelColor=1e1e2e)](https://github.com/Gvolexe/GvolTools)<br>
syncgeo pulls prefix data from RIPEstat to build the geofeed; each tool is described under [Projects](#-projects)

## 🚀 Projects:
**🌍 ASN tools**

- 🧭 **[syncgeo](https://github.com/ASN218429/scripts)** <img src="assets/icons/chips/python.svg" width="68" height="20" alt="Python" title="Python"> <img src="assets/icons/chips/githubactions.svg" width="111" height="20" alt="GitHub Actions" title="GitHub Actions"><br>Dependency-free terminal workbench: finds the prefixes RIPEstat sees, lets you assign and split their location blocks, validates them and writes RFC 8805 and JSON. Splits change locations, never BGP announcements
- 📡 **[geofeed](https://github.com/ASN218429/geofeed)** <img src="assets/icons/chips/python.svg" width="68" height="20" alt="Python" title="Python"> <img src="assets/icons/chips/cloudflareworkers.svg" width="132" height="20" alt="Cloudflare Workers" title="Cloudflare Workers"> <img src="assets/icons/chips/githubactions.svg" width="111" height="20" alt="GitHub Actions" title="GitHub Actions"><br>The public RFC 8805 geofeed and network JSON, served at [cdn.as218429.net](https://cdn.as218429.net)
- 🌐 **[website](https://github.com/ASN218429/website)** <img src="assets/icons/chips/cloudflareworkers.svg" width="132" height="20" alt="Cloudflare Workers" title="Cloudflare Workers"> <img src="assets/icons/chips/githubactions.svg" width="111" height="20" alt="GitHub Actions" title="GitHub Actions"><br>The AS218429 network website, with operator contacts and registry and geofeed links

**🧰 Server tools**

- 🔧 **[GvolTools](https://github.com/Gvolexe/GvolTools)** <img src="assets/icons/chips/python.svg" width="68" height="20" alt="Python" title="Python"><br>CLI tools for SSH-managed servers: host inventory, hardening and audits, key management, DNS/TLS checks and backups

**🎨 Side projects**

- 🌾 **[Replanish](https://github.com/Gvolexe/ReplanishEnchantment)** <img src="assets/icons/chips/kotlin.svg" width="62" height="20" alt="Kotlin" title="Kotlin"><br>Minecraft plugin and mod: harvest a mature crop with a Replanish hoe and it replants itself
- 🤖 **[RevTickCalculator](https://github.com/Gvolexe/RevTickCalculator)** <img src="assets/icons/chips/python.svg" width="68" height="20" alt="Python" title="Python"><br>Encoder tick calculator for FTC and FGC robots, written with Georgemech

# 📊 GitHub activity
![GitHub profile metrics](assets/profile-metrics.svg)

### 🏆 Achievements
<picture>
  <source media="(max-width: 600px)" srcset="assets/activity-badges-mobile.svg">
  <img src="assets/activity-badges.svg" alt="Pixel-art GitHub achievement badges showing each achievement's rank, name, count and description, from the same daily Metrics data" width="720">
</picture><br>
<sub>Refreshed daily by GitHub Actions with gh-metrics/metrics. The contribution calendar covers the past year.</sub>

### ✍️ Random Dev Quote
![Random dev quote](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical)
