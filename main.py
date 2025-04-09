import pygame
from pygame.locals import *
from logging import *

logger = getLogger(__name__)


# Klasse voor de App
class App:
    def __init__(self):
        logger.debug("__init__ called.")
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 750, 400

    def on_init(self):
        logger.debug("on_init called.")
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Brandmeld/OI Installatie")

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def draw_button(self, surface, x, y, width, height, color, text, font):
        pygame.draw.rect(surface, color, (x, y, width, height))
        self.draw_text(text, font, (255, 255, 255), surface, x + 10, y + 10)

    def on_event(self, event):
        logger.debug("on_event called.")
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        logger.debug("on_loop called.")
        pass

    def on_render(self):
        logger.debug("on_render called.")
        font = pygame.font.Font(None, 36)

        if self._running:
            # Teken startmenu
            self._display_surf.fill((0, 0, 0))  # Vul het scherm met zwart
            self.draw_text("Welkom bij de Brandmeld/OI Installatie Simulator", font, (255, 255, 255), self._display_surf,
                           100, 100)

            # Teken de startknop
            self.draw_button(self._display_surf, 220, 200, 200, 50, (0, 128, 0), "Start Oefening", font)
            self.draw_button(self._display_surf, 220, 270, 200, 50, (255, 0, 0), "Afsluiten", font)

        pygame.display.update()

    def on_cleanup(self):
        logger.debug("on_cleanup called.")
        pygame.quit()

    def on_execute(self):
        logger.debug("on_execute called.")
        self.on_init()

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if 220 <= mouse_x <= 420 and 200 <= mouse_y <= 250:  # Startknop
                        self._running = False  # Start de simulatie (gaat naar het hoofdprogramma)
                    elif 220 <= mouse_x <= 420 and 270 <= mouse_y <= 320:  # Afsluitknop
                        self._running = False  # Verlaat de applicatie

            self.on_loop()
            self.on_render()

        self.on_cleanup()


# Hoofdprogramma
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
