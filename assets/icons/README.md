# Profile icons

Technology logos come from [Devicon](https://github.com/devicons/devicon), release
[v2.18.0](https://github.com/devicons/devicon/releases/tag/v2.18.0), commit
`ff435a0fff0391aefbf70d63a3fe7cfe64f82df0`. Each file was downloaded from
`https://raw.githubusercontent.com/devicons/devicon/ff435a0fff0391aefbf70d63a3fe7cfe64f82df0/icons/<name>/<file>`
and the variants were checked against `devicon.json` at the same commit.

- `devicon/`: unmodified upstream SVGs, plus Devicon's MIT `LICENSE`.
- `cards/` (Tech Stack and Infrastructure) and `chips/` (project lines): local wrappers
  that embed the upstream SVG markup unchanged on a Catppuccin tile and add a text label.
  The Proxmox card crops the view of `proxmox-original-wordmark.svg` to its X symbol.
  The source file itself is untouched.

| Name | Devicon file | Used in |
| --- | --- | --- |
| C | `c/c-original.svg` | card |
| C# | `csharp/csharp-original.svg` | card |
| Go | `go/go-original.svg` | card |
| JavaScript | `javascript/javascript-original.svg` | card |
| Java | `java/java-original.svg` | card |
| Rust | `rust/rust-original.svg` | card |
| Zig | `zig/zig-original.svg` | card |
| PHP | `php/php-original.svg` | card, chip |
| Python | `python/python-original.svg` | card, chip |
| Kotlin | `kotlin/kotlin-original.svg` | chip |
| Linux | `linux/linux-original.svg` | card |
| Proxmox VE | `proxmox/proxmox-original-wordmark.svg` | card |
| Ansible | `ansible/ansible-original.svg` | card |
| Shell & SSH | `bash/bash-original.svg` | card |
| Cloudflare Workers | `cloudflareworkers/cloudflareworkers-original.svg` | card, chip |
| GitHub Actions | `githubactions/githubactions-original.svg` | card, chip |

Devicon's MIT license covers the icon files. The logos remain trademarks of their
owners and appear here only to name the technology.

Devicon has no icons for Technitium, Pterodactyl, Pelican, Convoy, Paymenter or WHMCS,
so the README keeps their shields.io badges.
