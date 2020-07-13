#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intervaltree
Version  : 3.0.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/e8/f9/76237755b2020cd74549e98667210b2dd54d3fb17c6f4a62631e61d31225/intervaltree-3.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/f9/76237755b2020cd74549e98667210b2dd54d3fb17c6f4a62631e61d31225/intervaltree-3.0.2.tar.gz
Summary  : Editable interval tree data structure for Python 2 and 3
Group    : Development/Tools
License  : Apache-2.0
Requires: intervaltree-license = %{version}-%{release}
Requires: intervaltree-python = %{version}-%{release}
Requires: intervaltree-python3 = %{version}-%{release}
Requires: sortedcontainers
BuildRequires : buildreq-distutils3
BuildRequires : pytest
BuildRequires : pytest-python
BuildRequires : sortedcontainers

%description
[![Build status badge][]][build status]

intervaltree
============

A mutable, self-balancing interval tree for Python 2 and 3. Queries may be by point, by range overlap, or by range envelopment.

This library was designed to allow tagging text and time intervals, where the intervals include the lower bound but not the upper bound.

**Version 3 changes!**

* The `search(begin, end, strict)` method no longer exists. Instead, use one of these:
    * `at(point)`
    * `overlap(begin, end)`
    * `envelop(begin, end)`
* The `extend(items)` method no longer exists. Instead, use `update(items)`.
* Methods like `merge_overlaps()` which took a `strict` argument consistently default to `strict=True`. Before, some methods defaulted to `True` and others to `False`.

Installing
----------

```sh
pip install intervaltree
```

Features
--------

* Supports Python 2.7 and Python 3.4+ (Tested under 2.7, and 3.4 thru 3.7)
* Initializing
    * blank `tree = IntervalTree()`
    * from an iterable of `Interval` objects (`tree = IntervalTree(intervals)`)
    * from an iterable of tuples (`tree = IntervalTree.from_tuples(interval_tuples)`)

* Insertions
    * `tree[begin:end] = data`
    * `tree.add(interval)`
    * `tree.addi(begin, end, data)`

* Deletions
    * `tree.remove(interval)`             (raises `ValueError` if not present)
    * `tree.discard(interval)`            (quiet if not present)
    * `tree.removei(begin, end, data)`    (short for `tree.remove(Interval(begin, end, data))`)
    * `tree.discardi(begin, end, data)`   (short for `tree.discard(Interval(begin, end, data))`)
    * `tree.remove_overlap(point)`
    * `tree.remove_overlap(begin, end)`   (removes all overlapping the range)
    * `tree.remove_envelop(begin, end)`   (removes all enveloped in the range)

* Point queries
    * `tree[point]`
    * `tree.at(point)`                    (same as previous)

* Overlap queries
    * `tree[begin:end]`
    * `tree.overlap(begin, end)`          (same as previous)

* Envelop queries
    * `tree.envelop(begin, end)`

* Membership queries
    * `interval_obj in tree`              (this is fastest, O(1))
    * `tree.containsi(begin, end, data)`
    * `tree.overlaps(point)`
    * `tree.overlaps(begin, end)`

* Iterable
    * `for interval_obj in tree:`
    * `tree.items()`

* Sizing
    * `len(tree)`
    * `tree.is_empty()`
    * `not tree`
    * `tree.begin()`          (the `begin` coordinate of the leftmost interval)
    * `tree.end()`            (the `end` coordinate of the rightmost interval)

* Set-like operations
    * union
        * `result_tree = tree.union(iterable)`
        * `result_tree = tree1 | tree2`
        * `tree.update(iterable)`
        * `tree |= other_tree`

    * difference
        * `result_tree = tree.difference(iterable)`
        * `result_tree = tree1 - tree2`
        * `tree.difference_update(iterable)`
        * `tree -= other_tree`

    * intersection
        * `result_tree = tree.intersection(iterable)`
        * `result_tree = tree1 & tree2`
        * `tree.intersection_update(iterable)`
        * `tree &= other_tree`

    * symmetric difference
        * `result_tree = tree.symmetric_difference(iterable)`
        * `result_tree = tree1 ^ tree2`
        * `tree.symmetric_difference_update(iterable)`
        * `tree ^= other_tree`

    * comparison
        * `tree1.issubset(tree2)` or `tree1 <= tree2`
        * `tree1 <= tree2`
        * `tree1.issuperset(tree2)` or `tree1 > tree2`
        * `tree1 >= tree2`
        * `tree1 == tree2`

