from libqtile import bar
from libqtile.config import Screen

from settings.widgets import primary_screen_widgets, secondary_screen_widgets

screens = [
    Screen(top = bar.Bar(
        primary_screen_widgets,
        22,
        opacity = 0.96)
        ),
    Screen(top = bar.Bar(
        secondary_screen_widgets,
        18,
        opacity = 0.95)
        )
]
