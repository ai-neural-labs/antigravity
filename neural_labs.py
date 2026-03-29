#!/usr/bin/env python3
"""
neural_labs.py  —  Animated ASCII art: "Neural Labs"
Animations:  Loading bars  ▸  Matrix rain  ▸  Slide-in reveal
             Rainbow pulse  ▸  Network signal  ▸  Final splash
Works in: Windows Terminal, PowerShell, any ANSI true-color terminal.
"""

import time, sys, os, random, math

# ── Enable ANSI / VT100 on Windows ───────────────────────────────────────────
def _enable_ansi_windows():
    """Enable Virtual Terminal Processing so ANSI escape codes render correctly."""
    if sys.platform != "win32":
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # Get stdout handle (-11 = STD_OUTPUT_HANDLE)
        handle = kernel32.GetStdHandle(-11)
        # Get current mode
        mode = ctypes.c_ulong()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))
        # Add ENABLE_VIRTUAL_TERMINAL_PROCESSING (0x0004)
        kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except Exception:
        pass  # Non-fatal: colors just won't show in very old terminals

_enable_ansi_windows()

# ── ANSI helpers ──────────────────────────────────────────────────────────────
def rgb(r, g, b): return f"\033[38;2;{r};{g};{b}m"
RST  = "\033[0m"
BOLD = "\033[1m"
DIM  = "\033[2m"
HIDE = "\033[?25l"
SHOW = "\033[?25h"
CLR  = "\033[2J\033[H"

def w(s):
    sys.stdout.write(s); sys.stdout.flush()

def clr():
    w(CLR)

def grad(text, r1, g1, b1, r2, g2, b2):
    """Horizontal gradient across text."""
    n = max(len(text) - 1, 1)
    out = ""
    for i, ch in enumerate(text):
        t = i / n
        out += rgb(int(r1+(r2-r1)*t), int(g1+(g2-g1)*t), int(b1+(b2-b1)*t)) + ch
    return out + RST

def wave(text, frame, row=0):
    """Animated rainbow wave across text."""
    out = ""
    for i, ch in enumerate(text):
        a = (i * 0.18) + (frame * 0.22) + (row * 0.55)
        out += rgb(
            int(127 + 127 * math.sin(a)),
            int(127 + 127 * math.sin(a + 2.094)),
            int(127 + 127 * math.sin(a + 4.189)),
        ) + ch
    return out + RST

# ── ASCII art ─────────────────────────────────────────────────────────────────
NEURAL = [
    r"  ███╗   ██╗███████╗██╗   ██╗██████╗  █████╗ ██╗     ",
    r"  ████╗  ██║██╔════╝██║   ██║██╔══██╗██╔══██╗██║     ",
    r"  ██╔██╗ ██║█████╗  ██║   ██║██████╔╝███████║██║     ",
    r"  ██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██╔══██║██║     ",
    r"  ██║ ╚████║███████╗╚██████╔╝██║  ██║██║  ██║███████╗",
    r"  ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝",
]

LABS = [
    r"   ██╗      █████╗ ██████╗ ███████╗",
    r"   ██║     ██╔══██╗██╔══██╗██╔════╝",
    r"   ██║     ███████║██████╔╝███████╗",
    r"   ██║     ██╔══██║██╔══██╗╚════██║",
    r"   ███████╗██║  ██║██████╔╝███████║",
    r"   ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝",
]

# ── Scene 1: Boot loading bars ────────────────────────────────────────────────
def scene_loading():
    clr()
    steps = [
        ("Initializing synaptic core",   (0, 200, 255)),
        ("Loading neural weights",        (100, 255, 100)),
        ("Calibrating attention layers",  (255, 180, 0)),
        ("Warming up transformers",       (200, 80, 255)),
        ("Neural Labs ready",            (0, 255, 160)),
    ]
    BAR = 42

    print()
    print(BOLD + grad("  ╔══════════════════════════════════════════════╗",  0,200,255, 140,0,255))
    print(BOLD + grad("  ║         N E U R A L   L A B S   v2.0        ║",  0,200,255, 140,0,255))
    print(BOLD + grad("  ╚══════════════════════════════════════════════╝",  0,200,255, 140,0,255) + RST)
    print()

    for label, (cr, cg, cb) in steps:
        print(f"  {DIM}{rgb(cr,cg,cb)}{label}...{RST}")
        for i in range(BAR + 1):
            filled = rgb(cr, cg, cb) + BOLD + "█" * i
            empty  = DIM + rgb(40, 40, 60) + "░" * (BAR - i)
            pct    = rgb(cr, cg, cb) + BOLD + f"{int(i/BAR*100):3d}%"
            sys.stdout.write(f"\r  {filled}{empty}{RST}  {pct}{RST}")
            sys.stdout.flush()
            time.sleep(0.016)
        sys.stdout.write(f"\r  {rgb(cr,cg,cb)}{'█'*BAR}{RST}  {rgb(cr,cg,cb)}{BOLD}100% ✔{RST}\n")
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(0.4)

