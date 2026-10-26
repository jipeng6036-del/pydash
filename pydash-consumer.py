import csv
import io
import json
import sys
import pydash

rows=list(csv.DictReader(io.StringIO('item,amount\nfirst,10\nmiddle,20\nlast,30\n')))
visits=pydash.reduce_right(rows,lambda acc,row,index:acc+[{'row':index,'item':row['item']}],[])
totals=pydash.reductions_right(rows,lambda acc,row,index:acc+int(row['amount'])*(index+1),0)
expected=[{'row':2,'item':'last'},{'row':1,'item':'middle'},{'row':0,'item':'first'}]
result={'python':sys.version,'packageFile':pydash.__file__,'visits':visits,'totals':totals,'expectedVisits':expected,'expectedTotals':[90,130,140],'pass':visits==expected and totals==[90,130,140]}
print(json.dumps(result,indent=2))
if not result['pass']:
    sys.exit(1)
