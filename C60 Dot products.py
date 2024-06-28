import sympy as sp
import os


# Define the symbolic variable r
r = sp.Symbol('r')

# Manually define 60 points
N_1_1 = (1 / (r + 1), (1 + sp.sqrt(5)) * r / (2 * (r + 1)), 0)
N_1_2 =(1 / (r + 1), r / (2 * (r + 1)), -sp.sqrt(5 + 2 * sp.sqrt(5)) * r / (2 * (r + 1)))
N_1_3 = (1 / (r + 1), (-(3 + sp.sqrt(5)) * r) / (4 * (r + 1)), -sp.sqrt(5 + sp.sqrt(5)) * r / ((r + 1) * 2 * sp.sqrt(2)))
N_1_4 = (1 / (r + 1), -(3 + sp.sqrt(5)) * r / (4 * (r + 1)), sp.sqrt(5 + sp.sqrt(5)) * r / ((r + 1) * 2 * sp.sqrt(2)))
N_1_5 = (1 / (r + 1), r / (2 * (r + 1)), sp.sqrt(5 + 2 * sp.sqrt(5)) * r / (2 * (r + 1)))
N_2_1 = (((5 + sp.sqrt(5)) * r + sp.sqrt(5)) / (5 * (r + 1)), ((-5 - sp.sqrt(5)) * r + 4 * sp.sqrt(5)) / (10 * (r + 1)), 0)
N_2_2 = (sp.sqrt(5) / 5, (sp.sqrt(5) * (4 - r)) / (10 * (r + 1)), sp.sqrt(5 + 2 * sp.sqrt(5)) * r / (2 * (r + 1)))
N_2_3 = (-((3 + sp.sqrt(5)) * r - 2) / (2 * sp.sqrt(5) * (r + 1)), ((3 + sp.sqrt(5)) * r + 8) / (4 * sp.sqrt(5) * (r + 1)), sp.sqrt(5 + sp.sqrt(5)) * r / (2 * sp.sqrt(2) * (r + 1)))
N_2_4 = (-((3 + sp.sqrt(5)) * r - 2) / (2 * sp.sqrt(5) * (r + 1)), ((3 + sp.sqrt(5)) * r + 8) / (4 * sp.sqrt(5) * (r + 1)), -sp.sqrt(5 + sp.sqrt(5)) * r / (2 * sp.sqrt(2) * (r + 1)))
N_2_5 = (sp.sqrt(5) / 5, (sp.sqrt(5) * (4 - r)) / (10 * (r + 1)), -sp.sqrt(5 + 2 * sp.sqrt(5)) * r / (2 * (r + 1)))
N_3_1 = (((5 + sp.sqrt(5)) * r + sp.sqrt(5)) / (5 * (r + 1)), ((-5 - sp.sqrt(5)) * r + 4 * sp.sqrt(5)) / (10 * (r + 1)) * (sp.sqrt(5) - 1) / 4, ((-5 - sp.sqrt(5)) * r + 4 * sp.sqrt(5)) / (10 * (r + 1)) * sp.sqrt((5 + sp.sqrt(5)) / 8))
N_3_2 = (sp.sqrt(5) / 5, (5 + sp.sqrt(5)) / (4 * (r + 1)) + (-15 - 7 * sp.sqrt(5)) / 20, (sp.sqrt(50 - 10 * sp.sqrt(5)) * r + 2 * sp.sqrt(10 * (5 + sp.sqrt(5)))) / (20 * (r + 1)))
N_3_3 = ((2 - (3 + sp.sqrt(5)) * r) / (2 * sp.sqrt(5) * (1 + r)), -((5 + sp.sqrt(5)) * r) / (8 * (1 + r)) + ((-1 + sp.sqrt(5)) * (8 + (3 + sp.sqrt(5)) * r)) / (16 * sp.sqrt(5) * (1 + r)), sp.sqrt((5 + sp.sqrt(5)) / 10))
N_3_4 = (-((3 + sp.sqrt(5)) * r - 2) / (2 * sp.sqrt(5) * (r + 1)), (3 * sp.sqrt(5) * r + 15 * r - 2 * sp.sqrt(5) + 10) / (20 * (r + 1)), +(sp.sqrt(2 * (5 + sp.sqrt(5))) * ((5 - sp.sqrt(5)) * r + 4 * sp.sqrt(5))) / (40 * (r + 1)))
N_3_5 = (sp.sqrt(5) / 5, ((sp.sqrt(5) - 1) * (4 - r)) / (8 * sp.sqrt(5) * (r + 1)) + sp.sqrt((5 + sp.sqrt(5)) * (5 + 2 * sp.sqrt(5)) / 2) * r / (4 * (r + 1)), -(sp.sqrt(5 * (5 + 2 * sp.sqrt(5))) * r - sp.sqrt(10 * (5 + sp.sqrt(5)))) / (10 * (r + 1)))
N_4_1 = (((5 + sp.sqrt(5)) * r + sp.sqrt(5)) / (5 * (r + 1)), ((5 + 3 * sp.sqrt(5)) * r - 2 * (5 + sp.sqrt(5))) / (20 * (r + 1)), (sp.sqrt((5 - sp.sqrt(5)) / 2) * ((-5 - sp.sqrt(5)) * r + 4 * sp.sqrt(5))) / (20 * (r + 1)))
N_4_2 = (sp.sqrt(5) / 5, (sp.sqrt(5) * (4 - r)) / (10 * (r + 1)) * (-sp.sqrt(5) - 1) / 4 + sp.sqrt(5 + 2 * sp.sqrt(5)) * r / (2 * (r + 1)) * sp.sqrt((5 - sp.sqrt(5)) / 8), (sp.sqrt(5) * (4 - r)) / (10 * (r + 1)) * sp.sqrt((5 - sp.sqrt(5)) / 8) - sp.sqrt(5 + 2 * sp.sqrt(5)) * r / (2 * (r + 1)) * (-sp.sqrt(5) - 1) / 4)
N_4_3 = (-((3 + sp.sqrt(5)) * r - 2) / (2 * sp.sqrt(5) * (r + 1)), ((3 + sp.sqrt(5)) * r + 8) / (4 * sp.sqrt(5) * (r + 1)) * (-sp.sqrt(5) - 1) / 4 - sp.sqrt(5 + sp.sqrt(5)) * r / (2 * sp.sqrt(2) * (r + 1)) * sp.sqrt((5 - sp.sqrt(5)) / 8), ((3 + sp.sqrt(5)) * r + 8) / (4 * sp.sqrt(5) * (r + 1)) * sp.sqrt((5 - sp.sqrt(5)) / 8) + sp.sqrt(5 + sp.sqrt(5)) * r / (2 * sp.sqrt(2) * (r + 1)) * (-sp.sqrt(5) - 1) / 4)
N_4_4 = (-((3 + sp.sqrt(5)) * r - 2) / (2 * sp.sqrt(5) * (r + 1)), ((3 + sp.sqrt(5)) * r + 8) / (4 * sp.sqrt(5) * (r + 1)) * (-sp.sqrt(5) - 1) / 4 + sp.sqrt(5 + sp.sqrt(5)) * r / (2 * sp.sqrt(2) * (r + 1)) * sp.sqrt((5 - sp.sqrt(5)) / 8), ((3 + sp.sqrt(5)) * r + 8) / (4 * sp.sqrt(5) * (r + 1)) * sp.sqrt((5 - sp.sqrt(5)) / 8) - sp.sqrt(5 + sp.sqrt(5)) * r / (2 * sp.sqrt(2) * (r + 1)) * (-sp.sqrt(5) - 1) / 4)
N_4_5 = (sp.sqrt(5) / 5, (sp.sqrt(5) * (4 - r)) / (10 * (r + 1)) * (-sp.sqrt(5) - 1) / 4 - sp.sqrt(5 + 2 * sp.sqrt(5)) * r / (2 * (r + 1)) * sp.sqrt((5 - sp.sqrt(5)) / 8), (sp.sqrt(5) * (4 - r)) / (10 * (r + 1)) * sp.sqrt((5 - sp.sqrt(5)) / 8) + sp.sqrt(5 + 2 * sp.sqrt(5)) * r / (2 * (r + 1)) * (-sp.sqrt(5) - 1) / 4)
N_5_1 = (((5 + sp.sqrt(5)) * r + sp.sqrt(5)) / (5 * (r + 1)), ((5 + 3 * sp.sqrt(5)) * r - 2 * (5 + sp.sqrt(5))) / (20 * (r + 1)), (sp.sqrt((5 - sp.sqrt(5)) / 2) * (-(-5 - sp.sqrt(5)) * r - 4 * sp.sqrt(5))) / (20 * (r + 1)))
N_5_2 = (sp.sqrt(5) / 5, ((5 + sp.sqrt(5)) * (3 * r - 2)) / (20 * (r + 1)), (sp.sqrt(5) * (4 - r)) / (10 * (r + 1)) * sp.sqrt((5 - sp.sqrt(5)) / 8) - sp.sqrt(5 + 2 * sp.sqrt(5)) * r / (2 * (r + 1)) * (-sp.sqrt(5) - 1) / 4)
N_5_3 = (-((3 + sp.sqrt(5)) * r - 2) / (2 * sp.sqrt(5) * (r + 1)), (3 * sp.sqrt(5) * r - 5 * r - 2 * sp.sqrt(5) - 10) / (20 * (r + 1)), (sp.sqrt(5) * (4 - r)) / (10 * (r + 1)) * sp.sqrt((5 - sp.sqrt(5)) / 8) - sp.sqrt(5 + 2 * sp.sqrt(5)) * r / (2 * (r + 1)) * (-sp.sqrt(5) - 1) / 4)
N_5_4 = (-((3 + sp.sqrt(5)) * r - 2) / (2 * sp.sqrt(5) * (r + 1)), -((5 + 7 * sp.sqrt(5)) * r + 2 * sp.sqrt(5) + 10) / (20 * (r + 1)), (((3 + sp.sqrt(5)) * r + 8) / (4 * sp.sqrt(5) * (r + 1))) * (-sp.sqrt((5 - sp.sqrt(5)) / 8)) + (-sp.sqrt(5 + sp.sqrt(5)) * r / (2 * sp.sqrt(2) * (r + 1))) * ((-sp.sqrt(5) - 1) / 4))
N_5_5 = (sp.sqrt(5) / 5, (-5 - sp.sqrt(5)) / 10, (8 * sp.sqrt(5 * (5 + 2 * sp.sqrt(5))) * r - 4 * sp.sqrt(50 - 10 * sp.sqrt(5))) / (40 * (r + 1)))
N_6_1 = (((5 + sp.sqrt(5)) * r + sp.sqrt(5)) / (5 * (r + 1)), 1 / (2 * (r + 1)) - 1 / (2 * sp.sqrt(5)), (sp.sqrt((5 + sp.sqrt(5)) / 2) * (sp.sqrt(5) * r + 5 * r - 4 * sp.sqrt(5))) / (20 * (r + 1)))
N_6_2 = (sp.sqrt(5) / 5, ((sp.sqrt(5) - 1) * (4 - r)) / (8 * sp.sqrt(5) * (r + 1)) + sp.sqrt((5 + sp.sqrt(5)) * (5 + 2 * sp.sqrt(5)) / 2) * r / (4 * (r + 1)), (sp.sqrt(5 * (5 + 2 * sp.sqrt(5))) * r - sp.sqrt(10 * (5 + sp.sqrt(5)))) / (10 * (r + 1)))
N_6_3 = (-((3 + sp.sqrt(5)) * r - 2) / (2 * sp.sqrt(5) * (r + 1)), (3 * sp.sqrt(5) * r + 15 * r - 2 * sp.sqrt(5) + 10) / (20 * (r + 1)), -(sp.sqrt(2 * (5 + sp.sqrt(5))) * ((5 - sp.sqrt(5)) * r + 4 * sp.sqrt(5))) / (40 * (r + 1)))
N_6_4 = ((2 - (3 + sp.sqrt(5)) * r) / (2 * sp.sqrt(5) * (1 + r)), -((5 + sp.sqrt(5)) * r) / (8 * (1 + r)) + ((-1 + sp.sqrt(5)) * (8 + (3 + sp.sqrt(5)) * r)) / (16 * sp.sqrt(5) * (1 + r)), -sp.sqrt((5 + sp.sqrt(5)) / 10))
N_6_5 = (sp.sqrt(5) / 5, -((15 + 7 * sp.sqrt(5)) * r + 2 * sp.sqrt(5) - 10) / (20 * (r + 1)), (sp.sqrt(10 * (5 + sp.sqrt(5))) * (r - 4) - 5 * (sp.sqrt(5) - 1) * sp.sqrt(5 + 2 * sp.sqrt(5)) * r) / (40 * (r + 1)))
N_7_1 = (1, 1, 1)
N_7_2 = (1, 1, 1)
N_7_3 = (1, 1, 1)
N_7_4 = (1, 1, 1)
N_7_5 = (1, 1, 1)
N_8_1 = (1, 1, 1)
N_8_2 = (1, 1, 1)
N_8_3 = (1, 1, 1)
N_8_4 = (1, 1, 1)
N_8_5 = (1, 1, 1)
N_9_1 = (1, 1, 1)
N_9_2 = (1, 1, 1)
N_9_3 = (1, 1, 1)
N_9_4 = (1, 1, 1)
N_9_5 = (1, 1, 1)
N_10_1 =(1, 1, 1)
N_10_2 = (1, 1, 1)
N_10_3 = (1, 1, 1)
N_10_4 = (1, 1, 1)
N_10_5 = (1, 1, 1)
N_11_1 = (1, 1, 1)
N_11_2 = (1, 1, 1)
N_11_3 =(1, 1, 1)
N_11_4 = (1, 1, 1)
N_11_5 = (1, 1, 1)
N_12_1 =(1, 1, 1)
N_12_2 = (1, 1, 1)
N_12_3 = (1, 1, 1)
N_12_4 = (1, 1, 1)
N_12_5 = (1, 1, 1)

