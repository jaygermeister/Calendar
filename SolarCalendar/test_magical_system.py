#!/usr/bin/env python3
"""
Test script for the Magical System
Demonstrates the integration of Regardie's Tree of Life teachings with astronomical calculations
"""

from solar_calendar.magical_system import MagicalSystem, Sephirah
from solar_calendar.consciousness_system import ConsciousnessLevel, BarrierType
from datetime import datetime
import pytz

def main():
    print("=== JAYGERIAN MAGICAL SYSTEM TEST ===")
    print("Integrating Regardie's Tree of Life with astronomical calculations")
    print("=====================================\n")
    
    # Initialize the magical system
    magical_system = MagicalSystem()
    
    # Get today's path
    today = datetime.now(pytz.UTC)
    today_path = magical_system.get_path_for_date(today)
    
    print(f"TODAY'S TREE OF LIFE PATH: {today_path.sephirah.value}")
    print(f"Element: {today_path.element.value}")
    print(f"Tarot Card: {today_path.tarot_card}")
    print(f"Consciousness Level: {today_path.consciousness_level.value}")
    print(f"Barrier: {today_path.barrier.value}")
    print(f"Magical Practices: {', '.join([p.value for p in today_path.magical_practices])}")
    print(f"Description: {today_path.description}")
    print(f"Keywords: {', '.join(today_path.keywords)}")
    print(f"Hebrew Letter: {today_path.hebrew_letter}")
    print(f"Color: {today_path.color}")
    print(f"Symbol: {today_path.symbol}")
    
    # Get ritual timing
    ritual_timing = magical_system.get_ritual_timing(today_path.sephirah)
    print(f"\nOPTIMAL RITUAL TIMING:")
    print(f"Best Time: {ritual_timing['best_time']}")
    print(f"Color: {ritual_timing['color']}")
    print(f"Symbol: {ritual_timing['symbol']}")
    print(f"Hebrew Letter: {ritual_timing['hebrew_letter']}")
    
    # Get path progression
    progression = magical_system.get_path_progression(today_path.sephirah)
    print(f"\nRECOMMENDED PATH PROGRESSION:")
    for i, sephirah in enumerate(progression, 1):
        print(f"{i}. {sephirah.value}")
    
    # Test different Sephirot
    print("\n=== TESTING DIFFERENT SEPHIROT ===")
    test_sephirot = [Sephirah.KETER, Sephirah.TIFERET, Sephirah.MALKUTH]
    
    for sephirah in test_sephirot:
        print(f"\n--- {sephirah.value} ---")
        consciousness_work = magical_system.get_consciousness_work(sephirah)
        print(f"Consciousness Level: {consciousness_work['level'].value}")
        print(f"Barrier: {consciousness_work['barrier'].value}")
        print(f"Practices: {', '.join([p.value for p in consciousness_work['practices']])}")
        print(f"Keywords: {', '.join(consciousness_work['keywords'])}")
        
        ritual_timing = magical_system.get_ritual_timing(sephirah)
        print(f"Best Time: {ritual_timing['best_time']}")
        print(f"Color: {ritual_timing['color']}")
        print(f"Symbol: {ritual_timing['symbol']}")

if __name__ == "__main__":
    main() 