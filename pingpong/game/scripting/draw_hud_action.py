from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        stats = cast.get_actors(STATS_GROUP)[0]
        stats2 = cast.get_actors(STATS_GROUP)[1]

        self._draw_label(cast, PLAYER1_GROUP,
                         PLAYER1_FORMAT, stats.get_score())
        self._draw_label(cast, PLAYER2_GROUP,
                         PLAYER2_FORMAT, stats2.get_score())
        self._draw_label(cast, ROUND_GROUP, ROUND_FORMAT, stats.get_level())

    def _draw_label(self, cast, group, format_str, data):
        the_value_to_display = format_str.format(data)
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(the_value_to_display)
        position = label.get_position()
        self._video_service.draw_text(text, position)
