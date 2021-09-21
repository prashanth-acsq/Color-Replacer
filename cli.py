import sys
import numpy as np
import matplotlib.pyplot as plt

import utils as u

#####################################################################################################

### USING OPENCV PLOTTING BACKEND ###

# from cv2 import namedWindow, setMouseCallback, destroyAllWindows, EVENT_LBUTTONDOWN

# args_1 = "--name"
# args_2 = "--factor"

# name = "Image_1.jpg"
# factor = None
# r, g, b = 0, 0, 0

# if args_1 in sys.argv:
#     name = sys.argv[sys.argv.index(args_1) + 1]
# if args_2 in sys.argv:
#     factor = float(sys.argv[sys.argv.index(args_2) + 1])

# if factor:
#     image = u.downscale(u.read_image(name), False), factor=factor)
# else:
#     image = u.read_image(name, False)


# def app():
#     args_1 = "--new-color"
#     new_r, new_g, new_b = 0, 0, 0
    
#     if args_1 in sys.argv:
#         new_r = int(sys.argv[sys.argv.index(args_1) + 1])
#         new_g = int(sys.argv[sys.argv.index(args_1) + 2])
#         new_b = int(sys.argv[sys.argv.index(args_1) + 3])


#     def get_color(event, x, y, flags, param):
#         global r, g, b, image
#         if(event == EVENT_LBUTTONDOWN):
#             print(x, y)
#             r, g, b = image[y, x, 2], image[y, x, 1], image[y, x, 0]
    
#     winname = "Image"
#     namedWindow(winname)
#     setMouseCallback(winname, get_color)
#     u.cv2_show(image, winname)
#     destroyAllWindows()

#     new_image = image.copy()
#     new_image = np.where(new_image == (b, g, r), (new_b, new_g, new_r), new_image).astype("uint8")

#     u.cv2_show(new_image, "New Image")
#     destroyAllWindows()

#####################################################################################################

### USING MATPLOTLIB PLOTTING BACKEND ###

def app():
    args_1 = "--name"
    args_2 = "--factor"
    args_3 = "--new-color"
    args_4 = "--save"

    name = "Image_1.jpg"
    factor = None
    new_r, new_g, new_b = 0, 0, 0
    save = None

    if args_1 in sys.argv:
        name = sys.argv[sys.argv.index(args_1) + 1]
    if args_2 in sys.argv:
        factor = float(sys.argv[sys.argv.index(args_2) + 1])
    if args_3 in sys.argv:
        new_r = int(sys.argv[sys.argv.index(args_3) + 1])
        new_g = int(sys.argv[sys.argv.index(args_3) + 2])
        new_b = int(sys.argv[sys.argv.index(args_3) + 3])
    if args_4 in sys.argv:
        save = True

    if factor:
        image = u.downscale(u.read_image(name, True), factor=factor)
    else:
        image = u.read_image(name, True)
    
    def get_color(event):
        global r, g, b
        r = image[int(event.ydata), int(event.xdata), 0]
        g = image[int(event.ydata), int(event.xdata), 1]
        b = image[int(event.ydata), int(event.xdata), 2]
    
    fig = plt.figure()
    fig.canvas.mpl_connect("button_press_event", get_color)
    plt.imshow(image)
    plt.axis("off")
    plt.show()

    new_image = image.copy()
    new_image = np.where(new_image == (r, g, b), (new_r, new_g, new_b), new_image).astype("uint8")

    if save:
        u.save_image(name, new_image, True)
    else:
        u.show(new_image, True)

#####################################################################################################

# # Same Result
# new_image[:, :, 0][new_image[:, :, 0] == r] = new_r
# new_image[:, :, 1][new_image[:, :, 1] == g] = new_g
# new_image[:, :, 2][new_image[:, :, 2] == b] = new_b

#####################################################################################################

