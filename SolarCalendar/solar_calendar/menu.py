"""
Interactive Menu System for the Astronomical Tarot
Provides a user-friendly interface for exploring the tarot system.
"""

import sys
from datetime import datetime
import pytz
from .calendar import SolarCalendar
from .tarot_system import (
    MAJOR_ARCANA, MINOR_ARCANA, COURT_CARDS, SPECIAL_CARDS,
    TAROT_SPREADS, get_card_by_constellation, Element, get_special_cards_for_date
)
from .tarot_visualization import (
    visualize_card, create_spread_visualization,
    create_constellation_map, create_constellation_bar
)
from .magical_system import MagicalSystem, Sephirah

def get_current_datetime():
    """Get current datetime in UTC."""
    return datetime.now(pytz.UTC)

def clear_screen():
    """Clear the terminal screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the program header."""
    print("\n" + "="*60)
    print(" " * 20 + "🌟 Astronomical Tarot System 🌟")
    print("="*60)
    print("\nWelcome to the Astronomical Tarot System!")
    print("This system combines traditional tarot with astronomical events")
    print("and the 13-month calendar. Choose an option below to begin.\n")

def print_menu():
    """Print the main menu options."""
    print("\nMain Menu:")
    print("1. View Current Cards - See cards relevant to today's date")
    print("2. Explore Major Arcana - Browse the 22 Major Arcana cards")
    print("3. Explore Minor Arcana - Browse the Minor Arcana cards by element")
    print("4. Explore Court Cards - Browse the Court Cards (Pages, Knights, Queens, Kings)")
    print("5. Explore Special Cards - Browse special astronomical and seasonal cards")
    print("6. View Available Spreads - See different tarot reading layouts")
    print("7. Perform a Reading - Get a reading based on current constellations")
    print("8. View Constellation Map - See the constellation layout and associations")
    print("9. View Calendar System - See the 13-month calendar and astronomical dates")
    print("10. View Magical System - Explore Tree of Life and magical practices")
    print("11. Exit - Close the program")
    print("\nEnter your choice (1-11): ", end="")
    sys.stdout.flush()

def get_current_cards():
    """Get and display cards relevant to the current date."""
    try:
        calendar = SolarCalendar()
        current_constellation = calendar.get_current_constellation()
        current_card = get_card_by_constellation(current_constellation)
        
        clear_screen()
        print_header()
        print("Current Cards:")
        print("-"*60)
        
        if current_card:
            print("\nCurrent Constellation Card:")
            print(visualize_card(current_card))
            print(f"\nCurrent Constellation: {current_constellation}")
            print(f"Duration in this constellation: {calendar.constellations[current_constellation]['duration']} days")
        
        input("\nPress Enter to return to the main menu...")
    except Exception as e:
        print(f"\nError: {str(e)}")
        input("\nPress Enter to return to the main menu...")

def explore_cards(card_type, cards_dict):
    """Generic function to explore any type of cards."""
    while True:
        try:
            clear_screen()
            print_header()
            print(f"{card_type} Cards:")
            print("-"*60)
            
            # Display card names with numbers
            for i, (name, card) in enumerate(cards_dict.items(), 1):
                if card_type == "Special Cards" and hasattr(card, 'date_ranges'):
                    # For cross-quarter days, show both traditional and astronomical dates
                    if name in ["The Imbolc", "The Beltane", "The Lughnasadh", "The Samhain"]:
                        print(f"{i}. {name} (Traditional: {card.date_ranges['traditional']})")
                    else:
                        print(f"{i}. {name} ({card.date_ranges['traditional']})")
                else:
                    print(f"{i}. {name}")
            
            print(f"\n{len(cards_dict) + 1}. Back to Main Menu")
            print("\nEnter card number to view details (or 'b' to go back): ", end="")
            sys.stdout.flush()
            
            choice = input().strip()
            if choice.lower() == 'b':
                return
            
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= len(cards_dict):
                    card_name = list(cards_dict.keys())[choice_num - 1]
                    clear_screen()
                    print_header()
                    card = cards_dict[card_name]
                    print(visualize_card(card))
                    
                    # Display date ranges for special cards
                    if card_type == "Special Cards" and hasattr(card, 'date_ranges'):
                        print("\nDate Ranges:")
                        print(f"Traditional: {card.date_ranges['traditional']}")
                        print(f"New Calendar: {card.date_ranges['new_calendar']}")
                        if 'astronomical' in card.date_ranges:
                            print(f"Astronomical: {card.date_ranges['astronomical']}")
                        else:
                            print(f"Astronomical: {card.date_ranges['astronomical']}")
                    
                    input("\nPress Enter to continue...")
                elif choice_num == len(cards_dict) + 1:
                    return
                else:
                    print("Invalid choice. Please try again.")
                    input("\nPress Enter to continue...")
            except ValueError:
                print("Please enter a valid number.")
                input("\nPress Enter to continue...")
        except Exception as e:
            print(f"\nError: {str(e)}")
            input("\nPress Enter to continue...")

