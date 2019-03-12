import git
import os
from pathlib import Path

yara_directory='/data/yara'
yara_file = '/data/yara/all.yara'
yara_git = 'git://github.com/Yara-Rules/rules.git'
yara_file_list = []

def git_clone ():
    try:
        try:
            os.stat(yara_directory)
        except:
            os.mkdir(yara_directory)
        git.Git(yara_directory).clone(yara_git)
        yara_collect()
    except:
        print('Error when git clone')

def yara_collect():
    try:
        for d, dirs, files in os.walk(yara_directory+'/rules/Webshells/'):
            for nm in files:
                if nm.endswith(".yar"):
                    yara_file_list.append(os.path.join(d, nm))
        make_yara_file()
    except:
        print('Cant parse files in directory')
    try:
        for d, dirs, files in os.walk(yara_directory+'/rules/malware/'):
            for nm in files:
                if nm.endswith(".yar"):
                    yara_file_list.append(os.path.join(d, nm))
        make_yara_file()
    except:
        print('Cant parse files in directory')


def make_yara_file():
    with open(yara_file, 'w') as outfile:
        for fname in yara_file_list:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    print('Yara file is created')

if __name__ == "__main__":
    git_clone()

