import multiprocessing as mp
import queue
from pathlib import Path
from threading import Thread
from time import sleep

from PIL import Image

def print_number(mp_queue: mp.Queue) -> None:
    while True:
        msg = mp_queue.get()

        if msg == "stop":
            print("Stopping Process")
            break

        else:
            thread = Thread(target=load_image, args=(msg,))
            thread.start()

def load_image(msg: Path) -> None:
    print(f'Loading {msg.name}')
    image = Image.open(msg)
    print(f'Loaded {msg.name}: {image.width}x{image.height}')
    image.thumbnail((128, 128))
    print(f'Thumb {msg.name}: {image.width}x{image.height}')
    rawImage = image.tobytes()
    format = image.mode
    formatLength = len(format) if format else 4
    # pygImage = ImageData(image.width, image.height, format, rawImage, -image.width * formatLength)
    # sprite = Sprite(pygImage)

def main() -> None:
    mp_queue = mp.Queue()
    process = mp.Process(target=print_number, args=(queue,))
    process.start()

    folder = Path('/Users/steve/Pictures/Yasmin Disney')

    for image in folder.iterdir():
        if image.suffix.lower() in ['.jpg', 'jpeg']:
            mp_queue.put(image)

    mp_queue.put("stop")

    print("Waiting for Process to Stop")

    while process.is_alive():
        sleep(0.05)

    process.close()

if __name__ == "__main__":
    main()
