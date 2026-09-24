locations = [
    ("Palus", 18.5204, 73.8567),
    ("Vita", 19.0760, 72.8777),
    ("Karve", 19.9975, 73.7898),
    ("Sangli", 17.3850, 78.4867)
]

print("1. Original Locations:")
print(locations)

print("\n2. Accessing Tuple Elements:")

first_location = locations[0]

print("Name:", first_location[0])
print("Latitude:", first_location[1])
print("Longitude:", first_location[2])


print("\n3. Tuple Unpacking:")

name, latitude, longitude = first_location

print("Name:", name)
print("Latitude:", latitude)
print("Longitude:", longitude)

print("\n4. Extracted Coordinate Tuples:")

coordinates = []

for name, latitude, longitude in locations:
    coordinate = (latitude, longitude)
    coordinates.append(coordinate)

for latitude, longitude in coordinates:
    print(f"Latitude = {latitude}, Longitude = {longitude}")
    
print("\n5. Sorted by Latitude:")

sorted_by_latitude = sorted(
    locations,
    key=lambda location: location[1]
)

for name, latitude, longitude in sorted_by_latitude:
    print(f"{name}: ({latitude}, {longitude})")

print("\n6. Sorted by Longitude:")

sorted_by_longitude = sorted(
    locations,
    key=lambda location: location[2]
)

for name, latitude, longitude in sorted_by_longitude:
    print(f"{name}: ({latitude}, {longitude})")