def view_spreads():
    """Display available tarot spreads."""
    try:
        clear_screen()
        print_header()
        print("Available Spreads:")
        print("-"*60)
        
        for name, spread in TAROT_SPREADS.items():
            print(f"\n{name}")
            print(f"Cards: {spread['num_cards']}")
            print(f"Description: {spread['description']}")
            print("-"*30)
        
        input("\nPress Enter to return to the main menu...")
    except Exception as e:
        print(f"\nError: {str(e)}")
        input("\nPress Enter to return to the main menu...")

def perform_reading():
    """Perform a tarot reading using the current constellation spread."""
    try:
        clear_screen()
        print_header()
        print("Performing Reading...")
        print("-"*60)
        
        # Get current constellation card for present
        calendar = SolarCalendar()
        current_constellation = calendar.get_current_constellation()
        present_card = get_card_by_constellation(current_constellation)
        
        # Get previous constellation for past
        constellations = list(calendar.constellations.keys())
        current_index = constellations.index(current_constellation)
        past_constellation = constellations[current_index - 1]
        past_card = get_card_by_constellation(past_constellation)
        
        # Get next constellation for future
        future_constellation = constellations[(current_index + 1) % len(constellations)]
        future_card = get_card_by_constellation(future_constellation)
        
        # Display the reading
        if past_card:
            print("\n🌟 Past - The Path Behind:")
            print(visualize_card(past_card))
            
        if present_card:
            print("\n🌟 Present - Where You Stand:")
            print(visualize_card(present_card))
            
        if future_card:
            print("\n🌟 Future - The Path Ahead:")
            print(visualize_card(future_card))
        
        print("\nReading complete! ✨")
        input("\nPress Enter to return to the main menu...")
    except Exception as e:
        print(f"\nError: {str(e)}")
        input("\nPress Enter to return to the main menu...")

def view_constellation_map():
    """Display the constellation map."""
    try:
        clear_screen()
        print_header()
        print("Constellation Map:")
        print("-"*60)
        print(create_constellation_map(MAJOR_ARCANA))
        input("\nPress Enter to return to the main menu...")
    except Exception as e:
        print(f"\nError: {str(e)}")
        input("\nPress Enter to return to the main menu...")

def view_calendar_system():
    """Display the 13-month calendar system and astronomical dates."""
    try:
        clear_screen()
        print_header()
        print("13-Month Calendar System")
        print("-"*60)
        
        calendar = SolarCalendar()
        current_date = datetime.now(pytz.UTC)  # Make current_date timezone-aware
        current_month = calendar.get_current_month()
        
        # Calculate current day in the 13-month calendar
        month_start = datetime.strptime(current_month['dates'].split(' - ')[0], '%B %d')
        month_start = month_start.replace(year=current_date.year, tzinfo=pytz.UTC)  # Make month_start timezone-aware
        if month_start > current_date:
            month_start = month_start.replace(year=current_date.year - 1)
        
        days_in_month = current_month['days']
        delta = current_date - month_start
        current_day = delta.days + 1
        week_day = ((current_day - 1) % 7) + 1  # 1-7 for days of the week
        
        # Display current date information in both systems
        print("\n📅 Today's Date in Both Calendar Systems:")
        print("-"*40)
        print(f"Traditional Calendar: {current_date.strftime('%A, %B %d, %Y')}")
        print(f"13-Month Calendar: {current_month['name']} {current_month['symbol']}")
        print(f"Current Period: {current_month['dates']}")
        print(f"Current Day: Day {current_day} of {days_in_month}")
        print(f"Week Day: {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][week_day-1]}")
        
        # Get constellation era date
        era_date = calendar.get_constellation_era_date(current_date)
        print(f"\nConstellation Era: Year {era_date['ce_year']} of the Age of {era_date['current_age']}")
        print(f"Progress: {era_date['age_percentage']}% through current age")
        
        # Display today's cards
        print("\n🌟 Today's Associated Cards:")
        print("-"*40)
        
        # Get constellation card
        current_constellation = calendar.get_current_constellation()
        constellation_card = get_card_by_constellation(current_constellation)
        if constellation_card:
            print(f"\nConstellation Card for {current_constellation}:")
            print(visualize_card(constellation_card))
            if hasattr(constellation_card, 'duration_days'):
                print(f"Duration in this constellation: {constellation_card.duration_days} days")
        
        # Get special cards for today
        special_cards = get_special_cards_for_date(current_date)
        if special_cards:
            print("\nSpecial Cards Active Today:")
            for card in special_cards:
                print(visualize_card(card))
                if hasattr(card, 'date_ranges'):
                    print("\nDate Ranges:")
                    print(f"Traditional: {card.date_ranges['traditional']}")
                    print(f"New Calendar: {card.date_ranges['new_calendar']}")
                    if 'astronomical' in card.date_ranges:
                        print(f"Astronomical: {card.date_ranges['astronomical']}")
        else:
            print("\nNo special cards active today")
        
        # Get astronomical events
        events = calendar.get_upcoming_events(30)  # Next 30 days
        
        # Display upcoming astronomical events
        print("\n📆 Upcoming Astronomical Events:")
        print("-"*40)
        for event in events:
            event_date = event['date']
            if event_date.tzinfo is None:  # Make event_date timezone-aware if it isn't
                event_date = event_date.replace(tzinfo=pytz.UTC)
            days_until = (event_date - current_date).days
            print(f"• {event['name']}: {event_date.strftime('%B %d, %Y')} ({days_until} days from now)")
        
        # Display all months in the calendar
        print("\n📅 Complete 13-Month Calendar:")
        print("-"*40)
        for key, month in calendar.months.items():
            if isinstance(key, int):  # Regular months
                print(f"{month['symbol']} {month['name']}: {month['dates']}")
            else:  # Special days
                print(f"{month['symbol']} {month['name']}: {month['dates']} (Special)")
        
        input("\nPress Enter to return to the main menu...")
    except Exception as e:
        print(f"\nError: {str(e)}")
        input("\nPress Enter to return to the main menu...")

