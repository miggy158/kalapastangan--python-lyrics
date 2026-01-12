import time
import sys

print("\n\n")

lyrics = [
    ("Oh, ooh", 4.6, 0.49),
    ("Mamamatay akong nakangiti", 1.22, 0.13),
    ("Kapag ikaw ang nasa aking tabi", 1.21, 0.13),
    ("Mabubuhay akong nagsisisi", 1.15, 0.12),
    ("Kapag isang araw hindi kita mapapangiti", 1.13, 0.10),
    ("Kalapastangan ang 'di ka ibigin", 1.13, 0.10),
    ("Kalokohan ang 'di ka isipin", 1.13, 0.10),
    ("Kung ang mundo ay biglang gugunawin", 1.12, 0.10),
    ("Ikaw ang una kong hahanapin", 1.12, 0.10),
]

def type_out(text, char_delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def play_lyrics(lyrics):
    for line, line_delay, char_delay in lyrics:
        type_out(line, char_delay)
        time.sleep(line_delay)

if __name__ == "__main__":
    play_lyrics(lyrics)
