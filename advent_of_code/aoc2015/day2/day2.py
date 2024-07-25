

def process_gift(d) -> int:
    l, w, h = map(int, d.split('x'))
    sides = sorted([l,w,h])
    ribbon = 2*sides[0] + 2*sides[1]
    bow = l*w*h
    return bow + ribbon


with open('input', 'r') as f:
    dimensions_str = f.read()

all_dimensions = dimensions_str.splitlines()

areas = list(map(process_gift, all_dimensions))

print(sum(areas))

# for dimension in all_dimensions:
#     area = process_gift(dimension)
#     print(f"{dimension=}, {area=}")