from setuptools import setup

setup(
    name = 'gnome-favorites-edit',
    version = '0.0.1',
    description = 'Edit dash favorites of gnome-shell.',
    author = 'Shuma Yoshioka',
    author_email = 's64.stdio@gmail.com',
    url = 'https://github.com/S64/gnome-favorites-edit',
    packages = ['gnome_favorites_edit'],
    entry_points = {
        'console_scripts': [
            'gnome-favorites-edit=gnome_favorites_edit.main:main',
        ]
    }
)
