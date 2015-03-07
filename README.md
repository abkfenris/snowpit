# snowpit

This library plans to contain:

- Functions for encoding and decoding SnowPilot and CAAML XML formatted data
- Classes for snowpits, layers, stability tests, stability observations, and weather observations

## Installation

## Classes

### Snowpits

### Layers

### Stability Tests

### Stability Observations

### Weather Observations

## XML encoding/decoding

All of the classes implemented in this library can be encoded and decoded from SnowPilot and CAAML XML with `snowpit.dump`, `snowpit.dumps`, `snowpit.load`, `snowpit.loads`

```python

>>> import snowpit

>>> pit_data = open('2014-01-04.xml')
>>> snowpit.load(pit_data)
{}

```
