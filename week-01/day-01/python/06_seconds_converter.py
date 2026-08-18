seconds = int(input(f"enter seconds :"))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(f"your clock is {hours}:{minutes}:{remaining_seconds}")