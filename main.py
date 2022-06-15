import glob
from pathlib import Path

from PIL import Image
from PIL.ExifTags import TAGS


def get_image(image_fp):
    """
    Load the image into memory and return it's reference.
    """
    img = Image.open(image_fp)
    return img


def confirm(msg):
    """
    Produce a confirmation message asking if the user is sure they wanna proceed with an action.

    Arguments:
        msg (string): The confirmation question you wanna ask the user (i.e. 'Are you sure')

    Returns:
       
    """
    valid_yes_responses = ['y', 'yes', 'ya', 'true', 'ja', 'si', 'da', 'oui', 'yep']
    ans = input(msg) + ' [y/N]: '

    # All valid response strings are shown above while defining "valid_yes_response"
    # Below; we'll check to see if the confirmation response (after all characters
    # are converted to lower-case, and spaces are stripped from the string) matches
    # any afirmative confirmation response string contained within the
    # 'valid_yes_response' list

    ans = ans.replace(' ', '')


def get_exif(pil_image):
    """
    Iterate through the picture-object's exif data, build a list of found data and 
    return it to the caller.


    Arguments:
        pil_image (IMG

    """
    return pil_image.getdata()


def print_exif(pil_image):
    """
    The print_exif function prints the EXIF metadata of a PIL image object.

    Args:
        pil_image: Access the meta-data of the image

    Returns:
        A dictionary of meta-data found in the image

    """
    # Create a list to save meta-data found in the 'pil_image' object.

    for tag, value in pil_image._getexif().items():
        print(TAGS.get(tag), value)


def create_image(pil_image):
    """
    The create_image function creates a new image object from an existing PIL Image.
    The function takes one argument, the original PIL Image object and returns a new
    PIL Image object with the meta-data removed.

    Args:
        pil_image: Instantiate a new image object

    Returns:
        A new image object with the meta-data from the original image

    """
    # Instantiate a new image object
    img = Image.new(pil_image.mode, pil_image.size)

    data = list(img.getdata())

    # Fill 'putdata' property with meta-data from image
    img.putdata(data)

    # Return the image object to the caller now that we're done with it.
    return img


def save_image(new_pil_image, fp):
    """
    Save the new image-file to storage.

    Arguments:
        pil_image(Image.open):
            An already-instantiated pil.Image object that one wants saved to the
            persistent-storage of the device.

        fp(str|Path):
            The system file-path that you'd like to save the image object to.

    Returns:
        Two possibilities:
            * A path.Path object pointing to where the picture was
              successfully written (if true), or;

            * bool(False) indicating that the operation did not complete successfully.
    """
    new_pil_image.save(fp)


def load_image(image_fp):
    """
    Load the image from a given filepath to the system memory, then return the resulting object.
   
    Note:
        'load_image' is indeed an alias for 'get_image' 
 
    """
    return get_image(image_fp)


def resolve_path(fp):
    """
    The resolve_path function takes a filepath and returns the path to an existing file.
    If the input is not a valid path, it returns None.

    Args:
        fp: Get the file path of the file that is being read

    Returns:
        The absolute path of a file

    """
    return Path(fp).expanduser().resolve()


def find_images(starting_dir='./', find_extensions=None):
    """
    The find_images function searches a directory for image files.
    It returns a list of paths to the images found.

    Args:
        starting_dir='./': Indicate the directory to start
        find_extensions=None: Pass a list of extensions to the find_images function

    Returns:
        A list of paths to images
    """

    # Create a list to contain image paths found.
    image_paths = []

    # If no extensions were provided, we'll provide a couple defaults.
    if find_extensions is None:
        find_extensions = ['jpg', 'png']

    # Make sure the path resolves.
    starting_dir = resolve_path(starting_dir)

    print(str(starting_dir))

    starting_dir_string = str(starting_dir)

    if isinstance(find_extensions, list):
        for ext in find_extensions:
            imgs = glob.glob(f'{starting_dir_string}/*.{ext}')
            for img in imgs:
                image_paths.append(img)

    return image_paths

#
#     confirm = input('Are you sure you wish to overwrite the orriginal image? [y/N]: ')
#
# if confirm:
#     new_img = Image.new(img.mode, img.size)
#     new_img.putdata(data)
#     new_img.save(IMG_FP)
