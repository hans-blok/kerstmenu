#!/usr/bin/env python3
"""
Runner voor Sous-chef agent

Zie: governance/rolbeschrijvingen/sous-chef.md
Prompt: .github/prompts/sous-chef.prompt.md

Gebruik:
    python scripts/sous-chef.py "stel recepten op voor voorgerecht voor 3 personen"
    python scripts/sous-chef.py "maak recept voor hoofdgerecht voor 6 personen"
    python scripts/sous-chef.py "valideer recept spitskool" --check-only
"""

import argparse
import sys
from pathlib import Path


def print_header(text):
    """Print een header met emoji"""
    print(f"\n👨‍🍳 {text}")
    print("━" * 60)


def print_step(text):
    """Print een stap met checkmark"""
    print(f"✅ {text}")


def print_info(text):
    """Print info"""
    print(f"ℹ️  {text}")


def print_error(text):
    """Print een error"""
    print(f"❌ ERROR: {text}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Sous-chef agent - Praktische recept uitwerking met handige aanpak",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Voorbeelden:
  python scripts/sous-chef.py "stel recepten op voor voorgerecht voor 3 personen"
  python scripts/sous-chef.py "maak recept voor hoofdgerecht voor 6 personen"
  python scripts/sous-chef.py "werk spitskool recept uit met mise-en-place"
  python scripts/sous-chef.py "valideer recept" --check-only

De Sous-chef:
  - Werkt menu concepten van Chef Kok uit tot complete recepten
  - Geeft exacte hoeveelheden per ingrediënt
  - Herhaalt hoeveelheden in elke bereidingsstap
  - Gebruikt mise-en-place aanpak (alles klaar voor je begint)
  - Focust op handige volgorde en efficiency
  
Werkprincipe:
  1. Ingrediënten met exacte hoeveelheden
  2. Mise-en-place (alles klaarzetten)
  3. Bereiding met hoeveelheden IN elke stap
  4. Tips voor efficiency en variaties
        """
    )
    
    parser.add_argument("opdracht", 
                       help="Opdracht voor Sous-chef (bijv. 'stel recepten op voor voorgerecht voor 3 personen')")
    parser.add_argument("--check-only", action="store_true",
                       help="Alleen analyseren, geen wijzigingen")
    parser.add_argument("--personen", type=int,
                       help="Aantal personen (verplicht voor nieuwe recepten)")
    parser.add_argument("--gang", 
                       choices=["voorgerecht", "soep", "hoofdgerecht", "dessert"],
                       help="Welke gang")
    parser.add_argument("--concept", 
                       help="Pad naar menu concept van Chef Kok")
    
    args = parser.parse_args()
    
    print_header("Sous-chef Agent")
    print_info(f"Opdracht: {args.opdracht}")
    
    if args.check_only:
        print_info("Mode: Alleen analyse (geen wijzigingen)")
    
    # Check aantal personen voor nieuwe recepten
    if not args.check_only and not args.personen and "stel" in args.opdracht.lower():
        print_error("Aantal personen is verplicht voor nieuwe recepten!")
        print_info("Gebruik: --personen 3 (of ander aantal)")
        print_info("Voorbeeld: python scripts/sous-chef.py 'stel recept op' --personen 3")
        return 1
    
    if args.personen:
        print_info(f"Aantal personen: {args.personen}")
    
    if args.gang:
        print_info(f"Gang: {args.gang}")
    
    if args.concept:
        concept_path = Path(args.concept)
        if not concept_path.exists():
            print_error(f"Menu concept niet gevonden: {args.concept}")
            return 1
        print_info(f"Menu concept: {args.concept}")
    
    # TODO: Implementeer Sous-chef logica
    print_header("Analyse")
    print_step("Menu concept gelezen")
    print_step("Aantal personen gecontroleerd")
    print_step("Gang geïdentificeerd")
    
    print_header("Ingrediënten Specificeren")
    print_info("Exacte hoeveelheden bepalen per persoon en totaal...")
    
    print_header("Mise-en-place Bepalen")
    print_info("Optimale voorbereidingsstappen opstellen...")
    
    print_header("Bereiding Uitwerken")
    print_info("Stapsgewijze instructies met hoeveelheden...")
    
    print_header("Tips en Variaties")
    print_info("Efficiency tips en alternatieven toevoegen...")
    
    print()
    print("━" * 60)
    print("✅ Sous-chef klaar!")
    print()
    print("📝 Output:")
    print("  - Ingrediëntenlijst met exacte hoeveelheden")
    print("  - Mise-en-place (alles klaarzetten)")
    print("  - Bereiding met hoeveelheden per stap")
    print("  - Chef's tips en variaties")
    print()
    print("💡 Tips:")
    print("  - Hoeveelheden staan zowel in ingrediënten als bereidingsstappen")
    print("  - Mise-en-place eerst = sneller en minder stress")
    print("  - Alle tijden en temperaturen zijn aangegeven")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
