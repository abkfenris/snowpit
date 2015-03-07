snowpit
=======

This library plans to contain:

- Functions for encoding and decoding SnowPilot and CAAML XML formatted data
- Classes for snowpits, layers, stability tests, stability observations, and weather observations

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
