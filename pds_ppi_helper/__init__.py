"""A module for searching NASA PDS's PPI node.

classes
    SearchResults: Gives the results of a search with the given search terms.
    DataSet: Gives metadata about a dataset.

functions
    search: Returns a SearchResults object for the given search terms.
    get_dataset: Returns a DataSet object for the given unique id.
"""


from time import sleep
import requests
import json
import pandas as pd


# Constants
PDS_PPI_URL = 'https://pds-ppi.igpp.ucla.edu/'


class SearchResults():
    """Gives the results of a search and metadata about the search.
    Sleeps first in order to be polite to NASA PDS. :D

    Attributes:
    numfound -- the number of results returned by the query.
    results -- a pandas DataFrame which stores the search results.
    """
    def __init__(self,query:str):
        sleep(2)
        r = requests.get(PDS_PPI_URL + query)
        search_results_json = json.loads(r.content)
        search_results = pd.DataFrame(search_results_json['response']['docs'])
        self.numfound = search_results_json['response']['numFound']
        self.results = search_results


class DataSet():
    """Retrieves detailed metadata about a dataset.
    Sleeps first for politeness.
    
    Attributes:
    numfound -- The number of results returned by the query. This should always be 1.
    dataset -- A dict which stores all available metadata about the dataset.
    
    Methods:
    describe -- Prints the description of the dataset.
    """
    def __init__(self,query:str):
        sleep(2)
        r = requests.get(PDS_PPI_URL + query)
        search_results_json = json.loads(r.content)
        search_results = search_results_json['response']['docs'][0]
        self.numfound = search_results_json['response']['numFound']
        self.dataset = search_results
        self.url = PDS_PPI_URL+'search/view/?f=yes&id=pds://PPI/'+self.dataset['id']

    def describe(self):
        """Prints the description of the dataset.
        """
        print(self.dataset['VOLUME_NAME']+'\n')
        print(self.dataset['description'])
        print('For more information, please visit\n'+self.url)


def __write_query(mission='all',instrument='all',target='all',keyword=None,nrows='10'):
    ## Return the metadex query string to append to PDS_PPI_URL.
    query=''
    if mission != 'all':
        query='MISSION_NAME:('+mission+')'
    if instrument != 'all':
        if query != '':
            query += ' AND '
        query += 'INSTRUMENT_ID:'+instrument
    if target != 'all':
        if query !='':
            query += ' AND '
        query += 'TARGET_NAME:('+target+')'
    if keyword != None:
        if query != '':
            query += ' AND '
        query += keyword
    if (mission == 'all' and
        instrument == 'all' and
        target == 'all' and
        keyword == None):
        query = '*:*'
    
    query += ' AND active:true'
    url_params = ('/metadex/select/?'
    'q='+query+'&start=0&rows='+nrows+'&indent=on&wt=json&fl=MISSION_NAME,'
    'id,certified,VOLUME_NAME,AUTHORITY,SPACECRAFT_NAME,'
    'TARGET_NAME,INSTRUMENT_ID,INSTRUMENT_TYPE,'
    'VOLUME_SERIES_NAME,description&sort=id asc')
    return url_params


def search(mission='all',instrument='all',target='all',keyword=None,nrows='10'):
    """Returns a SearchResults object for the given search terms.
    
    Keyword arguments:
    mission -- The name of a mission (for example, Juno, Cassini-Huygens, or Galileo).
    instrument -- The name of an instrument (for example, MAG, PLS, or CRT).
    target -- The name of a target (for example, Jupiter, Saturn, or Enceladus).
    keyword -- An arbitrary keyword (such as calibrated or raw).
    nrows -- The maximum number of results to return, as a string. The default is '10'.
    """
    params = __write_query(mission,instrument,target,keyword,nrows)
    return SearchResults(params)


def get_dataset(dataset_id):
    """Returns a DataSet object with the given id.
    
    Keyword arguments:
    id -- The unique id associated with the dataset, as in SearchResults.results['id'].
    """
    nrows = '10'
    query = 'id:({}) AND active:true'.format(dataset_id)
    params = ('/metadex/select/?'
    'q='+query+'&start=0&rows='+nrows+'&indent=on&wt=json&sort=id asc')
    return DataSet(params)
