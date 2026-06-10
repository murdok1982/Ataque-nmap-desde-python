# 🔍 Ataque-nmap-desde-python

Scripts Python para automatizar escaneos **Nmap** con perfiles predefinidos y salida estructurada.

⚠️ **Uso exclusivo en entornos autorizados, redes propias o laboratorios de pentesting.**

## Instalación

```bash
pip install -r requirements.txt
# Nmap debe estar instalado en el sistema:
# Linux:   apt install nmap
# Windows: choco install nmap
```

## Uso

```bash
# Escaneo básico
python NmapPython/nmap_scanner.py 192.168.1.1

# Escaneo de vulnerabilidades
python NmapPython/nmap_scanner.py 192.168.1.1 -t vuln

# Descubrimiento de rango CIDR
python NmapPython/nmap_scanner.py 192.168.1.0/24 --range

# Salida JSON
python NmapPython/nmap_scanner.py 192.168.1.1 --json

# Guardar en archivo
python NmapPython/nmap_scanner.py 192.168.1.1 -o resultado.txt
```

## Perfiles de escaneo

| Perfil | Flags | Uso |
|--------|-------|-----|
| `basic` | `-sV -sC -T4` | Escaneo estándar con scripts |
| `stealth` | `-sS -T2 -f` | Escaneo silencioso fragmentado |
| `udp` | `-sU --top-ports 100` | Puertos UDP principales |
| `vuln` | `-sV --script=vuln` | Detección de vulnerabilidades |
| `full` | `-sV -sC -p-` | Todos los puertos (lento) |
| `ping` | `-sn` | Solo descubrimiento de hosts |

## Autor

**MuRDoK** — [github.com/murdok1982](https://github.com/murdok1982)

---

## 💰 Apoya Este Proyecto

<div align="center">

### ¡Donaciones en Bitcoin Bienvenidas!

[![Bitcoin](https://img.shields.io/badge/Bitcoin-000000?style=for-the-badge&logo=bitcoin&logoColor=white)](https://bitcoin.org)

```
┌──────────────────────────────────────────────────┐
│             ₿ BTC Donation Address ₿              │
├──────────────────────────────────────────────────┤
│                                                  │
│  bc1qqphwht25vjzlptwzjyjt3sex7e3p8twn390fkw     │
│                                                  │
│  Network: Bitcoin (BTC)                          │
│                                                  │
│  Escanea el QR desde tu wallet:                  │
└──────────────────────────────────────────────────┘
```

![Bitcoin QR](https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=bitcoin:bc1qqphwht25vjzlptwzjyjt3sex7e3p8twn390fkw)

**Direccion:** `bc1qqphwht25vjzlptwzjyjt3sex7e3p8twn390fkw`

*Apoya el desarrollo de herramientas de ciberseguridad open-source!* 🙏

</div>

---

## Support / Apoya este proyecto

I build open-source projects focused on applied AI, automation, and data intelligence.
Over on my GitHub you'll find things like AI-powered analysis engines, OSINT platforms for open-source research, Windows automation tools, and experiments with language models.
Everything is public and free, so anyone can use it, study it, or build on top of it. github.com/murdok1982

Keeping these projects alive takes a lot of hours. If any of them have helped you out or you just like what I'm doing, you can support me with a coffee: ko-fi.com/murdok1982

Every contribution goes straight back into shipping more open-source code.
