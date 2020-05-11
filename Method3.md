# Method Three

In a Command Prompt, PowerShell Window or Terminal:

- Usage:

  - run `py Method3.py Width Height ImageCount`
  
  - or copy the create_image method and use that in your own code
  
  - Example:
```py
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


def iwantanewrandomimage():
    create_image(100, 100, 1)

 ```
    
    