# List of all points
points = [
    N_1_1, N_1_2, N_1_3, N_1_4, N_1_5,
    N_2_1, N_2_2, N_2_3, N_2_4, N_2_5,
    N_3_1, N_3_2, N_3_3, N_3_4, N_3_5,
    N_4_1, N_4_2, N_4_3, N_4_4, N_4_5,
    N_5_1, N_5_2, N_5_3, N_5_4, N_5_5,
    N_6_1, N_6_2, N_6_3, N_6_4, N_6_5,
    N_7_1, N_7_2, N_7_3, N_7_4, N_7_5,
    N_8_1, N_8_2, N_8_3, N_8_4, N_8_5,
    N_9_1, N_9_2, N_9_3, N_9_4, N_9_5,
    N_10_1, N_10_2, N_10_3, N_10_4, N_10_5,
    N_11_1, N_11_2, N_11_3, N_11_4, N_11_5,
    N_12_1, N_12_2, N_12_3, N_12_4, N_12_5
]

for i in range(len(points)):
    x, y, z = points[i]
    points[i] = (sp.simplify(x), sp.simplify(y), sp.simplify(z))
# Function to calculate the distance between a point and the origin
def distance_to_origin(point):
    return sp.sqrt(point[0]*point[0] + point[1]*point[1] + point[2]*point[2])

