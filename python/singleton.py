# -*- coding: utf-8 -*-

#
# Singleton Design Pattern Python implementation.
# More information at <http://en.wikipedia.org/wiki/Singleton_pattern>
#
# Copyright (C) 2010-2011  José Francisco Calvo Moreno
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# José Francisco Calvo Moreno <josefranciscocalvo@gmail.com>
#

"""
This is an example of use of the Singleton Pattern:

We create a three new Singleton objects:
>>> singleton_1 = Singleton()
>>> singleton_2 = Singleton()
>>> singleton_3 = Singleton()

We can test that all the three objects are the same
>>> id(singleton_1) == id(singleton_2) == id(singleton_3)
True
>>> singleton_1 == singleton_2 == singleton_3
True

We can even add a custom attribute to one of them
>>> singleton_1.message = "I am a Singleton"

And test that the same message is present in the rest of the singletons
>>> singleton_1.message == singleton_2.message == singleton_3.message
True
"""

class Singleton(object):
    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(*args, **kwargs)
        return cls.instance


if __name__ == '__main__':
    import doctest
    doctest.testmod()

