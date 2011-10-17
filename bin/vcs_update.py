#!/usr/bin/env python
" Universal script to update the VCS. "

import os
import optparse

__author__ = 'Kirill Klenov <horneds@gmail.com>'
__version__ = '0.01'


SCMS = {
    '.svn' : 'svn update %s',
    '.git' : 'cd %s && git co master && git pull -v',
    '.bzr' : 'cd %s && bzr pull',
    '.hg'  : 'cd %s && hg pull && hg update',
}


def run(path):

    if os.path.isfile(path):
        return

    for item in os.listdir(path):
        if SCMS.has_key(item):
            print '\nFind: %s\n' % path, '$', SCMS[item] % path
            os.system(SCMS[item] % path)
            if item == '.svn':
                return

    for folder in os.listdir(path):
        run(os.path.join(path, folder))


def main():
    p = optparse.OptionParser(
        version=__version__,
        usage="%prog [DIRNAME]",
        description= '''"scm_up.py" is script to recursive update all SCMs (Bazaar, Darcs, Git, Git SVN, Mercurial, Subversion) directories.''')

    args = p.parse_args()[1]
    path = args[0] if args else os.getcwd()
    run(path)


if __name__ == '__main__':
    main()
