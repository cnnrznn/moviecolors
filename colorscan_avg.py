import imageio
import numpy as np
import sys

fn = sys.argv[1]
#outfn = sys.argv[2]

reader = imageio.get_reader(fn)
#fps = reader.get_meta_data()['fps']
#writer = imageio.get_writer(outfn, fps=fps)

for i, im in enumerate(reader):
    color = np.mean(im, axis=(0, 1))
    print('{} {} {}'.format(color[0], color[1], color[2]))
    #im[:, :, :] = color
    #writer.append_data(im)

#writer.close()
