import os
import sys
import cv2
import platform
import numpy as np
import matplotlib.pyplot as plt


BASE_PATH: str   = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH: str  = os.path.join(BASE_PATH, "input")
OUTPUT_PATH: str = os.path.join(BASE_PATH, "output")


def get_image(path: str) -> np.ndarray:
    return cv2.cvtColor(src=cv2.imread(path, cv2.IMREAD_COLOR), code=cv2.COLOR_BGR2RGB)


def show_images(
    image_1: np.ndarray,
    image_2: np.ndarray, 
    cmap_1: str="gnuplot2",
    cmap_2: str="gnuplot2",
    title_1: str="Original",
    title_2: str="Processed",
) -> None:

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(image_1, cmap=cmap_1)
    plt.axis("off")
    if title_1: plt.title(title_1)
    plt.subplot(1, 2, 2)
    plt.imshow(image_2, cmap=cmap_2)
    plt.axis("off")
    if title_2: plt.title(title_2)
    if platform.system() == "Windows":
        figmanager = plt.get_current_fig_manager()
        figmanager.window.state("zoomed")
    plt.show()


def main():

    args_1: tuple = ("--filename", "-f")
    args_2: tuple = ("--new-red", "-nr")
    args_3: tuple = ("--new-green", "-ng")
    args_4: tuple = ("--new-blue", "-nb")
    args_5: tuple = ("--save", "-s")

    filename: str = "Test_1.jpg"
    new_red: int = 0
    new_green: int = 0
    new_blue: int = 0
    save: bool = False

    if args_1[0] in sys.argv: filename = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv: new_red = int(sys.argv[sys.argv.index(args_2[0]) + 1])
    if args_2[1] in sys.argv: new_red = int(sys.argv[sys.argv.index(args_2[1]) + 1])

    if args_3[0] in sys.argv: new_green = int(sys.argv[sys.argv.index(args_3[0]) + 1])
    if args_3[1] in sys.argv: new_green = int(sys.argv[sys.argv.index(args_3[1]) + 1])

    if args_4[0] in sys.argv: new_blue = int(sys.argv[sys.argv.index(args_4[0]) + 1])
    if args_4[1] in sys.argv: new_blue = int(sys.argv[sys.argv.index(args_4[1]) + 1])

    if args_5[0] in sys.argv or args_5[1] in sys.argv: save = True

    assert filename in os.listdir(INPUT_PATH), f"{filename} not found in input directory"
    assert new_red >= 0 and new_red <= 255, "Supported value range = [0 - 255]"
    assert new_green >= 0 and new_green <= 255, "Supported value range = [0 - 255]"
    assert new_blue >= 0 and new_blue <= 255, "Supported value range = [0 - 255]"

    image = get_image(os.path.join(INPUT_PATH, filename))

    def get_color(event):
        global r, g, b
        r = image[int(event.ydata), int(event.xdata), 0]
        g = image[int(event.ydata), int(event.xdata), 1]
        b = image[int(event.ydata), int(event.xdata), 2]
        plt.close()
    
    fig = plt.figure()
    fig.canvas.mpl_connect("button_press_event", get_color)
    plt.imshow(image, cmap="gnuplot2")
    plt.axis("off")
    plt.title("Click anywhere on the image")
    if platform.system() == "Windows":
        figmanager = plt.get_current_fig_manager()
        figmanager.window.state("zoomed")
    plt.show()

    new_image = image.copy()
    new_image = np.where(new_image == (r, g, b), (new_red, new_green, new_blue), new_image).astype("uint8")

    if save: 
        cv2.imwrite(os.path.join(OUTPUT_PATH, filename[:-4] + " - Processed.jpg"), cv2.cvtColor(src=new_image, code=cv2.COLOR_RGB2BGR))
    else: 
        show_images(image, new_image)


if __name__ == "__main__":
    sys.exit(main() or 0)
