"""
CLI interface for the Solar Calendar system.
"""

import click
from datetime import datetime
from .calendar import SolarCalendar
from .astronomy import AstronomicalEvents
from .zodiac import ZodiacCalculator
from .tarot_system import (
    TarotCard, MAJOR_ARCANA, MINOR_ARCANA, COURT_CARDS, SPECIAL_CARDS,
    TAROT_SPREADS, get_card_by_constellation, Element
)
from .tarot_visualization import (
    visualize_card, create_spread_visualization,
    create_constellation_map, create_constellation_bar
)

@click.group()
def cli():
    """Solar Calendar System - Choose a command to begin"""
    pass

@cli.group()
def tarot():
    """Tarot reading commands"""
    pass

@tarot.command()
@click.option('--spread', type=click.Choice(list(TAROT_SPREADS.keys())), help='Choose a spread for the reading')
def reading(spread):
    """Perform a tarot reading"""
    if not spread:
        spread = "Constellation Path"  # Default spread
        
    spread_info = TAROT_SPREADS[spread]
    click.echo(f"\n=== {spread} Reading ===")
    click.echo(spread_info['description'])
    
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
        click.echo("\n🌟 Past - The Path Behind:")
        click.echo(visualize_card(past_card))
        
    if present_card:
        click.echo("\n🌟 Present - Where You Stand:")
        click.echo(visualize_card(present_card))
        
    if future_card:
        click.echo("\n🌟 Future - The Path Ahead:")
        click.echo(visualize_card(future_card))
    
    click.echo("\nReading complete! ✨")

@cli.command(name='calendar')
def display_calendar_cmd():
    """Display current calendar information"""
    calendar = SolarCalendar()
    current_date = datetime.now()
    current_constellation = calendar.get_constellation(current_date)
    
    click.echo("\n=== Current Calendar Information ===")
    click.echo(f"Date: {current_date.strftime('%Y-%m-%d')}")
    click.echo(f"Current Constellation: {current_constellation}")
    
    # Display constellation duration
    if current_constellation:
        constellation_data = calendar.constellations[current_constellation]
        duration = constellation_data["duration"]
        click.echo(f"Duration in current constellation: {duration} days")
        click.echo(f"Progress: {create_constellation_bar(duration)}")

@cli.command(name='constellations')
def show_constellations():
    """Display constellation map and transit times"""
    calendar = SolarCalendar()
    click.echo("\n=== Constellation Map ===")
    
    # Display all constellations with their transit times
    for constellation, data in calendar.constellations.items():
        start_month, start_day = data["start_date"]
        end_month, end_day = data["end_date"]
        duration = data["duration"]
        
        # Create progress bar
        progress_bar = create_constellation_bar(duration)
        
        click.echo(f"\n{constellation}")
        click.echo(f"Transit: {calendar.format_date(start_month, start_day)} - {calendar.format_date(end_month, end_day)}")
        click.echo(f"Duration: {progress_bar} ({duration} days)")

@cli.command(name='cards')
def show_all_cards():
    """Display all available tarot cards"""
    click.echo("\n=== All Tarot Cards ===")
    click.echo(f"Total Cards: {len(MAJOR_ARCANA) + len(MINOR_ARCANA) + len(COURT_CARDS)}")
    
    # Show Major Arcana
    click.echo("\n=== Major Arcana ===")
    for name, card in MAJOR_ARCANA.items():
        element_symbol = {
            Element.FIRE: "🔥",
            Element.WATER: "💧",
            Element.AIR: "💨",
            Element.EARTH: "🌍",
            Element.ETHER: "✨"
        }.get(card.element, "")
        
        click.echo(f"\n{name}")
        click.echo(f"Element: {element_symbol} {card.element.value}")
        click.echo(f"Keywords: {', '.join(card.keywords)}")
        click.echo(f"Description: {card.description}")
        if card.duration_days:
            click.echo(f"Duration: {create_constellation_bar(card.duration_days)} ({card.duration_days} days)")
        click.echo("-" * 30)
    
    # Show Minor Arcana
    click.echo("\n=== Minor Arcana ===")
    for element in Element:
        click.echo(f"\n{element.value} Suit:")
        for name, card in MINOR_ARCANA.items():
            if card.element == element:
                click.echo(f"\n{name}")
                click.echo(f"Keywords: {', '.join(card.keywords)}")
                click.echo(f"Description: {card.description}")
                click.echo("-" * 30)

@cli.command(name='spreads')
def list_spreads():
    """List available tarot spreads"""
    click.echo("\n=== Available Spreads ===")
    for name, spread in TAROT_SPREADS.items():
        click.echo(f"\n{name}")
        click.echo(f"Cards: {spread['num_cards']}")
        click.echo(f"Description: {spread['description']}")
        click.echo("-" * 30)

@tarot.command()
@click.argument('card_name')
def card_by_name(card_name):
    """Show details of a specific tarot card by name."""
    # Search in Major Arcana
    if card_name in MAJOR_ARCANA:
        click.echo(visualize_card(MAJOR_ARCANA[card_name]))
        return
    
    # Search in Minor Arcana
    if card_name in MINOR_ARCANA:
        click.echo(visualize_card(MINOR_ARCANA[card_name]))
        return
    
    # Search in Court Cards
    if card_name in COURT_CARDS:
        click.echo(visualize_card(COURT_CARDS[card_name]))
        return
    
    # Search in Special Cards
    if card_name in SPECIAL_CARDS:
        click.echo(visualize_card(SPECIAL_CARDS[card_name]))
        return
    
    click.echo(f"Card not found: {card_name}")

def create_constellation_bar(duration, width=20):
    """Create a visual progress bar for constellation duration."""
    filled = "█" * int(duration * width / 45)  # 45 is max duration (Virgo)
    empty = "░" * (width - len(filled))
    return filled + empty

def main():
    """Main entry point for the CLI."""
    cli()

if __name__ == "__main__":
    main() 