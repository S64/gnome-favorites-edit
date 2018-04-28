# gnome-favorites-edit

[![CircleCI](https://circleci.com/gh/S64/gnome-favorites-edit.svg?style=svg)](https://circleci.com/gh/S64/gnome-favorites-edit)

CLI app of dash favorites editor for gnome-shell.

<img src="https://imgur.com/download/BnrJJh2" width="350"/>

## Usages

```sh
gnome-favorites-edit put google-chrome.desktop
# Perfect! If run when you've already added, throws error.
gnome-favorites-edit put google-chrome.desktop --ignore-errors
# You can ignore error. Useful for Ansible, Puppet, Chef.
gnome-favorites-edit remove googke-chrome.desktop
# It's same.
```

## Installation

on Ubuntu:

```sh
# Download package from /releases before execute this.
sudo apt-get install -f ./gnome-favorites-edit_0.0.1-1_all.deb
```

or Fedora:

```sh
# Download package from /releases before execute this.
sudo dnf install ./gnome-favorites-edit-0.0.1-1.noarch.rpm
```

## License

```
Copyright 2018 Shuma Yoshioka

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
