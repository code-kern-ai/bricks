from util.configs import build_generator_premium_config
from util.enums import State
from . import nyt_news_search, INPUT_EXAMPLE


def get_config():
    return build_generator_premium_config(
        function=nyt_news_search,
        input_example=INPUT_EXAMPLE,
        data_type="text",
        issue_id=209,
        tabler_icon="News",
        state=State.PUBLIC
    )
