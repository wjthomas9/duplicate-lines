import sublime, sublime_plugin

class DuplicateLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit, up = False):
        for region in self.view.sel():
            line = self.view.line(region)
            line_contents = self.view.substr(line)

            if up:
              self.view.insert(edit, line.end(), "\n" + line_contents)
            else:
              self.view.insert(edit, line.begin(), line_contents + "\n")