# ── Scene 2: Matrix rain ───────────────────────────────────────────────────────
def scene_matrix(frames=52):
    COLS = 64
    ROWS = 18
    CHARS = "01アイウエオカキクケコ∑∆Ωπ≡∫∂01ABCDEF"

    state = [
        [random.randint(-ROWS, 0), random.uniform(0.5, 1.2), random.randint(4, 13)]
        for _ in range(COLS)
    ]

    for frame in range(frames):
        canvas  = [[" "] * COLS for _ in range(ROWS)]
        palette = [[(0, 0, 0)] * COLS for _ in range(ROWS)]

        for c in range(COLS):
            head, spd, trail = state[c]
            head += spd * 0.6
            if head - trail > ROWS + 4:
                head  = random.randint(-8, 0)
                trail = random.randint(4, 13)
                spd   = random.uniform(0.5, 1.2)
            state[c] = [head, spd, trail]

            for r in range(ROWS):
                dist = int(head) - r
                if dist == 0:
                    canvas[r][c]  = random.choice(CHARS)
                    palette[r][c] = (210, 255, 210)
                elif 0 < dist <= trail:
                    fade = 1.0 - dist / trail
                    canvas[r][c]  = random.choice(CHARS)
                    palette[r][c] = (0, int(40 + 180 * fade), int(20 * fade))

        clr()
        for r in range(ROWS):
            row_str = "  "
            for c in range(COLS):
                ch = canvas[r][c]
                cr, cg, cb = palette[r][c]
                row_str += (rgb(cr, cg, cb) + ch + RST) if ch != " " else " "
            print(row_str)

        # Tease the brand name after halfway
        if frame > frames * 0.55:
            alpha = (frame - frames * 0.55) / (frames * 0.45)
            if alpha > 0.2:
                line = "  >>>  NEURAL LABS  —  System Online  <<<"
                r2 = int(0 + 100 * alpha)
                g2 = int(200 * alpha)
                b2 = int(100 + 155 * alpha)
                print()
                print(BOLD + rgb(r2, g2, b2) + line.center(66) + RST)
        time.sleep(0.055)

# ── Scene 3: Slide-in banner ───────────────────────────────────────────────────
def scene_reveal():
    all_lines   = NEURAL + [""] + LABS
    max_len     = max(len(l) for l in all_lines)

    for reveal in range(0, max_len + 1, 3):
        clr()
        print()
        print(BOLD + grad("  ┌" + "─" * 62 + "┐",
                          0, 200, 255, 150, 0, 255))
        print(BOLD + grad("  │" + "  NEURAL LABS  —  Artificial Intelligence Research  ".center(62) + "│",
                          0, 200, 255, 150, 0, 255))
        print(BOLD + grad("  └" + "─" * 62 + "┘",
                          0, 200, 255, 150, 0, 255) + RST)
        print()

        for i, line in enumerate(all_lines):
            visible = line[:reveal]
            hidden  = DIM + rgb(20, 20, 35) + line[reveal:] + RST
            if i < 6:       # NEURAL
                colored = BOLD + grad(visible, 0, 220, 255, 80, 30, 255)
            elif line == "": # spacer
                colored = ""
            else:           # LABS
                colored = BOLD + grad(visible, 255, 170, 0, 255, 40, 160)
            print(colored + hidden)

        time.sleep(0.018)
    time.sleep(0.3)

