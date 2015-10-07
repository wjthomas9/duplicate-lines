Better Duplicate Lines command for Sublime Text
================

**A modified version of the duplicate_line command for Sublime Text that allows you to duplicate multiple lines of text without worrying about the position of the cursor. If you use your keyboard to highlight the text you want to duplicate, this modified command is for you. (Although, I think it's better even if you use a mouse to select text too.)**

I wasn't happy with the way the duplicate_line command was working in Sublime Text, so I made a modified version. This modified command will still duplicate a single line the same way. The behavior is slightly different, however, when duplicating **multiple** lines.

Rather than having to fully select the area to duplicate, you can now simply run your cursor selection over multiple lines, and this command will duplicate any lines that are even a **part** of the selection. So, if your cursor is in the middle of the line, it will still duplicate from the hard beginning of the first line in the selection to the end of the last line selected, and it will duplicate all of it directly below your selection. *(The original command literally duplicates from wherever your cursor is positioned to where it ends, which created extra keystrokes for me.)* This also means your selection no longer has to include empty space from the previous line to your selection in order to duplicate to a new line. It's a small difference, but if you prefer Eclipse-like behavior with this command, you'll like this.


Get it with the Sublime Text package manager
------------------

Note: If you've previously installed my command using the method above, it's a good idea to undo that before installing via package manager. (Remove the duplicate_lines.py file from the directory in the **without package manager** directions below, and remove the key command from your **Key Bindings - User** file.

1. Launch Sublime Text Package manager
2. Search for Duplicate Lines, and choose it to install it as a package.


Without Package Manager
-----------------

1. Download the repo
2. In Sublime Text 2 or 3, go to Preferences -> Browse Packages
3. Extract the contents to the folder
4. Edit your Key Bindings - User file (and bind whatever command to it that you want)

```{ "keys": ["super+shift+d"], "command": "duplicate_lines" }```

```{ "keys": ["super+shift+u"], "command": "duplicate_lines", "args": { "up": true } }```


Enjoy.
