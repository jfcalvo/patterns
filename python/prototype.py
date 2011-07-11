# -*- coding: utf-8 -*-

#
# Prototype Design Pattern Python implementation.
# More information at <http://en.wikipedia.org/wiki/Prototype_pattern>
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
This is an example of use of the Prototype Pattern:

We create a new class that inherits from the Prototype Class
>>> class Email(Prototype):
...     to = ''
...     subject = ''
...     message = ''

Creating a new instance to prototype the class Email
>>> prototype_email = Email()

Setting the fields of our email prototype
>>> prototype_email.subject = 'Hello'
>>> prototype_email.message = 'Hello World!'

Now we can use our prototype to create new emails instances
>>> email_one = prototype_email.clone()
>>> email_two = prototype_email.clone()

This must be different instances
>>> id(prototype_email) != id(email_one) != id(email_two)
True

The fields must be equal in all the instances
>>> prototype_email.to == email_one.to == email_two.to
True
>>> prototype_email.subject == email_one.subject == email_two.subject
True
>>> prototype_email.message == email_one.message == email_two.message
True
"""

from copy import deepcopy


class Prototype(object):

    def clone(self):
        return deepcopy(self)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

