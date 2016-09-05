### -*- coding: utf-8 -*-
###
###  Copyright (C) 2016 Peter Williams <pwil3058@gmail.com>
###
### This program is free software; you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation; version 2 of the License only.
###
### This program is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU General Public License for more details.
###
### You should have received a copy of the GNU General Public License
### along with this program; if not, write to the Free Software
### Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

def create_flag_generator():
    """
    Create a new flag generator
    """
    next_flag_num = 0
    while True:
        yield 2 ** next_flag_num
        next_flag_num += 1

quote_if_needed = lambda string: string if string.count(" ") == 0 else "\"" + string + "\""

quoted_join = lambda strings, joint=" ": joint.join((quote_if_needed(file_path) for file_path in strings))

def strings_to_quoted_list_string(strings):
    if len(strings) == 1:
        return quote_if_needed(strings[0])
    return quoted_join(strings[:-1], ", ") + _(" and ") + quote_if_needed(strings[-1])

