import random
import os
from hashids import Hashids

def get_hashid(saltname):
    return Hashids(salt=saltname, min_length=10)

def generate_random_color():
    """Generate a random hex color code"""
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

def rename_image(instance, filename):
    ext = filename.split('.')[-1]
    path = 'user/'
    new_filename = f'{instance.user.username}.{ext}'
    return os.path.join(path, new_filename)