"""
Tarot Visualization System
Provides ASCII art and visualization tools for the astronomical tarot system.
"""

from typing import List, Dict
from .tarot_system import TarotCard, Element, CardType

def create_card_frame(title: str, width: int = 40) -> str:
    """Create an ASCII frame for a tarot card."""
    top_bottom = "═" * width
    sides = "║"
    return f"""
╔{top_bottom}╗
║{title.center(width)}║
╠{top_bottom}╣
"""

def create_constellation_bar(duration: int, max_duration: int = 45, width: int = 30) -> str:
    """Create a visual bar representing constellation duration."""
    bar_length = int((duration / max_duration) * width)
    return "█" * bar_length + "░" * (width - bar_length)

def visualize_card(card: TarotCard) -> str:
    """Create an ASCII visualization of a tarot card."""
    frame = create_card_frame(card.name)
    
    # Add element symbol
    element_symbol = {
        Element.FIRE: "🔥",
        Element.WATER: "💧",
        Element.AIR: "💨",
        Element.EARTH: "🌍",
        Element.ETHER: "✨"
    }.get(card.element, "")
    
    # Add constellation duration bar if applicable
    duration_bar = ""
    if card.duration_days:
        duration_bar = f"\nDuration: {create_constellation_bar(card.duration_days)} ({card.duration_days} days)"
    
    # Add keywords
    keywords = "\nKeywords: " + ", ".join(card.keywords) if card.keywords else ""
    
    # Add description
    description = f"\n\n{card.description}" if card.description else ""
    
    # Add image description
    image_desc = f"\n\nImage: {card.image_description}" if card.image_description else ""
    
    return f"""
{frame}
Element: {element_symbol} {card.element.value if card.element else "N/A"}
Constellation: {card.constellation if card.constellation else "N/A"}{duration_bar}{keywords}{description}{image_desc}
"""

def create_spread_visualization(spread_name: str, cards: List[TarotCard]) -> str:
    """Create a visualization of a tarot spread."""
    spread_visual = f"\n=== {spread_name} ===\n"
    
    for i, card in enumerate(cards, 1):
        spread_visual += f"\nPosition {i}:\n"
        spread_visual += visualize_card(card)
    
    return spread_visual

def create_constellation_map(cards: Dict[str, TarotCard]) -> str:
    """Create a visual map of constellations and their associated cards."""
    map_visual = "\n=== Constellation Map (Starting from Aurora 1) ===\n"
    
    # Get calendar information
    from .calendar import SolarCalendar
    calendar = SolarCalendar()
    
    # Define the order of constellations starting from Aurora 1 (March 21)
    constellation_order = [
        "Pisces",      # March 11 - April 18
        "Aries",       # April 18 - May 13
        "Taurus",      # May 13 - June 21
        "Gemini",      # June 21 - July 20
        "Cancer",      # July 20 - August 10
        "Leo",         # August 10 - September 16
        "Virgo",       # September 16 - October 30
        "Libra",       # October 30 - November 23
        "Scorpius",    # November 23 - November 29
        "Ophiuchus",   # November 29 - December 17
        "Sagittarius", # December 17 - January 20
        "Capricornus", # January 20 - February 16
        "Aquarius"     # February 16 - March 11
    ]
    
    # Create the map
    for constellation_name in constellation_order:
        const_data = calendar.constellations[constellation_name]
        start_month, start_day = const_data["start_date"]
        end_month, end_day = const_data["end_date"]
        duration = const_data["duration"]
        
        # Find the corresponding card
        card = next((c for c in cards.values() if c.constellation == constellation_name), None)
        
        # Format Gregorian dates
        start_date = f"{calendar.month_names[start_month]} {start_day}"
        end_date = f"{calendar.month_names[end_month]} {end_day}"
        
        # Find corresponding 13-month calendar period
        month_info = None
        for key, month in calendar.months.items():
            if isinstance(key, int):  # Regular months
                month_start_str = month["dates"].split(" - ")[0]
                month_start_month, month_start_day = calendar._parse_date(month_start_str)
                
                # Check if constellation starts during this month
                if (start_month > month_start_month or 
                    (start_month == month_start_month and start_day >= month_start_day)):
                    month_info = month
        
        # Create duration bar
        duration_bar = create_constellation_bar(duration)
        
        # Add to map
        map_visual += f"\n{constellation_name}: {duration_bar} ({duration} days)"
        map_visual += f"\nGregorian: {start_date} - {end_date}"
        
        if month_info:
            map_visual += f"\n13-Month: {month_info['name']} {month_info['symbol']} ({month_info['dates']})"
        
        if card:
            map_visual += f"\nAssociated Card: {card.name}"
            map_visual += f"\nElement: {card.element.value if card.element else 'N/A'}"
            map_visual += f"\nKeywords: {', '.join(card.keywords)}\n"
        
        map_visual += "-" * 40 + "\n"
    
    return map_visual 