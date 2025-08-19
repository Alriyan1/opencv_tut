def convert_pixel_distance_to_meters(pixel_distance,reference_height_in_meters,reference_height_in_pixel):
    return (pixel_distance * reference_height_in_meters)/reference_height_in_pixel

def convert_meters_to_pixel_distance(meters,reference_height_in_meters,reference_height_in_pixel):
    return (meters*reference_height_in_pixel)/reference_height_in_meters