* Restructuring
    * `chop(begin, end)`      (slice intervals and remove everything between `begin` and `end`, optionally modifying the data fields of the chopped-up intervals)
    * `slice(point)`          (slice intervals at `point`)
    * `split_overlaps()`      (slice at all interval boundaries, optionally modifying the data field)
    * `merge_overlaps()` (joins overlapping intervals into a single interval, optionally merging the data fields)
    * `merge_equals()` (joins intervals with matching ranges into a single interval, optionally merging the data fields)

* Copying and typecasting
    * `IntervalTree(tree)`    (`Interval` objects are same as those in tree)
    * `tree.copy()`           (`Interval` objects are shallow copies of those in tree)
    * `set(tree)`             (can later be fed into `IntervalTree()`)
    * `list(tree)`            (ditto)

* Pickle-friendly
* Automatic AVL balancing

Examples
--------

* Getting started

    ``` python
    >>> from intervaltree import Interval, IntervalTree
    >>> t = IntervalTree()
    >>> t
    IntervalTree()

    ```

* Adding intervals - any object works!

    ``` python
    >>> t[1:2] = "1-2"
    >>> t[4:7] = (4, 7)
    >>> t[5:9] = {5: 9}

    ```

* Query by point

    The result of a query is a `set` object, so if ordering is important,
    you must sort it first.

    ``` python
    >>> sorted(t[6])
    [Interval(4, 7, (4, 7)), Interval(5, 9, {5: 9})]
    >>> sorted(t[6])[0]
    Interval(4, 7, (4, 7))

    ```

* Query by range

    Note that ranges are inclusive of the lower limit, but non-inclusive of the upper limit. So:

    ``` python
    >>> sorted(t[2:4])
    []

    ```

    Since our search was over `2 ≤ x < 4`, neither `Interval(1, 2)` nor `Interval(4, 7)`
    was included. The first interval, `1 ≤ x < 2` does not include `x = 2`. The second
    interval, `4 ≤ x < 7`, does include `x = 4`, but our search interval excludes it. So,
    there were no overlapping intervals. However:

    ``` python
    >>> sorted(t[1:5])
    [Interval(1, 2, '1-2'), Interval(4, 7, (4, 7))]

    ```

    To only return intervals that are completely enveloped by the search range:

    ``` python
    >>> sorted(t.envelop(1, 5))
    [Interval(1, 2, '1-2')]

    ```

* Accessing an `Interval` object

    ``` python
    >>> iv = Interval(4, 7, (4, 7))
    >>> iv.begin
    4
    >>> iv.end
    7
    >>> iv.data
    (4, 7)

    >>> begin, end, data = iv
    >>> begin
    4
    >>> end
    7
    >>> data
    (4, 7)

    ```

* Constructing from lists of intervals

    We could have made a similar tree this way:

    ``` python
    >>> ivs = [(1, 2), (4, 7), (5, 9)]
    >>> t = IntervalTree(
    ...    Interval(begin, end, "%d-%d" % (begin, end)) for begin, end in ivs
    ... )

    ```

    Or, if we don't need the data fields:

    ``` python
    >>> t2 = IntervalTree(Interval(*iv) for iv in ivs)

    ```

    Or even:

    ``` python
    >>> t2 = IntervalTree.from_tuples(ivs)

    ```

* Removing intervals

    ``` python
    >>> t.remove(Interval(1, 2, "1-2"))
    >>> sorted(t)
    [Interval(4, 7, '4-7'), Interval(5, 9, '5-9')]

    >>> t.remove(Interval(500, 1000, "Doesn't exist"))  # raises ValueError
    Traceback (most recent call last):
    ValueError

    >>> t.discard(Interval(500, 1000, "Doesn't exist"))  # quietly does nothing

    >>> del t[5]  # same as t.remove_overlap(5)
    >>> t
    IntervalTree()

    ```

    We could also empty a tree entirely:

    ``` python
    >>> t2.clear()
    >>> t2
    IntervalTree()

    ```

    Or remove intervals that overlap a range:

    ``` python
    >>> t = IntervalTree([
    ...     Interval(0, 10),
    ...     Interval(10, 20),
    ...     Interval(20, 30),
    ...     Interval(30, 40)])
    >>> t.remove_overlap(25, 35)
    >>> sorted(t)
    [Interval(0, 10), Interval(10, 20)]

    ```

    We can also remove only those intervals completely enveloped in a range:

    ``` python
    >>> t.remove_envelop(5, 20)
    >>> sorted(t)
    [Interval(0, 10)]

    ```

