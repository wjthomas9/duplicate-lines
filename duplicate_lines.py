import sublime, sublime_plugin

class DuplicateLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit, up = False):
        last_caret_region = [(selection.begin(), selection.end()) for selection in self.view.sel()]
        for region in self.view.sel():
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
