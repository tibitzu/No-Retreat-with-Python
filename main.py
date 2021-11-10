import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("No Retreat")
icon = pygame.image.load("assets/goblin.png")
pygame.display.set_icon(icon)


def main():

    running = True
    while running:

        screen.fill((150, 0, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


if __name__ == "__main__":
    main()
