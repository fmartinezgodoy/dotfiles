from libqtile.config import Click, Drag
from libqtile.lazy import lazy

mod = "mod4"

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
        desc="Arrastrar ventana"),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
        desc="Modificar tamaño de ventana"),
    Click([mod], "Button2", lazy.window.bring_to_front(),
        desc="Traer al frente")
]
