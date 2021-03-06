#!/usr/bin/env python

import argparse
import gi
from gi.repository import Gio, GLib

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('mode', choices = ['put', 'remove'])
    parser.add_argument('app', help = 'Filename of application entry. e.g. `app.desktop`.')
    parser.add_argument('--ignore-errors', action = 'store_true')

    args = parser.parse_args()

    schema = Gio.Settings('org.gnome.shell')
    values = schema.get_value('favorite-apps').unpack()

    already = args.app in values

    if args.mode == 'put':
        if already:
            if not args.ignore_errors: raise RuntimeError('Already added.')
        else:
            values += [args.app]
            schema.set_value('favorite-apps', GLib.Variant('as', values))
    elif args.mode == 'remove':
        if not already:
            if not args.ignore_errors: raise RuntimeError('Not in favorites.')
        else:
            values.remove(args.app)
            schema.set_value('favorite-apps', GLib.Variant('as', values))

if __name__ == '__main__': main()
