#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import unittest
import nose
from nose.plugins.multiprocess import MultiProcess
import new
import json
import httplib
import base64
import os
import sys
import time
from fxaTest.fxaTestCase import FxaTestCase

chosen_browsers = [
    # ('Linux', 'android', '4.3'),
    # ('Linux', 'android', '4.2'),
    # ('Linux', 'android', '4.1'),
    # ('Linux', 'android', '4.0'),
    # ('OS X 10.8', 'iphone', '6.1'),
    # ('OS X 10.8', 'iphone', '6.0'),
    # ('OS X 10.8', 'ipad', '6.1'),
    # ('OS X 10.8', 'ipad', '6.0'),
    # ('OS X 10.9', 'iphone', '7.1'),
    # ('OS X 10.9', 'iphone', '7.0'),
    # ('OS X 10.9', 'ipad', '7.1'),
    # ('OS X 10.9', 'ipad', '7.0'),
    # ('Windows 8.1', 'iexplore', '11'),
    # ('Windows 8.1', 'firefox', '26'),
    # ('Windows 8.1', 'firefox', '27'),
    # ('Windows 8.1', 'firefox', '28'),
    # ('Windows 8.1', 'firefox', '29'),
    # ('Windows 8.1', 'chrome', '27'),
    # ('Windows 8.1', 'chrome', '28'),
    # ('Windows 8.1', 'chrome', '29'),
    # ('Windows 8.1', 'chrome', '30'),
    # ('Windows 8.1', 'chrome', '31'),
    # ('Windows 8.1', 'chrome', '32'),
    # ('Windows 8.1', 'chrome', '33'),
    # ('Windows 8.1', 'chrome', '34'),
    # ('Windows 8.1', 'chrome', 'beta'),
    # ('Windows 7', 'iexplore', '9'),
    # ('OS X 10.9', 'firefox', '26'),
    # ('OS X 10.9', 'firefox', '27'),
    # ('OS X 10.9', 'firefox', '28'),
    # ('OS X 10.9', 'safari', '7'),
    # ('OS X 10.9', 'chrome', '31'),
    # ('OS X 10.9', 'chrome', '32'),
    # ('OS X 10.9', 'chrome', '33'),
    # ('OS X 10.9', 'chrome', '34'),
    # ('Windows 7', 'iexplore', '8'),
    # ('Windows 7', 'opera', '11'),
    # ('Windows 7', 'opera', '12'),
    # ('Windows 7', 'iexplore', '10'),
    # ('Windows 7', 'firefox', '26'),
    # ('Windows 7', 'firefox', '27'),
    # ('Windows 7', 'firefox', '28'),
    # ('Windows 7', 'firefox', '29'),
    # ('Windows 7', 'chrome', '27'),
    # ('Windows 7', 'chrome', '28'),
    # ('Windows 7', 'chrome', '29'),
    # ('Windows 7', 'chrome', '30'),
    # ('Windows 7', 'chrome', '31'),
    # ('Windows 7', 'chrome', '32'),
    # ('Windows 7', 'chrome', '33'),
    # ('Windows 7', 'chrome', '34'),
    # ('Windows 7', 'chrome', 'beta'),
    # ('Windows 8', 'iexplore', '10'),
    # ('Windows 8', 'firefox', '26'),
    # ('Windows 8', 'firefox', '27'),
    # ('Windows 8', 'firefox', '28'),
    # ('Windows 8', 'firefox', '29'),
    # ('Windows 8', 'chrome', '27'),
    # ('Windows 8', 'chrome', '28'),
    # ('Windows 8', 'chrome', '29'),
    # ('Windows 8', 'chrome', '30'),
    # ('Windows 8', 'chrome', '31'),
    # ('Windows 8', 'chrome', '32'),
    # ('Windows 8', 'chrome', '33'),
    # ('Windows 8', 'chrome', '34'),
    # ('Windows 8', 'chrome', 'beta'),
    # ('Windows 7', 'iexplore', '11'),
    # ('OS X 10.8', 'safari', '6'),
    # ('OS X 10.8', 'chrome', '27'),
    # ('OS X 10.8', 'chrome', '28'),
    # ('OS X 10.8', 'chrome', '31'),
    # ('OS X 10.8', 'chrome', '32'),
    # ('OS X 10.8', 'chrome', '33'),
    # ('OS X 10.8', 'chrome', '34'),
    # ('OS X 10.8', 'chrome', 'beta'),
    # ('Linux', 'opera', '12'),
    # ('Linux', 'firefox', '26'),
    # ('Linux', 'firefox', '27'),
    # ('Linux', 'firefox', '28'),
    ('Linux', 'firefox', '29'),
    # ('Linux', 'chrome', '27'),
    # ('Linux', 'chrome', '28'),
    # ('Linux', 'chrome', '29'),
    # ('Linux', 'chrome', '30'),
    # ('Linux', 'chrome', '31'),
    # ('Linux', 'chrome', '32'),
    # ('Linux', 'chrome', '33'),
    # ('Linux', 'chrome', '34'),
]


classes = {}
for os, browser, version in chosen_browsers:
    # Make a new class name for the actual test cases
    name = "%s_%s_%s_%s" % (FxaTestCase.__name__, os, browser, version)
    name = name.encode('ascii')
    if name.endswith("."): name = name[:-1]
    for x in ".-_":
        name = name.replace(x, " ")

    # Copy the magic __dict__ from the original class
    d = dict(FxaTestCase.__dict__)
    # Update the new class' dict with a new name and a __test__ == True
    d.update({'__test__': True,
              '__name__': name,
              # Set these properties dynamically, the test uses them to
              # instantiate the browser
              'name': name,
              'os': os,
              'br': browser,
              'version': version
             })

    # append the new class to the classes dict
    classes[name] = new.classobj(name, (FxaTestCase,), d)

globals().update(classes)

# this is just handy. If __main__, just run the tests in multiple processes
if __name__ == "__main__":
    nose.core.run(argv=["nosetests", "-vv",
                        "--processes", len(chosen_browsers),
                        "--process-timeout", 500,
                        __file__],
                  plugins=[MultiProcess()])
