aquarium_length = int(input())
aquarium_width = int(input())
aquarium_height = int(input())
taken_space_percent = float(input()) / 100

aquarium_total_volume = (aquarium_length * aquarium_width * aquarium_height) / 1000

taken_space = aquarium_total_volume * taken_space_percent

aquarium_volume = aquarium_total_volume - taken_space

print(aquarium_volume)
