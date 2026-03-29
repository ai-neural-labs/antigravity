#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                        ASCII Art Generator Script                               ║
║                         "AI Neural Labs" Banner                                 ║
╚══════════════════════════════════════════════════════════════════════════════════╝
"""

import time
import sys
import os

# ANSI color codes
CYAN    = "\033[96m"
MAGENTA = "\033[95m"
YELLOW  = "\033[93m"
GREEN   = "\033[92m"
BLUE    = "\033[94m"
WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"


BANNER = r"""
  █████╗ ██╗    ███╗   ██╗███████╗██╗   ██╗██████╗  █████╗ ██╗
 ██╔══██╗██║    ████╗  ██║██╔════╝██║   ██║██╔══██╗██╔══██╗██║
 ███████║██║    ██╔██╗ ██║█████╗  ██║   ██║██████╔╝███████║██║
 ██╔══██║██║    ██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██╔══██║██║
 ██║  ██║██║    ██║ ╚████║███████╗╚██████╔╝██║  ██║██║  ██║███████╗
 ╚═╝  ╚═╝╚═╝    ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

 ██╗      █████╗ ██████╗ ███████╗
 ██║     ██╔══██╗██╔══██╗██╔════╝
 ██║     ███████║██████╔╝███████╗
 ██║     ██╔══██║██╔══██╗╚════██║
 ███████╗██║  ██║██████╔╝███████║
 ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝
"""

NEURAL_NET = r"""
         [INPUT]            [HIDDEN]          [OUTPUT]
           o ─────────────── o
           │ ╲             ╱ │ ╲
           │  ╲           ╱  │  ╲
           o   ╲─────────╱   o   ╲──── o  ◄── PREDICTION
           │   ╱─────────╲   │   ╱
           │  ╱           ╲  │  ╱
           o ─────────────── o ╱
                               ╲
           o ─────────────── o  ╲──── o  ◄── CONFIDENCE
           │ ╲             ╱ │ ╱
           │  ╲           ╱  │╱
           o   ╲─────────╱   o
"""

TAGLINE = r"""
   ┌─────────────────────────────────────────────────────────────────┐
   │          ⚡  Powering the Future of Intelligence  ⚡           
   │        🧠  Deep Learning │ NLP │ Computer Vision │ AI         🧠  
   └─────────────────────────────────────────────────────────────────┘
"""

SEPARATOR = "═" * 74


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def typewrite(text, color="", delay=0.003):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)


def print_with_border(text, color=CYAN):
    width = 74
    lines = text.strip().split("\n")
    print(color + "╔" + "═" * width + "╗" + RESET)
    for line in lines:
        padded = line.ljust(width)[:width]
        print(color + "║" + WHITE + padded + color + "║" + RESET)
    print(color + "╚" + "═" * width + "╝" + RESET)


def animate_loading():
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    steps = [
        "Initializing neural pathways",
        "Loading synaptic weights",
        "Calibrating inference engine",
        "Activating AI cores",
        "Booting AI Neural Labs",
    ]
    for step in steps:
        for i in range(12):
            sys.stdout.write(f"\r  {CYAN}{frames[i % len(frames)]}{RESET}  {DIM}{step}...{RESET}   ")
            sys.stdout.flush()
            time.sleep(0.06)
        sys.stdout.write(f"\r  {GREEN}✔{RESET}  {step}... {GREEN}Done{RESET}          \n")
    print()


def main():
    clear_screen()

    # ── Header ────────────────────────────────────────────────────────────────
    print()
    print(MAGENTA + BOLD + SEPARATOR + RESET)
    print(MAGENTA + BOLD + "  ✦  Welcome to " + YELLOW + "AI NEURAL LABS" + MAGENTA + "  ─  Pioneering Artificial Intelligence  ✦" + RESET)
    print(MAGENTA + BOLD + SEPARATOR + RESET)
    print()

    time.sleep(0.4)

    # ── Loading animation ──────────────────────────────────────────────────────
    animate_loading()

    # ── Main banner ────────────────────────────────────────────────────────────
    for line in BANNER.split("\n"):
        gradient_colors = [CYAN, BLUE, MAGENTA, CYAN, BLUE, MAGENTA]
        color = gradient_colors[hash(line) % len(gradient_colors)]
        typewrite(line + "\n", color=BOLD + color, delay=0.001)

    time.sleep(0.3)

    # ── Neural net diagram ─────────────────────────────────────────────────────
    print(GREEN + BOLD + "  Neural Network Architecture:" + RESET)
    for line in NEURAL_NET.split("\n"):
        typewrite(line + "\n", color=DIM + GREEN, delay=0.005)

    time.sleep(0.2)

    # ── Tagline ────────────────────────────────────────────────────────────────
    for line in TAGLINE.split("\n"):
        typewrite(line + "\n", color=YELLOW + BOLD, delay=0.004)

    # ── Footer ─────────────────────────────────────────────────────────────────
    print()
    print(CYAN + "─" * 74 + RESET)
    typewrite("  © 2026 AI Neural Labs  │  All rights reserved  │  v1.0.0\n", color=DIM + WHITE, delay=0.005)
    print(CYAN + "─" * 74 + RESET)
    print()


if __name__ == "__main__":
    main()
