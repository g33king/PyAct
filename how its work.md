# How it's work?
basically, everything in the game is called sprite, except solid things, they called blocks.
every object has 6 features:
1. window - the window were this obj will appears and do his functionality.
2. x - the location in the x axis of the window (in the screen with the case of window).
3. y - the location in the y axis of the window (in the screen with the case of window).
4. width - the width of this object.
5. height - the height of this object.
6. texture - how the object will look.

Calling a class will look like this: `objName = ActObjType(main, 50, 50, 3500, 2500, "image.png"{, objName'sFunction()})`

# Windows
creating a window:
`winName = ActWindow(0, 0, 200, 200)`