# Function to calculate the dot product between two points
def dot_product(point1, point2):
    return point1[0]*point2[0] + point1[1]*point2[1] + point1[2]*point2[2]

# Coefficient for homothety
coefficient = 2 * (r + 1) / sp.sqrt(4 + r*r * (1 + sp.sqrt(5))*(1 + sp.sqrt(5)))
coefficient=sp.simplify(coefficient)

# Function to multiply every coordinate by the coefficient
def multiply(point, coeff):
    return (sp.simplify(point[0]* coeff), sp.simplify(point[1] * coeff), sp.simplify(point[2] * coeff))

transformed_points = []
for point in points:
    transformed_points.append(tuple(sp.simplify(coord) for coord in multiply(point, coefficient)))

# Create the final list of points by negating the first 30 points
final_points = transformed_points[:30]
for i in range(30):
    final_points.append((-final_points[i][0], -final_points[i][1], -final_points[i][2]))
# Calculate the dot product between every pair of points
dot_products = {}


# Calculate the dot product between every pair of points
dot_products = {}
for i in range(len(final_points)):
    for j in range(1, len(final_points)):
        dot_products[(i, j)] = dot_product(final_points[i], final_points[j])
        dot_products[(i, j)] = sp.simplify(dot_products[(i, j)])

# Function to calculate the frequency of each unique dot product
def calculate_dot_product_frequencies(dot_products):
    frequencies = {}
    for dot_product in dot_products.values():
        if dot_product not in frequencies:
            frequencies[dot_product] = 1
        else:
            frequencies[dot_product] += 1
    return frequencies

