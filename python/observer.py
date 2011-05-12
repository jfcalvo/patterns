#
# Observer Design Patter Python implementation.
# This version of the Observer design pattern include events.
# You can register an observer in a subject for different events.
# More information at <http://en.wikipedia.org/wiki/Observer_pattern>
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


class Subject(object):
    
    def __init__(self):
        self.events = dict()

    def register(self, observer, event):
        # Init the event with an empty list
        if not self.events.has_key(event):
            self.events[event] = list()
        # Adding the observer for the event
        self.events[event].append(observer)

    def unregister(self, observer, event):
        if self.events.has_key(event):
            # Remove the observer for the event
            if observer in self.events[event]:
                self.events[event].remove(observer)
            # Remove the event if its empty
            if len(self.events[event]) == 0:
                self.events.pop(event)

    def notify(self, event):
        if self.events.has_key(event):
            for observer in self.events[event]:
                observer.notify(event)


class Observer(object):

    def __init__(self, name):
        self.name = name

    def notify(self, event):
        print '{name} executing {event}'.format(name=self.name, event=event)


def main():
    # Creating our subject
    subject = Subject()
    
    # Creating some observers
    observer1 = Observer('observer1')
    observer2 = Observer('observer2')
    observer3 = Observer('observer3')
    observer4 = Observer('observer4')

    subject.register(observer1, 'event1')
    subject.register(observer2, 'event1')
    subject.register(observer3, 'event1')
    subject.register(observer4, 'event2')

    subject.unregister(observer3, 'event1')
    subject.register(observer3, 'event2')
    
    subject.notify('event1')
    subject.notify('event2')


if __name__ == '__main__':
    main()
