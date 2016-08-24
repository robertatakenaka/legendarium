Legendarium
===========

* Python library to handle SciELO`s bibliographic legend
* License: BSD
* Compatible With: python 2.7 and 3.5

[![Build Status](https://travis-ci.org/scieloorg/legendarium.svg)](https://travis-ci.org/scieloorg/legendarium)

See Build: https://travis-ci.org/scieloorg/legendarium


Develop API Usage
---------

<pre>
<code>
>>>from legendarium import Legendarium
>>>leg_dict = {'acron_title': 'Rev.Mal-Estar Subj', 'year_pub': '2011', 'volume': '67', 'number': '9', 'fpage': '154', 'lpage':'200', 'article_id':'e00120416'}
>>>leg = Legendarium(**leg_dict)
>>>leg.stamp
>>>Rev.Mal-Estar Subj 2011;67(9):154-200
</code>
</pre>


For develop version
====================

-e git+git@github.com:scieloorg/legendarium#egg=legendarium
