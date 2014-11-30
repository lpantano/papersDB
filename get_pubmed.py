from cogent.db.ncbi import EFetch

pmid = '17708774'
ef = EFetch(id=pmid, db='pubmed', rettype='citation', retmode='xml')
cite = ef.read()
for line in cite.splitlines()[:5]:
    print line
