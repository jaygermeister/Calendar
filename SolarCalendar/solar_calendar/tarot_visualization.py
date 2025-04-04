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
    map_visual = "\n=== Constellation Map ===\n"
    
    # Sort cards by duration
    sorted_cards = sorted(
        [card for card in cards.values() if card.constellation],
        key=lambda x: x.duration_days or 0,
        reverse=True
    )
    
    for card in sorted_cards:
        if card.constellation:
            duration_bar = create_constellation_bar(card.duration_days or 0)
            map_visual += f"\n{card.constellation}: {duration_bar} ({card.duration_days} days)"
            map_visual += f"\nAssociated Card: {card.name}"
            map_visual += f"\nKeywords: {', '.join(card.keywords)}\n"
    
    return map_visual 