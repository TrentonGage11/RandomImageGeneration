### Credit to Method 3 goes to this author: https://gist.github.com/sparkstar
import os, time, numpy, PIL
from PIL import Image
 
def create_image(width = 1920, height = 1080, num_of_images = 100):
    width = int(width)
    height = int(height)
    num_of_images = int(num_of_images)
 
    current = time.strftime("%Y%m%d%H%M%S")
    os.mkdir(current)
 
    for n in range(num_of_images):
        filename = '{0}/{0}_{1:03d}.jpg'.format(current, n)
        rgb_array = numpy.random.rand(height,width,3) * 255
        print(f"On image #{n}, Name: {filename}")
        image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')
        image.save(filename)
        print(f"Image #{n} Saved")
 
def main(args):
    if len(args) >= 3:
        print(f"Arg Count: {len(args)}\nArgs: {args}\nStarting...")
        create_image(width = args[0], height = args[1], num_of_images = args[2])
    elif len(args) < 3:
       print(f"You have supplied insignificant argument variables!\nWidth, Height, Number of Images")
    else:
        print(f"Arg Count: {len(args)}\n['1920', '1080', '100']\nStarting...")
        create_image(width=1920, height=1080, num_of_images=100)
    return 0
 
if __name__ == '__main__':
    import sys 
    status = main(sys.argv[1:])
    sys.exit(status)
