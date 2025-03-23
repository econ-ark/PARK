# Exploring Econ-ARK via Jupyter Notebooks

[Paul Romer](http://paulromer.net)'s blog post [Jupyter, Mathematica, and the Future of the Research Paper](https://paulromer.net/jupyter-mathematica-and-the-future-of-the-research-paper/) makes a persuasive case that [Jupyter notebooks](http://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html) are now a highly effective tool for scholarly communication, and that eventually research papers will take a form like Jupyter notebooks.

Romer has posted an example [on his GitHub site](https://github.com/paulromer149/) of how such a notebook can be used to illustrate a quantitative point in a rich context with text, symbolic mathematics, and computational results.  This is done by creating [a dedicated GitHub repo](https://github.com/paulromer149/Qn_temp/) containing the notebook along with the configuration information needed to execute it.
Given such a repo, [MyBinder.org](http://MyBinder.org) can be used to create a url which, [when retrieved](https://mybinder.org/v2/gh/paulromer149/Qn_temp/master?filepath=.%2FTriangle.ipynb), opens the notebook in a 'live' browser window that (eventually; be patient) allows the user to execute the code that produces the results in the notebook.  (It does this by spinning up a dedicated [Docker](https://en.wikipedia.org/wiki/Docker_(software)) instance that performs the calculations on demand).

(Romer has configured the notebook so that the code is not visible by default; but for any result, the code can be exposed by selecting the cell in the notebook above the result and clicking the 'show/hide' icon '^' in the toolbar).

The creation of Jupyter notebooks like this one will be the default method in Econ-ARK of demonstrating the capabilities of [Tools](), executing [Examples](), and running Models[]().
