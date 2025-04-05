"""
Magical System Integration
Combines Regardie's Tree of Life teachings with astronomical calculations
and consciousness development practices.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime
import pytz
from .calendar import SolarCalendar
from .tarot_system import TarotCard, Element, get_card_by_constellation
from .consciousness_system import ConsciousnessLevel, BarrierType

class Sephirah(Enum):
    KETER = "Crown"
    CHOKHMAH = "Wisdom"
    BINAH = "Understanding"
    CHESED = "Mercy"
    GEVURAH = "Severity"
    TIFERET = "Beauty"
    NETZACH = "Victory"
    HOD = "Splendor"
    YESOD = "Foundation"
    MALKUTH = "Kingdom"

class MagicalPractice(Enum):
    MEDITATION = "Meditation"
    VISUALIZATION = "Visualization"
    RITUAL = "Ritual"
    BREATHWORK = "Breathwork"
    DIVINATION = "Divination"
    ALCHEMY = "Alchemy"

@dataclass
class TreeOfLifePath:
    sephirah: Sephirah
    element: Element
    tarot_card: str
    consciousness_level: ConsciousnessLevel
    barrier: BarrierType
    magical_practices: List[MagicalPractice]
    description: str
    keywords: List[str]
    hebrew_letter: str
    color: str
    symbol: str

class MagicalSystem:
    def __init__(self):
        self.calendar = SolarCalendar()
        
        # Initialize Tree of Life paths
        self.paths = {
            Sephirah.KETER: TreeOfLifePath(
                sephirah=Sephirah.KETER,
                element=Element.ETHER,
                tarot_card="The Fool",
                consciousness_level=ConsciousnessLevel.COSMIC,
                barrier=BarrierType.IGNORANCE,
                magical_practices=[MagicalPractice.MEDITATION, MagicalPractice.VISUALIZATION],
                description="The Crown - Pure consciousness and divine unity",
                keywords=["unity", "divine will", "pure consciousness", "transcendence"],
                hebrew_letter="א",
                color="White",
                symbol="∞"
            ),
            Sephirah.CHOKHMAH: TreeOfLifePath(
                sephirah=Sephirah.CHOKHMAH,
                element=Element.FIRE,
                tarot_card="The Magician",
                consciousness_level=ConsciousnessLevel.SPIRITUAL,
                barrier=BarrierType.SEPARATION,
                magical_practices=[MagicalPractice.RITUAL, MagicalPractice.BREATHWORK],
                description="Wisdom - The first flash of divine light",
                keywords=["wisdom", "inspiration", "divine spark", "creation"],
                hebrew_letter="ב",
                color="Gray",
                symbol="⚡"
            ),
            Sephirah.BINAH: TreeOfLifePath(
                sephirah=Sephirah.BINAH,
                element=Element.WATER,
                tarot_card="The High Priestess",
                consciousness_level=ConsciousnessLevel.MENTAL,
                barrier=BarrierType.ATTACHMENT,
                magical_practices=[MagicalPractice.DIVINATION, MagicalPractice.MEDITATION],
                description="Understanding - The receptive principle of creation",
                keywords=["understanding", "receptivity", "form", "limitation"],
                hebrew_letter="ג",
                color="Black",
                symbol="☽"
            ),
            Sephirah.CHESED: TreeOfLifePath(
                sephirah=Sephirah.CHESED,
                element=Element.WATER,
                tarot_card="The Empress",
                consciousness_level=ConsciousnessLevel.EMOTIONAL,
                barrier=BarrierType.FEAR,
                magical_practices=[MagicalPractice.RITUAL, MagicalPractice.ALCHEMY],
                description="Mercy - The expansive force of divine love",
                keywords=["mercy", "love", "expansion", "abundance"],
                hebrew_letter="ד",
                color="Blue",
                symbol="💙"
            ),
            Sephirah.GEVURAH: TreeOfLifePath(
                sephirah=Sephirah.GEVURAH,
                element=Element.FIRE,
                tarot_card="The Tower",
                consciousness_level=ConsciousnessLevel.PHYSICAL,
                barrier=BarrierType.RESISTANCE,
                magical_practices=[MagicalPractice.RITUAL, MagicalPractice.BREATHWORK],
                description="Severity - The restrictive force of divine judgment",
                keywords=["severity", "strength", "discipline", "limitation"],
                hebrew_letter="ה",
                color="Red",
                symbol="⚔️"
            ),
            Sephirah.TIFERET: TreeOfLifePath(
                sephirah=Sephirah.TIFERET,
                element=Element.AIR,
                tarot_card="The Sun",
                consciousness_level=ConsciousnessLevel.SPIRITUAL,
                barrier=BarrierType.SEPARATION,
                magical_practices=[MagicalPractice.MEDITATION, MagicalPractice.VISUALIZATION],
                description="Beauty - The harmonizing principle of balance",
                keywords=["beauty", "harmony", "balance", "integration"],
                hebrew_letter="ו",
                color="Yellow",
                symbol="☀️"
            ),
            Sephirah.NETZACH: TreeOfLifePath(
                sephirah=Sephirah.NETZACH,
                element=Element.FIRE,
                tarot_card="The Star",
                consciousness_level=ConsciousnessLevel.EMOTIONAL,
                barrier=BarrierType.ATTACHMENT,
                magical_practices=[MagicalPractice.RITUAL, MagicalPractice.ALCHEMY],
                description="Victory - The enduring force of divine persistence",
                keywords=["victory", "endurance", "passion", "persistence"],
                hebrew_letter="ז",
                color="Green",
                symbol="🌿"
            ),
            Sephirah.HOD: TreeOfLifePath(
                sephirah=Sephirah.HOD,
                element=Element.WATER,
                tarot_card="The Moon",
                consciousness_level=ConsciousnessLevel.MENTAL,
                barrier=BarrierType.IGNORANCE,
                magical_practices=[MagicalPractice.DIVINATION, MagicalPractice.VISUALIZATION],
                description="Splendor - The intellectual force of divine communication",
                keywords=["splendor", "communication", "intellect", "magic"],
                hebrew_letter="ח",
                color="Orange",
                symbol="🌙"
            ),
            Sephirah.YESOD: TreeOfLifePath(
                sephirah=Sephirah.YESOD,
                element=Element.AIR,
                tarot_card="The World",
                consciousness_level=ConsciousnessLevel.PHYSICAL,
                barrier=BarrierType.FEAR,
                magical_practices=[MagicalPractice.RITUAL, MagicalPractice.BREATHWORK],
                description="Foundation - The connecting force of divine manifestation",
                keywords=["foundation", "manifestation", "connection", "dreams"],
                hebrew_letter="ט",
                color="Purple",
                symbol="🌍"
            ),
            Sephirah.MALKUTH: TreeOfLifePath(
                sephirah=Sephirah.MALKUTH,
                element=Element.EARTH,
                tarot_card="The World",
                consciousness_level=ConsciousnessLevel.PHYSICAL,
                barrier=BarrierType.RESISTANCE,
                magical_practices=[MagicalPractice.RITUAL, MagicalPractice.ALCHEMY],
                description="Kingdom - The material manifestation of divine presence",
                keywords=["kingdom", "manifestation", "matter", "earth"],
                hebrew_letter="ת",
                color="Brown",
                symbol="🏰"
            )
        }

    def get_path_for_date(self, date: datetime = None) -> TreeOfLifePath:
        """Get the most appropriate Tree of Life path for a given date."""
        if date is None:
            date = datetime.now(pytz.UTC)
            
        # Get current astronomical conditions
        constellation = self.calendar.get_current_constellation()
        
        # Match path to current constellation's card
        constellation_card = get_card_by_constellation(constellation)
        
        if constellation_card:
            for path in self.paths.values():
                if path.tarot_card == constellation_card.name:
                    return path
                
        # Default to Tiferet if no specific match
        return self.paths[Sephirah.TIFERET]

    def get_practice_for_path(self, sephirah: Sephirah) -> List[MagicalPractice]:
        """Get the magical practices associated with a specific Sephirah."""
        return self.paths[sephirah].magical_practices

    def get_consciousness_work(self, sephirah: Sephirah) -> Dict:
        """Get the consciousness work associated with a specific Sephirah."""
        path = self.paths[sephirah]
        return {
            "level": path.consciousness_level,
            "barrier": path.barrier,
            "practices": path.magical_practices,
            "keywords": path.keywords
        }

    def get_path_progression(self, current_sephirah: Sephirah) -> List[Sephirah]:
        """Get the recommended progression through the Tree of Life."""
        sephirot_order = [
            Sephirah.MALKUTH,
            Sephirah.YESOD,
            Sephirah.HOD,
            Sephirah.NETZACH,
            Sephirah.TIFERET,
            Sephirah.GEVURAH,
            Sephirah.CHESED,
            Sephirah.BINAH,
            Sephirah.CHOKHMAH,
            Sephirah.KETER
        ]
        
        current_index = sephirot_order.index(current_sephirah)
        return sephirot_order[current_index:]

    def get_ritual_timing(self, sephirah: Sephirah) -> Dict:
        """Get the optimal timing for rituals based on the Sephirah."""
        path = self.paths[sephirah]
        return {
            "element": path.element,
            "color": path.color,
            "symbol": path.symbol,
            "hebrew_letter": path.hebrew_letter,
            "best_time": self._get_best_time_for_element(path.element)
        }

    def _get_best_time_for_element(self, element: Element) -> str:
        """Get the best time of day for working with a specific element."""
        element_times = {
            Element.ETHER: "dawn",
            Element.FIRE: "noon",
            Element.WATER: "sunset",
            Element.AIR: "midnight",
            Element.EARTH: "midnight"
        }
        return element_times.get(element, "dawn") 