def half_to_another(melody):
    for old,new in zip(['C#','D#','F#','G#','A#'],['H','I','J','K','L']):
        melody = melody.replace(old,new)
    return melody

def solution(m, musicinfos):
    satisfy = []
    m = half_to_another(m)
    for n, music in enumerate(musicinfos):
        [time_from, time_to, title, melody] = music.split(',')

        time_from = int(time_from[:2]) * 60 + int(time_from[3:])
        time_to = int(time_to[:2]) * 60 + int(time_to[3:])
        interval = time_to - time_from

        melody = half_to_another(melody)
        melody_heard = ''
        i = 0
        while len(melody_heard) < interval:
            idx = i % len(melody)
            melody_heard += melody[idx]
            i += 1
        if m in melody_heard:
            satisfy.append((interval,-n,title))

    if satisfy:
        return max(satisfy)[2]
    else:
        return '(None)'

print(solution('ABCDEFG',['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))