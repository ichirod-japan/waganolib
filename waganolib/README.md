A Multi-purpose package designed for **japanese**-related functions

# Haversine

To use one of the basic functions on this module, also known as **haversine** you can copy the following code for testing:
```py
print(calculation.haversine(52.370216, 4.895168, 52.520008,
    13.404954) == 945793.4375088713)
```
Harversine gets you the ability to Calculate the great circle distance between two points on the 
earth (specified in decimal degrees), returns the distance in
meters.
All arguments must be of equal length.
**:param lon1:** longitude of first place
**:param lat1:** latitude of first place
**:param lon2:** longitude of second place
**:param lat2:** latitude of second place
**:return:** distance in meters between the two sets of coordinates
*So far, this is not japanese-related but is included in calculation.py so as to help you in the field*
*of math and algebra. Other calculation functions will be listed in future updates on here.*

# mean([])

Mean is a default feature that would allow you to Calculate the arithmetic mean ("the average") of data:
```py
>>> mean([-1.0, 2.5, 3.25, 5.75])
2.625
```
The calculation of the average is a known default, but has been tweaked a little to fit the purpose.

# median([])

Median is a feature that is similar to the one previously shown, mean, and it calculates the standard median of discrete data:
```py
>>> median([2, 3, 4, 5])
3.5
```

Median has an extension which calculates the median, or 50th percentile, of data grouped into class intervals
centred on the data values provided. E.g. if your data points are rounded to
the nearest whole number:
```py
>>> median_grouped([2, 2, 3, 3, 3, 4])  #doctest: +ELLIPSIS
2.8333333333...
```
This should be interpreted in this way: you have two data points in the class
interval 1.5-2.5, three data points in the class interval 2.5-3.5, and one in
the class interval 3.5-4.5. The median of these data points is 2.8333...
Calculating variability or spread

# stdev

stdev is a feature that calculates the standard deviation of sample data:
```py
>>> stdev([2.5, 3.25, 5.5, 11.25, 11.75])  #doctest: +ELLIPSIS
4.38961843444...
```
If you have previously calculated the mean, you can pass it as the optional
second argument to the four "spread" functions to avoid recalculating it:
```py
>>> data = [1, 2, 2, 4, 4, 4, 5, 6]
>>> mu = mean(data)
>>> pvariance(data, mu)
2.5

Exceptions
```

# _sum

Yet another feature in calculation.py is the _sum.
the _sum returns a high-precision sum of the given numeric data as a fraction,
    together with the type to be converted to and the count of items.
    If optional argument ``start`` is given, it is added to the total.
    If ``data`` is empty, ``start`` (defaulting to 0) is returned.
    Examples
    --------
```py
    >>> _sum([3, 2.25, 4.5, -0.5, 1.0], 0.75)
    (<class 'float'>, Fraction(11, 1), 5)
```
    Some sources of round-off error will be avoided:
```py
    # Built-in sum returns zero.
    >>> _sum([1e50, 1, -1e50] * 1000)
    (<class 'float'>, Fraction(1000, 1), 3000)
```
    Fractions and Decimals are also supported:
```py
    >>> from fractions import Fraction as F
    >>> _sum([F(2, 3), F(7, 5), F(1, 4), F(5, 6)])
    (<class 'fractions.Fraction'>, Fraction(63, 20), 4)
    >>> from decimal import Decimal as D
    >>> data = [D("0.1375"), D("0.2108"), D("0.3061"), D("0.0419")]
    >>> _sum(data)
    (<class 'decimal.Decimal'>, Fraction(6963, 10000), 4)
```
    Mixed types are currently treated as an error, except that int is
    allowed.

# Summary

I don't think you expected this, but I won't list all features over here, you can find most of the features of calculation.py at https://github.com/python/cpython/blob/master/Lib/statistics.py, where most features reside.
There is only a calculation.py file for now, since the module is still on 0.5.2, but the japanese-related features will be added very soon, and it is frantically being worked on!
