from pico2d import *
import game_framework
import game_world


class ItemMode:
    def __init__(self, boy):
        self.boy = boy
        self.image = None

    def init(self):
        self.image = load_image('item_select.png')

    def finish(self):
        self.image = None

    def handle_events(self):
        for event in get_events():
            if event.type == SDL_QUIT:
                game_framework.quit()
                return
            elif event.type == SDL_KEYDOWN and event.key in (SDLK_i, SDLK_ESCAPE):
                game_framework.pop_mode()
                return
            else:
                self.boy.handle_event(event)

    def update(self):
        # 아이템 창이 열려 있어도 게임은 계속 진행한다.
        game_world.update()

    def render(self):
        clear_canvas()
        game_world.render()
        self.image.draw(400, 460)
        update_canvas()
