import os
from shutil import copyfile
from distutils.dir_util import copy_tree

home_path = "/Users/kevin"
config_path = os.path.join(home_path, ".config")
backup_path = os.path.join(home_path, "_config")

config_files = [
  # .zshrc
  [os.path.join(home_path, ".zshrc"), os.path.join(backup_path, "zsh", ".zshrc")],
  
  # .nv
  [os.path.join(home_path, ".nv"), os.path.join(backup_path, "nv", ".nv")]
]

config_directories = [
  # zsh
  [os.path.join(home_path, ".zsh"), os.path.join(backup_path, "zsh", "config")],
  # nvim
  [os.path.join(config_path, "nvim"), os.path.join(backup_path, "nvim")]
]

for config_file in config_files:
  if not os.path.exists(os.path.dirname(config_file[1])):
    print("Creating directory %s" % os.path.dirname(config_file[1]))
    os.makedirs(os.path.dirname(config_file[1]))

  print("Copying %s to %s" % (config_file[0], config_file[1]))
  copyfile(config_file[0], config_file[1])

for config_directory in config_directories:
  print("Copying %s to %s" % (config_directory[0], config_directory[1]))
  copy_tree(config_directory[0], config_directory[1])
