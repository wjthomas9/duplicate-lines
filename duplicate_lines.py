import sublime, sublime_plugin
from sublime import Region

class DuplicateLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit, up = False):
        last_caret_region = [(selection.begin(), selection.end()) for selection in self.view.sel()]
        for region in self.view.sel():
            # if there's a selection, and ends with "\n" we don't want to also duplicate the next line
            if not region.empty():
                if "\n" in self.view.substr(region)[-1]:
                    region = Region(region.begin(), region.end() - 1)

            line = self.view.line(region)
            line_contents = self.view.substr(line)

            if up:
              self.view.insert(edit, line.end(), "\n" + line_contents)
            else:
              self.view.insert(edit, line.begin(), line_contents + "\n")

        if up:
            self.view.sel().clear()
            for selection in last_caret_region:
                self.view.sel().add(sublime.Region(selection[0], selection[1]))
