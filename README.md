# gnome-favorites-edit

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
