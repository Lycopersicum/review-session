'''This module is responsible for finding certain format images
in specified directory. Module automatically displays images and allows
to transfer image or take other actions with keyboard shortcuts.'''

import sys
import tkinter
from os import walk, makedirs
from os.path import exists as path_exists, join as join_path
from shutil import copyfile as copy, move
from PIL import Image, ImageTk

def check_level(root_pathname, pathname):
    '''Return level difference between two directories.'''
    return len(pathname.split('/')) - len(root_pathname.split('/'))

def filter_extentions(file_list, extentions, case_sensitive=False):
    '''Return file list with extentions that are required.'''
    matching_filenames = []
    for filename in file_list:
        if case_sensitive and filename.split('.')[-1] in extentions:
            matching_filenames.append(filename)
        elif filename.split('.')[-1].lower() in extentions:
            matching_filenames.append(filename)
    return matching_filenames

def find_pictures(root_path, extentions, level=0):
    '''Return pictures from root dir that have right extention.'''
    pictures_list = []

    for (dirpath, dirnames, filenames) in walk(root_path):
        if check_level(root_path, dirpath) <= level:
            for filename in filter_extentions(filenames, extentions):
                pictures_list.append(join_path(dirpath, filename))
    return sorted(pictures_list)

def get_tk_image(path, size, angle=0):
    '''Return resized Tkinter.PhotoImage image object from pathname.'''
    image = Image.open(path)
    ratio = max(image.size[0]/size[0], image.size[1]/size[1])
    image.close()
    new_size = [int(axis/ratio) for axis in image.size]
    if angle % 180 == 90:
        new_size = [new_size[1], new_size[0]]

    image = Image.open(path)
    image = image.resize(new_size, Image.ANTIALIAS)
    image = image.rotate(angle)
    return ImageTk.PhotoImage(image)

class ReviewSession:
    '''Class holds and formats pictures, controls tkinter.'''
    def __init__(self, root_directory, directories, settings):
        self.picture = 0
        self.root_directory = root_directory
        self.directories = directories
        self.settings = settings

        for directory in self.directories:
            if not path_exists(join_path(self.root_directory,
                                         self.directories[directory])):
                makedirs(join_path(self.root_directory,
                                   self.directories[directory]))

        self.pictures = find_pictures(root_directory, settings['extentions'])
        self.initialise_tk()

    def initialise_tk(self):
        '''Initialise Tkinter, show image, bind keyboard bindings.'''
        self.root = tkinter.Tk()
        tk_image = get_tk_image(self.pictures[self.picture],
                                self.settings['size'])
        self.panel = tkinter.Label(self.root, image=tk_image)
        self.panel.pack(side='bottom', fill='both', expand='yes')

        self.root.bind('<Return>', self.next_picture)
        self.root.bind('<Escape>', self.quit)
        self.root.bind('<Left>', self.previous_picture)
        self.root.bind('<Right>', self.skip)

        self.root.bind('<g>', self.good_picture)
        self.root.bind('<n>', self.next_picture)
        self.root.bind('<q>', self.quit)
        self.root.bind('<p>', self.previous_picture)
        self.root.bind('<s>', self.skip)

        self.root.bind('<R>', self.rotate_right)
        self.root.bind('<L>', self.rotate_left)

        self.root.mainloop()

    def skip(self, event):
        '''Do not review image (leave it at original directory.'''
        self.picture += 1

        if self.picture == len(self.pictures):
            sys.exit(0)
        tk_image = get_tk_image(self.pictures[self.picture],
                                self.settings['size'])
        self.panel.configure(image=tk_image)
        self.panel.image = tk_image

    def previous_picture(self, event):
        '''Show previously reviewed image.'''
        self.picture -= 1

        tk_image = get_tk_image(self.pictures[self.picture],
                                self.settings['size'])
        self.panel.configure(image=tk_image)
        self.panel.image = tk_image

    def rotate_right(self, event):
        '''Display image rotated to right.'''

        tk_image = get_tk_image(self.pictures[self.picture],
                                self.settings['size'], -90)
        self.panel.configure(image=tk_image)
        self.panel.image = tk_image

    def rotate_left(self, event):
        '''Display image rotated to left.'''

        tk_image = get_tk_image(self.pictures[self.picture],
                                self.settings['size'], 90)
        self.panel.configure(image=tk_image)
        self.panel.image = tk_image

    def next_picture(self, event):
        '''Move picture to reviewed pictures directory.'''
        move(self.pictures[self.picture],
             join_path(
                 self.root_directory, self.directories['reviewed'],
                 self.pictures[self.picture].split('/')[-1]
             ))
        self.pictures[self.picture] = join_path(
            self.root_directory, self.directories['reviewed'],
            self.pictures[self.picture].split('/')[-1]
            )
        self.skip(event)

    def good_picture(self, event):
        '''Move picture to good pictures directory, confirm review.'''
        copy(self.pictures[self.picture],
             join_path(
                 self.root_directory, self.directories['good'],
                 self.pictures[self.picture].split('/')[-1]
             ))
        self.next_picture(event)

    def quit(self, event):
        '''Quit script.'''
        sys.exit(0)
