# coding: utf-8

import re


class Legendarium(object):

    def __init__(self, acron_title='', year_pub='', volume='', number='',
                 fpage='', lpage='', article_id='', suppl_number=''):

        self.acron_title = acron_title
        self.year_pub = str(year_pub)
        self.volume = volume
        self.number = number
        self.suppl_number = suppl_number
        self.fpage = fpage
        self.lpage = lpage
        self.article_id = article_id

    def __unicode__(self):
        return self.stamp

    def __str__(self):
        return self.stamp

    def __repr__(self):
        return self.stamp

    def _get_numbers(self, text):
        """
        Get just numbers in a text.
        """
        if text:
            return re.sub("[^0-9]", "", text)
        else:
            return ''

    def _clean_year_pub(self):
        """
        Clean the year removing all caracter and keep just 4/1 numbers.
        """
        if self.year_pub:
            year = self._get_numbers(self.year_pub)
            if len(year) == 4:
                return ' {0}'.format(year[:4])
            else:
                raise ValueError(u'Probably not a valid year')
        else:
            return u''

    def _clean_volume(self):
        """
        Clean the volume removing all caracter and keep just numbers.
        """
        return self._get_numbers(self.volume)

    def _clean_number(self):
        """
        Clean the number stripped the beginning and the end of the string.
        """
        if self.number:
            return self.number.strip()
        else:
            return ''

    def _clean_acron_title(self):
        """
        Clean the title stripped the beginning and the end of the string.
        """
        return self.acron_title.strip()

    def _clean_suppl_number(self):
        """
        Clean the suppl_number stripped the beginning and the end of the string.
        """
        if self.suppl_number:
            return self.suppl_number.strip()
        else:
            return ''

    def get_journal(self):
        """
        Method to build the journal, it can have ``year_pub`` or not.
        """
        if self.acron_title:
            title = self._clean_acron_title()
        else:
            raise ValueError(u'The journal is mandatory to mount the bibliographic legend')

        year_pub = self._clean_year_pub()

        return u'{0}{1}'.format(title, year_pub)

    def get_issue(self):
        """
        Method to build the issue.
        """
        volume = self._clean_volume()
        number = self._clean_number()
        suppl = self._clean_suppl_number()

        if number or suppl:
            number = u'({0}{1})'.format(number, '{0}suppl.{1}'.format(' ' if number else '', suppl) if suppl else '')

        if volume or number:
            return u'{0}{1}{2}'.format(';', volume, number)
        else:
            return u''

    def get_article(self):
        """
        Method to build the article.
        """
        article = u''

        if self.article_id:
            article = self.article_id
        elif self.fpage and self.lpage:
            article = u'{0}-{1}'.format(self.fpage, self.lpage)
        elif self.fpage:
            article = self.fpage
        elif self.lpage:
            article = self.lpage
        else:
            return article

        return u'{0}{1}'.format(':', article)

    @property
    def stamp(self):
        """
        Print the legend follow the basic definition:

            REVISTA ANO;VOLUME(NUMBER):ID_ARTICLE
        """
        args = [self.get_journal(), self.get_issue(), self.get_article()]

        return u'{0}{1}{2}'.format(*args)
