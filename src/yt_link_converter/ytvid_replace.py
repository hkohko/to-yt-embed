import re


def check_matches_long(msg: str) -> str:
    domain = "https://www.youtube.com/embed/"
    pattern_long = (
        r"(\w+://www\.)(youtube\.com/)(?:watch|live)(\W(?:v=)?[^\?]+)(?:\W\w+=.+)?"
    )
    pattern_video_id = r"\W\w=([\w-]+)"
    matches_long = re.match(pattern_long, msg, re.IGNORECASE)
    if matches_long is None:
        return matches_long
    video_id = re.match(pattern_video_id, matches_long.group(3), re.IGNORECASE)
    return domain + video_id.group(1)


def main(msg: str):
    result_long = check_matches_long(msg)
    converted_link = result_long
    return converted_link
