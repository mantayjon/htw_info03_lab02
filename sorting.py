class PhotoShoot:

    def __init__(self, *fileName):
        self.fileName = fileName

    def sortByFileName(self):
        sorted_files = sorted(self.fileName)
        return sorted_files


file_sorter = PhotoShoot('sunset_over_the_mountains.jpg',
                         'colorful_flowers_in_bloom.png',
                         'old_vintage_camera.jpg',
                         'happy_family_at_the_beach.jpg',
                         'majestic_eagle_in_flight.png',
                         'misty_forest_in_autumn.jpg',
                         'beautiful_sunrise_over_the_ocean.jpg',
                         'cute_kitten_playing_with_a_ball.jpg',
                         'snow_capped_mountains_in_winter.jpg',
                         'abstract_artwork_in_vibrant_colors.png',
                         'red_roses_in_a_glass_vase.jpg',
                         'happy_couple_enjoying_a_picnic.jpg',
                         'tropical_beach_with_palm_trees.jpg',
                         'majestic_lion_standing_proudly.png',
                         'colorful_hot_air_balloon_in_the_sky.jpg',
                         'peaceful_lake_reflecting_the_mountain.jpg',
                         'cozy_cabin_in_the_woods.jpg',
                         'delicious_fruit_salad_on_a_plate.jpg',
                         'snowy_owl_perched_on_a_branch.png',
                         'beautiful_wildflowers_in_a_field.jpg')
sorted_files = file_sorter.sortByFileName()
print(sorted_files)
