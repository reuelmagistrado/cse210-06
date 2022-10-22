from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket = cast.get_actors(RACKET_GROUP)[0]
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        y = position.get_y()

        position = position.add(velocity)

        if y < 0:
            position = Point(SCREEN_WIDTH - RACKET_HEIGHT, 0)
        elif y > (SCREEN_HEIGHT - RACKET_HEIGHT):
            position = Point(position.get_x(),
                             SCREEN_HEIGHT - RACKET_HEIGHT)

        body.set_position(position)

        racket2 = cast.get_actors(RACKET_GROUP)[1]
        body2 = racket2.get_body()
        velocity2 = body2.get_velocity()
        position2 = body2.get_position()
        y2 = position2.get_y()

        position2 = position2.add(velocity2)

        if y2 < 0:
            position2 = Point(0, 0)
        elif y2 > (SCREEN_HEIGHT - RACKET_HEIGHT):
            position2 = Point(position2.get_x(),
                              SCREEN_HEIGHT - RACKET_HEIGHT)

        body2.set_position(position2)
