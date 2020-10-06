from libqtile import bar, widget

from settings.theme import colors

def base(bg = "dark",
         fg = "light"):
    return {
        "background" : colors[bg], 
        "foreground" : colors[fg]
    }

def group_box_defautl(fontsize = 30):
    return {
        "fontsize" : fontsize,
        "font" : "Lekton",
        "border" : colors["dark"],
        "padding" : 5,
    }

def icon(bg = "dark",
         fg = "light",
         fontsize = 16,
         font = "Lekton",
         text = "?"):
    return widget.TextBox(
        **base(bg, fg),
        fontsize = fontsize,
        font = font,
        text = text,
        padding = 3
    )

def separator(bg = "dark",
              fg = "light",
              padding = 5):
    return widget.Sep(
        **base(bg, fg),
        linewidth = 0,
        padding = padding
    )

# Widgets para la pantalla principal

primary_screen_widgets = [

    widget.AGroupBox(
        **base(),
        **group_box_defautl()
    ),

    widget.Spacer(
        **base(),
        length = bar.STRETCH
    ),

    icon(
        fg="light",
        bg="dark",
        fontsize=20, 
        text=""
    ),

    widget.CheckUpdates(
        **base(),
        font = "Inconsolata Bold",
        fontsize = 14,
        display_format = "{updates}",
        no_update_string = "0",
        update_interval = 60
    ),

    separator(),

    widget.Clock(
        **base(),
        format = "%a %d/%m%Y - %I:%M %P",
        font = "Inconsolata Bold",
        fontsize = 14,
        padding = 5
    ),

    icon(
        bg = "dark",
        fg = "light",
        fontsize = 36,
        text = ""
    ),

    separator(),
]

# Widgets para la pantalla secundaria

secondary_screen_widgets = [

    widget.AGroupBox(
        **base(),
        **group_box_defautl(fontsize = 26)
    ),

    widget.Spacer(
        **base(),
        length = bar.STRETCH
    ),

    icon(
        bg = "dark",
        fg = "light",
        fontsize = 30,
        text = ""
    ),

    separator(),   
]

# Configuraciones estándar

widget_defaults = dict(
    font='Inconsolata',
    fontsize=16,
    padding=3,
)

extension_defaults = widget_defaults.copy()
