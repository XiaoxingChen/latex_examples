#!/usr/bin/python3
import argparse
import os
import shutil

def handleAutoComplete():
    if sys.platform == 'linux':
        complete_cmd = 'complete -F _longopt {}'.format(os.path.basename(__file__))
        bashrc_path = os.path.expanduser('~/.bashrc')
        with open(bashrc_path) as f:
            if not complete_cmd in f.read():
                os.system('echo "{}" >> {}'.format(complete_cmd, bashrc_path))
    else:
        pass

class BuildDirectory():
    def __init__(self):
        self.script_folder = os.path.abspath(os.path.dirname(__file__))
        self.build_root = os.path.join(self.script_folder, 'build')

def runBuild(dirs):
    os.makedirs(dirs.build_root, exist_ok=True)
    os.chdir(dirs.build_root)
    os.system("pdflatex {}".format(os.path.join(dirs.script_folder, '*.tex')))
    os.chdir(dirs.script_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean', action='store_true', help='Clean build folder')
    args = parser.parse_args()
    dirs = BuildDirectory()

    if args.clean:
        shutil.rmtree(dirs.build_root, ignore_errors=True)
        quit()

    runBuild(dirs)

    
    


    