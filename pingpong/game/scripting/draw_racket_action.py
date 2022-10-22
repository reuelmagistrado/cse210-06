from constants import *
from game.scripting.action import Action


class DrawRacketAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        racket = cast.get_actors(RACKET_GROUP)[0]
        racket2 = cast.get_actors(RACKET_GROUP)[1]

        body = racket.get_body()
        body2 = racket2.get_body()

        if racket.is_debug():
            rectangle = body.get_rectangle()
            rectangle2 = body2.get_rectangle()

            self._video_service.draw_rectangle(rectangle, PURPLE)
            self._video_service.draw_rectangle(rectangle2, PURPLE)

        animation = racket.get_animation()
        animation2 = racket2.get_animation()

        image = animation.next_image()
        image2 = animation2.next_image()

        position = body.get_position()
        position2 = body2.get_position()

        self._video_service.draw_image(image, position)
        self._video_service.draw_image(image2, position2)
