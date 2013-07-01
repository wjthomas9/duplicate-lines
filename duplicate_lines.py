import sublime, sublime_plugin

class DuplicateLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                line_contents = self.view.substr(line) + '\n'
                self.view.insert(edit, line.begin(), line_contents)
            else:
                line = self.view.line(region)
                self.view.run_command("expand_selection", {"to": line.begin()})
                region_contents = self.view.substr(self.view.line(region)) + '\n'
                self.view.insert(edit, line.begin(), region_contents)
