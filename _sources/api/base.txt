``snowpit``
===================

XML encoding and decoding
-------------------------

To load an xml file encoded in either SnowPilot or CAAML XML formats use
``snowpit.load`` on a file object

.. code:: python

  >>> import snowpit

  >>> pit_data = open('2014-01.04.xml', 'rb')

  >>> snowpit.load(pit_data)
  <Snowpit 2014-01-04 10:15 - 44.552, -70.9080>
