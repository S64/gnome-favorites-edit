from setuptools import setup
from setuptools.command.install import install
import os
import subprocess

class CustomInstallCommand(install):
    def run(self):
        print('Compile gsettings schemas')
        subprocess.run(['/usr/lib/x86_64-linux-gnu/glib-2.0/glib-compile-schemas', '/usr/share/glib-2.0/schemas'])
        print('Execute install')
        install.run(self)


setup(
    name = 'gnome-favorites-edit',
    version = '0.0.1',
    description = 'Edit dash favorites of gnome-shell.',
    author = 'Shuma Yoshioka',
    author_email = 's64.stdio@gmail.com',
    packages = ['gnome_favorites_edit'],
    entry_points = {
        'console_scripts': [
            'gnome-favorites-edit=gnome_favorites_edit.main:main',
        ]
    },
    cmdclass = {
        'install': CustomInstallCommand,
    }
)
