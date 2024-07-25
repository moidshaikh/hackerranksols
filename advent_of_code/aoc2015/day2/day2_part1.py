

def process_gift(d) -> int:
    l, w, h = map(int, d.split('x'))
    areas = [2*l*w, 2*w*h, 2*h*l]
    surface_area = sum(areas)
    extra_paper = int(min(areas)/2)
    return surface_area + extra_paper

with open('input', 'r') as f:
    dimensions_str = f.read()
    
all_dimensions = dimensions_str.splitlines()

areas = list(map(process_gift, all_dimensions))

print(sum(areas))

# for dimension in all_dimensions:
#     area = process_gift(dimension)
#     print(f"{dimension=}, {area=}")