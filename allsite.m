clear
sta1 ='blewitt_pass'  
sta2 ='corral_pass'
sta3 ='cougar_mountain'
sta4 ='fish_lake'
sta5 ='harts_pass'
sta6 ='lone_pine'
sta7 ='lyman_lake'
sta8 ='olallie_meadows'
sta9 ='park_creek'
sta10 ='pigtail_peak'
sta11 ='pope_ridge'
sta12 ='potato_hill'
sta13 ='rainy_pass'
sta14 ='sheep_canyon'
sta15 ='spencer_meadow'
sta16 ='stampede_pass'
sta17 ='stevens_pass'
sta18 ='surprise_lakes'
sta19 ='white_pass'

snow = zeros(19,35)*nan;

for k = 1:19
 ks = num2str(k);
 a = '[y,s]  = readdat(';
 b = ['sta' ks ')'];
 %snow(k,1:19)  = readdat(nm)
 eval([a b]) ;
 d = s(:)';
 snow(k,1:35)=d;
end

yr = y;
all = cascademean(snow);
all = all(:);



% plotting
hold off
plot(yr,all,'g.-')
hold on
plot(yr,mean(all)*ones(size(yr)),'g--')


en  = [1983 1987 1992 1998 2016];
oen = [1988 1995 2003 2005 2007 2010 ] ;
ens = 0;
g=0;
for k = 1:length(en)
    f = find(yr==en(k));
    if ~isempty(f)
       plot(yr(f),all(f),'rsq')
       ens = ens +all(f);
       g=g+1;
    end
end
enm = ens./g;


oens = 0;
g=0;
for k = 1:length(oen)
    f = find(yr==oen(k));
    if ~isempty(f)
       plot(yr(f),all(f),'rv');
       oens = oens +all(f);
       g=g+1;
    end
end
otherenm = oens./g;
mn = mean(all);
stdev = std(all);

ln = [1989 1999 2000 2011]
oln = [1985 1996 2001 2008 2012]

lns = 0;
g=0;
for k = 1:length(ln)
    f = find(yr==ln(k));
    if ~isempty(f)
       plot(yr(f),all(f),'bsq');
       lns = lns +all(f);
       g=g+1;
    end
end
lnm = lns./g;

olns = 0;
g=0;
for k = 1:length(oln)
    f = find(yr==oln(k));
    if ~isempty(f)
       plot(yr(f),all(f),'b^');
       olns = olns +all(f);
       g=g+1;
    end
end
otherlnm = olns./g;

title('1 Apr SWE, squares for OLR ENSO (red=en,blue=ln) and triangles for other ENSO yrs')


save allsites yr all

lnm
otherlnm
enm
otherenm
mn
stdev
