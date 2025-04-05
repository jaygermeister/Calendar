"""
Consciousness Development System
Integrates precise astronomical calculations with spiritual correspondences
for personal growth and higher consciousness development.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime, timedelta
import pytz
from .calendar import SolarCalendar
from .tarot_system import TarotCard, Element

class ConsciousnessLevel(Enum):
    PHYSICAL = "Physical Awareness"
    EMOTIONAL = "Emotional Intelligence"
    MENTAL = "Mental Clarity"
    SPIRITUAL = "Spiritual Connection"
    COSMIC = "Cosmic Consciousness"

class BarrierType(Enum):
    FEAR = "Fear and Limitation"
    ATTACHMENT = "Attachment and Desire"
    IGNORANCE = "Ignorance and Confusion"
    SEPARATION = "Separation and Division"
    RESISTANCE = "Resistance to Change"

@dataclass
class ConsciousnessPractice:
    name: str
    level: ConsciousnessLevel
    barrier: BarrierType
    description: str
    duration_minutes: int
    astronomical_timing: Dict[str, str]
    tarot_cards: List[str]

class ConsciousnessSystem:
    def __init__(self):
        self.calendar = SolarCalendar()
        
        # Practices aligned with astronomical events
        self.practices = {
            "Dawn Meditation": ConsciousnessPractice(
                name="Dawn Meditation",
                level=ConsciousnessLevel.SPIRITUAL,
                barrier=BarrierType.IGNORANCE,
                description="Connect with the rising sun's energy for clarity and new beginnings",
                duration_minutes=30,
                astronomical_timing={
                    "best_time": "sunrise",
                    "constellation": "Aries",
                    "phase": "new_moon"
                },
                tarot_cards=["The Healer", "The Transformation"]
            ),
            "Solar Integration": ConsciousnessPractice(
                name="Solar Integration",
                level=ConsciousnessLevel.COSMIC,
                barrier=BarrierType.SEPARATION,
                description="Align with solar energy for cosmic consciousness expansion",
                duration_minutes=45,
                astronomical_timing={
                    "best_time": "solar_noon",
                    "constellation": "Leo",
                    "phase": "full_moon"
                },
                tarot_cards=["The Sun", "The Star"]
            ),
            "Lunar Reflection": ConsciousnessPractice(
                name="Lunar Reflection",
                level=ConsciousnessLevel.EMOTIONAL,
                barrier=BarrierType.ATTACHMENT,
                description="Work with lunar cycles for emotional healing and release",
                duration_minutes=60,
                astronomical_timing={
                    "best_time": "moonrise",
                    "constellation": "Cancer",
                    "phase": "waning_moon"
                },
                tarot_cards=["The Moon", "The High Priestess"]
            ),
            "Stellar Gateway": ConsciousnessPractice(
                name="Stellar Gateway",
                level=ConsciousnessLevel.COSMIC,
                barrier=BarrierType.FEAR,
                description="Connect with stellar energies for cosmic consciousness expansion",
                duration_minutes=90,
                astronomical_timing={
                    "best_time": "midnight",
                    "constellation": "Ophiuchus",
                    "phase": "new_moon"
                },
                tarot_cards=["The Star", "The World"]
            )
        }
        
        # Consciousness development paths
        self.development_paths = {
            "Elemental Mastery": {
                "description": "Master the elements within and without",
                "practices": ["Dawn Meditation", "Solar Integration"],
                "barriers": [BarrierType.FEAR, BarrierType.ATTACHMENT]
            },
            "Cosmic Connection": {
                "description": "Develop direct connection with cosmic consciousness",
                "practices": ["Stellar Gateway", "Solar Integration"],
                "barriers": [BarrierType.SEPARATION, BarrierType.RESISTANCE]
            },
            "Emotional Alchemy": {
                "description": "Transform emotional patterns through lunar work",
                "practices": ["Lunar Reflection", "Dawn Meditation"],
                "barriers": [BarrierType.ATTACHMENT, BarrierType.IGNORANCE]
            }
        }

    def get_practice_for_date(self, date: datetime = None) -> ConsciousnessPractice:
        """Get the most appropriate consciousness practice for a given date."""
        if date is None:
            date = datetime.now(pytz.UTC)
            
        # Get current astronomical conditions
        constellation = self.calendar.get_current_constellation()
        events = self.calendar.get_upcoming_events(days_ahead=1)
        
        # Match practice to current conditions
        for practice in self.practices.values():
            if practice.astronomical_timing["constellation"] == constellation:
                return practice
                
        # Default to Dawn Meditation if no specific match
        return self.practices["Dawn Meditation"]

    def get_development_path(self, barrier: BarrierType) -> Dict:
        """Get the most appropriate development path for overcoming a specific barrier."""
        for path_name, path_data in self.development_paths.items():
            if barrier in path_data["barriers"]:
                return {
                    "name": path_name,
                    **path_data
                }
        return None

    def get_practice_schedule(self, days: int = 7) -> List[Dict]:
        """Get a schedule of practices for the next specified number of days."""
        schedule = []
        current_date = datetime.now(pytz.UTC)
        
        for i in range(days):
            date = current_date + timedelta(days=i)
            practice = self.get_practice_for_date(date)
            schedule.append({
                "date": date,
                "practice": practice.name,
                "timing": practice.astronomical_timing,
                "description": practice.description
            })
            
        return schedule 