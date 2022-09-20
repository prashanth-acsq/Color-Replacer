import os
import sys
import cv2
import argparse
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
    figmanager = plt.get_current_fig_manager()
    figmanager.window.state("zoomed")
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f", type=str, default="Test_1.jpg", help="Filename of the Image")
    parser.add_argument("--downscale", "-ds", type=float, default=None, help="Downscale Factor")
    parser.add_argument("--new-red", "-nr", type=int, default=0, help="New Red Channel Color [0, 255]")
    parser.add_argument("--new-green", "-ng", type=int, default=0, help="New Green  Channel Color [0, 255]")
    parser.add_argument("--new-blue", "-nb", type=int, default=0, help="New Blue Channel Color [0, 255]")
    parser.add_argument("--save", "-s", action="store_true", help="Save Mode")
    args = parser.parse_args()

    assert args.filename in os.listdir(INPUT_PATH), "File not foundin input directory"
    assert args.new_red >= 0 and args.new_red <= 255, "[0 - 255]"
    assert args.new_green >= 0 and args.new_green <= 255, "[0 - 255]"
    assert args.new_blue >= 0 and args.new_blue <= 255, "[0 - 255]"

    image = get_image(os.path.join(INPUT_PATH, args.filename))

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
    figmanager = plt.get_current_fig_manager()
    figmanager.window.state("zoomed")
    plt.show()

    new_image = image.copy()
    new_image = np.where(new_image == (r, g, b), (args.new_red, args.new_green, args.new_blue), new_image).astype("uint8")

    if args.save: cv2.imwrite(os.path.join(OUTPUT_PATH, args.filename[:-4] + " - Processed.jpg"), cv2.cvtColor(src=new_image, code=cv2.COLOR_RGB2BGR))
    else: show_images(image, new_image)

if __name__ == "__main__":
    sys.exit(main() or 0)
