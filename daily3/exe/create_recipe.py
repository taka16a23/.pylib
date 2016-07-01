#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""create_recipe -- DESCRIPTION

"""
import sys
from daily3.exe.webpage import ChromeWebpage, ChromeWebpageObserver
from xahk.rectangle import Point

from recipe._recipe import SEIKYO_URL, RECIPE_URL


FAVORITE_URL = 'https://shop.nanairo.coop/front/bb/shiga/product/productlist?dt=f&pc=15111000&b=TmpBean--70806817'
ORDERED_URL = 'https://shop.nanairo.coop/front/bb/shiga/order/orderhistory?pc=15111000&b=TmpBean--70806817'


class SeikyoMove(ChromeWebpageObserver):
    r"""SeikyoMove

    SeikyoMove is a ChromeWebpageObserver.
    Responsibility:
    """
    point = Point(1550, 70)

    def on_chrome_window_created(self, webpage):
        """SUMMARY

        name()

        @Return:

        @Error:
        """
        window = webpage.window
        window.move(self.point).check()
        if not window.is_maximized():
            window.maximize().check()


def _main():
    webpage = ChromeWebpage((SEIKYO_URL, FAVORITE_URL, ORDERED_URL, RECIPE_URL))
    webpage.add_observer(SeikyoMove())
    webpage.start()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# create_recipe.py ends here
