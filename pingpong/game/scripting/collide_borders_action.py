from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        ball2 = cast.get_actors(BALL_GROUP)[1]

        body = ball.get_body()
        body2 = ball2.get_body()

        position = body.get_position()
        position2 = body2.get_position()

        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)

        stats = cast.get_first_actor(STATS_GROUP)
        stats2 = cast.get_actors(STATS_GROUP)[1]

        if x < FIELD_LEFT:
            stats.next_level()
            stats2.add_points()
            if stats.get_level() < MAXIMUM_ROUND:
                callback.on_next(TRY_AGAIN)
            else:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            stats.next_level()
            stats.add_points()

            if stats.get_level() < MAXIMUM_ROUND:
                callback.on_next(TRY_AGAIN, position2)
            else:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)

        if y < FIELD_TOP:
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)
