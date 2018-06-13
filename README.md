# pds-ppi-helper
This is a helpful python package for interfacing with the Planetary Plasma Interactions node on NASA's Planetary Data System ([PDS-PPI](https://pds-ppi.igpp.ucla.edu/))!
Our goals are to create a useful python package to navigate through the PDS-PPI datasets and inform users of both download and exploration capability.


## Installation

1.  Download or clone this repository.
2.  From within `pds-ppi-helper/`, run the following command to install the package: `pip install .`
3.  Try running `pds-ppi-helper/example_script.py` either from the command line
    with `$ python example_script.py` or from the Ipython terminal with `%run example_script.py`


## Examples

### Do a search

    import pds_ppi_helper as pds
    
    my_search = pds.search(target = 'Europa', nrows = '10', keyword='highres')
    
    print('Found {} results!'.format(my_search.numfound))
    print(my_search.results)
    

## License
This repository is licensed under [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
This work is not affiliated or supported by NASA and we do not make a guarantee of the accuracy of data or tools for scientific or research purposes.


## Contributors and Acknowledgments 
This package has been developed in collaboration by planetary scientists [C. D. K. Harris](https://github.com/cdkharris) and [A. R. Azari](https://github.com/astro-abby).

