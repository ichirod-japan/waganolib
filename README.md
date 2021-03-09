Wagano is a Multi-purpose package designed for **japanese**-related functions.
An extension of its features goes to a calculation.py file, where different features associated with math overlay.

![Logo](https://github.com/ichirod-japan/waganolib/blob/main/images/wagano.jfif?raw=true)

# Table of Contents

[Requirements](https://github.com/ichirod-japan/waganolib#requirements)

[Installation](https://github.com/ichirod-japan/waganolib#installation)

[Help](https://github.com/ichirod-japan/waganolib#help)

[Build Source Code](https://github.com/ichirod-japan/waganolib#build-source-code)

[License](https://github.com/ichirod-japan/waganolib#license)

[Features](https://github.com/ichirod-japan/waganolib#features)

[Haversine](https://github.com/ichirod-japan/waganolib#Haversine)

[Mean](https://github.com/ichirod-japan/waganolib#mean)

[Median](https://github.com/ichirod-japan/waganolib#median)

[Stdev](https://github.com/ichirod-japan/waganolib#stdev)

[_sum](https://github.com/ichirod-japan/waganolib#_sum)

[Summary](https://github.com/ichirod-japan/waganolib#summary)


# Requirements

There is one thing you must have installed (the basics) before installing this module:

- Python 3.6.8

It may work on other versions, however, it has not been tested whether it'll work on them or not.

# Installation

One of the recommended ways to install wagano is by PyPi's pip.
```
pip install wagano
```
____________
Another way to get wagano is to git clone.

```
git clone https://github.com/ichirod-japan/waganolib.git
```
Then you can run the setup file from there.
```
python setup.py install
```
(or if you're on a Unix-Like OS (such as MacOS or Linux), use `sudo python setup.py install`)

# Help

If you need help or have an issue, do not hesitate to open one at https://github.com/ichirod-japan/waganolib/issues
Very soon, this module is going to have a documentation to answer some of the basic questions.
Remember before submitting an issue, check other issues (closed as well) and see if your question has already been answered.

# build-source-code

If you want to use features that are currently in development, or you want to contribute to wagano, you will need to build wagano locally from its source code, rather than pip installing it.

Installing from source is fairly automated. The most work will involve compiling and installing all the wagano dependencies (not much, really). Once that is done, run the setup.py script which will attempt to auto-configure, build, and install wagano.

# License

This library is distributed under the [MIT License](https://github.com/ichirod-japan/waganolib/blob/main/LICENSE) which can be found in the `waganolib/LICENSE` file.

# Features

The following is a content table for all the **features** and only features of this README.md file.
[Haversine](https://github.com/ichirod-japan/waganolib#Haversine)
[Mean](https://github.com/ichirod-japan/waganolib#mean)
[Median](https://github.com/ichirod-japan/waganolib#median)
[Stdev](https://github.com/ichirod-japan/waganolib#stdev)
[_sum](https://github.com/ichirod-japan/waganolib#_sum)
[Summary](https://github.com/ichirod-japan/waganolib#summary)

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

# Table of 4 Following features

==================  =============================================
Function            Description
==================  =============================================
pvariance           Population variance of data.
variance            Sample variance of data.
pstdev              Population standard deviation of data.
stdev               Sample standard deviation of data.
==================  =============================================

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
