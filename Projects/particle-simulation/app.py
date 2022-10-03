import pygame as pg
from particle import Particle


def main():
    pg.init()

    window = pg.display.set_mode([960, 540])
    clock = pg.time.Clock()
    running = True
    particles = []

    while running:
        window.fill([0, 0, 20])

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        clicked = pg.mouse.get_pressed()[0]
        if clicked:
            mouse_pos = pg.mouse.get_pos()
            [particles.append(Particle(mouse_pos)) for _ in range(3)]

        to_be_removed = []
        for particle in particles:
            particle.draw(window)
            particle.update()

            if particle.is_dead():
                to_be_removed.append(particle)

        [particles.remove(p) for p in to_be_removed]

        pg.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
