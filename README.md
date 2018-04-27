# gnome-favorites-edit

[![Snap Status](https://build.snapcraft.io/badge/S64/gnome-favorites-edit.svg)](https://build.snapcraft.io/user/S64/gnome-favorites-edit) [![CircleCI](https://circleci.com/gh/S64/gnome-favorites-edit.svg?style=svg)](https://circleci.com/gh/S64/gnome-favorites-edit)

CLI app of dash favorites editor for gnome-shell.

# Usages

```sh
gnome-favorites-edit put google-chrome.desktop
# Perfect! If run when you've already added, throws error.
gnome-favorites-edit put google-chrome.desktop --ignore-errors
# You can ignore error. Useful for Ansible, Puppet, Chef.
gnome-favorites-edit remove googke-chrome.desktop
# It's same.
```
