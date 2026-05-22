from project import keydirection,speed_update,is_game_running
import pygame 
def test_keydirection():
    assert keydirection({pygame.K_w: True, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}) == 'UP'
    assert keydirection({pygame.K_w: False, pygame.K_s: True, pygame.K_a: False, pygame.K_d: False}) == 'DOWN'
    assert keydirection({pygame.K_w: False, pygame.K_s: False, pygame.K_a: True, pygame.K_d: False}) == 'LEFT'
    assert keydirection({pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: True}) == 'RIGHT'
    assert keydirection({pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}) == "RIGHT"

def test_speed_update():
    assert speed_update(50,12)==14
    assert speed_update(100,14)==18
    assert speed_update(180,22)==22
    assert speed_update(230,22)==24
    assert speed_update(0,12)==12


def test_is_game_running():
    assert is_game_running([100, 50], [[100, 50], [90, 50], [80, 50]]) == True
    assert is_game_running([0, 50], [[0, 50], [10, 50], [20, 50]])== False
    assert is_game_running([700, 50], [[700, 50], [690, 50], [680, 50]])== False
    assert is_game_running([100, 0], [[100, 0], [100, 10], [100, 20]])== False
    assert is_game_running([100, 500], [[100, 500], [100, 490], [100, 480]])==False
    assert is_game_running([100, 50], [[100, 50], [90, 50], [80, 50], [100, 50]])==False