function [enm,noenm,lnm,nolnm,mn,stdev,ret,yr1] = tseries(nm)
% usage: [enm,noenm,lnm,nolnm,mn,stdev,ret,yr1] = tseries('name_of_site') 
% enm =  olr el nino mean
% noenm = non-OLR el nino mean
% lnm = olr la nina mean
% nolnm = non-OLR La Nina mean
% mn = overall time series mean
% stdev = time series standard deviation
% ret = data returned as [year(:) data(:)]
% y1 = first year of data

a = nm
b = 'load ';
d = '.dat';
c = [b a d];
eval(c);
eval(strcat('d=',a,';'));
wch = 9;

da = d(:,wch);
dap = da;
fb = find(da < -9.9);
dap(fb) = nan;
hold off
plot(d(:,1),dap,'g.-')
ret = [d(:,1) dap];
hold on
plot(d(:,1),mymean(dap)*ones(size(d(:,1))),'g--')
s =  size(d);
s = s(1);
dm = d - ones(s,1)*mean(d);
yr = d(:,1);
yr1 = yr(1);


f = find(da > -9.9);
da = da(f);
yr=yr(f);

en  = [1983 1987 1992 1998 2016];
noen = [1988 1995 2003 2005 2007 2010] ;
ens = 0;
g=0; 
for k = 1:length(en)
    f = find(yr==en(k));
    if ~isempty(f)
       plot(yr(f),da(f),'rsq')
       ens = ens +da(f);
       g=g+1;
    end
end
enm = ens./g;


noens = 0;
g=0;
for k = 1:length(noen)
    f = find(yr==noen(k));
    if ~isempty(f)
       plot(yr(f),da(f),'rv');
       noens = noens +da(f);
       g=g+1;
    end
end
noenm = noens./g;


mn = mean(da);
stdev = std(da);

ln = [1989 1999 2000 2011 2021]
noln = [1985 1996 2001 2008 2012]

lns = 0;
g=0;
for k = 1:length(ln)
    f = find(yr==ln(k));
    if ~isempty(f)
       plot(yr(f),da(f),'bsq');
       lns = lns +da(f);
       g=g+1;
    end
end
lnm = lns./g;

nolns = 0;
g=0;
for k = 1:length(noln)
    f = find(yr==noln(k));
    if ~isempty(f)
       plot(yr(f),da(f),'b^');
       nolns = nolns +da(f);
       g=g+1;
    end
end
nolnm = nolns./g;

title('1 Apr SWE, squares for OLR ENSO (red=en,blue=ln) and triangles for other ENSO yrs')

