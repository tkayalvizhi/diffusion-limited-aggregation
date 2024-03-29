import os

from tkinter import *
from PIL import Image, ImageTk
from Field import Field
import numpy as np


def transform_matrix(matrix):
    return 255 - matrix * 255


def save(img, count, folder_name):
    img = img.convert("L")
    img.save(folder_name + '/' + f'img_{str(count).zfill(5)}.png')


class DlaSimulation(object):
    def __init__(self, dimension,
                 stickiness=0.05,
                 drift: float = 1,
                 radius=500,
                 frame_rate=100,
                 iterations=40000,
                 folder_name: str = 'frames',
                 from_edge=False):

        self.master = Tk()
        self.master.update()
        self.field = Field(dim=dimension,
                           stickiness=stickiness,
                           drift=drift,
                           radius=radius,
                           from_edge=from_edge)

        if not os.path.isdir(folder_name + '/'):
            os.mkdir(folder_name + '/')

        # if not os.path.isdir(folder_name + '/matrix/'):
        #     os.mkdir(folder_name + '/matrix/')

        self.canvas = Canvas(self.master, width=dimension, height=dimension)
        self.canvas.pack()
        self.run(iterations, frame_rate, folder_name)
        self.master.mainloop()

    def run(self, iterations, frame_rate, folder_name):
        # step = 0
        for matrix, count in self.field.random_walk(iterations):
            # img = Image.fromarray(transform_matrix(matrix))
            # save(img, step, folder_name)
            # self.update_canvas(img)
            # step += 1
            if count % frame_rate == 0:
                img = Image.fromarray(transform_matrix(matrix))
                self.update_canvas(img)
                save(img, count, folder_name)
                # step += 1
                # np.save(folder_name+"/matrix/matrix.npy")

    def update_canvas(self, img):
        imgTk = ImageTk.PhotoImage(image=img)
        self.canvas.create_image(0, 0, image=imgTk, anchor='nw')
        self.master.update()


if __name__ == "__main__":

    if sys.argv[7].lower() == 'true':
        from_edge = True
    else:
        from_edge = False

    file = open("arguments.txt", 'a')
    file.write(f'{sys.argv}\n')
    file.close()

    DlaSimulation(dimension=int(sys.argv[1]),
                  stickiness=float(sys.argv[2]),
                  drift=float(sys.argv[3]),
                  radius=int(sys.argv[4]),
                  iterations=int(sys.argv[5]),
                  folder_name=sys.argv[6],
                  from_edge=from_edge,
                  frame_rate=int(sys.argv[8])
                  )
