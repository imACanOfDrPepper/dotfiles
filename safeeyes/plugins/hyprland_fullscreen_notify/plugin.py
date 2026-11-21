import json
import subprocess

GAMING_KEYWORDS = [
        "tetr.io",
        "tetrio",
        "steam_app_",
        "gamescope",
        "minecraft",
        ]

def should_use_notification():
    try:
        output = subprocess.check_output(["hyprctl", "activewindow", "-j"], text=True)
        data = json.loads(output)

        if bool(data.get("fullscreen", 0)):
            return True

        win_class = data.get("class", "").lower()
        win_title = data.get("title", "").lower()

        for keyword in GAMING_KEYWORDS:
            if keyword in win_class or keyword in win_title:
                return True

        return False
    except Exception:
        return False

def on_start_break(break_obj):
    if should_use_notification():
        duration = break_obj.duration
        is_long = break_obj.is_long_break()

        urgency = "critical" if is_long else "normal"
        title = "Safe Eyes — Long Break" if is_long else "Safe Eyes — Short Break"
        body = f"{break_obj.name} for {duration}s" if break_obj.name else f"Rest your eyes for {duration}s after this round!"

        subprocess.run([
            "notify-send",
            "-u", urgency,
            title,
            body
            ])
        return True
    return False
