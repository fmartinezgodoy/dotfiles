from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"
default_terminal = "alacritty"

keys = [

    # Qtile control
    Key([mod, "control"], "r", lazy.restart(),
        desc="Reiniciar qtile"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Cerrar qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Abrir cmd"),

    # Navegar entre ventanas del escritorio actual
    Key([mod], "j", lazy.layout.down(),
        desc="Desplazarse hacia abajo"),
    Key([mod], "k", lazy.layout.up(),
        desc="Desplazarse hacia arriba"),
    Key([mod], "h", lazy.layout.left(),
        desc="Desplazarse hacia la izquierda"),
    Key([mod], "l", lazy.layout.right(),
        desc="Desplazarse hacia la derecha"),

    # Mover ventanas dentro del escritorio actual
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Mover ventana hacia abajo"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Mover ventana hacia arriba"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Mover ventana hacia la izquierda"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Mover vantana hacia la derecha"),


    Key([mod], "Return", lazy.spawn(default_terminal),
        desc="Lanzar terminal"),

    # Cerrar ventana seleccionada
    Key([mod], "w", lazy.window.kill(), 
        desc="Cerrar la ventana seleccionada"),

    # Layouts
    Key([mod], "Tab", lazy.next_layout(),
        desc="Intercambiar layouts"),

    # Rofi
    Key([mod], "m", lazy.spawn("rofi -show drun"),
        desc="Lanzar menu de rofi"),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show"),
        desc="Lanzar multitarea de rofi"),
    
    # Ranger
    Key([mod], "e", lazy.spawn("ranger"),
        desc="Lanzar ranger"),

    # Binds de volumen
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"), 
        desc="Disminuir volumen con boton correspondiente del teclado"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        desc="Aumentar volumen con boton correspondiente del teclado"),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Mutear audio con boton correspondiente del teclado"),

    # Scrot (capturas de pantalla)
    Key([mod], "s", lazy.spawn("scrot '%Y-%m-%d_%I:%M:%S_$wx$h_scrot.png' -e 'mv $f ~/Images/Screenshots/'"),
        desc="Tomar captura de pantalla")
]
