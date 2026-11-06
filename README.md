<p align="center">
  <img src="assets/profile-banner.svg" alt="Gvol: hosting infrastructure, networks and automation. AS218429." width="100%">
</p>

# 💫 About Me:
🛠️ I work at [Novacloud](https://novacloud-hosting.com), [Galenius Nodes](https://www.galeniusnodes.com/) and [MellonLab](https://mellonlab.org/)<br>
🌍 I run [AS218429](https://bgp.tools/as/218429): BGP over IPv4 and IPv6, RIPE reverse DNS and Technitium zones. It is the backbone behind Ruxora and Galenius Nodes<br>
🗺️ I build the AS218429 tools: [syncgeo](https://github.com/ASN218429/scripts), the [geofeed](https://github.com/ASN218429/geofeed) and the [network website](https://github.com/ASN218429/website)<br>
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

![BGP AS218429](https://img.shields.io/badge/BGP-AS218429-fab387?style=for-the-badge&labelColor=1e1e2e) ![IPv4 and IPv6](https://img.shields.io/badge/IPv4%20%2B%20IPv6-94e2d5?style=for-the-badge) ![RIPE reverse DNS](https://img.shields.io/badge/RIPE-reverse%20DNS-89dceb?style=for-the-badge&labelColor=1e1e2e) ![Technitium DNS](https://img.shields.io/badge/Technitium-DNS-89b4fa?style=for-the-badge&labelColor=1e1e2e) ![Pterodactyl](https://img.shields.io/badge/Pterodactyl-10539F?style=for-the-badge&logo=pterodactyl&logoColor=white) ![Pelican](https://img.shields.io/badge/Pelican-panel-74c7ec?style=for-the-badge&labelColor=1e1e2e) ![Convoy](https://img.shields.io/badge/Convoy-panel-b4befe?style=for-the-badge&labelColor=1e1e2e) ![Paymenter](https://img.shields.io/badge/Paymenter-billing-cba6f7?style=for-the-badge&labelColor=1e1e2e) ![WHMCS](https://img.shields.io/badge/WHMCS-billing-f5c2e7?style=for-the-badge&labelColor=1e1e2e) ![RIPEstat](https://img.shields.io/badge/RIPEstat-prefixes-74c7ec?style=for-the-badge&labelColor=1e1e2e) ![RFC 8805 geofeed](https://img.shields.io/badge/RFC%208805-geofeed-f9e2af?style=for-the-badge&labelColor=1e1e2e)

- 🖥️ **Proxmox VE** clusters and VMs, provisioned with Ansible, with guest IP pools and bridged networking
- 🌍 **AS218429**: IPv4 and IPv6 announcements, RIPE reverse DNS delegations, Technitium authoritative and reverse zones
- 🗺️ **Geofeed and network metadata**: RFC 8805 geofeed and JSON prefix metadata for the prefixes RIPEstat sees announced, managed with syncgeo and deployed to a Cloudflare Worker by GitHub Actions
- 💳 **Panels and billing**: Paymenter, Pelican, Convoy, Pterodactyl/Calagopus and WHMCS integrations
- 🐧 **Linux over SSH**: host inventory, auditing, DNS/TLS checks and backups with GvolTools

## 🚀 Projects:
**🌍 ASN tools**

- 🧭 **[syncgeo](https://github.com/ASN218429/scripts)** <img src="assets/icons/chips/python.svg" width="68" height="20" alt="Python" title="Python"> <img src="assets/icons/chips/githubactions.svg" width="111" height="20" alt="GitHub Actions" title="GitHub Actions"><br>Dependency-free terminal workbench for the AS218429 geofeed: finds the announced prefixes visible in RIPEstat, splits them into location blocks you assign explicitly, validates countries, regions and coverage, then writes the RFC 8805 feed with dry runs and atomic saves. Splitting never changes BGP announcements
- 📡 **[geofeed](https://github.com/ASN218429/geofeed)** <img src="assets/icons/chips/python.svg" width="68" height="20" alt="Python" title="Python"> <img src="assets/icons/chips/cloudflareworkers.svg" width="132" height="20" alt="Cloudflare Workers" title="Cloudflare Workers"> <img src="assets/icons/chips/githubactions.svg" width="111" height="20" alt="GitHub Actions" title="GitHub Actions"><br>RFC 8805 CSV and JSON network and prefix metadata, served from a Cloudflare Worker at [cdn.as218429.net](https://cdn.as218429.net) after GitHub Actions validation
- 🌐 **[website](https://github.com/ASN218429/website)** <img src="assets/icons/chips/cloudflareworkers.svg" width="132" height="20" alt="Cloudflare Workers" title="Cloudflare Workers"> <img src="assets/icons/chips/githubactions.svg" width="111" height="20" alt="GitHub Actions" title="GitHub Actions"><br>The AS218429 network website on Cloudflare Workers, with operator contacts and registry and geofeed links

**🧰 Hosting tools**

- 🔧 **[GvolTools](https://github.com/Gvolexe/GvolTools)** <img src="assets/icons/chips/python.svg" width="68" height="20" alt="Python" title="Python"><br>CLI toolkit for SSH-managed servers: host hardening, SSH auditing, key management, DNS checks and host inventory
- 🦅 **[Pelican × Paymenter](https://github.com/Gvolexe/PelicanExtentionPaymenter)** <img src="assets/icons/chips/php.svg" width="54" height="20" alt="PHP" title="PHP"><br>Paymenter extension that creates, suspends, upgrades and terminates Pelican servers, with node tags and port ranges
- 🪙 **[NowPayments](https://github.com/Gvolexe/NowPayments)** <img src="assets/icons/chips/php.svg" width="54" height="20" alt="PHP" title="PHP"><br>Crypto checkout gateway for Paymenter with HMAC-signed IPN callbacks and invoice status updates

**🎨 Side projects**

- 🌾 **[Replanish](https://github.com/Gvolexe/ReplanishEnchantment)** <img src="assets/icons/chips/kotlin.svg" width="62" height="20" alt="Kotlin" title="Kotlin"><br>Minecraft plugin and mod: harvest a mature crop with a Replanish hoe and it replants itself
- 🤖 **[RevTickCalculator](https://github.com/Gvolexe/RevTickCalculator)** <img src="assets/icons/chips/python.svg" width="68" height="20" alt="Python" title="Python"><br>Encoder tick calculator for FTC and FGC robots, written with Georgemech

# 📊 GitHub Stats:
![Gvol's GitHub stats](https://github-readme-stats.shion.dev/api?username=Gvolexe&theme=catppuccin_mocha&hide_border=false&count_private=true) ![Most used languages](https://github-readme-stats.shion.dev/api/top-langs/?username=Gvolexe&theme=catppuccin_mocha&hide_border=false&include_all_commits=true&count_private=true&layout=compact)<br/>
![GitHub streak](https://streak-stats.demolab.com/?user=Gvolexe&theme=catppuccin_mocha&hide_border=false)

## 🏆 GitHub Trophies
![GitHub trophies](https://trophygithubreadmelang.cybee.dpdns.org/?username=Gvolexe&theme=radical&no-frame=false&no-bg=false&margin-w=4)

### ✍️ Random Dev Quote
![Random dev quote](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical)

### 🔝 Contribution Stats
![Contribution stats](assets/contribution-stats.svg)
