from src.yt_link_converter.ytvid_replace import check_matches_long


def main():
    url_list = [
        "https://www.youtube.com/watch?v=s9vSCABh1K8",
        "https://www.youtube.com/watch?v=MsORKg_x_Q8&pp=ygUPc2hpc2hpcm8gIGJvdGFu",
        "https://www.youtube.com/watch?v=u-V9on9C-10",
        "https://www.youtube.com/watch?v=4Em48XNB-i4",
        "https://www.youtube.com/watch?v=g32je_2-u4Y",
        "https://www.youtube.com/watch?v=f7EAfYXMXEE&pp=ygUPaG9sb2xpdmUgd2F0YW1l",
        "https://www.youtube.com/watch?v=AvtI8-90kQM&t=126s&pp=ygUPaG9sb2xpdmUgd2F0YW1l",
    ]
    result = list(map(check_matches_long, url_list))
    print(result)
