import re


def check_matches_long(msg: str) -> str:
    pattern_long = (
        r"(\w+://www\.)(youtube)(\.com/(?:watch|live)\W(?:v=)?[^\?]+)(?:\W\w+=.+)?"
    )
    matches_long = re.match(pattern_long, msg, re.IGNORECASE)
    if matches_long is None:
        return matches_long
    if matches_long.group(2) != "youtube":
        return None
    converted_link = re.sub(pattern_long, "\g<1>ymusicapp\g<3>", msg)
    if "live/" in converted_link:
        converted_link = converted_link.replace("live/", "watch?v=")
    return converted_link


def check_matches_short(msg: str) -> str:
    pattern_short = r"(\w+://)(youtu.be/)([^\?]+)(?:\W\w+=.+)?"
    matches_short = re.match(pattern_short, msg, re.IGNORECASE)
    if matches_short is None:
        return matches_short
    if matches_short.group(2) != "youtu.be/":
        return None
    converted_link = re.sub(pattern_short, "\g<1>ymusicapp.com/watch?v=\g<3>", msg)
    return converted_link


def main(msg: str):
    result_long = check_matches_long(msg)
    result_short = check_matches_short(msg)
    if all((result_short is None, result_long is None)):
        return msg
    converted_link = result_long if result_long is not None else result_short
    return converted_link


if __name__ == "__main__":
    sample_link = "https://www.youtube.com/watch?v=s9vSCABh1K8"
    result = main(sample_link)
    print(result)