# ── Scene 4: Rainbow pulse loop ────────────────────────────────────────────────
def scene_pulse(cycles=32):
    for frame in range(cycles):
        t = frame / cycles * math.pi * 2
        bright = 0.60 + 0.40 * math.sin(t)

        clr()
        print()

        # Animated border
        br = int(bright * (127 + 127 * math.sin(t)))
        bg_ = int(bright * 60)
        bb = int(bright * (127 + 127 * math.sin(t + math.pi)))
        print(BOLD + rgb(br, bg_, bb) + "  ╔" + "═" * 60 + "╗" + RST)
        title = "  ⚡  NEURAL LABS  ⚡  —  Powering Intelligence".center(60)
        print(BOLD + wave("  ║" + title + "║", frame) + RST)
        print(BOLD + rgb(br, bg_, bb) + "  ╚" + "═" * 60 + "╝" + RST)
        print()

        for i, line in enumerate(NEURAL):
            print(BOLD + wave(line, frame, i) + RST)
        print()
        for i, line in enumerate(LABS):
            print(BOLD + wave(line, frame, i + 8) + RST)

        print()
        # Stats row
        stats = [
            ("MODELS",   "42+",    (0, 200, 255)),
            ("PARAMS",   "175B",   (255, 180, 0)),
            ("ACCURACY", "98.7%",  (100, 255, 100)),
            ("UPTIME",   "99.99%", (200, 80, 255)),
        ]
        row = "  "
        for label, val, (sr, sg, sb) in stats:
            pulse = 0.7 + 0.3 * math.sin(t + hash(label) * 0.7)
            row += rgb(int(sr*pulse), int(sg*pulse), int(sb*pulse)) + BOLD
            row += f"[ {label}: {val} ]  " + RST
        print(row)

        time.sleep(0.085)

# ── Scene 5: Neural network signal propagation ────────────────────────────────
def scene_network(frames=90):
    # Node positions on a 14 x 58 character canvas
    # Format: (row, col)
    I_pos = [(1, 0),  (4, 0),  (8, 0),  (11, 0)]
    H_pos = [(0, 18), (3, 18), (6, 18), (9, 18), (12, 18)]
    O_pos = [(3, 38), (7, 38), (11, 38)]

    I_lbl = ["x₁", "x₂", "x₃", "x₄"]
    H_lbl = ["h₁", "h₂", "h₃", "h₄", "h₅"]
    O_lbl = ["ŷ₁", "ŷ₂", "ŷ₃"]

    ROWS, COLS = 15, 46
    PULSE_CHARS = ["·", "•", "◦", "○"]

    def make_canvas():
        canvas = [[(" ", (20, 20, 30)) for _ in range(COLS)] for _ in range(ROWS)]
        return canvas

    def put(canvas, r, c, text, color):
        for i, ch in enumerate(text):
            if 0 <= r < ROWS and 0 <= c + i < COLS:
                canvas[r][c + i] = (ch, color)

    def draw(canvas, active_layer, signal_t):
        c = make_canvas()

        # ── connections ──
        # I→H
        for (ir, ic) in I_pos:
            for (hr, hc) in H_pos:
                for step in range(1, 10):
                    t = step / 10
                    r = int(ir + (hr - ir) * t)
                    col = int(ic + 3 + (hc - ic - 3) * t)
                    if active_layer == 0:
                        dist = abs(t - signal_t)
                        intensity = max(0, 1 - dist * 8)
                        color = (int(intensity * 0), int(100 + intensity * 155), int(intensity * 80))
                    else:
                        color = (15, 60, 35)
                    ch = PULSE_CHARS[step % len(PULSE_CHARS)]
                    put(c, r, col, ch, color)

        # H→O
        for (hr, hc) in H_pos:
            for (or_, oc) in O_pos:
                for step in range(1, 10):
                    t = step / 10
                    r = int(hr + (or_ - hr) * t)
                    col = int(hc + 4 + (oc - hc - 4) * t)
                    if active_layer == 1:
                        dist = abs(t - signal_t)
                        intensity = max(0, 1 - dist * 8)
                        color = (int(intensity * 200), int(intensity * 80), int(intensity * 255))
                    else:
                        color = (15, 60, 35)
                    ch = PULSE_CHARS[step % len(PULSE_CHARS)]
                    put(c, r, col, ch, color)

        # ── nodes ──
        for i, ((r, col), lbl) in enumerate(zip(I_pos, I_lbl)):
            color = (0, 200, 255) if active_layer == 0 else (0, 80, 120)
            put(c, r, col, f"({lbl})", color)

        for i, ((r, col), lbl) in enumerate(zip(H_pos, H_lbl)):
            if active_layer == 1:
                color = (80, 255, 80)
            elif active_layer == 0:
                pulse = max(0, math.sin(signal_t * math.pi))
                color = (0, int(80 + 120 * pulse), int(60 * pulse))
            else:
                color = (0, 180, 80)
            put(c, r, col, f"({lbl})", color)

        for i, ((r, col), lbl) in enumerate(zip(O_pos, O_lbl)):
            if active_layer == 2:
                pulse = max(0, math.sin(signal_t * math.pi))
                color = (int(255 * pulse), int(180 * pulse), 0)
            elif active_layer == 1:
                color = (80, 60, 0)
            else:
                color = (200, 140, 0)
            put(c, r, col, f"[{lbl}]", color)

        # Layer labels
        put(c, ROWS-1, 0,  "INPUT ", (0, 160, 200))
        put(c, ROWS-1, 17, "HIDDEN", (0, 200, 80))
        put(c, ROWS-1, 38, "OUTPUT", (200, 140, 0))

        return c

    def render(canvas):
        lines = []
        for row in canvas:
            line = "  "
            for ch, (cr, cg, cb) in row:
                if ch == " ":
                    line += " "
                else:
                    line += rgb(cr, cg, cb) + ch + RST
            lines.append(line)
        return "\n".join(lines)

    for frame in range(frames):
        t = frame / frames
        if t < 0.4:
            layer = 0; sig = t / 0.4
        elif t < 0.75:
            layer = 1; sig = (t - 0.4) / 0.35
        else:
            layer = 2; sig = (t - 0.75) / 0.25

        canvas = draw(None, layer, sig)

        clr()
        print()
        print(BOLD + grad("  ┌──  Neural Network Signal Propagation  ──────────────────┐",
                          0, 200, 255, 120, 0, 255))
        print(BOLD + grad("  └──────────────────────────────────────────────────────────┘",
                          0, 200, 255, 120, 0, 255) + RST)
        print()
        print(render(canvas))
        print()

        # Stage indicator
        stages = ["INPUT → HIDDEN", "HIDDEN → OUTPUT", "OUTPUT  ✓"]
        stage_str = "  "
        for j, name in enumerate(stages):
            if j == layer:
                stage_str += BOLD + rgb(0, 220, 255) + f" ▶ {name} " + RST
            else:
                stage_str += DIM + rgb(50, 50, 70) + f"   {name}  " + RST
        print(stage_str)

        # Progress bar
        pct = int(t * 50)
        bar = rgb(0, 200, 255) + "█" * pct + DIM + rgb(30, 30, 50) + "░" * (50 - pct) + RST
        print(f"\n  Propagation: [{bar}]  {int(t*100):3d}%")
        time.sleep(0.065)


