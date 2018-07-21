#!/usr/bin/env python

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def info(self):
        return (self.name, self.job)

if __name__ == '__main__':
    mark = Person('ml', 'trainer')
    dave = Person('da', 'developer')

    print mark.job, dave.info()
