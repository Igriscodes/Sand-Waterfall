# Colorful Sand Waterfall

A particle simulation featuring rainbow-colored sand particles with realistic physics, built with Pygame.

## Features

- **Realistic sand physics** with gravity, diagonal falling, and horizontal sliding
- **Dynamic rainbow colors** using HSV color cycling
- **Symmetric particle spawning** from the center with natural distribution
- **Auto-restart** when sand pile reaches the top
- Real-time particle counter
- Runs at 60 FPS

## Requirements

```bash
pip install pygame
```

## Usage

```bash
python sand_simulation.py
```

Watch as colorful sand particles cascade down and form natural-looking piles. The simulation automatically resets when the sand reaches the top.

## How It Works

- **Particle Spawning**: Sand spawns from the top with 80% concentrated near the center using Gaussian distribution
- **Physics Engine**: Particles fall straight down, slide diagonally when blocked, or move horizontally to fill gaps
- **Color System**: HSV-based rainbow colors that gradually shift over time
- **Grid-Based**: 300×150 cell grid with 5-pixel cells (1500×750 window)

## Configuration

Customize these parameters in the script:
- `GRID_WIDTH` / `GRID_HEIGHT`: Grid dimensions (default: 300×150)
- `CELL_SIZE`: Pixel size per cell (default: 5)
- `FPS`: Frame rate (default: 60)
- `SPAWN_RATE`: Particles per frame (default: 8)
- `CENTER_SPAWN_WEIGHT`: Concentration at center (default: 0.80)

## License
[GNU Lesser General Public License v2.1](LICENSE) - Feel free to use and modify