# Calculate dot product frequencies
dot_product_frequencies = calculate_dot_product_frequencies(dot_products)

# Write results to the main text file
output_file = r"C:\Users\stefa\PycharmProjects\C60 Spectre\dot_product_distances.txt"
with open(output_file, 'w') as file:
    file.write("Distances and Dot Products:\n\n")

    # Write distances
    file.write("Distances:\n")
    for idx, point in enumerate(final_points):
        dist = sp.simplify(distance_to_origin(point))
        file.write(f"Distance from origin to N_{idx // 5 + 1}_{idx % 5 + 1}: {dist}\n")

    file.write("\n")

    # Write dot products
    file.write("Dot Products:\n")
    for (i, j), dot_product_value in dot_products.items():
        file.write(f"Dot product N_{i // 5 + 1}_{i % 5 + 1} . N_{j // 5 + 1}_{j % 5 + 1}: {dot_product_value}\n")

    file.write("\n")

    # Write dot product frequencies
    file.write("Dot Product Frequencies:\n")
    for dot_product, frequency in dot_product_frequencies.items():
        file.write(f"Dot product {dot_product}: seen {frequency} times\n")

print(f"Results written to {output_file}")

# Write each unique dot product and its frequency to separate files
output_dir = r"C:\Users\stefa\PycharmProjects\C60 Spectre\dot_product_frequencies"
os.makedirs(output_dir, exist_ok=True)

for dot_product, frequency in dot_product_frequencies.items():
    dot_product_file = os.path.join(output_dir, f"dot_product_{dot_product}.txt")
    with open(dot_product_file, 'w') as file:
        file.write(f"Dot product {dot_product}: seen {frequency} times\n")

print(f"Unique dot product frequencies written to {output_dir}")