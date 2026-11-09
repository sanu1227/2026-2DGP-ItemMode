import os

from pico2d import *
import game_framework
import game_world


class ItemMode:
    def __init__(self, boy):
        self.boy = boy
        self.image = None
        self.font = None

    def init(self):
        self.image = load_image('item_select.png')
        self.font = load_font(
            os.path.join(os.environ.get('WINDIR', 'C:\\Windows'),
                         'Fonts', 'malgun.ttf'), 20)

    def finish(self):
        self.image = None
        self.font = None

    def handle_events(self):
        for event in get_events():
            if event.type == SDL_QUIT:
                game_framework.quit()
                return
            elif event.type == SDL_KEYDOWN and event.key in (SDLK_i, SDLK_ESCAPE):
                game_framework.pop_mode()
                return
            elif event.type == SDL_KEYDOWN and event.key in (SDLK_0, SDLK_1, SDLK_2):
                self.boy.ball_size = {SDLK_0: 0, SDLK_1: 21, SDLK_2: 41}[event.key]
            else:
                self.boy.handle_event(event)

    def update(self):
        # 아이템 창이 열려 있어도 게임은 계속 진행한다.
        game_world.update()

    def render(self):
        clear_canvas()
        game_world.render()
        self.image.draw(400, 460)
        selection = {0: '공 없음', 21: '기본 공', 41: '큰 공'}[self.boy.ball_size]
        self.font.draw(265, 590, f'아이템 선택: {selection}', (0, 0, 0))
        self.font.draw(265, 330, '0/1/2: 선택  I/ESC: 닫기', (0, 0, 0))
        update_canvas()
