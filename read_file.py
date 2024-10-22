def read_layout(filepath):
    with open(filepath, 'r') as file:
        first_line = file.readline()
        vars = first_line.strip()
        x, y, x_start, y_start, num_items = vars.split()
        layout = [list(line.strip()) for line in file]
        return int(x), int(y), int(x_start), int(y_start), int(num_items), layout

#scenario_{a-d}{0-4}
filepath = 'scenario_a0.txt'
x, y, x_start, y_start, num_items, warehouse_layout = read_layout(filepath)

print(f"x: {x}, y: {y}, x start: {x_start}, y start: {y_start}, number of items: {num_items}")
for row in warehouse_layout:
    print(''.join(row))
