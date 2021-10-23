import pygame.sprite


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Load the list of images which make up the animation
        self.images = explosion_images
        # Initialize the current index to zero so the animation start with the first frame
        self.current_index = 0
        # Create the first image
        self.image = self.images[self.current_index]
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        # Set manually the center coordinates of the rect
        self.rect.center = (x, y)

    def update(self):
        # If we didn't reach the last image of the animation
        if self.current_index < len(self.images) - 1:
            # Increment the index value to update and display the next image of the animation
            self.current_index += 1
            self.image = self.images[self.current_index]
        # If we reached the last image of the animation
        else:
            # Remove the Sprite from all Groups
            self.kill()


# Executed on main.py launch
def load_images():
    # Create an empty list to store the images composing the explosion animation
    images = []
    for number in range(48):
        # Format the number with leading zeros to display 3 digits
        number = f"{number:03d}"
        # Load the image
        img = pygame.image.load(f'sprites/tile{number}.png')
        # Add the img to the list
        images.append(img)

    return images


# Store the list of images in a variable so we can call it anytime
explosion_images = load_images()
