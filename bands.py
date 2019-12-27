import svgwrite
import sys

_width='1'

fn = sys.argv[1]
outfn = sys.argv[2]

data = []

with open(fn) as inf:
    for line in inf:
        color = [float(x) for x in line.split()]
        data.append(color)

draw = svgwrite.Drawing(filename=outfn, height='100%', width='100%',
                        viewBox='0 0 {} {}'.format(_width, len(data)),
                        preserveAspectRatio='none')

for i, d in enumerate(data):
    draw.add(svgwrite.shapes.Line(start=(0, i), end=(_width, i),
                    style='stroke:rgb({},{},{})'.format(d[0], d[1], d[2])))

draw.save()
