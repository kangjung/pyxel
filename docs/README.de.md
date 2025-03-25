# <img src="images/pyxel_logo_152x64.png">

[![Downloads](https://static.pepy.tech/personalized-badge/pyxel?period=total&units=international_system&left_color=grey&right_color=blue&left_text=PyPI%20downloads)](https://pypi.org/project/pyxel/)
[![GitHub Repo stars](https://img.shields.io/github/stars/kitao/pyxel?style=social)](https://github.com/kitao/pyxel)
[![GitHub forks](https://img.shields.io/github/forks/kitao/pyxel?style=social)](https://github.com/kitao/pyxel)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/kitao?label=Sponsor%20me&logo=github%20sponsors&style=social)](https://github.com/sponsors/kitao)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H27VDKD)

[ [English](../README.md) | [中文](README.cn.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Português](README.pt.md) | [Русский](README.ru.md) | [Türkçe](README.tr.md) | [Українська](README.uk.md) ]

**Pyxel** ist eine Retro-Spiel-Engine für Python.

Die Spezifikationen sind von Retro-Spielkonsolen inspiriert, wie z. B. der Unterstützung von nur 16 Farben und 4 Klangkanälen, sodass Sie ganz einfach pixelartige Spiele erstellen können.

[<img src="images/pyxel_thanks.png" width="460">](https://github.com/kitao/pyxel/wiki/Pyxel-User-Examples) [<img src="images/pyxel_book.png" width="180">](https://gihyo.jp/book/2025/978-4-297-14657-3)

Die Entwicklung von Pyxel wird durch das Feedback der Benutzer vorangetrieben. Bitte geben Sie Pyxel einen Stern auf GitHub!

<p>
<a href="https://kitao.github.io/pyxel/wasm/examples/10_platformer.html">
<img src="images/10_platformer.gif" width="290">
</a>
<a href="https://kitao.github.io/pyxel/wasm/examples/30sec_of_daylight.html">
<img src="images/30sec_of_daylight.gif" width="350">
</a>
<a href="https://kitao.github.io/pyxel/wasm/examples/02_jump_game.html">
<img src="images/02_jump_game.gif" width="330">
</a>
<a href="https://kitao.github.io/pyxel/wasm/examples/megaball.html">
<img src="images/megaball.gif" width="310">
</a>
<a href="https://kitao.github.io/pyxel/wasm/examples/image_editor.html">
<img src="images/image_tilemap_editor.gif" width="320">
</a>
<a href="https://kitao.github.io/pyxel/wasm/examples/sound_editor.html">
<img src="images/sound_music_editor.gif" width="320">
</a>
</p>

Die Spezifikationen und APIs von Pyxel sind inspiriert von [PICO-8](https://www.lexaloffle.com/pico-8.php) und [TIC-80](https://tic80.com/).

Pyxel ist unter der [MIT-Lizenz](../LICENSE) Open Source und kostenlos zu verwenden. Lass uns beginnen, Retro-Spiele mit Pyxel zu erstellen!

## Spezifikationen

- Läuft auf Windows, Mac, Linux und Web
- Programmierung in Python
- Anpassbare Bildschirmgröße
- 16-Farben-Palette
- 3 256x256 große Bildbanken
- 8 256x256 große Kachelkarten
- 4 Kanäle mit 64 definierbaren Klängen
- 8 Musiktracks, die beliebige Klänge kombinieren können
- Eingaben über Tastatur, Maus und Gamepad
- Werkzeuge zum Bearbeiten von Bildern und Klängen
- Benutzererweiterbare Farben, Kanäle und Datenbanken

### Farbpallette

<img src="images/05_color_palette.png">

<img src="images/pyxel_palette.png">

## Installation

### Windows

Nachdem Sie [Python3](https://www.python.org/) (Version 3.8 oder höher) installiert haben, führen Sie den folgenden Befehl aus:

```sh
pip install -U pyxel
```

Wenn Sie Python mit dem offiziellen Installer installieren, stellen Sie sicher, dass Sie die Option `Add Python 3.x to PATH` aktivieren, um den `pyxel` Befehl zu ermöglichen.

### Mac

Nachdem Sie [Homebrew](https://brew.sh/) installiert haben, führen Sie die folgenden Befehle aus:

```sh
brew install pipx
pipx ensurepath
pipx install pyxel
```

Um Pyxel nach der Installation zu aktualisieren, führen Sie `pipx upgrade pyxel` aus.

### Linux

Nachdem Sie das SDL2-Paket (`libsdl2-dev` für Ubuntu), [Python3](https://www.python.org/) (Version 3.8 oder höher) und `python3-pip` installiert haben, führen Sie den folgenden Befehl aus:

```sh
sudo pip3 install -U pyxel
```

Wenn der vorherige Befehl fehlschlägt, ziehen Sie in Betracht, Pyxel aus dem Quellcode zu bauen, indem Sie die Anweisungen im [Makefile](../Makefile) befolgen.

### Web

Die Web-Version von Pyxel benötigt keine Installation von Python oder Pyxel und läuft auf PCs, Smartphones und Tablets mit unterstützten Webbrowsern.

Für detaillierte Anweisungen konsultieren Sie bitte [diese Seite](pyxel-web-en.md).

### Beispiele ausführen

Nachdem Sie Pyxel installiert haben, können Sie die Beispiele mit dem folgenden Befehl in das aktuelle Verzeichnis kopieren:

```sh
pyxel copy_examples
```

Die folgenden Beispiele werden in Ihr aktuelles Verzeichnis kopiert:

<table>
<tr>
<td>01_hello_pyxel.py</td>
<td>Die einfachste Anwendung</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/01_hello_pyxel.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/01_hello_pyxel.py">Code</a></td>
</tr>
<tr>
<td>02_jump_game.py</td>
<td>Sprungspiel mit Pyxel-Ressourcendatei</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/02_jump_game.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/02_jump_game.py">Code</a></td>
</tr>
<tr>
<td>03_draw_api.py</td>
<td>Demonstration der Zeichen-APIs</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/03_draw_api.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/03_draw_api.py">Code</a></td>
</tr>
<tr>
<td>04_sound_api.py</td>
<td>Demonstration der Audio-APIs</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/04_sound_api.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/04_sound_api.py">Code</a></td>
</tr>
<tr>
<td>05_color_palette.py</td>
<td>Farbenpalettenliste</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/05_color_palette.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/05_color_palette.py">Code</a></td>
</tr>
<tr>
<td>06_click_game.py</td>
<td>Mausklickspiel</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/06_click_game.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/06_click_game.py">Code</a></td>
</tr>
<tr>
<td>07_snake.py</td>
<td>Schlangenspiel mit BGM</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/07_snake.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/07_snake.py">Code</a></td>
</tr>
<tr>
<td>08_triangle_api.py</td>
<td>Demonstration der Dreiecks-Zeichen-APIs</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/08_triangle_api.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/08_triangle_api.py">Code</a></td>
</tr>
<tr>
<td>09_shooter.py</td>
<td>Shoot'em up Spiel mit Bildschirmübergängen und MML</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/09_shooter.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/09_shooter.py">Code</a></td>
</tr>
<tr>
<td>10_platformer.py</td>
<td>Seiten-scrollendes Plattformspiel mit Karte</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/10_platformer.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/10_platformer.py">Code</a></td>
</tr>
<tr>
<td>11_offscreen.py</td>
<td>Offscreen-Rendering mit der Image-Klasse</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/11_offscreen.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/11_offscreen.py">Code</a></td>
</tr>
<tr>
<td>12_perlin_noise.py</td>
<td>Perlin-Rausch-Animation</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/12_perlin_noise.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/12_perlin_noise.py">Code</a></td>
</tr>
<tr>
<td>13_bitmap_font.py</td>
<td>Zeichnen einer Bitmap-Schriftart</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/13_bitmap_font.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/13_bitmap_font.py">Code</a></td>
</tr>
<tr>
<td>14_synthesizer.py</td>
<td>Synthesizer unter Verwendung von Audioerweiterungsfunktionen</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/14_synthesizer.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/14_synthesizer.py">Code</a></td>
</tr>
<tr>
<td>15_tiled_map_file.py</td>
<td>Laden und Zeichnen einer Tiled Map File (.tmx)</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/15_tiled_map_file.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/15_tiled_map_file.py">Code</a></td>
</tr>
<tr>
<td>16_transform.py</td>
<td>Bildrotation und -skalierung</td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/16_transform.html">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/16_transform.py">Code</a></td>
</tr>
<tr>
<td>99_flip_animation.py</td>
<td>Animation mit der Flip-Funktion (nur für Nicht-Web-Plattformen)</td>
<td><a href="https://github.com/kitao/pyxel/blob/main/docs/images/99_flip_animation.gif">Demo</a></td>
<td><a href="https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/99_flip_animation.py">Code</a></td>
</tr>
<tr>
<td>30sec_of_daylight.pyxapp</td>
<td>Gewinner des 1. Pyxel Jam von <a href="https://x.com/helpcomputer0">Adam</a></td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/30sec_of_daylight.html">Demo</a></td>
<td><a href="https://github.com/kitao/30SecondsOfDaylight">Code</a></td>
</tr>
<tr>
<td>megaball.pyxapp</td>
<td>Arcade Ball-Physikspiel von <a href="https://x.com/helpcomputer0">Adam</a></td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/megaball.html">Demo</a></td>
<td><a href="https://github.com/kitao/megaball">Code</a></td>
</tr>
<tr>
<td>8bit-bgm-gen.pyxapp</td>
<td>Hintergrundmusikgenerator von <a href="https://x.com/frenchbread1222">frenchbread</a></td>
<td><a href="https://kitao.github.io/pyxel/wasm/examples/8bit-bgm-gen.html">Demo</a></td>
<td><a href="https://github.com/shiromofufactory/8bit-bgm-generator">Code</a></td>
</tr>
</table>

Die Beispiele können mit den folgenden Befehlen ausgeführt werden:

```sh
cd pyxel_examples
pyxel run 01_hello_pyxel.py
pyxel play 30sec_of_daylight.pyxapp
```

## Verwendung

### Anwendung erstellen

Importieren Sie das Pyxel-Modul in Ihr Python-Skript, geben Sie die Fenstergröße mit der `init`-Funktion an und starten Sie die Pyxel-Anwendung mit der `run`-Funktion.

```python
import pyxel

pyxel.init(160, 120)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

pyxel.run(update, draw)
```

Die Argumente der `run`-Funktion sind die `update`-Funktion, die die Frame-Aktualisierungen verarbeitet, und die `draw`-Funktion, die das Zeichnen auf dem Bildschirm übernimmt.

In einer tatsächlichen Anwendung wird empfohlen, den Pyxel-Code in einer Klasse zu kapseln, wie im Folgenden gezeigt:

```python
import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()
```

Um einfache Grafiken ohne Animation zu erstellen, können Sie die `show`-Funktion verwenden, um Ihren Code zu vereinfachen.

```python
import pyxel

pyxel.init(120, 120)
pyxel.cls(1)
pyxel.circb(60, 60, 40, 7)
pyxel.show()
```

### Anwendung ausführen

Ein erstelltes Skript kann mit dem `python`-Befehl ausgeführt werden:

```sh
python PYTHON_SCRIPT_FILE
```

Es kann auch mit dem `pyxel run`-Befehl ausgeführt werden:

```sh
pyxel run PYTHON_SCRIPT_FILE
```

Darüber hinaus überwacht der Befehl `pyxel watch` Änderungen in einem angegebenen Verzeichnis und führt das Programm automatisch erneut aus, wenn Änderungen erkannt werden:

```sh
pyxel watch WATCH_DIR PYTHON_SCRIPT_FILE
```

Die Überwachung des Verzeichnisses kann durch Drücken von `Ctrl(Command)+C` gestoppt werden.

### Sondertastenoperationen

Während eine Pyxel-Anwendung läuft, können die folgenden speziellen Tastenaktionen ausgeführt werden:

- `Esc`<br>
  Die Anwendung beenden
- `Alt(Option)+1`<br>
  Den Screenshot auf dem Desktop speichern
- `Alt(Option)+2`<br>
  Den Startzeitpunkt der Bildschirmaufnahme zurücksetzen
- `Alt(Option)+3`<br>
  Ein Bildschirmaufnahmevideo auf dem Desktop speichern (bis zu 10 Sekunden)
- `Alt(Option)+8` oder `A+B+X+Y+DL` auf dem Gamepad<br>
  Die Bildschirmskalierung zwischen maximal und ganzzahlig umschalten
- `Alt(Option)+9` oder `A+B+X+Y+DR` auf dem Gamepad<br>
  Zwischen Bildschirmmodi (Crisp/Smooth/Retro) wechseln
- `Alt(Option)+0` oder `A+B+X+Y+DU` auf dem Gamepad<br>
  Den Leistungsmonitor (FPS/`update` Zeit/`draw` Zeit) umschalten
- `Alt(Option)+Enter` oder `A+B+X+Y+DD` auf dem Gamepad<br>
  Den Vollbildmodus umschalten
- `Shift+Alt(Option)+1/2/3`<br>
  Bildbank 0, 1 oder 2 auf dem Desktop speichern
- `Shift+Alt(Option)+0`<br>
  Die aktuelle Farbpalette auf dem Desktop speichern

### So erstellen Sie Ressourcen

Pyxel Editor kann Bilder und Klänge erstellen, die in einer Pyxel-Anwendung verwendet werden.

Sie können Pyxel Editor mit dem folgenden Befehl starten:

```sh
pyxel edit PYXEL_RESOURCE_FILE
```

Wenn die angegebene Pyxel-Ressourcendatei (.pyxres) vorhanden ist, wird sie geladen. Andernfalls wird eine neue Datei mit dem angegebenen Namen erstellt. Wenn die Ressourcendatei weggelassen wird, wird eine neue Datei mit dem Namen `my_resource.pyxres` erstellt.

Nachdem Sie Pyxel Editor gestartet haben, können Sie zu einer anderen Ressourcendatei wechseln, indem Sie diese auf Pyxel Editor ziehen und ablegen.

Die erstellte Ressourcendatei kann mit der `load`-Funktion geladen werden.

Pyxel Editor hat die folgenden Bearbeitungsmodi.

**Bildeditor**

Der Modus zum Bearbeiten des Bildes in jeder **Bilderbank**.

<a href="https://kitao.github.io/pyxel/wasm/examples/image_editor.html">
<img src="images/image_editor.gif">
</a>

Sie können eine Bilddatei (PNG/GIF/JPEG) in den Bildeditor ziehen und ablegen, um das Bild in die aktuell ausgewählte Bilderbank zu laden.

**Kachelkarteeditor**

Der Modus zum Bearbeiten von **Kachelkarten**, in denen Bilder aus den Bilderbanken in einem Kachelmuster angeordnet sind.

<a href="https://kitao.github.io/pyxel/wasm/examples/tilemap_editor.html">
<img src="images/tilemap_editor.gif">
</a>

Ziehen Sie eine TMX-Datei (Tiled Map File) in den Kachelkarteneditor, um deren ebene 0 in die aktuell ausgewählte Kachelkarte zu laden.

**Klangeditor**

Der Modus zum Bearbeiten von **Klängen**, die für Melodien und Effekte verwendet werden.

<a href="https://kitao.github.io/pyxel/wasm/examples/sound_editor.html">
<img src="images/sound_editor.gif">
</a>

**Musikeditor**

Der Modus zum Bearbeiten von **Musiken**, in denen die Klänge in der Reihenfolge der Wiedergabe angeordnet sind.

<a href="https://kitao.github.io/pyxel/wasm/examples/music_editor.html">
<img src="images/music_editor.gif">
</a>

### Weitere Methoden zur Erstellung von Ressourcen

Pyxel-Bilder und Kachelkarten können auch mit folgenden Methoden erstellt werden:

- Erstellen Sie ein Bild aus einer Liste von Zeichenfolgen mit der `Image.set`-Funktion oder der `Tilemap.set`-Funktion
- Laden Sie eine Bilddatei (PNG/GIF/JPEG) mit der `Image.load`-Funktion in die Pyxel-Palette

Pyxel-Klänge können ebenfalls mit der folgenden Methode erstellt werden:

- Erstellen Sie einen Klang aus Zeichenfolgen mit der `Sound.set`-Funktion oder der `Music.set`-Funktion

Bitte beachten Sie die API-Referenz für die Verwendung dieser Funktionen.

### So verteilen Sie Anwendungen

Pyxel unterstützt ein dediziertes Dateiformat für die Verteilung von Anwendungen (Pyxel-Anwendungsdatei), das plattformübergreifend ist.

Eine Pyxel-Anwendungsdatei (.pyxapp) wird mit dem Befehl `pyxel package` erstellt:

```sh
pyxel package APP_DIR STARTUP_SCRIPT_FILE
```

Wenn Sie Ressourcen oder zusätzliche Module einfügen möchten, legen Sie diese im Anwendungsverzeichnis ab.

Metadaten können zur Laufzeit angezeigt werden, indem Sie sie im folgenden Format im Startskript angeben. Felder außer `title` und `author` sind optional.

```python
# title: Pyxel Platformer
# author: Takashi Kitao
# desc: A Pyxel platformer example
# site: https://github.com/kitao/pyxel
# license: MIT
# version: 1.0
```

Die erstellte Anwendungsdatei kann mit dem Befehl `pyxel play` ausgeführt werden:

```sh
pyxel play PYXEL_APP_FILE
```

Eine Pyxel-Anwendungsdatei kann auch mit den Befehlen `pyxel app2exe` oder `pyxel app2html` in eine ausführbare Datei oder eine HTML-Datei umgewandelt werden.

## API-Referenz

### System

- `width`, `height`<br>
  Die Breite und Höhe des Bildschirms

- `frame_count`<br>
  Die Anzahl der vergangenen Frames

- `init(width, height, [title], [fps], [quit_key], [display_scale], [capture_scale], [capture_sec])`<br>
  Initialisiert die Pyxel-Anwendung mit der Bildschirmgröße (`width`, `height`). Folgende Optionen können angegeben werden: der Fenstertitel mit `title`, die Bildrate mit `fps`, die Taste zum Beenden der Anwendung mit `quit_key`, der Anzeigeskalierungsfaktor mit `display_scale`, der Bildaufnahmeskalierungsfaktor mit `capture_scale` und die maximale Aufnahmezeit des Bildschirmvideos mit `capture_sec`.<br>
  Beispiel: `pyxel.init(160, 120, title="My Pyxel App", fps=60, quit_key=pyxel.KEY_NONE, capture_scale=3, capture_sec=0)`

- `run(update, draw)`<br>
  Startet die Pyxel-Anwendung und ruft die `update`-Funktion zur Aktualisierung des Frames und die `draw`-Funktion zum Zeichnen auf.

- `show()`<br>
  Zeigt den Bildschirm an und wartet, bis die `Esc`-Taste gedrückt wird.

- `flip()`<br>
  Aktualisiert den Bildschirm um einen Frame. Die Anwendung beendet sich, wenn die `Esc`-Taste gedrückt wird. Diese Funktion ist in der Webversion nicht verfügbar.

- `quit()`<br>
  Beendet die Pyxel-Anwendung.

### Ressourcen

- `load(filename, [excl_images], [excl_tilemaps], [excl_sounds], [excl_musics])`<br>
  Lädt die Ressourcen-Datei (.pyxres). Wenn eine Option auf `True` gesetzt wird, wird die entsprechende Ressource vom Laden ausgeschlossen. Wenn im gleichen Verzeichnis wie die Ressourcen-Datei eine Palettendatei (.pyxpal) mit demselben Namen existiert, werden auch die Anzeigefarben der Palette aktualisiert. Die Palettendatei enthält hexadezimale Einträge für die Anzeigefarben (z.B. `1100ff`), getrennt durch Zeilenumbrüche. Die Palettendatei kann auch verwendet werden, um die in Pyxel Editor angezeigten Farben zu ändern.

- `user_data_dir(vendor_name, app_name)`<br>
  Gibt das basierend auf `vendor_name` und `app_name` erstellte Benutzerverzeichnis zurück. Wenn das Verzeichnis nicht existiert, wird es automatisch erstellt. Es wird verwendet, um Highscores, Spielfortschritte und ähnliche Daten zu speichern.<br>
  Beispiel: `print(pyxel.user_data_dir("Takashi Kitao", "Pyxel Shooter"))`

### Eingabe

- `mouse_x`, `mouse_y`<br>
  Die aktuelle Position des Mauszeigers

- `mouse_wheel`<br>
  Der aktuelle Wert des Mausrads

- `btn(key)`<br>
  Gibt `True` zurück, wenn die Taste `key` gedrückt ist, andernfalls `False`. ([Liste der Tastendefinitionen](../python/pyxel/__init__.pyi))

- `btnp(key, [hold], [repeat])`<br>
  Gibt `True` zurück, wenn die Taste `key` in diesem Frame gedrückt wurde, andernfalls `False`. Wenn `hold` und `repeat` angegeben sind, wird nach dem Halten der Taste `key` für `hold` Frames oder länger, `True` alle `repeat` Frames zurückgegeben.

- `btnr(key)`<br>
  Gibt `True` zurück, wenn die Taste `key` in diesem Frame losgelassen wurde, andernfalls `False`.

- `mouse(visible)`<br>
  Zeigt den Mauszeiger an, wenn `visible` `True` ist, und blendet ihn aus, wenn `visible` `False` ist. Auch wenn der Mauszeiger ausgeblendet ist, wird seine Position weiterhin aktualisiert.

### Grafik

- `colors`<br>
  Liste der Anzeigefarben der Palette. Die Anzeigefarbe wird durch einen 24-Bit-Wert angegeben. Verwende `colors.from_list` und `colors.to_list`, um Python-Listen direkt zuzuweisen und abzurufen.<br>
  Beispiel: `old_colors = pyxel.colors.to_list(); pyxel.colors.from_list([0x111111, 0x222222, 0x333333]); pyxel.colors[15] = 0x112233`

- `images`<br>
  Liste der Bildbanken (Instanzen der Image-Klasse) (0-2)<br>
  Beispiel: `pyxel.images[0].load(0, 0, "title.png")`

- `tilemaps`<br>
  Liste der Kachelkarten (Instanzen der Tilemap-Klasse) (0-7)

- `clip(x, y, w, h)`<br>
  Setzt den Zeichenbereich des Bildschirms von (`x`, `y`) mit einer Breite von `w` und einer Höhe von `h`. Rufe `clip()` auf, um den Zeichenbereich auf den gesamten Bildschirm zurückzusetzen.

- `camera(x, y)`<br>
  Ändert die Koordinaten der oberen linken Ecke des Bildschirms in (`x`, `y`). Rufe `camera()` auf, um die Koordinaten der oberen linken Ecke auf (`0`, `0`) zurückzusetzen.

- `pal(col1, col2)`<br>
  Ersetzt beim Zeichnen die Farbe `col1` durch `col2`. Rufe `pal()` auf, um zur ursprünglichen Palette zurückzukehren.

- `dither(alpha)`<br>
  Wendet beim Zeichnen Dithering (Pseudo-Transparenz) an. Setze `alpha` im Bereich von `0.0` bis `1.0`, wobei `0.0` transparent und `1.0` undurchsichtig ist.

- `cls(col)`<br>
  Löscht den Bildschirm mit der Farbe `col`.

- `pget(x, y)`<br>
  Gibt die Farbe des Pixels bei (`x`, `y`) zurück.

- `pset(x, y, col)`<br>
  Zeichnet ein Pixel mit der Farbe `col` bei (`x`, `y`).

- `line(x1, y1, x2, y2, col)`<br>
  Zeichnet eine Linie in der Farbe `col` von (`x1`, `y1`) nach (`x2`, `y2`).

- `rect(x, y, w, h, col)`<br>
  Zeichnet ein Rechteck mit einer Breite von `w`, einer Höhe von `h` und der Farbe `col` ab (`x`, `y`).

- `rectb(x, y, w, h, col)`<br>
  Zeichnet die Umrisse eines Rechtecks mit einer Breite von `w`, einer Höhe von `h` und der Farbe `col` ab (`x`, `y`).

- `circ(x, y, r, col)`<br>
  Zeichnet einen Kreis mit einem Radius von `r` und der Farbe `col` bei (`x`, `y`).

- `circb(x, y, r, col)`<br>
  Zeichnet die Umrisse eines Kreises mit einem Radius von `r` und der Farbe `col` bei (`x`, `y`).

- `elli(x, y, w, h, col)`<br>
  Zeichnet eine Ellipse mit einer Breite von `w`, einer Höhe von `h` und der Farbe `col` ab (`x`, `y`).

- `ellib(x, y, w, h, col)`<br>
  Zeichnet die Umrisse einer Ellipse mit einer Breite von `w`, einer Höhe von `h` und der Farbe `col` ab (`x`, `y`).

- `tri(x1, y1, x2, y2, x3, y3, col)`<br>
  Zeichnet ein Dreieck mit den Eckpunkten (`x1`, `y1`), (`x2`, `y2`), (`x3`, `y3`) und der Farbe `col`.

- `trib(x1, y1, x2, y2, x3, y3, col)`<br>
  Zeichnet die Umrisse eines Dreiecks mit den Eckpunkten (`x1`, `y1`), (`x2`, `y2`), (`x3`, `y3`) und der Farbe `col`.

- `fill(x, y, col)`<br>
  Füllt den Bereich, der mit der gleichen Farbe wie (`x`, `y`) verbunden ist, mit der Farbe `col`.

- `blt(x, y, img, u, v, w, h, [colkey], [rotate], [scale])`<br>
  Kopiert den Bereich der Größe (`w`, `h`) von (`u`, `v`) der Bildbank `img`(0-2) nach (`x`, `y`). Wenn `w` und/oder `h` einen negativen Wert haben, wird der Bereich horizontal und/oder vertikal gespiegelt. Wenn `colkey` angegeben ist, wird diese Farbe als transparent behandelt. Wenn `rotate` (in Grad), `scale` (1.0 = 100%) oder beides angegeben sind, werden die entsprechenden Transformationen angewendet.

<img src="images/blt_figure.png">

- `bltm(x, y, tm, u, v, w, h, [colkey], [rotate], [scale])`<br>
  Kopiert den Bereich der Größe (`w`, `h`) von (`u`, `v`) der Kachelkarte `tm` (0-7) nach (`x`, `y`). Wenn `w` und/oder `h` einen negativen Wert haben, wird der Bereich horizontal und/oder vertikal gespiegelt. Wenn `colkey` angegeben ist, wird diese Farbe als transparent behandelt. Wenn `rotate` (in Grad), `scale` (1.0 = 100%) oder beides angegeben sind, werden die entsprechenden Transformationen angewendet. Die Größe einer Kachel beträgt 8x8 Pixel und wird als Tupel `(image_tx, image_ty)` in der Kachelkarte gespeichert.

<img src="images/bltm_figure.png">

- `text(x, y, s, col)`<br>
  Zeichnet den String `s` in der Farbe `col` bei (`x`, `y`).

### Audio

- `sounds`<br>
  Liste der Klänge (Instanzen der Sound-Klasse) (0-63)<br>
  Beispiel: `pyxel.sounds[0].speed = 60`

- `musics`<br>
  Liste der Musiken (Instanzen der Music-Klasse) (0-7)

- `play(ch, snd, [tick], [loop], [resume])`<br>
  Spielt den Klang `snd`(0-63) auf dem Kanal `ch`(0-3). Wenn `snd` eine Liste ist, werden die Klänge nacheinander abgespielt. Die Startposition kann durch `tick` (1 Tick = 1/120 Sekunden) angegeben werden. Wenn `loop` auf `True` gesetzt ist, wird die Wiedergabe wiederholt. Um nach dem Ende der Wiedergabe zum vorherigen Klang zurückzukehren, setze `resume` auf `True`.

- `playm(msc, [tick], [loop])`<br>
  Spielt die Musik `msc`(0-7). Die Startposition kann durch `tick` (1 Tick = 1/120 Sekunden) angegeben werden. Wenn `loop` auf `True` gesetzt ist, wird die Wiedergabe wiederholt.

- `stop([ch])`<br>
  Stoppt die Wiedergabe des angegebenen Kanals `ch`(0-3). Rufe `stop()` auf, um alle Kanäle zu stoppen.

- `play_pos(ch)`<br>
  Gibt die Wiedergabeposition des Klangs auf Kanal `ch`(0-3) als Tupel `(sound_no, note_no)` zurück. Gibt `None` zurück, wenn die Wiedergabe gestoppt wurde.

### Mathematik

- `ceil(x)`<br>
  Gibt die kleinste ganze Zahl zurück, die größer oder gleich `x` ist.

- `floor(x)`<br>
  Gibt die größte ganze Zahl zurück, die kleiner oder gleich `x` ist.

- `sgn(x)`<br>
  Gibt `1` zurück, wenn `x` positiv ist, `0`, wenn es `0` ist, und `-1`, wenn es negativ ist.

- `sqrt(x)`<br>
  Gibt die Quadratwurzel von `x` zurück.

- `sin(deg)`<br>
  Gibt den Sinus von `deg` Grad zurück.

- `cos(deg)`<br>
  Gibt den Kosinus von `deg` Grad zurück.

- `atan2(y, x)`<br>
  Gibt den Arkustangens von `y`/`x` in Grad zurück.

- `rseed(seed)`<br>
  Setzt den Seed des Zufallszahlengenerators.

- `rndi(a, b)`<br>
  Gibt eine zufällige Ganzzahl zurück, die größer oder gleich `a` und kleiner oder gleich `b` ist.

- `rndf(a, b)`<br>
  Gibt eine zufällige Gleitkommazahl zurück, die größer oder gleich `a` und kleiner oder gleich `b` ist.

- `nseed(seed)`<br>
  Setzt den Seed des Perlin-Rauschens.

- `noise(x, [y], [z])`<br>
  Gibt den Perlin-Rauschwert für die angegebenen Koordinaten zurück.

### Image-Klasse

- `width`, `height`<br>
  Die Breite und Höhe des Bildes

- `set(x, y, data)`<br>
  Setzt das Bild bei (`x`, `y`) mithilfe einer Liste von Strings.<br>
  Beispiel: `pyxel.images[0].set(10, 10, ["0123", "4567", "89ab", "cdef"])`

- `load(x, y, filename)`<br>
  Lädt eine Bilddatei (PNG/GIF/JPEG) bei (`x`, `y`).

- `pget(x, y)`<br>
  Gibt die Farbe des Pixels bei (`x`, `y`) zurück.

- `pset(x, y, col)`<br>
  Zeichnet ein Pixel mit der Farbe `col` bei (`x`, `y`).

### Tilemap-Klasse

- `width`, `height`<br>
  Die Breite und Höhe der Kachelkarte

- `imgsrc`<br>
  Das Bildbank (0-2), das von der Kachelkarte referenziert wird

- `set(x, y, data)`<br>
  Setzt die Kachelkarte bei (`x`, `y`) mithilfe einer Liste von Strings.<br>
  Beispiel: `pyxel.tilemap(0).set(0, 0, ["0000 0100 a0b0", "0001 0101 a1b1"])`

- `load(x, y, filename, layer)`<br>
  Lädt die `layer`(0-) aus der TMX-Datei (Tiled Map File) bei (`x`, `y`).

- `pget(x, y)`<br>
  Gibt die Kachel bei (`x`, `y`) zurück. Eine Kachel wird als Tupel `(image_tx, image_ty)` dargestellt.

- `pset(x, y, tile)`<br>
  Zeichnet eine Kachel bei (`x`, `y`). Eine Kachel wird als Tupel `(image_tx, image_ty)` dargestellt.

### Sound-Klasse

- `notes`<br>
  Liste der Noten (0-127). Je höher die Zahl, desto höher der Ton. Note `33` entspricht 'A2'(440Hz). Pausen werden durch `-1` dargestellt.

- `tones`<br>
  Liste der Töne (0:Triangle / 1:Square / 2:Pulse / 3:Noise)

- `volumes`<br>
  Liste der Lautstärken (0-7)

- `effects`<br>
  Liste der Effekte (0:None / 1:Slide / 2:Vibrato / 3:FadeOut / 4:Half-FadeOut / 5:Quarter-FadeOut)

- `speed`<br>
  Wiedergabegeschwindigkeit. `1` ist die schnellste, und je größer die Zahl, desto langsamer die Wiedergabe. Bei `120` dauert ein Ton 1 Sekunde.

- `set(notes, tones, volumes, effects, speed)`<br>
  Setzt Noten, Töne, Lautstärken und Effekte mithilfe eines Strings. Wenn die Länge der Töne, Lautstärken oder Effekte kürzer als die Noten ist, werden sie von Anfang an wiederholt.

- `set_notes(notes)`<br>
  Setzt die Noten mithilfe eines Strings aus `CDEFGAB`+`#-`+`01234` oder `R`. Es wird nicht zwischen Groß- und Kleinschreibung unterschieden, und Leerzeichen werden ignoriert.<br>
  Beispiel: `pyxel.sounds[0].set_notes("g2b-2d3r rf3f3f3")`

- `set_tones(tones)`<br>
  Setzt die Töne mithilfe eines Strings aus `TSPN`. Es wird nicht zwischen Groß- und Kleinschreibung unterschieden, und Leerzeichen werden ignoriert.<br>
  Beispiel: `pyxel.sounds[0].set_tones("ttss pppn")`

- `set_volumes(volumes)`<br>
  Setzt die Lautstärken mithilfe eines Strings aus `01234567`. Es wird nicht zwischen Groß- und Kleinschreibung unterschieden, und Leerzeichen werden ignoriert.<br>
  Beispiel: `pyxel.sounds[0].set_volumes("7777 7531")`

- `set_effects(effects)`<br>
  Setzt die Effekte mithilfe eines Strings aus `NSVFHQ`. Es wird nicht zwischen Groß- und Kleinschreibung unterschieden, und Leerzeichen werden ignoriert.<br>
  Beispiel: `pyxel.sounds[0].set_effects("nfnf nvvs")`

- `mml(mml_str)`<br>
  Legt die zugehörigen Parameter mithilfe von [Music Macro Language (MML)](https://en.wikipedia.org/wiki/Music_Macro_Language) fest. Verfügbare Befehle sind `T`(1-900), `@`(0-3), `O`(0-4), `>`, `<`, `Q`(1-8), `V`(0-7), `X`(0-7), `L`(1/2/4/8/16/32) und `CDEFGABR`+`#+-`+`.~&`. Weitere Informationen zu den Befehlen finden Sie auf [dieser Seite](faq-en.md).<br>
  Beispiel: `pyxel.sounds[0].mml("t120 @1 o3 q6 l8 x0:12345 c4&c<g16r16>c.<g16 v4 >c.&d16 x0 e2~c2~")`

- `save(filename, count, [ffmpeg])`<br>
  Erstellt eine WAV-Datei, die den Sound `count`-mal wiederholt. Wenn FFmpeg installiert ist und `ffmpeg` auf `True` gesetzt wird, wird auch eine MP4-Datei erstellt.

### Music-Klasse

- `seqs`<br>
  Eine zweidimensionale Liste der Klänge (0-63) über mehrere Kanäle

- `set(seq0, seq1, seq2, ...)`<br>
  Setzt die Listen von Klängen (0-63) für jeden Kanal. Wenn eine leere Liste angegeben wird, wird dieser Kanal nicht für die Wiedergabe verwendet.<br>
  Beispiel: `pyxel.musics[0].set([0, 1], [], [3])`

- `save(filename, count, [ffmpeg])`<br>
  Erstellt eine WAV-Datei, die die Musik `count`-mal wiederholt. Wenn FFmpeg installiert ist und `ffmpeg` auf `True` gesetzt wird, wird auch eine MP4-Datei erstellt.

### Fortgeschrittene API

Pyxel enthält eine "Fortgeschrittene API", die in diesem Dokument nicht erwähnt wird, da sie Benutzer verwirren oder spezielles Wissen erfordern könnte.

Wenn Sie von Ihren Fähigkeiten überzeugt sind, versuchen Sie, mit [diesem](../python/pyxel/__init__.pyi) als Leitfaden erstaunliche Werke zu schaffen!

## Wie man beiträgt

### Probleme melden

Verwenden Sie den [Issue Tracker](https://github.com/kitao/pyxel/issues), um Fehlerberichte und Funktions- oder Verbesserungsanfragen einzureichen. Stellen Sie sicher, dass es vor der Einreichung eines neuen Problems keine ähnlichen offenen Probleme gibt.

### Funktionstest

Jeder, der den Code manuell testet und Fehler oder Verbesserungsvorschläge im [Issue Tracker](https://github.com/kitao/pyxel/issues) meldet, ist sehr willkommen!

### Pull-Requests einreichen

Patches und Fixes werden in Form von Pull-Requests (PRs) akzeptiert. Stellen Sie sicher, dass das Problem, das der Pull-Request behandelt, im Issue Tracker offen ist.

Die Einreichung eines Pull-Requests impliziert, dass Sie zustimmen, Ihren Beitrag unter der [MIT-Lizenz](../LICENSE) zu lizenzieren.

## Weitere Informationen

- [FAQ](faq-en.md)
- [Benutzersamples](https://github.com/kitao/pyxel/wiki/Pyxel-User-Examples)
- [Entwicklers X-Konto](https://x.com/kitao)
- [Discord-Server (Englisch)](https://discord.gg/Z87eYHN)
- [Discord-Server (Japanisch)](https://discord.gg/qHA5BCS)

## Lizenz

Pyxel ist lizenziert unter der [MIT-Lizenz](../LICENSE). Es kann in proprietärer Software wiederverwendet werden, vorausgesetzt, dass alle Kopien der Software oder wesentliche Teile davon eine Kopie der MIT-Lizenzbedingungen und einen Copyright-Hinweis enthalten.

## Sponsoren suchen

Pyxel sucht Sponsoren auf GitHub Sponsors. Bitte ziehen Sie in Betracht, Pyxel zu sponsern, um dessen fortlaufende Wartung und Funktionsentwicklung zu unterstützen. Als Vorteil können Sponsoren direkt mit dem Pyxel-Entwickler beraten. Für weitere Details besuchen Sie bitte [diese Seite](https://github.com/sponsors/kitao).
