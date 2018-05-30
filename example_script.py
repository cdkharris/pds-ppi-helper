"""This script may be run from an Ipython terminal with:
%run example_script.py
"""

import pds_ppi_helper as pds

target = "Jupiter"

search = pds.search(target=target)

print('Found {} results!'.format(search.numfound))
print(search.results)
