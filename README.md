# review-session
Review session is Python module dedicated for reviewing pictures and moving them to directories with only one keyboard click.

## Documentation

### Dependencies

Currently ```PIL``` and ```tkinter``` are used on my project, you can get it with pip:
```$ sudo pip3 install pillow python-tk```
for Debian based distributions (Debian, Ubuntu):
```$ sudo apt-get install python3-tk python3-pil```

### Setup explanations

- ```root_directory```: _String_ that should contain path to your pictures folder.
- ```directories```: _Dictionary_ which keys are cases of picture "quality", and values are directory names. For example good or average categories could contain: ```'good': 'goodPictures', 'average': 'averagePictures'```.
-    ```good```: By default module filters only good picture, it copies pictures to specified.
-    ```all```: By default all pictures are skipped and stays at original location, unless you press __```n```__ or __```g```__.

- ```settings```: _Dictionary_, which contains following keys and values:
-    ```extentions```: _List_, which should contain extentions that you would want to preview.
-    ```size```: _List_, which contains width and height limits (Maximum size that picture would take).
    
### Keyboard shortcuts:

- __```g```__: G stands for _good picture_, make a copy in ```root_directory/good_directory```, also move it to ```root_directory/reviewed_pictures``` directory.
- __```n```__ or __```Return```__: N stands for _normal_ or _next_ picture, for instance if you reviewed picture, but you do not want to move it to specific folder.
- __```s```__ or __```Right cursor```__: S stands for _skip picture_, when picture is skipped, nothing happens to it, it stays at original directory.
- __```p```__ or __```Left cursor```__: P stands for _previous picture_, this button opens previously reviewed picture.
- __```q```__ or __```Esc```__: Q stands fir _quit_, by pressing ```q``` or ```Escape```, you will stop script.

- __```shift + R```__: _Rotate to right_.
- __```shift + L```__: _Rotate to left_ (currently rotating images produces weird result).
