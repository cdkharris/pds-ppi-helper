# pds-ppi-helper<a id="sec-1" name="sec-1"></a>
This is a helpful python package for interfacing with the Planetary Plasma Interactions node on NASA's Planetary Data System ([PDS-PPI](https://pds-ppi.igpp.ucla.edu/))! Our goals are to create a useful python package to navigate through the PPI PDS site and inform users of both download and exploration capability.


<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. pds-ppi-helper</a>
<ul>
<li><a href="#sec-1-1">1.1. Installation</a></li>
<li><a href="#sec-1-2">1.2. Examples</a>
<ul>
<li><a href="#sec-1-2-1">1.2.1. Do a search</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

## Installation<a id="sec-1-1" name="sec-1-1"></a>

1.  Download or clone this repository.
2.  From within `pds-ppi-helper/`, run the following command to install the package: `pip install .`
3.  Try running `pds-ppi-helper/example_script.py` either from the command line
    with `$ python example_script.py` or from the Ipython terminal with `%run example_script.py`

## Examples<a id="sec-1-2" name="sec-1-2"></a>

### Do a search<a id="sec-1-2-1" name="sec-1-2-1"></a>

    import pds_ppi_helper as pds
    
    my_search = pds.search(target = 'Europa', nrows = '10', keyword='highres')
    
    print('Found {} results!'.format(my_search.numfound))
    print(my_search.results)
    


## License
This repository is liscensed under [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). This work is not affiliated or supported by NASA and we do not make a guarantee of the accuracy of data or tools for scientific or research purposes.

## Contribtors and Acknowledgments 
This package has been developed in collaboration with planetary scientist [C. D. K. Harris](https://github.com/cdkharris) and [A. R. Azari](https://github.com/astro-abby).

Last update 5/30/2018
