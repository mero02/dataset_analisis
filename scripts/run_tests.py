#!/usr/bin/env python3
"""
Script para ejecutar tests con diferentes opciones
"""

import subprocess
import sys
import argparse
from pathlib import Path


def run_command(command, description):
    """Ejecuta un comando y maneja errores"""
    print(f"\n🔄 {description}")
    print(f"Comando: {' '.join(command)}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("✅ Comando ejecutado exitosamente")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando comando: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Ejecutar tests del proyecto")
    parser.add_argument(
        "--type", 
        choices=["unit", "integration", "all", "coverage"],
        default="all",
        help="Tipo de tests a ejecutar"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Ejecutar con verbose"
    )
    parser.add_argument(
        "--fast",
        action="store_true",
        help="Ejecutar solo tests rápidos (excluir slow)"
    )
    
    args = parser.parse_args()
    
    # Configurar comando base
    cmd = [sys.executable, "-m", "pytest"]
    
    if args.verbose:
        cmd.append("-v")
    
    if args.fast:
        cmd.extend(["-m", "not slow"])
    
    # Configurar según tipo
    if args.type == "unit":
        cmd.extend(["-m", "unit"])
        description = "Ejecutando tests unitarios"
    elif args.type == "integration":
        cmd.extend(["-m", "integration"])
        description = "Ejecutando tests de integración"
    elif args.type == "coverage":
        cmd.extend([
            "--cov=src",
            "--cov-report=html",
            "--cov-report=term-missing",
            "--cov-fail-under=80"
        ])
        description = "Ejecutando tests con cobertura"
    else:  # all
        description = "Ejecutando todos los tests"
    
    # Agregar directorio de tests
    cmd.append("tests/")
    
    # Ejecutar comando
    success = run_command(cmd, description)
    
    if success:
        print("\n🎉 Todos los tests pasaron exitosamente!")
        return 0
    else:
        print("\n💥 Algunos tests fallaron")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 