import spritePro as s


class GameScene(s.Scene):
    def __init__ (self):
    super().__init__()
        bg = s.Sprite('background_bird.png',pos=(200,300),size=(400,600))
        bird = s.Sprite('bird.png',pos=(100,300),size=(50,50))
        self.player_body = s.add_physics(self.bird, s.PhysicsConfig(bounce=0.0))
        s.physics.set_gravity(980)
        s.physics.set_bounds(s.pygame.Rect(0,0,400,600))

if __name__ == '__main__':
    s.run(size=(400,600), title="Flappy Bird")
