import pandas as pd

# Dictionaries to hold calculation details
problem_shapes = [0.75,0.75,0.75,0.75,0.75]
problem_dimensions = [0.5,0.5,0.5,0.5,0.5]
problem_perimeter = [1,2,3,4,5]
problem_area = [0.4,0.5,0.6,0.7,0.8]
base_dict = {
    "Shapes": problem_shapes,
    "Dimensions": problem_dimensions,
    "Perimeter": problem_perimeter,
    "Area": problem_area
}

while True:
    # Create DataFrame to store calculation results
    base_frame = pd.DataFrame(base_dict)


base_frame = pd.DataFrame(base_dict)

# table calculation
problem_shapes.append(shape_choice)
problem_dimensions.append(dimension)
problem_area.append(area)
problem_perimeter.append(perimeter)

# Output the table with Shape data
print(base_frame)


