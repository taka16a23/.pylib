from .html_tag_gen import HTMLTagGenerator
from .show import Show

class Recipe(Show, HTMLTagGenerator):
    """Class Recipe
    """
    # Attributes:

    # Operations
    def show(self):
        """function show

        returns
        """
        return None # should raise NotImplementedError()

    def generate_html_tag(self):
        """function generate_html_tag

        returns
        """
        return None # should raise NotImplementedError()
