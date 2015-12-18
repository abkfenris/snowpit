snowpit
=======

This library plans to contain:

- Functions for encoding and decoding SnowPilot and CAAML XML formatted data
- Classes for snowpits, layers, stability tests, stability observations, and weather observations

+---------------+-------------------+
| Requirements  | |requires.io|     |
+---------------+-------------------+
| Code Health   | |landscape|       |
|               | |quantifiedcode|  |
|               |                   |
|               | |scrutinizer|     |
|               | |codeclimate|     |
|               | |codacy|          |
+---------------+-------------------+
| Issues        | |issues|          |
+---------------+-------------------+


.. |landscape| image:: https://landscape.io/github/abkfenris/snowpit/master/landscape.svg?style=flat
    :target: https://landscape.io/github/abkfenris/snowpit/master
    :alt: Code Health
.. |quantifiedcode| image:: https://www.quantifiedcode.com/api/v1/project/5422d6b89ddd45edb3b25841e48b805e/badge.svg
    :target: https://www.quantifiedcode.com/app/project/5422d6b89ddd45edb3b25841e48b805e
    :alt: Code Issues
.. |scrutinizer| image:: https://scrutinizer-ci.com/g/abkfenris/snowpit/badges/quality-score.png?b=master
    :target: https://scrutinizer-ci.com/g/abkfenris/snowpit/?branch=master
    :alt: Scrutinizer Code Quality
.. |requires.io| image:: https://requires.io/github/abkfenris/snowpit/requirements.svg?branch=master
    :target: https://requires.io/github/abkfenris/snowpit/requirements/?branch=master
    :alt: Requirements Status
.. |issues| image:: https://img.shields.io/github/issues/abkfenris/snowpit.svg
    :target: https://github.com/abkfenris/snowpit/issues
.. |codeclimate| image:: https://codeclimate.com/github/abkfenris/snowpit/badges/gpa.svg
    :target: https://codeclimate.com/github/abkfenris/snowpit
.. |codacy| image:: https://api.codacy.com/project/badge/grade/49c8bcf03b864a569a833a7c1be15236
    :target: https://www.codacy.com/app/abk/snowpit


**Table of Contents**

.. contents::
    :backlinks: none
    :local:

Installation
------------

Classes
-------

Snowpit
~~~~~~~

.. code:: python

  >>> from snowpit import Snowpit

  >>> pit = Snowpit()

Layers
~~~~~~

Stability Tests
~~~~~~~~~~~~~~~

Stability Observations
~~~~~~~~~~~~~~~~~~~~~~

Weather Observations
~~~~~~~~~~~~~~~~~~~~

XML encoding/decoding
---------------------

All of the classes implemented in this library can be encoded and decoded from SnowPilot and CAAML XML with `snowpit.dump`, `snowpit.dumps`, `snowpit.load`, and `snowpit.loads`

.. code:: python

  >>> import snowpit

  >>> pit_data = open('2014-01-04.xml') # open a SnowPilot encoded XML

  >>> snowpit.load(pit_data)
  <snowpit 2014-01-04 10:15 44.552, -70.9080>
