import sublime
import sublime_plugin
import os

class ExcludeIgnoredCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        w = self.view.window()
        pd = w.project_data()
        for folder_setting in pd['folders']:
            path            = folder_setting['path']
            file_patterns   = []
            folder_patterns = []
            gitignore       = os.path.join(path, ".gitignore")
            if (os.path.exists(gitignore)):
                for pattern in open(gitignore):
                    pattern = pattern.strip()
                    if (is_dir(path, pattern)):
                        folder_patterns.append(pattern)
                    elif (pattern[-1] == os.sep):
                        folder_patterns.append(pattern[:-1])
                    else:
                        file_patterns.append(pattern)
            folder_setting["file_exclude_patterns"]   = file_patterns
            folder_setting["folder_exclude_patterns"] = folder_patterns
        w.set_project_data(pd)

def is_dir(cwd, pattern):
    fullpath = os.path.join(cwd, pattern)
    return os.path.exists(fullpath) and os.path.isdir(fullpath)
