import pygame

class Class1(object):
    pygame.init()
    image = pygame.image.load('images\\fon.png')
    gamemusic = pygame.mixer.music.load('sounds\\S2.mp3')
    sound = pygame.mixer.Sound('sounds\\S.mp3')

    font = pygame.font.SysFont('serif', 32)
    msg = 'Инь Янь'
    text = font.render(msg, True, 'grey')

    def draw(self, g):
        g.fill('white')
        pygame.mixer.music.play(-1)
        pygame.mixer.Sound.play(self.sound)

        # pygame.draw.line(g, (255, 255, 100), (50, 50), (500, 100), 1)
        # pygame.draw.aaline(g, (255, 255, 100), (50, 60), (500, 110)) :-:
        # pygame.draw.line(g, 'white', (50, 70), (500, 120), 1)
        # pygame.draw.rect(g, 'black', (100, 100, 300, 300), 1)
        # pygame.draw.ellipse(g, 'black', (200, 300, 100, 400), 1)
        # pygame.draw.circle(g, 'white', (400, 400), 100, 1)
        # pygame.draw.arc(g, 'black', (250, 1, 300, 300), -1.57, 1.57, 10)
        # g.blit(image, (0, 0))

        pygame.draw.lines(g, 'black', True, [(100, 100), (200, 200), (100, 200)], 5)
        # pygame.draw.polygon(g, 'black', ((100, 200), (200, 200), (200, 300), (300, 300), (300, 400)), 0)
        g.blit(self.text, (350, 50))
        pygame.draw.rect(g, ('black'), (0, 0, 800, 600), 10)

        # Колизия
        def TEST(self, pos):
            if (pos[0] > self.rect.x and pos[0] < self.rect.x + self.rect.width
                    and pos[1] > self.rect.y and pos[1] < self.rect.y + self.rect.height):
                return True
            else:
                return False

