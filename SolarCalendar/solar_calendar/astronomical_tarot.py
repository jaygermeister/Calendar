"""
Astronomical Tarot System
A new tarot system that combines traditional tarot wisdom with astronomical accuracy.
Each card represents both a sephirah on the Tree of Life and an astronomical constellation/event.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime
import pytz

class Element(Enum):
    FIRE = "Fire"
    WATER = "Water"
    AIR = "Air"
    EARTH = "Earth"
    ETHER = "Ether"  # For Ophiuchus and special cards

class Planet(Enum):
    SUN = "Sun"
    MOON = "Moon"
    MERCURY = "Mercury"
    VENUS = "Venus"
    MARS = "Mars"
    JUPITER = "Jupiter"
    SATURN = "Saturn"
    URANUS = "Uranus"
    NEPTUNE = "Neptune"
    PLUTO = "Pluto"

class CardType(Enum):
    MAJOR = "Major Arcana"
    MINOR = "Minor Arcana"
    COURT = "Court Card"
    SPECIAL = "Special Card"

@dataclass
class AstronomicalTarotCard:
    name: str
    traditional_name: str  # Traditional tarot card name
    card_type: CardType
    element: Element
    planet: Planet
    constellation: Optional[str] = None
    sephirah: Optional[str] = None
    duration_days: Optional[int] = None
    keywords: List[str] = None
    description: str = ""
    astronomical_significance: str = ""
    magical_practices: List[str] = None
    hebrew_letter: Optional[str] = None
    color: Optional[str] = None
    symbol: Optional[str] = None
    date_ranges: Dict[str, str] = None

# Major Arcana Cards with Astronomical and Traditional Associations
ASTRONOMICAL_MAJOR_ARCANA = {
    "The Crown": AstronomicalTarotCard(
        name="The Crown",
        traditional_name="The Fool",
        card_type=CardType.MAJOR,
        element=Element.ETHER,
        planet=Planet.URANUS,
        constellation="Ophiuchus",
        sephirah="Keter",
        duration_days=18,
        keywords=["unity", "divine will", "pure consciousness", "transcendence", "healing", "transformation"],
        description="The Crown represents the highest point of consciousness and divine unity",
        astronomical_significance="Ophiuchus, the Serpent Bearer, represents healing and transformation in the cosmic dance",
        magical_practices=["Meditation", "Visualization", "Healing Rituals", "Energy Work"],
        hebrew_letter="א",
        color="White",
        symbol="∞"
    ),
    "The Wisdom": AstronomicalTarotCard(
        name="The Wisdom",
        traditional_name="The Magician",
        card_type=CardType.MAJOR,
        element=Element.FIRE,
        planet=Planet.MERCURY,
        constellation="Sagittarius",
        sephirah="Chokhmah",
        duration_days=33,
        keywords=["wisdom", "inspiration", "divine spark", "creation", "adventure", "exploration"],
        description="The Wisdom represents the first flash of divine light and creative force",
        astronomical_significance="Sagittarius, the Archer, points to higher knowledge and spiritual wisdom",
        magical_practices=["Ritual", "Breathwork", "Divination", "Pathworking"],
        hebrew_letter="ב",
        color="Gray",
        symbol="⚡"
    ),
    "The Understanding": AstronomicalTarotCard(
        name="The Understanding",
        traditional_name="The High Priestess",
        card_type=CardType.MAJOR,
        element=Element.WATER,
        planet=Planet.MOON,
        constellation="Pisces",
        sephirah="Binah",
        duration_days=38,
        keywords=["understanding", "receptivity", "form", "limitation", "intuition", "dreams"],
        description="The Understanding represents the receptive principle of creation and deep wisdom",
        astronomical_significance="Pisces, the Fishes, swims in the depths of the cosmic ocean",
        magical_practices=["Divination", "Meditation", "Dream Work", "Moon Rituals"],
        hebrew_letter="ג",
        color="Black",
        symbol="☽"
    ),
    "The Mercy": AstronomicalTarotCard(
        name="The Mercy",
        traditional_name="The Empress",
        card_type=CardType.MAJOR,
        element=Element.WATER,
        planet=Planet.VENUS,
        constellation="Cancer",
        sephirah="Chesed",
        duration_days=21,
        keywords=["mercy", "love", "expansion", "abundance", "nurturing", "protection"],
        description="The Mercy represents the expansive force of divine love and nurturing",
        astronomical_significance="Cancer, the Crab, represents the protective and nurturing aspects of creation",
        magical_practices=["Ritual", "Alchemy", "Love Magic", "Protection Work"],
        hebrew_letter="ד",
        color="Blue",
        symbol="💙"
    ),
    "The Severity": AstronomicalTarotCard(
        name="The Severity",
        traditional_name="The Tower",
        card_type=CardType.MAJOR,
        element=Element.FIRE,
        planet=Planet.MARS,
        constellation="Scorpius",
        sephirah="Gevurah",
        duration_days=6,
        keywords=["severity", "strength", "discipline", "limitation", "transformation", "power"],
        description="The Severity represents the restrictive force of divine judgment and transformation",
        astronomical_significance="Scorpius, the Scorpion, brings intense transformation and power",
        magical_practices=["Ritual", "Breathwork", "Banishing", "Protection"],
        hebrew_letter="ה",
        color="Red",
        symbol="⚔️"
    ),
    "The Beauty": AstronomicalTarotCard(
        name="The Beauty",
        traditional_name="The Sun",
        card_type=CardType.MAJOR,
        element=Element.AIR,
        planet=Planet.SUN,
        constellation="Leo",
        sephirah="Tiferet",
        duration_days=37,
        keywords=["beauty", "harmony", "balance", "integration", "creativity", "leadership"],
        description="The Beauty represents the harmonizing principle of balance and radiant power",
        astronomical_significance="Leo, the Lion, brings the radiant power of the sun and creative force",
        magical_practices=["Meditation", "Visualization", "Solar Rituals", "Creative Work"],
        hebrew_letter="ו",
        color="Yellow",
        symbol="☀️"
    ),
    "The Victory": AstronomicalTarotCard(
        name="The Victory",
        traditional_name="The Star",
        card_type=CardType.MAJOR,
        element=Element.FIRE,
        planet=Planet.JUPITER,
        constellation="Libra",
        sephirah="Netzach",
        duration_days=23,
        keywords=["victory", "endurance", "passion", "persistence", "balance", "harmony"],
        description="The Victory represents the enduring force of divine persistence and balance",
        astronomical_significance="Libra, the Scales, brings balance and harmony to the cosmic dance",
        magical_practices=["Ritual", "Alchemy", "Balance Work", "Harmony Magic"],
        hebrew_letter="ז",
        color="Green",
        symbol="🌿"
    ),
    "The Splendor": AstronomicalTarotCard(
        name="The Splendor",
        traditional_name="The Moon",
        card_type=CardType.MAJOR,
        element=Element.WATER,
        planet=Planet.NEPTUNE,
        constellation="Capricornus",
        sephirah="Hod",
        duration_days=28,
        keywords=["splendor", "communication", "intellect", "magic", "ambition", "discipline"],
        description="The Splendor represents the intellectual force of divine communication",
        astronomical_significance="Capricornus, the Sea Goat, bridges earthly and spiritual realms",
        magical_practices=["Divination", "Visualization", "Communication Magic", "Ritual Work"],
        hebrew_letter="ח",
        color="Orange",
        symbol="🌙"
    ),
    "The Foundation": AstronomicalTarotCard(
        name="The Foundation",
        traditional_name="The World",
        card_type=CardType.MAJOR,
        element=Element.AIR,
        planet=Planet.SATURN,
        constellation="Aquarius",
        sephirah="Yesod",
        duration_days=24,
        keywords=["foundation", "manifestation", "connection", "dreams", "innovation", "progress"],
        description="The Foundation represents the connecting force of divine manifestation",
        astronomical_significance="Aquarius, the Water Bearer, brings innovation and collective consciousness",
        magical_practices=["Ritual", "Breathwork", "Foundation Work", "Manifestation Magic"],
        hebrew_letter="ט",
        color="Purple",
        symbol="🌍"
    ),
    "The Kingdom": AstronomicalTarotCard(
        name="The Kingdom",
        traditional_name="The World",
        card_type=CardType.MAJOR,
        element=Element.EARTH,
        planet=Planet.PLUTO,
        constellation="Virgo",
        sephirah="Malkuth",
        duration_days=45,
        keywords=["kingdom", "manifestation", "matter", "earth", "abundance", "fertility"],
        description="The Kingdom represents the material manifestation of divine presence",
        astronomical_significance="Virgo, the Harvest, brings abundance and earthly manifestation",
        magical_practices=["Ritual", "Alchemy", "Earth Magic", "Manifestation Work"],
        hebrew_letter="ת",
        color="Brown",
        symbol="🏰"
    ),
    "The Great Year": AstronomicalTarotCard(
        name="The Great Year",
        traditional_name="The Wheel of Fortune",
        card_type=CardType.MAJOR,
        element=Element.ETHER,
        planet=Planet.URANUS,
        keywords=["cycles", "evolution", "cosmic time", "precession", "change", "destiny"],
        description="Represents the 25,772-year cycle of the precession of the equinoxes",
        astronomical_significance="The complete cycle of the Great Year, marking the evolution of consciousness",
        magical_practices=["Time Magic", "Cycle Work", "Evolutionary Rituals", "Cosmic Meditation"],
        hebrew_letter="ס",
        color="Indigo",
        symbol="⭕"
    ),
    "The Solstice": AstronomicalTarotCard(
        name="The Solstice",
        traditional_name="The Sun",
        card_type=CardType.MAJOR,
        element=Element.FIRE,
        planet=Planet.SUN,
        keywords=["extremes", "balance", "turning points", "illumination", "power", "clarity"],
        description="Symbolizes the longest and shortest days, moments of maximum light and darkness",
        astronomical_significance="The solar turning points that mark the extremes of light and darkness",
        magical_practices=["Solar Rituals", "Light Magic", "Balance Work", "Power Magic"],
        hebrew_letter="ש",
        color="Gold",
        symbol="☀️"
    ),
    "The Equinox": AstronomicalTarotCard(
        name="The Equinox",
        traditional_name="The Temperance",
        card_type=CardType.MAJOR,
        element=Element.AIR,
        planet=Planet.MERCURY,
        keywords=["balance", "harmony", "equality", "transition", "integration", "flow"],
        description="Represents perfect balance between day and night, light and dark",
        astronomical_significance="The moments of perfect balance between light and darkness",
        magical_practices=["Balance Magic", "Integration Work", "Flow Rituals", "Harmony Magic"],
        hebrew_letter="מ",
        color="Silver",
        symbol="⚖️"
    ),
    "The Eclipse": AstronomicalTarotCard(
        name="The Eclipse",
        traditional_name="The Tower",
        card_type=CardType.MAJOR,
        element=Element.ETHER,
        planet=Planet.PLUTO,
        keywords=["revelation", "transformation", "alignment", "mystery", "change", "power"],
        description="Symbolizes rare moments of cosmic alignment and revelation",
        astronomical_significance="The rare alignment of celestial bodies that brings transformation",
        magical_practices=["Eclipse Magic", "Transformation Work", "Revelation Rituals", "Power Magic"],
        hebrew_letter="פ",
        color="Black",
        symbol="🌑"
    )
}

# Special Cards for Astronomical Events
SPECIAL_CARDS = {
    "The New Moon": AstronomicalTarotCard(
        name="The New Moon",
        traditional_name="The Moon",
        card_type=CardType.SPECIAL,
        element=Element.WATER,
        planet=Planet.MOON,
        keywords=["beginnings", "potential", "darkness", "mystery", "intuition"],
        description="Represents the dark phase of the moon, a time of new beginnings",
        astronomical_significance="The moon's dark phase, marking new lunar cycles",
        magical_practices=["New Moon Rituals", "Beginnings Magic", "Intuition Work"],
        hebrew_letter="ל",
        color="Black",
        symbol="🌑"
    ),
    "The Full Moon": AstronomicalTarotCard(
        name="The Full Moon",
        traditional_name="The Moon",
        card_type=CardType.SPECIAL,
        element=Element.WATER,
        planet=Planet.MOON,
        keywords=["completion", "illumination", "manifestation", "clarity", "power"],
        description="Represents the moon's full phase, a time of completion and power",
        astronomical_significance="The moon's full phase, marking completion of lunar cycles",
        magical_practices=["Full Moon Rituals", "Completion Magic", "Power Work"],
        hebrew_letter="מ",
        color="Silver",
        symbol="🌕"
    ),
    "The Planetary Alignment": AstronomicalTarotCard(
        name="The Planetary Alignment",
        traditional_name="The Star",
        card_type=CardType.SPECIAL,
        element=Element.ETHER,
        planet=Planet.URANUS,
        keywords=["alignment", "harmony", "cosmic order", "divine timing", "synchronicity"],
        description="Represents rare alignments of planets that bring cosmic harmony",
        astronomical_significance="Rare alignments of multiple planets in the sky",
        magical_practices=["Alignment Magic", "Harmony Work", "Cosmic Rituals"],
        hebrew_letter="צ",
        color="Blue",
        symbol="✨"
    )
}

def get_card_by_constellation(constellation: str) -> Optional[AstronomicalTarotCard]:
    """Get the tarot card associated with a specific constellation."""
    for card in ASTRONOMICAL_MAJOR_ARCANA.values():
        if card.constellation == constellation:
            return card
    return None

def get_card_by_sephirah(sephirah: str) -> Optional[AstronomicalTarotCard]:
    """Get the tarot card associated with a specific sephirah."""
    for card in ASTRONOMICAL_MAJOR_ARCANA.values():
        if card.sephirah == sephirah:
            return card
    return None

def get_special_cards_for_date(date: datetime = None) -> List[AstronomicalTarotCard]:
    """Get special cards that are relevant to a specific date."""
    if date is None:
        date = datetime.now(pytz.UTC)
    
    special_cards = []
    
    # Add logic here to determine special cards based on astronomical events
    # This would include checking for eclipses, planetary alignments, etc.
    
    return special_cards 