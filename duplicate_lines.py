import sublime, sublime_plugin

class DuplicateLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        for region in self.view.sel():
            line = self.view.full_line(region)
            line_contents = self.view.substr(line)
            self.view.insert(edit, line.end() if args.get('up', False) else line.begin(), line_contents)
