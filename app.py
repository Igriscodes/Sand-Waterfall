import pygame
import colorsys
import random

GRID_WIDTH = 300
GRID_HEIGHT = 150
CELL_SIZE = 5
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
SPAWN_RATE = 8
CENTER_SPAWN_WEIGHT = 0.80

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Colorful Sand Waterfall")
clock = pygame.time.Clock()

grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def hsv_to_rgb(hue, saturation, value):
    r, g, b = colorsys.hsv_to_rgb(hue / 360.0, saturation, value)
    return (int(r * 255), int(g * 255), int(b * 255))

def spawn_particles(frame_count):
    center_x = GRID_WIDTH // 2
    base_hue = (frame_count * 0.5) % 360
    for _ in range(SPAWN_RATE):
        if random.random() < CENTER_SPAWN_WEIGHT:
            offset = int(abs(random.gauss(0, GRID_WIDTH / 8)))
            direction = 1 if random.randint(0, 1) == 0 else -1
            x = center_x + (direction * offset)
            x = max(0, min(GRID_WIDTH - 1, x))
        else:
            x = random.randint(0, GRID_WIDTH - 1)
        y = 0
        hue = (base_hue + random.uniform(-3, 3)) % 360
        saturation = random.uniform(0.85, 0.95)
        value = random.uniform(0.85, 0.95)
        color = hsv_to_rgb(hue, saturation, value)
        if grid[y][x] is None:
            grid[y][x] = color

def check_peak_at_top():
    center_x = GRID_WIDTH // 2
    center_range = int(GRID_WIDTH * 0.2)
    check_height = int(GRID_HEIGHT * 0.08)
    count = 0
    for y in range(check_height):
        for x in range(center_x - center_range, center_x + center_range + 1):
            if 0 <= x < GRID_WIDTH and grid[y][x] is not None:
                count += 1
    threshold = check_height * center_range * 2 * 0.5
    return count > threshold

def apply_physics():
    for y in range(GRID_HEIGHT - 2, -1, -1):
        x_order = list(range(GRID_WIDTH))
        random.shuffle(x_order)
        for x in x_order:
            if grid[y][x] is None:
                continue
            particle = grid[y][x]
            if grid[y + 1][x] is None:
                grid[y][x] = None
                grid[y + 1][x] = particle
            else:
                diag_options = []
                if x > 0 and grid[y + 1][x - 1] is None:
                    diag_options.append(x - 1)
                if x < GRID_WIDTH - 1 and grid[y + 1][x + 1] is None:
                    diag_options.append(x + 1)
                if diag_options:
                    new_x = random.choice(diag_options)
                    grid[y][x] = None
                    grid[y + 1][new_x] = particle
                else:
                    slide_options = []
                    if x > 0 and grid[y][x - 1] is None:
                        slide_options.append(x - 1)
                    if x < GRID_WIDTH - 1 and grid[y][x + 1] is None:
                        slide_options.append(x + 1)
                    if slide_options:
                        new_x = random.choice(slide_options)
                        grid[y][x] = None
                        grid[y][new_x] = particle

def count_particles():
    return sum(1 for row in grid for cell in row if cell is not None)

def clear_grid():
    global grid
    grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def render(particle_count):
    screen.fill(BACKGROUND_COLOR)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] is not None:
                pygame.draw.rect(screen, grid[y][x],
                                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    font = pygame.font.Font(None, 24)
    text = font.render(f"Particles: {particle_count}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()

running = True
frame_count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    spawn_particles(frame_count)
    apply_physics()
    particle_count = count_particles()
    if check_peak_at_top():
        clear_grid()
        frame_count = 0
    render(particle_count)
    clock.tick(FPS)
    frame_count += 1
pygame.quit()
