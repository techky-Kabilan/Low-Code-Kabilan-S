"""Local Python lookup illustration only. No Zoho API calls."""
import random,time,statistics,json
rng=random.Random(241501502); records=[{'id':i,'status':rng.choice(['Submitted','Approved','Settled']),'amount':rng.randrange(1000,90000)}for i in range(20000)]
ids=[rng.randrange(20000)for _ in range(600)]; index={r['id']:r for r in records}
def scan():return [next(r['amount'] for r in records if r['id']==key)for key in ids]
def lookup():return [index[key]['amount']for key in ids]
assert scan()==lookup(); ts=[];td=[]
for _ in range(5):
 t=time.perf_counter();scan();ts.append((time.perf_counter()-t)*1000)
 t=time.perf_counter();lookup();td.append((time.perf_counter()-t)*1000)
bench={'fixture_records':20000,'lookups_per_run':600,'runs':5,'scan_median_ms':round(statistics.median(ts),3),'dictionary_median_ms':round(statistics.median(td),3),'equal_outputs':True,'scope':'Local Python illustration only. Excludes index construction and is not a Zoho Creator benchmark.'}
print(json.dumps(bench,indent=2))
