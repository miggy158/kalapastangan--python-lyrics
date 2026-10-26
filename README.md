# Kalapastangan — Python Lyrics

A tiny Python script that "plays" the lyrics of **Kalapastangan** in the terminal, typing out each line character by character with a pause between lines — like a live lyric video, but in your console.

## Requirements

- Python 3.6 or newer
- No third-party packages — only the standard library (`time` and `sys`)

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/miggy158/kalapastangan--python-lyrics.git
cd kalapastangan--python-lyrics
python main.py
```

The lyrics will be typed out in your terminal. Press `Ctrl+C` to stop at any time.

## How it works

The lyrics live in a single list at the top of `main.py`. Each entry is a tuple of three values:

```python
("Mamamatay akong nakangiti", 1.22, 0.13)
#   ^ the line                 ^     ^
#   delay before next line (s)        delay per character (s)
```

Two small functions do the work:

| Function | Purpose |
| --- | --- |
| `type_out(text, char_delay)` | Writes `text` one character at a time, flushing after each character so it appears live, then prints a newline. |
| `play_lyrics(lyrics)` | Loops over the lyric list, calls `type_out` for each line, and sleeps for that line's `line_delay`. |

The script only runs when executed directly, thanks to the `if __name__ == "__main__":` guard at the bottom.

## Customizing

- **Change the lyrics** — edit the `lyrics` list in `main.py`.
- **Change the pacing** — tweak the second value (line delay) and third value (character delay) of each tuple. Larger numbers mean slower playback.
- **Reuse the effect elsewhere** — `type_out` and `play_lyrics` are plain functions, so you can import them:

```python
from main import play_lyrics

play_lyrics([
    ("Hello, world", 1.0, 0.05),
    ("Goodbye, world", 1.0, 0.05),
])
```

> Note: importing `main` will not play the built-in lyrics, because of the `__main__` guard.

## Project structure

```
kalapastangan--python-lyrics/
├── main.py     # the lyrics and the typing effect
└── README.md   # this file
```

## License

No license has been specified for this project. The lyrics themselves belong to their respective copyright holders.
