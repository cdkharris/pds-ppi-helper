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

This should return something like the following:

    Found 3 results!
    
      AUTHORITY                  ...                                                       id
    0       PPI                  ...                      GO-J-EPD-2-REDR-HIGHRES-SECTOR-V1.0
    1       PPI                  ...                    GO-J-HIC-3-RDR-HIGHRES-COUNTRATE-V1.0
    2       PPI                  ...                              GO-J-MAG-3-RDR-HIGHRES-V1.0
    
    [3 rows x 11 columns]

We've found 3 'highres' datasets about Europa. `my_search.results` is a [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe) which stores a table of information about the results.

To learn what information we have retrieved for each result, we can do:

    my_search.results.keys()

Which ought to return:

    Index(['AUTHORITY', 'INSTRUMENT_ID', 'INSTRUMENT_TYPE', 'MISSION_NAME',
       'SPACECRAFT_NAME', 'TARGET_NAME', 'VOLUME_NAME', 'VOLUME_SERIES_NAME',
       'certified', 'description', 'id'],
      dtype='object')

To learn what missions these results come from, we can do:

    my_search.results['MISSION_NAME']

Which ought to return:

    0    GALILEO
    1    GALILEO
    2    GALILEO
    Name: MISSION_NAME, dtype: object

So all these results come from the Galileo Orbiter.

We can look at the description of the result at index 2 with:

    print(my_search.results.iloc[2]['description'])

Which returns:

    This data set contains the Galileo Orbiter Jupiter MAG
    High-Res. Magnetic-Field Data High resolution &#40;1/3 sec&#41; Galileo
    Magnetometer data and browse plots from the Jovian satellite flybys
    &#40;Io, Europa, Ganymede, Callisto, and Amalthea&#41; and other points of
    interest in the magnetosphere.

So we searched for high-resolution datasets about Europa, and we found a dataset which contains Magnetometer data from flybys of the Galilean moons.

### Get a dataset

We can use search results to find even more information about a given dataset.

The unique id of a dataset in the search results can be accessed with:

    print(my_search.results.iloc[2]['id'])

Which should return:

    GO-J-MAG-3-RDR-HIGHRES-V1.0

We can then get all available metadata about the dataset with:

    my_dataset = pds.get_dataset(my_search.results.iloc[2]['id'])

We can describe this dataset with:

    my_dataset.describe()

Which should return:

    Galileo Orbiter Jupiter MAG High-Res. Magnetic-Field Data
    
    This data set contains the Galileo Orbiter Jupiter MAG
    High-Res. Magnetic-Field Data High resolution &#40;1/3 sec&#41; Galileo
    Magnetometer data and browse plots from the Jovian satellite flybys
    &#40;Io, Europa, Ganymede, Callisto, and Amalthea&#41; and other points of
    interest in the magnetosphere.
    
    For more information, please visit
    https://pds-ppi.igpp.ucla.edu/search/view/?f=yes&id=pds://PPI/GO-J-MAG-3-RDR-HIGHRES-V1.0

And we can see what kinds of information are now available with:

    my_dataset.dataset.keys()

Which should return:

    dict_keys(['VOLUME_ID', 'AUTHORITY', 'PDS_VERSION', 'description', 'VOLUME_SET_ID', 'id', 'VOLUMES', 'PUBLICATION_DATE', 'MISSION_NAME', 'createDate', 'clickCount', 'active', 'startdate', 'stopdate', 'VOLUME_NAME', 'VOLUME_SET_NAME', 'VOLUME_SERIES_NAME', 'slot', 'updateDate', 'errata', 'certified', 'nssdcaStatus', 'nssdcaLastUpdatedDate', 'nssdcaId', 'size', 'archiveStatus', 'archiveType', 'INSTRUMENT_TYPE', 'DATA_SET_ID', 'INSTRUMENT_NAME', 'TARGET_NAME', 'keyword', 'SPACECRAFT_NAME', 'INSTRUMENT_ID'])


## License
This repository is licensed under [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
This work is not affiliated or supported by NASA and we do not make a guarantee of the accuracy of data or tools for scientific or research purposes.


## Contributors and Acknowledgments 
This package has been developed in collaboration by planetary scientists [C. D. K. Harris](https://github.com/cdkharris) and [A. R. Azari](https://github.com/astro-abby).