* Chopping

    We could also chop out parts of the tree:

    ``` python
    >>> t = IntervalTree([Interval(0, 10)])
    >>> t.chop(3, 7)
    >>> sorted(t)
    [Interval(0, 3), Interval(7, 10)]

    ```

    To modify the new intervals' data fields based on which side of the interval is being chopped:

    ``` python
    >>> def datafunc(iv, islower):
    ...     oldlimit = iv[islower]
    ...     return "oldlimit: {0}, islower: {1}".format(oldlimit, islower)
    >>> t = IntervalTree([Interval(0, 10)])
    >>> t.chop(3, 7, datafunc)
    >>> sorted(t)[0]
    Interval(0, 3, 'oldlimit: 10, islower: True')
    >>> sorted(t)[1]
    Interval(7, 10, 'oldlimit: 0, islower: False')

    ```

* Slicing

    You can also slice intervals in the tree without removing them:

    ``` python
    >>> t = IntervalTree([Interval(0, 10), Interval(5, 15)])
    >>> t.slice(3)
    >>> sorted(t)
    [Interval(0, 3), Interval(3, 10), Interval(5, 15)]

    ```

    You can also set the data fields, for example, re-using `datafunc()` from above:

    ``` python
    >>> t = IntervalTree([Interval(5, 15)])
    >>> t.slice(10, datafunc)
    >>> sorted(t)[0]
    Interval(5, 10, 'oldlimit: 15, islower: True')
    >>> sorted(t)[1]
    Interval(10, 15, 'oldlimit: 5, islower: False')

    ```

Future improvements
-------------------

See the [issue tracker][] on GitHub.

Based on
--------

* Eternally Confuzzled's [AVL tree][Confuzzled AVL tree]
* Wikipedia's [Interval Tree][Wiki intervaltree]
* Heavily modified from Tyler Kahn's [Interval Tree implementation in Python][Kahn intervaltree] ([GitHub project][Kahn intervaltree GH])
* Incorporates contributions from:
    * [konstantint/Konstantin Tretyakov][Konstantin intervaltree] of the University of Tartu (Estonia)
    * [siniG/Avi Gabay][siniG intervaltree]
    * [lmcarril/Luis M. Carril][lmcarril intervaltree] of the Karlsruhe Institute for Technology (Germany)

Copyright
---------

* [Chaim Leib Halbert][GH], 2013-2018
* Modifications, [Konstantin Tretyakov][Konstantin intervaltree], 2014

Licensed under the [Apache License, version 2.0][Apache].

The source code for this project is at https://github.com/chaimleib/intervaltree


[build status badge]: https://travis-ci.org/chaimleib/intervaltree.svg?branch=master
[build status]: https://travis-ci.org/chaimleib/intervaltree
[GH]: https://github.com/chaimleib/intervaltree
[issue tracker]: https://github.com/chaimleib/intervaltree/issues
[Konstantin intervaltree]: https://github.com/konstantint/PyIntervalTree
[siniG intervaltree]: https://github.com/siniG/intervaltree
[lmcarril intervaltree]: https://github.com/lmcarril/intervaltree
[Confuzzled AVL tree]: http://www.eternallyconfuzzled.com/tuts/datastructures/jsw_tut_avl.aspx
[Wiki intervaltree]: http://en.wikipedia.org/wiki/Interval_tree
[Kahn intervaltree]: http://zurb.com/forrst/posts/Interval_Tree_implementation_in_python-e0K
[Kahn intervaltree GH]: https://github.com/tylerkahn/intervaltree-python
[Apache]: http://www.apache.org/licenses/LICENSE-2.0

%package license
Summary: license components for the intervaltree package.
Group: Default

%description license
license components for the intervaltree package.


%package python
Summary: python components for the intervaltree package.
Group: Default
Requires: intervaltree-python3 = %{version}-%{release}

%description python
python components for the intervaltree package.


%package python3
Summary: python3 components for the intervaltree package.
Group: Default
Requires: python3-core
Provides: pypi(intervaltree)

%description python3
python3 components for the intervaltree package.


%prep
%setup -q -n intervaltree-3.0.2
cd %{_builddir}/intervaltree-3.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583158440
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intervaltree
cp %{_builddir}/intervaltree-3.0.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/intervaltree/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intervaltree/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
