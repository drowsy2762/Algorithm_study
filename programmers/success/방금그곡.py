# 2026-09-28
def replace_sharp(melody):
    melody = melody.replace("C#", "c")
    melody = melody.replace("D#", "d")
    melody = melody.replace("F#", "f")
    melody = melody.replace("G#", "g")
    melody = melody.replace("A#", "a")
    melody = melody.replace("B#", "b")
    return melody


def get_play_time(start_time, end_time):
    start_h, start_m = map(int, start_time.split(":"))
    end_h, end_m = map(int, end_time.split(":"))

    return (end_h * 60 + end_m) - (start_h * 60 + start_m)


def solution(m, musicinfos):
    target_melody = replace_sharp(m)
    best_title = "(None)"
    max_play_time = -1

    for info in musicinfos:
        start_time, end_time, title, sheet = info.split(",")
        play_time = get_play_time(start_time, end_time)
        sheet = replace_sharp(sheet)
        sheet_len = len(sheet)
        repeated_sheet = (sheet * (play_time // sheet_len + 1))[:play_time]

        if target_melody in repeated_sheet:
            if play_time > max_play_time:
                max_play_time = play_time
                best_title = title

    return best_title
