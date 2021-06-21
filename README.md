# SNOTEL
Python and Matlab code for processing and analyzing snotel data
## Acquiring data
Human-readable SNOTEL and Snow Course Data is available at `wcc.nrcs.usda.gov/snow`
For example, WA state sites are listed at `http://wcc.sc.egov.usda.gov/nwcc/rgrpt?report=snowcourse&state=WA`
and OR sites are listed at `http://wcc.sc.egov.usda.gov/nwcc/rgrpt?report=snowcourse&state=OR`
The data can be acquired by, for example, clicking the `Historic` tab next to the Site Name (eg. Blewitt Pass)
and copy and pasting the text into a file (e.g. blewitt_pass.txt). The python script `stripinfo.py` will then reformat and save the NRCS data in a form that can be loaded into Matlab
- stripinfo.py  example command line uasge: `>>> python stripinfo.py blewitt_pass.txt`   Output, in this case, will be called `blewitt_pass.dat`
