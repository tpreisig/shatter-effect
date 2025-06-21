# Shatter - Visual Effects

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-orange)

A Pygame-based application that creates a visual effect of "shard" particles emanating from the mouseFormater.

- ➡️ Your mouse click location initiates a sparkling explosion effect.
- ➡️ Shards move outward, fade over time, and eventually disappear after a set lifespan.

## Features

- **Mouse Click Effect**: Click anywhere on the screen to generate 40 shards that radiate outward from the click position.
- **Dynamic Shards**: Each shard has a random angle, speed, and scale, and fades out over a 4-second lifespan.
- **Background Color Change**: Press the `Tab` key to change the background to a random dark color (RGB values between 0 and 40).
- **Smooth Animation**: Runs at a configurable FPS (defined in `config.py`), with delta-time-based movement for consistent behavior across frame rates.
- **Custom Cursor**: Uses a crosshair cursor for precise clicking.

## Requirements

- Python 3.x
- Pygame library (`pip install pygame-ce`)

## Installation

1. Clone or download this repository.
2. Install the required dependencies:
   ```bash
   pip install pygame-ce