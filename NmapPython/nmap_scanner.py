#!/usr/bin/env python3
"""
Ataque-nmap-desde-python — Automatización de escaneos Nmap con Python
Autor: MuRDoK | github.com/murdok1982
⚠️  Uso exclusivo en entornos autorizados y laboratorios propios.
"""
import subprocess
import sys
import json
import argparse
from datetime import datetime

SCAN_PROFILES = {
    "basic":   ["-sV", "-sC", "-T4"],
    "stealth": ["-sS", "-T2", "-f"],
    "udp":     ["-sU", "-T4", "--top-ports", "100"],
    "vuln":    ["-sV", "--script=vuln", "-T4"],
    "full":    ["-sV", "-sC", "-p-", "-T4"],
    "ping":    ["-sn"],
}


def run_nmap(target: str, scan_type: str = "basic", output_file: str = None) -> dict:
    """Ejecuta nmap contra el objetivo y devuelve los resultados."""
    flags = SCAN_PROFILES.get(scan_type, SCAN_PROFILES["basic"])
    cmd = ["nmap"] + flags + [target]
    if output_file:
        cmd += ["-oN", output_file]

    print(f"[*] Ejecutando: {' '.join(cmd)}")
    print(f"[*] Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        return {
            "target": target,
            "scan_type": scan_type,
            "command": " ".join(cmd),
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "timestamp": datetime.now().isoformat(),
        }
    except FileNotFoundError:
        print("[-] ERROR: nmap no instalado.")
        print("    Linux:   apt install nmap")
        print("    Windows: choco install nmap")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("[-] ERROR: Timeout excedido (300s)")
        sys.exit(1)


def scan_range(cidr: str) -> list:
    """Descubre hosts activos en un rango CIDR."""
    result = run_nmap(cidr, "ping")
    hosts = [
        line.split()[-1].strip("()")
        for line in result["stdout"].splitlines()
        if "Nmap scan report for" in line
    ]
    print(f"[+] Hosts activos encontrados: {len(hosts)}")
    return hosts


def main():
    parser = argparse.ArgumentParser(
        description="Automatización de escaneos Nmap — solo uso autorizado"
    )
    parser.add_argument("target", help="IP, hostname o rango CIDR objetivo")
    parser.add_argument("-t", "--type", choices=list(SCAN_PROFILES.keys()),
                        default="basic", help="Perfil de escaneo (default: basic)")
    parser.add_argument("-o", "--output", help="Guardar resultados en archivo .txt")
    parser.add_argument("--json", action="store_true", help="Salida en formato JSON")
    parser.add_argument("--range", action="store_true", help="Modo descubrimiento CIDR")

    args = parser.parse_args()
    print("=" * 60)
    print("  NMAP PYTHON SCANNER — Uso solo en entornos autorizados")
    print("=" * 60)

    if args.range:
        hosts = scan_range(args.target)
        if args.json:
            print(json.dumps({"hosts": hosts}, indent=2))
        return 0

    result = run_nmap(args.target, args.type, args.output)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(result["stdout"])
        if result["stderr"]:
            print(f"[STDERR]: {result['stderr']}", file=sys.stderr)

    if args.output:
        print(f"[+] Resultados guardados en: {args.output}")
    return result["returncode"]


if __name__ == "__main__":
    sys.exit(main())
