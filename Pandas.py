import pandas

# dictionaries to hold calculation details
all_shapes = ["a", "b", "c", "d"]
all_dimensions = [7.50, 7.50,10.50,10.50]
all_Perimeter = [0, 0, 0.53, 0]
all_Area = [0, 0, 0.53, 0]

base_dict = {
    "Shapes": all_shapes,
    "Dimensions": all_dimensions,
    "Perimeter": all_Perimeter,
    "Area": all_Area
}

base_frame = pandas.DataFrame(base_dict)

# output table within Shape data
print(base_frame)