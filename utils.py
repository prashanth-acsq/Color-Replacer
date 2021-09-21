import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from termcolor import colored
os.system("color")

#####################################################################################################

def myprint(text: str, color: str) -> None:
    print(colored(text=text, color=color))


def breaker(num=50, char="*"):
    myprint("\n" + num*char + "\n", "magenta")

#####################################################################################################

def downscale(image: np.ndarray, factor: float) -> np.ndarray:
    if len(image.shape) == 2:
        h, w = image.shape
    elif len(image.shape) == 3:
        h, w, _ = image.shape
    return cv2.resize(src=image, dsize=(int(w/factor), int(h/factor)))


def read_image(name: str, change_color_space=True) -> np.ndarray:
    if change_color_space:
        return cv2.cvtColor(src=cv2.imread(os.path.join(READ_PATH, name), cv2.IMREAD_COLOR), code=cv2.COLOR_BGR2RGB)
    else:
        return cv2.imread(READ_PATH, name, cv2.IMREAD_COLOR)


def save_image(name: str, image: np.ndarray, change_color_space=True) -> None:
    if change_color_space:
        cv2.imwrite(os.path.join(SAVE_PATH, name), cv2.cvtColor(src=image, code=cv2.COLOR_RGB2BGR))
    else:
        cv2.imwrite(os.path.join(SAVE_PATH, name), image)


def show(image: np.ndarray, title=None) -> None:
    plt.figure()
    plt.imshow(image)
    plt.axis("off")
    if title:
        plt.title(title)
    plt.show()


def cv2_show(image: np.ndarray, winname: str):
    cv2.imshow(winname=winname, mat=image)
    cv2.waitKey(0)

#####################################################################################################

READ_PATH = "./Files"
SAVE_PATH = "./Processed"

#####################################################################################################
