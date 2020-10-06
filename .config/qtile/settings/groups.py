from libqtile.config import Group, Key
from libqtile.lazy import lazy

from settings.keys import keys

mod = "mod4"

# Declaro nos nombres de los grupos
groups_names = ["", "", "", ""]

# Declaro el orden de los keybinds
key_binds = ["z", "x", "c", "v"]

# Genero los grupos
groups = [Group(name) for name in groups_names]

for order, group in enumerate(groups):

    current_key_bind = key_binds[order]

    keys.extend([
        # Cambiar al grupo de trabajo [order]
        Key([mod],
            current_key_bind,
            lazy.group[group.name].toscreen()
            ),
        # Mover ventana al grupo de trabajo [order]
        Key([mod, "shift"],
            current_key_bind,
            lazy.window.togroup(group.name)
            )
    ])

