from cogent.db.ncbi import EFetch
import xml.etree.ElementTree as ET

pmid = '17708774'


def read(pmid):
    ef = EFetch(id=pmid, db='pubmed', rettype='citation', retmode='xml')
    cite = ef.read()
    root = ET.fromstring(cite)
    pmid = root[0][0].findall("PMID")[0].text
    abstract = root[0][0][4].findall("Abstract")[0][0].text
    journal = root[0][0][4].findall("Journal")[0][2].text
    year = root[0][0][2][0].text
    return (year, pmid, journal, abstract)
