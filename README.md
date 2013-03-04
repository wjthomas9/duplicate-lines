duplicate-lines
================

**A modified version of the duplicate_line command for Sublime Text 2 that allows you to duplicate multiple lines of text without worrying about the position of the cursor. If you use your keyboard to highlight the text you want to duplicate, this modified command is for you. (Although, I think it's better even if you use a mouse to select text too.)**

I wasn't happy with the way the duplicate_line command was working in Sublime Text 2, so I made a modified version. This modified command will still duplicate a single line the same way. The behavior is slightly different, however, when duplicating **multiple** lines.

Rather than having to fully select the area to duplicate, you can now simply run your cursor selection over multiple lines, and this command will duplicate any lines that are even a **part** of the selection. So, if your cursor is in the middle of the line, it will still duplicate from the hard beginning of the first line in the selection to the end of the last line selected, and it will duplicate all of it directly below your selection. *(The original command literally duplicates from wherever your cursor is positioned to where it ends, which created extra keystrokes for me.)* This also means your selection no longer has to include empty space from the previous line to your selection in order to duplicate to a new line. It's a small difference, but if you prefer Eclipse-like behavior with this command, you'll like this.

How to use
-----------------

1. Download the repo and place duplicate_lines.py (Not misspelled. It's called duplicate_line**s**) in your **~/Library/Application Support/Sublime Text 2/Packages/User** directory
2. Add the key binding below to your Key Bindings - User file (and bind whatever command to it that you want)

```{ "keys": ["super+shift+d"], "command": "duplicate_lines" }```

Get it with the Sublime Text 2 package manager
------------------

Enjoy.