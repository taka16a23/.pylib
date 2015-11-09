#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""graph -- DESCRIPTION

"""
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties


class SalesHistoryLineGraph(object):
    r"""SalesHistoryLineGraph

    SalesHistoryLineGraph is a object.
    Responsibility:
    """
    def __init__(self, sales):
        r"""

        @Arguments:
        - `sales`:
        - `title`:
        """
        self._sales = list(sales)

    def append(self, sales):
        r"""SUMMARY

        append(sales)

        @Arguments:
        - `sales`:

        @Return:

        @Error:
        """
        self._sales.append(sales)

    def _create_graph(self, ):
        r"""SUMMARY

        _create_graph()

        @Return:

        @Error:
        """
        _, ax = pyplot.subplots()
        # x
        x_ticks = [i.period for i in self._sales]
        x = range(0, len(x_ticks)) # make count x
        pyplot.xlim(min(x) - 0.5, max(x) + 0.5)
        pyplot.xticks(x, x_ticks, rotation='vertical') # spacing and vertical show
        # y
        y = [i.price for i in self._sales]
        ymin, ymax = min(y), max(y)
        yspace = ymax / 10
        pyplot.ylim(ymin - yspace, ymax + yspace) # spacing
        # average
        pyplot.figtext(0.78, 0.25, 'Average: {}'.format(sum(y) / len(y)),
                       color='red', fontweight='bold') # relative insert text
        # plot
        ax.plot(x, y, 'bo-', linewidth=1.5)
        # for japanese
        fp = FontProperties(
            fname='/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf')
        # title
        pyplot.title(self._sales[0].order_no + ':' + self._sales[0].name,
                     fontdict={'fontproperties':fp}, size=20, y=1.08)
        # label
        pyplot.legend(prop=fp)
        pyplot.xlabel('Periods', fontsize=20)
        pyplot.ylabel(u'値段(円)', fontsize=20, fontdict={'fontproperties':fp})
        # annotate to point
        for X, Y, Z in zip(x, y, y):
            # Annotate the points 5 _points_ above and to the left of the vertex
            ax.annotate('{}'.format(Z), xy=(X,Y), xytext=(-5, 5),
                        textcoords='offset points', size='large',
                        fontweight='roman')
        # fit
        pyplot.tight_layout()

    def save(self, path):
        r"""SUMMARY

        save(path)

        @Arguments:
        - `path`:

        @Return:

        @Error:
        """
        self._create_graph()
        pyplot.savefig(path)

    def show(self, ):
        r"""SUMMARY

        show()

        @Return:

        @Error:
        """
        self._create_graph()
        pyplot.show()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# graph.py ends here
