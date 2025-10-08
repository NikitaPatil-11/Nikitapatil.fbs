

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume

# Example usage
radius = str(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)

print(f"Volume of the sphere: {volume:.2f}")