def view_magical_system():
    """Display the magical system information."""
    try:
        clear_screen()
        print_header()
        print("Tree of Life Magical System")
        print("-"*60)
        
        magical_system = MagicalSystem()
        today = datetime.now(pytz.UTC)
        today_path = magical_system.get_path_for_date(today)
        
        print("\n🌟 Today's Tree of Life Path:")
        print("-"*40)
        print(f"Path: {today_path.sephirah.value}")
        print(f"Element: {today_path.element.value}")
        print(f"Tarot Card: {today_path.tarot_card}")
        print(f"Level: {today_path.consciousness_level.value}")
        print(f"Barrier to Overcome: {today_path.barrier.value}")
        print(f"Magical Practices: {', '.join([p.value for p in today_path.magical_practices])}")
        print(f"Description: {today_path.description}")
        print(f"Keywords: {', '.join(today_path.keywords)}")
        
        ritual_timing = magical_system.get_ritual_timing(today_path.sephirah)
        print("\n⏰ Optimal Ritual Timing:")
        print("-"*40)
        print(f"Best Time: {ritual_timing['best_time']}")
        print(f"Color: {ritual_timing['color']}")
        print(f"Symbol: {ritual_timing['symbol']}")
        print(f"Hebrew Letter: {ritual_timing['hebrew_letter']}")
        
        progression = magical_system.get_path_progression(today_path.sephirah)
        print("\n📈 Recommended Path Progression:")
        print("-"*40)
        for i, sephirah in enumerate(progression, 1):
            print(f"{i}. {sephirah.value}")
        
        print("\n🔮 Available Magical Practices:")
        print("-"*40)
        for practice in today_path.magical_practices:
            print(f"• {practice.value}")
            if practice.value == "Meditation":
                print("  - Best done at dawn or dusk")
                print("  - Focus on the path's keywords")
                print("  - Visualize the path's symbol")
            elif practice.value == "Visualization":
                print("  - Use the path's color")
                print("  - Work with the Hebrew letter")
                print("  - Connect with the element")
            elif practice.value == "Ritual":
                print("  - Perform at the optimal time")
                print("  - Use the corresponding colors and symbols")
                print("  - Incorporate the element")
            elif practice.value == "Breathwork":
                print("  - Align with the element's energy")
                print("  - Use the Hebrew letter as a mantra")
                print("  - Focus on overcoming the barrier")
            elif practice.value == "Divination":
                print("  - Use the associated tarot card")
                print("  - Connect with the path's energy")
                print("  - Seek insight about the barrier")
            elif practice.value == "Alchemy":
                print("  - Work with the element's properties")
                print("  - Transform the barrier's energy")
                print("  - Use color correspondences")
        
        input("\nPress Enter to return to the main menu...")
    except Exception as e:
        print(f"\nError: {str(e)}")
        input("\nPress Enter to return to the main menu...")

def main():
    """Main menu loop."""
    while True:
        try:
            clear_screen()
            print_header()
            print_menu()
            
            choice = input().strip()
            
            if choice == "1":
                get_current_cards()
            elif choice == "2":
                explore_cards("Major Arcana", MAJOR_ARCANA)
            elif choice == "3":
                explore_cards("Minor Arcana", MINOR_ARCANA)
            elif choice == "4":
                explore_cards("Court Cards", COURT_CARDS)
            elif choice == "5":
                explore_cards("Special Cards", SPECIAL_CARDS)
            elif choice == "6":
                view_spreads()
            elif choice == "7":
                perform_reading()
            elif choice == "8":
                view_constellation_map()
            elif choice == "9":
                view_calendar_system()
            elif choice == "10":
                view_magical_system()
            elif choice == "11":
                print("\nThank you for using the Astronomical Tarot System!")
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to continue...")
        except Exception as e:
            print(f"\nError: {str(e)}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main() 