# ── Final frame ────────────────────────────────────────────────────────────────
def scene_final():
    clr()
    print()
    print(BOLD + grad("  ╔" + "═"*62 + "╗", 0,200,255, 140,0,255))
    print(BOLD + grad("  ║" + " NEURAL LABS  —  Artificial Intelligence Research ".center(62) + "║",
                      0,200,255, 140,0,255))
    print(BOLD + grad("  ╚" + "═"*62 + "╝", 0,200,255, 140,0,255) + RST)
    print()
    for line in NEURAL:
        print(BOLD + grad(line, 0, 220, 255, 80, 30, 255) + RST)
    print()
    for line in LABS:
        print(BOLD + grad(line, 255, 170, 0, 255, 40, 160) + RST)
    print()
    print(BOLD + grad(
        "  ✦  Pioneering the Next Generation of Artificial Intelligence  ✦",
        0, 230, 255, 180, 40, 255) + RST)
    print()
    print(DIM + rgb(80,80,120) +
          "  © 2026 Neural Labs  ·  All systems operational  ·  v2.0.0" + RST)
    print()


# ── Entry ──────────────────────────────────────────────────────────────────────
def main():
    try:
        w(HIDE)
        scene_loading()
        scene_matrix(frames=52)
        scene_reveal()
        scene_pulse(cycles=32)
        scene_network(frames=90)
        scene_final()
        time.sleep(3)
    except KeyboardInterrupt:
        pass
    finally:
        w(SHOW + RST + "\n")
        print(BOLD + grad("  Neural Labs  —  Session ended.", 0, 230, 255, 200, 50, 255) + RST + "\n")

if __name__ == "__main__":
    main()
