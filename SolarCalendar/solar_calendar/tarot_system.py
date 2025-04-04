"""
Astronomical Tarot System
A new tarot system based on accurate astronomical data and the 13-month calendar.
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
    ETHER = "Ether"  # New element for Ophiuchus

class CardType(Enum):
    MAJOR = "Major Arcana"
    MINOR = "Minor Arcana"
    COURT = "Court Card"
    SPECIAL = "Special Card"

@dataclass
class TarotCard:
    name: str
    card_type: CardType
    element: Optional[Element] = None
    constellation: Optional[str] = None
    duration_days: Optional[int] = None
    keywords: List[str] = None
    description: str = ""
    image_description: str = ""
    date_ranges: Dict[str, str] = None

# Major Arcana Cards with Astronomical Associations
MAJOR_ARCANA = {
    "The Healer": TarotCard(
        name="The Healer",
        card_type=CardType.MAJOR,
        element=Element.ETHER,
        constellation="Ophiuchus",
        duration_days=18,
        keywords=["healing", "transformation", "wisdom", "rebirth"],
        description="Represents the healing journey and transformation through wisdom",
        image_description="A figure holding a serpent, surrounded by healing light"
    ),
    "The Harvest": TarotCard(
        name="The Harvest",
        card_type=CardType.MAJOR,
        element=Element.EARTH,
        constellation="Virgo",
        duration_days=45,
        keywords=["abundance", "fertility", "nurturing", "practicality"],
        description="Symbolizes the longest constellation transit and earthly abundance",
        image_description="A woman surrounded by golden wheat, holding a cornucopia"
    ),
    "The Transformation": TarotCard(
        name="The Transformation",
        card_type=CardType.MAJOR,
        element=Element.WATER,
        constellation="Scorpius",
        duration_days=6,
        keywords=["intensity", "transformation", "rebirth", "power"],
        description="Represents the intense but brief period of transformation",
        image_description="A scorpion transforming into a phoenix"
    ),
    "The Archer": TarotCard(
        name="The Archer",
        card_type=CardType.MAJOR,
        element=Element.FIRE,
        constellation="Sagittarius",
        duration_days=33,
        keywords=["adventure", "exploration", "philosophy", "freedom"],
        description="Symbolizes the journey of exploration and higher knowledge",
        image_description="A centaur archer aiming at the stars"
    ),
    "The Sea Goat": TarotCard(
        name="The Sea Goat",
        card_type=CardType.MAJOR,
        element=Element.EARTH,
        constellation="Capricornus",
        duration_days=28,
        keywords=["ambition", "discipline", "structure", "achievement"],
        description="Represents the balance between earthly and spiritual realms",
        image_description="A mythical creature with goat's body and fish's tail"
    ),
    "The Water Bearer": TarotCard(
        name="The Water Bearer",
        card_type=CardType.MAJOR,
        element=Element.AIR,
        constellation="Aquarius",
        duration_days=24,
        keywords=["innovation", "humanitarianism", "progress", "revolution"],
        description="Symbolizes the flow of new ideas and collective consciousness",
        image_description="A figure pouring water from an urn, creating a river of stars"
    ),
    "The Fishes": TarotCard(
        name="The Fishes",
        card_type=CardType.MAJOR,
        element=Element.WATER,
        constellation="Pisces",
        duration_days=38,
        keywords=["intuition", "dreams", "compassion", "mysticism"],
        description="Represents the deep connection to the subconscious and spiritual realms",
        image_description="Two fish swimming in opposite directions, connected by a silver cord"
    ),
    "The Ram": TarotCard(
        name="The Ram",
        card_type=CardType.MAJOR,
        element=Element.FIRE,
        constellation="Aries",
        duration_days=25,
        keywords=["initiative", "courage", "leadership", "new beginnings"],
        description="Symbolizes the spark of creation and the drive to begin anew",
        image_description="A golden ram charging through a field of stars"
    ),
    "The Bull": TarotCard(
        name="The Bull",
        card_type=CardType.MAJOR,
        element=Element.EARTH,
        constellation="Taurus",
        duration_days=37,
        keywords=["stability", "sensuality", "determination", "abundance"],
        description="Represents the grounding force of nature and material wealth",
        image_description="A powerful bull standing in a field of blooming flowers"
    ),
    "The Twins": TarotCard(
        name="The Twins",
        card_type=CardType.MAJOR,
        element=Element.AIR,
        constellation="Gemini",
        duration_days=31,
        keywords=["duality", "communication", "adaptability", "curiosity"],
        description="Symbolizes the dance of opposites and the power of connection",
        image_description="Two figures standing back to back, one looking to the past, one to the future"
    ),
    "The Crab": TarotCard(
        name="The Crab",
        card_type=CardType.MAJOR,
        element=Element.WATER,
        constellation="Cancer",
        duration_days=21,
        keywords=["nurturing", "protection", "intuition", "home"],
        description="Represents the protective shell and the nurturing heart",
        image_description="A crab emerging from its shell, surrounded by a protective circle of stars"
    ),
    "The Lion": TarotCard(
        name="The Lion",
        card_type=CardType.MAJOR,
        element=Element.FIRE,
        constellation="Leo",
        duration_days=37,
        keywords=["creativity", "leadership", "vitality", "self-expression"],
        description="Symbolizes the radiant power of the sun and creative force",
        image_description="A majestic lion with a mane of golden light"
    ),
    "The Scales": TarotCard(
        name="The Scales",
        card_type=CardType.MAJOR,
        element=Element.AIR,
        constellation="Libra",
        duration_days=23,
        keywords=["balance", "harmony", "justice", "partnership"],
        description="Represents the eternal quest for balance and harmony",
        image_description="Golden scales floating in the night sky, perfectly balanced"
    ),
    "The Great Year": TarotCard(
        name="The Great Year",
        card_type=CardType.MAJOR,
        element=Element.ETHER,
        keywords=["cycles", "evolution", "cosmic time", "precession"],
        description="Represents the 25,772-year cycle of the precession of the equinoxes",
        image_description="A cosmic clock showing the slow movement of the stars"
    ),
    "The Solstice": TarotCard(
        name="The Solstice",
        card_type=CardType.MAJOR,
        element=Element.FIRE,
        keywords=["extremes", "balance", "turning points", "illumination"],
        description="Symbolizes the longest and shortest days, moments of maximum light and darkness",
        image_description="A sun standing still at its highest and lowest points"
    ),
    "The Equinox": TarotCard(
        name="The Equinox",
        card_type=CardType.MAJOR,
        element=Element.AIR,
        keywords=["balance", "harmony", "equality", "transition"],
        description="Represents perfect balance between day and night, light and dark",
        image_description="A scale perfectly balanced between sun and moon"
    ),
    "The Eclipse": TarotCard(
        name="The Eclipse",
        card_type=CardType.MAJOR,
        element=Element.ETHER,
        keywords=["revelation", "transformation", "alignment", "mystery"],
        description="Symbolizes rare moments of cosmic alignment and revelation",
        image_description="Sun and moon perfectly aligned in the sky"
    ),
    "The Comet": TarotCard(
        name="The Comet",
        card_type=CardType.MAJOR,
        element=Element.FIRE,
        keywords=["change", "messenger", "transformation", "unexpected"],
        description="Represents sudden change and cosmic messages from beyond",
        image_description="A blazing comet streaking across the night sky"
    ),
    "The Nebula": TarotCard(
        name="The Nebula",
        card_type=CardType.MAJOR,
        element=Element.ETHER,
        keywords=["creation", "potential", "birth", "cosmic womb"],
        description="Symbolizes the creative potential and birth of new forms",
        image_description="A swirling cloud of cosmic dust and light"
    ),
    "The Black Hole": TarotCard(
        name="The Black Hole",
        card_type=CardType.MAJOR,
        element=Element.ETHER,
        keywords=["transformation", "mystery", "release", "rebirth"],
        description="Represents the point of no return and ultimate transformation",
        image_description="A swirling vortex of darkness surrounded by light"
    ),
    "The Supernova": TarotCard(
        name="The Supernova",
        card_type=CardType.MAJOR,
        element=Element.FIRE,
        keywords=["explosion", "creation", "destruction", "rebirth"],
        description="Symbolizes the explosive transformation and creation of new elements",
        image_description="A star exploding in a burst of cosmic light"
    )
}

# Special Cards for astronomical events and Ether aspects
SPECIAL_CARDS = {
    "The Winter Solstice": TarotCard(
        name="The Winter Solstice",
        card_type="Special",
        element=Element.ETHER,
        keywords=["rebirth", "potential", "cosmic mystery", "new beginnings"],
        description="The longest night, representing the depth of cosmic mystery and the promise of rebirth",
        image_description="A dark sky with a single bright star, surrounded by swirling cosmic energy",
        date_ranges={
            "traditional": "December 21-22",
            "new_calendar": "Yule (December 26 - January 22)",
            "astronomical": "Sun at lowest point in the sky, longest night"
        }
    ),
    "The Imbolc": TarotCard(
        name="The Imbolc",
        card_type="Special",
        element=Element.ETHER,
        keywords=["awakening", "purification", "inspiration", "potential"],
        description="The first stirrings of spring, representing spiritual awakening and purification",
        image_description="A single flame emerging from cosmic ice, surrounded by shooting stars",
        date_ranges={
            "traditional": "February 1-2",
            "new_calendar": "Twilight (January 23 - February 19)",
            "astronomical": "Midway between Winter Solstice and Spring Equinox"
        }
    ),
    "The Spring Equinox": TarotCard(
        name="The Spring Equinox",
        card_type="Special",
        element=Element.ETHER,
        keywords=["balance", "renewal", "growth", "harmony"],
        description="Perfect balance between light and dark, representing cosmic harmony and renewal",
        image_description="A scale perfectly balanced between sun and moon, with new growth emerging",
        date_ranges={
            "traditional": "March 20-21",
            "new_calendar": "Year Day (March 20)",
            "astronomical": "Sun crosses celestial equator, equal day and night"
        }
    ),
    "The Beltane": TarotCard(
        name="The Beltane",
        card_type="Special",
        element=Element.ETHER,
        keywords=["union", "fertility", "passion", "creation"],
        description="The height of spring, representing the union of cosmic forces and creative power",
        image_description="A maypole of light connecting earth and sky, surrounded by cosmic flowers",
        date_ranges={
            "traditional": "May 1",
            "new_calendar": "Blossom (April 18 - May 15)",
            "astronomical": "Midway between Spring Equinox and Summer Solstice"
        }
    ),
    "The Summer Solstice": TarotCard(
        name="The Summer Solstice",
        card_type="Special",
        element=Element.ETHER,
        keywords=["power", "illumination", "manifestation", "abundance"],
        description="The longest day, representing the height of cosmic power and manifestation",
        image_description="A radiant sun at its zenith, surrounded by golden cosmic energy",
        date_ranges={
            "traditional": "June 20-21",
            "new_calendar": "Solis (June 13 - July 10)",
            "astronomical": "Sun at highest point in the sky, longest day"
        }
    ),
    "The Lughnasadh": TarotCard(
        name="The Lughnasadh",
        card_type="Special",
        element=Element.ETHER,
        keywords=["harvest", "gratitude", "sacrifice", "abundance"],
        description="The first harvest, representing cosmic abundance and the cycle of giving and receiving",
        image_description="A golden field under cosmic light, with stars forming a cornucopia",
        date_ranges={
            "traditional": "August 1",
            "new_calendar": "Ember (August 8 - September 4)",
            "astronomical": "Midway between Summer Solstice and Autumn Equinox"
        }
    ),
    "The Autumn Equinox": TarotCard(
        name="The Autumn Equinox",
        card_type="Special",
        element=Element.ETHER,
        keywords=["harvest", "reflection", "preparation", "balance"],
        description="Perfect balance between light and dark, representing cosmic harvest and preparation",
        image_description="A scale balanced between sun and moon, with falling leaves of starlight",
        date_ranges={
            "traditional": "September 22-23",
            "new_calendar": "Equinox (October 3 - October 30)",
            "astronomical": "Sun crosses celestial equator, equal day and night"
        }
    ),
    "The Samhain": TarotCard(
        name="The Samhain",
        card_type="Special",
        element=Element.ETHER,
        keywords=["transition", "ancestors", "mystery", "veil"],
        description="The thinning of the veil between worlds, representing cosmic transition and mystery",
        image_description="A thin veil of stars separating two realms, with meteor showers passing through",
        date_ranges={
            "traditional": "October 31 - November 1",
            "new_calendar": "Frost (October 31 - November 27)",
            "astronomical": "Midway between Autumn Equinox and Winter Solstice"
        }
    ),
    "The Solstice": TarotCard(
        name="The Solstice",
        card_type="Special",
        element=Element.ETHER,
        keywords=["balance", "transition", "cosmic alignment", "spiritual gateway"],
        description="The moment of perfect balance between light and dark, representing the connection between earthly and cosmic cycles.",
        image_description="A radiant sun balanced perfectly between two pillars of light and dark, with stars forming a gateway between worlds"
    ),
    "The Equinox": TarotCard(
        name="The Equinox",
        card_type="Special",
        element=Element.ETHER,
        keywords=["harmony", "equilibrium", "cosmic balance", "spiritual awakening"],
        description="The point of perfect equilibrium, where day and night are equal, representing cosmic harmony and spiritual awakening.",
        image_description="A balanced scale floating in space, with the sun and moon in perfect alignment"
    ),
    "The Eclipse": TarotCard(
        name="The Eclipse",
        card_type="Special",
        element=Element.ETHER,
        keywords=["transformation", "revelation", "cosmic alignment", "spiritual insight"],
        description="A moment of cosmic alignment where the ordinary becomes extraordinary, revealing hidden truths and spiritual insights.",
        image_description="A celestial alignment where one cosmic body passes in front of another, creating a ring of light"
    ),
    "The Void": TarotCard(
        name="The Void",
        card_type="Special",
        element=Element.ETHER,
        keywords=["transition", "potential", "cosmic space", "spiritual journey"],
        description="The space between constellations, representing the cosmic void and spiritual transitions between states of being.",
        image_description="An infinite starfield with a dark void at its center, surrounded by swirling cosmic energy"
    )
}

# Minor Arcana - Numbered Cards (Ace through 10) for each element
MINOR_ARCANA = {
    # Ether Suit
    "Ace of Ether": TarotCard(
        name="Ace of Ether",
        card_type=CardType.MINOR,
        element=Element.ETHER,
        keywords=["potential", "spirit", "cosmic connection", "transcendence"],
        description="The spark of spiritual awakening and cosmic connection",
        image_description="A single point of pure light in the void of space"
    ),
    "Two of Ether": TarotCard(
        name="Two of Ether",
        card_type=CardType.MINOR,
        element=Element.ETHER,
        keywords=["balance", "duality", "harmony", "alignment"],
        description="The balance between material and spiritual realms",
        image_description="Two points of light forming a perfect equilibrium"
    ),
    "Three of Ether": TarotCard(
        name="Three of Ether",
        card_type=CardType.MINOR,
        element=Element.ETHER,
        keywords=["manifestation", "creation", "trinity", "synthesis"],
        description="The manifestation of spiritual energy in the material world",
        image_description="Three points of light forming a perfect triangle"
    ),
    "Four of Ether": TarotCard(
        name="Four of Ether",
        card_type=CardType.MINOR,
        element=Element.ETHER,
        keywords=["stability", "foundation", "protection", "sacred space"],
        description="The creation of sacred space and spiritual stability",
        image_description="Four points of light forming a perfect square"
    ),

    # Fire Suit (Wands)
    "Ace of Fire": TarotCard(
        name="Ace of Fire",
        card_type=CardType.MINOR,
        element=Element.FIRE,
        keywords=["inspiration", "creativity", "spiritual spark", "cosmic fire"],
        description="The spark of creative fire and spiritual inspiration, representing the pure essence of fire energy.",
        image_description="A single flame burning in the void, surrounded by cosmic energy"
    ),
    "Two of Fire": TarotCard(
        name="Two of Fire",
        card_type=CardType.MINOR,
        element=Element.FIRE,
        keywords=["planning", "discovery", "future vision"],
        description="The first steps of creative planning",
        image_description="Two flames dancing together in harmony"
    ),
    "Three of Fire": TarotCard(
        name="Three of Fire",
        card_type=CardType.MINOR,
        element=Element.FIRE,
        keywords=["expansion", "growth", "exploration"],
        description="The expansion of creative energy",
        image_description="Three flames forming a triangle of light"
    ),
    "Four of Fire": TarotCard(
        name="Four of Fire",
        card_type=CardType.MINOR,
        element=Element.FIRE,
        keywords=["celebration", "harmony", "completion"],
        description="The manifestation of creative success",
        image_description="Four flames creating a stable square of light"
    ),
    "Five of Fire": TarotCard(
        name="Five of Fire",
        card_type=CardType.MINOR,
        element=Element.FIRE,
        keywords=["competition", "conflict", "growth"],
        description="The challenge of creative conflict",
        image_description="Five flames dancing in chaotic patterns"
    ),
    "Six of Fire": TarotCard(
        name="Six of Fire",
        card_type=CardType.MINOR,
        element=Element.FIRE,
        keywords=["victory", "recognition", "pride"],
        description="The triumph of creative success",
        image_description="Six flames forming a victorious crown"
    ),
    "Seven of Fire": TarotCard(
        name="Seven of Fire",
        card_type=CardType.MINOR,
        element=Element.FIRE,
        keywords=["challenge", "courage", "determination"],
        description="The defense of creative vision",
        image_description="Seven flames forming a protective barrier"
    ),
    "Eight of Fire": TarotCard(
        name="Eight of Fire",
        card_type=CardType.MINOR,
        element=Element.FIRE,
        keywords=["speed", "movement", "action"],
        description="The swift progress of creative energy",
        image_description="Eight flames streaking across the cosmos"
    ),
    "Nine of Fire": TarotCard(
        name="Nine of Fire",
        card_type=CardType.MINOR,
        element=Element.FIRE,
        keywords=["resilience", "persistence", "strength"],
        description="The endurance of creative force",
        image_description="Nine flames standing strong against darkness"
    ),
    "Ten of Fire": TarotCard(
        name="Ten of Fire",
        card_type=CardType.MINOR,
        element=Element.FIRE,
        keywords=["burden", "responsibility", "completion"],
        description="The culmination of creative work",
        image_description="Ten flames forming a complete circle"
    ),

    # Water Suit (Cups)
    "Ace of Water": TarotCard(
        name="Ace of Water",
        card_type=CardType.MINOR,
        element=Element.WATER,
        keywords=["intuition", "emotion", "spiritual flow", "cosmic waters"],
        description="The source of emotional wisdom and spiritual intuition, representing the pure essence of water energy.",
        image_description="A single drop of water suspended in space, reflecting the cosmos"
    ),
    "Two of Water": TarotCard(
        name="Two of Water",
        card_type=CardType.MINOR,
        element=Element.WATER,
        keywords=["connection", "partnership", "harmony"],
        description="The flow of emotional connection",
        image_description="Two streams merging into one"
    ),
    "Three of Water": TarotCard(
        name="Three of Water",
        card_type=CardType.MINOR,
        element=Element.WATER,
        keywords=["celebration", "joy", "community"],
        description="The celebration of emotional bonds",
        image_description="Three fountains creating a rainbow"
    ),
    "Four of Water": TarotCard(
        name="Four of Water",
        card_type=CardType.MINOR,
        element=Element.WATER,
        keywords=["contemplation", "meditation", "apathy"],
        description="The stillness of emotional reflection",
        image_description="Four pools reflecting the stars"
    ),
    "Five of Water": TarotCard(
        name="Five of Water",
        card_type=CardType.MINOR,
        element=Element.WATER,
        keywords=["loss", "grief", "healing"],
        description="The healing of emotional wounds",
        image_description="Five streams falling into darkness"
    ),
    "Six of Water": TarotCard(
        name="Six of Water",
        card_type=CardType.MINOR,
        element=Element.WATER,
        keywords=["nostalgia", "memories", "innocence"],
        description="The return to emotional simplicity",
        image_description="Six pools reflecting past moments"
    ),
    "Seven of Water": TarotCard(
        name="Seven of Water",
        card_type=CardType.MINOR,
        element=Element.WATER,
        keywords=["choices", "imagination", "illusion"],
        description="The exploration of emotional possibilities",
        image_description="Seven cosmic pools showing different visions"
    ),
    "Eight of Water": TarotCard(
        name="Eight of Water",
        card_type=CardType.MINOR,
        element=Element.WATER,
        keywords=["journey", "seeking", "moving on"],
        description="The quest for emotional truth",
        image_description="Eight streams flowing to new horizons"
    ),
    "Nine of Water": TarotCard(
        name="Nine of Water",
        card_type=CardType.MINOR,
        element=Element.WATER,
        keywords=["satisfaction", "wishes", "contentment"],
        description="The fulfillment of emotional desires",
        image_description="Nine fountains granting cosmic wishes"
    ),
    "Ten of Water": TarotCard(
        name="Ten of Water",
        card_type=CardType.MINOR,
        element=Element.WATER,
        keywords=["harmony", "joy", "completion"],
        description="The perfection of emotional bliss",
        image_description="Ten pools creating a rainbow bridge"
    ),

    # Air Suit (Swords)
    "Ace of Air": TarotCard(
        name="Ace of Air",
        card_type=CardType.MINOR,
        element=Element.AIR,
        keywords=["thought", "clarity", "spiritual insight", "cosmic winds"],
        description="The breath of divine inspiration and spiritual clarity, representing the pure essence of air energy.",
        image_description="A swirling vortex of cosmic winds carrying stardust"
    ),
    "Two of Air": TarotCard(
        name="Two of Air",
        card_type=CardType.MINOR,
        element=Element.AIR,
        keywords=["decision", "balance", "stalemate"],
        description="The moment of choice and consideration",
        image_description="Two winds meeting in perfect balance"
    ),
    "Three of Air": TarotCard(
        name="Three of Air",
        card_type=CardType.MINOR,
        element=Element.AIR,
        keywords=["clarity", "truth", "revelation"],
        description="The revelation of difficult truths",
        image_description="Three lightning bolts illuminating the sky"
    ),
    "Four of Air": TarotCard(
        name="Four of Air",
        card_type=CardType.MINOR,
        element=Element.AIR,
        keywords=["rest", "recovery", "contemplation"],
        description="The stillness of mental peace",
        image_description="Four winds creating a peaceful sanctuary"
    ),
    "Five of Air": TarotCard(
        name="Five of Air",
        card_type=CardType.MINOR,
        element=Element.AIR,
        keywords=["conflict", "defeat", "learning"],
        description="The challenge of mental strife",
        image_description="Five harsh winds clashing in space"
    ),
    "Six of Air": TarotCard(
        name="Six of Air",
        card_type=CardType.MINOR,
        element=Element.AIR,
        keywords=["transition", "healing", "movement"],
        description="The journey to mental clarity",
        image_description="Six gentle winds guiding a cosmic journey"
    ),
    "Seven of Air": TarotCard(
        name="Seven of Air",
        card_type=CardType.MINOR,
        element=Element.AIR,
        keywords=["strategy", "preparation", "caution"],
        description="The planning of mental action",
        image_description="Seven winds weaving complex patterns"
    ),
    "Eight of Air": TarotCard(
        name="Eight of Air",
        card_type=CardType.MINOR,
        element=Element.AIR,
        keywords=["limitation", "restriction", "perspective"],
        description="The boundaries of mental perception",
        image_description="Eight winds forming a limiting cage"
    ),
    "Nine of Air": TarotCard(
        name="Nine of Air",
        card_type=CardType.MINOR,
        element=Element.AIR,
        keywords=["anxiety", "fear", "awakening"],
        description="The confrontation of mental fears",
        image_description="Nine winds swirling in nightmarish forms"
    ),
    "Ten of Air": TarotCard(
        name="Ten of Air",
        card_type=CardType.MINOR,
        element=Element.AIR,
        keywords=["ending", "rebirth", "transformation"],
        description="The completion of mental cycles",
        image_description="Ten winds clearing away the old"
    ),

    # Earth Suit (Pentacles)
    "Ace of Earth": TarotCard(
        name="Ace of Earth",
        card_type=CardType.MINOR,
        element=Element.EARTH,
        keywords=["manifestation", "abundance", "spiritual grounding", "cosmic earth"],
        description="The seed of material manifestation and spiritual grounding, representing the pure essence of earth energy.",
        image_description="A single crystal floating in space, radiating with cosmic energy"
    ),
    "Two of Earth": TarotCard(
        name="Two of Earth",
        card_type=CardType.MINOR,
        element=Element.EARTH,
        keywords=["balance", "adaptation", "juggling"],
        description="The dance of material balance",
        image_description="Two planets orbiting in harmony"
    ),
    "Three of Earth": TarotCard(
        name="Three of Earth",
        card_type=CardType.MINOR,
        element=Element.EARTH,
        keywords=["mastery", "collaboration", "skill"],
        description="The foundation of material creation",
        image_description="Three crystals forming a stable foundation"
    ),
    "Four of Earth": TarotCard(
        name="Four of Earth",
        card_type=CardType.MINOR,
        element=Element.EARTH,
        keywords=["security", "possession", "stability"],
        description="The foundation of material security",
        image_description="Four crystals forming a solid foundation"
    ),
    "Five of Earth": TarotCard(
        name="Five of Earth",
        card_type=CardType.MINOR,
        element=Element.EARTH,
        keywords=["hardship", "challenge", "perseverance"],
        description="The test of material resources",
        image_description="Five crystals dimmed by cosmic dust"
    ),
    "Six of Earth": TarotCard(
        name="Six of Earth",
        card_type=CardType.MINOR,
        element=Element.EARTH,
        keywords=["generosity", "balance", "sharing"],
        description="The flow of material abundance",
        image_description="Six crystals sharing their light"
    ),
    "Seven of Earth": TarotCard(
        name="Seven of Earth",
        card_type=CardType.MINOR,
        element=Element.EARTH,
        keywords=["patience", "evaluation", "investment"],
        description="The growth of material projects",
        image_description="Seven crystals slowly growing in power"
    ),
    "Eight of Earth": TarotCard(
        name="Eight of Earth",
        card_type=CardType.MINOR,
        element=Element.EARTH,
        keywords=["skill", "mastery", "dedication"],
        description="The development of material expertise",
        image_description="Eight crystals being carefully crafted"
    ),
    "Nine of Earth": TarotCard(
        name="Nine of Earth",
        card_type=CardType.MINOR,
        element=Element.EARTH,
        keywords=["abundance", "luxury", "self-reliance"],
        description="The achievement of material success",
        image_description="Nine crystals in a garden of plenty"
    ),
    "Ten of Earth": TarotCard(
        name="Ten of Earth",
        card_type=CardType.MINOR,
        element=Element.EARTH,
        keywords=["wealth", "completion", "legacy"],
        description="The manifestation of material abundance",
        image_description="Ten crystals forming a perfect matrix"
    ),
}

# Court Cards for each element
COURT_CARDS = {
    # Fire Court
    "Page of Fire": TarotCard(
        name="Page of Fire",
        card_type=CardType.COURT,
        element=Element.FIRE,
        keywords=["enthusiasm", "exploration", "curiosity"],
        description="The spark of new ideas and passion",
        image_description="A young figure holding a torch of cosmic fire"
    ),
    "Knight of Fire": TarotCard(
        name="Knight of Fire",
        card_type=CardType.COURT,
        element=Element.FIRE,
        keywords=["action", "adventure", "passion"],
        description="The force of creative action",
        image_description="A warrior riding a chariot of flames"
    ),
    "Queen of Fire": TarotCard(
        name="Queen of Fire",
        card_type=CardType.COURT,
        element=Element.FIRE,
        keywords=["passion", "creativity", "spiritual wisdom", "cosmic grace"],
        description="The embodiment of fire's creative power, representing spiritual passion and cosmic wisdom.",
        image_description="A graceful figure surrounded by dancing flames, wearing a crown of stars"
    ),
    "King of Fire": TarotCard(
        name="King of Fire",
        card_type=CardType.COURT,
        element=Element.FIRE,
        keywords=["leadership", "inspiration", "spiritual mastery", "cosmic authority"],
        description="The master of fire energy, representing spiritual leadership and cosmic inspiration.",
        image_description="A regal figure wreathed in cosmic flames, holding a staff of pure fire"
    ),

    # Water Court
    "Page of Water": TarotCard(
        name="Page of Water",
        card_type=CardType.COURT,
        element=Element.WATER,
        keywords=["intuition", "sensitivity", "messages"],
        description="The beginning of emotional awareness",
        image_description="A young figure by a cosmic ocean"
    ),
    "Knight of Water": TarotCard(
        name="Knight of Water",
        card_type=CardType.COURT,
        element=Element.WATER,
        keywords=["romance", "charm", "imagination"],
        description="The pursuit of emotional truth",
        image_description="A knight riding waves of starlight"
    ),
    "Queen of Water": TarotCard(
        name="Queen of Water",
        card_type=CardType.COURT,
        element=Element.WATER,
        keywords=["emotion", "psychic", "spiritual grace", "cosmic tides"],
        description="The embodiment of water's emotional depth, representing spiritual sensitivity and cosmic flow.",
        image_description="A graceful figure floating in cosmic waters, wearing a crown of moonstones"
    ),
    "King of Water": TarotCard(
        name="King of Water",
        card_type=CardType.COURT,
        element=Element.WATER,
        keywords=["wisdom", "intuition", "spiritual depth", "cosmic flow"],
        description="The master of water energy, representing spiritual wisdom and cosmic intuition.",
        image_description="A regal figure emerging from cosmic waters, holding a chalice of stars"
    ),

    # Air Court
    "Page of Air": TarotCard(
        name="Page of Air",
        card_type=CardType.COURT,
        element=Element.AIR,
        keywords=["curiosity", "learning", "communication"],
        description="The beginning of mental clarity",
        image_description="A young figure in swirling cosmic winds"
    ),
    "Knight of Air": TarotCard(
        name="Knight of Air",
        card_type=CardType.COURT,
        element=Element.AIR,
        keywords=["action", "intelligence", "truth"],
        description="The pursuit of mental clarity",
        image_description="A knight soaring through stellar winds"
    ),
    "Queen of Air": TarotCard(
        name="Queen of Air",
        card_type=CardType.COURT,
        element=Element.AIR,
        keywords=["thought", "communication", "spiritual insight", "cosmic breeze"],
        description="The embodiment of air's intellectual power, representing spiritual communication and cosmic insight.",
        image_description="A graceful figure floating on cosmic winds, wearing a crown of clouds"
    ),
    "King of Air": TarotCard(
        name="King of Air",
        card_type=CardType.COURT,
        element=Element.AIR,
        keywords=["intellect", "clarity", "spiritual vision", "cosmic winds"],
        description="The master of air energy, representing spiritual intellect and cosmic clarity.",
        image_description="A regal figure standing in cosmic winds, holding a sword of pure light"
    ),

    # Earth Court
    "Page of Earth": TarotCard(
        name="Page of Earth",
        card_type=CardType.COURT,
        element=Element.EARTH,
        keywords=["study", "practicality", "manifestation"],
        description="The beginning of material wisdom",
        image_description="A young figure studying cosmic crystals"
    ),
    "Knight of Earth": TarotCard(
        name="Knight of Earth",
        card_type=CardType.COURT,
        element=Element.EARTH,
        keywords=["responsibility", "routine", "commitment"],
        description="The pursuit of material goals",
        image_description="A knight traversing asteroid fields"
    ),
    "Queen of Earth": TarotCard(
        name="Queen of Earth",
        card_type=CardType.COURT,
        element=Element.EARTH,
        keywords=["abundance", "nurturing", "spiritual growth", "cosmic garden"],
        description="The embodiment of earth's nurturing power, representing spiritual practicality and cosmic growth.",
        image_description="A graceful figure standing in a cosmic garden, wearing a crown of crystals"
    ),
    "King of Earth": TarotCard(
        name="King of Earth",
        card_type=CardType.COURT,
        element=Element.EARTH,
        keywords=["stability", "abundance", "spiritual foundation", "cosmic earth"],
        description="The master of earth energy, representing spiritual stability and cosmic abundance.",
        image_description="A regal figure standing on cosmic earth, holding a globe of stars"
    )
}

# New Tarot Spreads
TAROT_SPREADS = {
    "Constellation Path": {
        "num_cards": 3,
        "description": "A three-card spread showing past, present, and future through the constellations"
    },
    "Elemental Cross": {
        "num_cards": 4,
        "description": "A four-card spread exploring the influence of each element"
    },
    "Solar Journey": {
        "num_cards": 7,
        "description": "A seven-card spread following the sun's path through the zodiac"
    },
    "Cosmic Mirror": {
        "num_cards": 5,
        "description": "A five-card spread reflecting the relationship between microcosm and macrocosm"
    },
    "Great Year Cycle": {
        "num_cards": 13,
        "description": "A comprehensive spread using all 13 constellation cards"
    }
}

def get_card_by_constellation(constellation: str) -> Optional[TarotCard]:
    """Get the tarot card associated with a specific constellation."""
    for card in MAJOR_ARCANA.values():
        if card.constellation == constellation:
            return card
    return None

def get_cards_by_duration(min_days: int, max_days: int) -> List[TarotCard]:
    """Get cards associated with constellations of specific duration ranges."""
    return [
        card for card in MAJOR_ARCANA.values()
        if card.duration_days and min_days <= card.duration_days <= max_days
    ]

def get_special_cards_for_date(date: datetime) -> List[TarotCard]:
    """Get special cards relevant to a specific date in the 13-month calendar."""
    from .calendar import SolarCalendar
    from .astronomy import AstronomicalEvents
    
    calendar = SolarCalendar()
    astronomy = AstronomicalEvents()
    
    relevant_cards = []
    year = date.year
    
    # Get all astronomical events for the year
    events = astronomy._get_equinox_solstice_events(
        datetime(year, 1, 1, tzinfo=pytz.UTC),
        datetime(year, 12, 31, tzinfo=pytz.UTC)
    )
    cross_quarters = astronomy.get_cross_quarter_dates(year)
    all_events = events + cross_quarters
    
    # Check if the date is close to any astronomical event
    for event in all_events:
        event_date = event['date']
        # Consider events within 3 days of the given date
        if abs((date - event_date).days) <= 3:
            card_name = f"The {event['name']}"
            if card_name in SPECIAL_CARDS:
                card = SPECIAL_CARDS[card_name]
                # Update the date_ranges to include the actual astronomical date
                if hasattr(card, 'date_ranges'):
                    card.date_ranges['astronomical'] = f"Actual date: {event_date.strftime('%B %d, %Y')}"
                relevant_cards.append(card)
    
    return relevant_cards 