#!/usr/bin/env python3
"""Launcher for the Qt GUI application."""

import os
import sys
import matplotlib

matplotlib.use("Agg")


def _ensure_standard_streams() -> None:
    """Provide writable fallback streams for windowed builds without a console."""
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w", encoding="utf-8")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w", encoding="utf-8")


_ensure_standard_streams()

if __name__ == "__main__":
    from src.gui import main
    sys.exit(main())
