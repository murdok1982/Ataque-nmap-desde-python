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
