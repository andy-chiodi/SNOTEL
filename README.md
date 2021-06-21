# SNOTEL
Python and Matlab code for processing and analyzing snotel data
## Acquiring data
Human-readable SNOTEL and Snow Course Data is available at `https://www.wcc.nrcs.usda.gov/snow`

For example, WA state sites are listed at `https://wcc.sc.egov.usda.gov/nwcc/rgrpt?report=snowcourse&state=WA`
and OR sites are listed at `https://wcc.sc.egov.usda.gov/nwcc/rgrpt?report=snowcourse&state=OR`

The data can be acquired by, for example, clicking the `Historic` tab next to the Site Name (eg. Blewitt Pass)
and copy and pasting the text into a file (e.g. blewitt_pass.txt). The python script `stripinfo.py` will then reformat and save the NRCS data in a form that can be loaded into Matlab

- `stripinfo.py`  command-line example: `>>> python stripinfo.py blewitt_pass.txt`. Output, in this case, will be called `blewitt_pass.dat`

## Processing data in Matlab

- `tseries.m` Matlab example: `[enm,noenm,lnm,nolnm,mn,stdev,ret,yr1] = tseries('blewit_pass')`

`tseries.m` loads a .dat file created by `stripinfo.py` and plots the snow-water equivalent (SWE) data

- `allsite.m`  Matlab example: `>> allsite`

`allsite.m` averages the SWE data from the sites listed in it and plots the resulting all-site-averaged time series.  This script also saves the averaged data to a .mat file for use in `boot.m`.

- `boot.m` Matlab example: `>>[obs_mean,p,sig95] = boot(year,data,[1989 1999 2000 2011 2021])`
`boot.m` uses a Bootstrap/Monte Carlo approach (sub-sampling with replacement) to estimate the statistical significance of a composite average. For example, the .mat file created by running `allsite.m` can be loaded into Matlab, providing variables `yr` (list of years) and `all` (list of all-site averaged SWE for each year).  Then, `[obs_mean,p,sig95] = boot(yr,all,[1989 1999 2000 2011])` will calculate the average over the subset of years given to boot (that is, [1989 1999 2000 2011]) and the overall average and determine the likelihood that the sub-set (in this case, OLR LA NINA composite) average could be attributed to chance alone.
