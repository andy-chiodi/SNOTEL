function [obs_mean,p,sig95,l,ne] = boot(year,data,eyrs)
%usage: [en,pen,nen,pnen,ln,pln,nln,pnln] = boot(year,data)


%yen  = [1983 1987 1992 1998 2016];
%ynen = [1988 1995 2003 2005 2007 2010 ] ;
%yln = [1989 1999 2000 2011]
%ynln = [1985 1996 2001 2008 2012]

ie = ytoi(eyrs,year);
%ne = length(ie);
[obs_mean,ne] = lmean(data(ie));
N = 1000;
f = find(~isnan(data) & data > -9.9);
data = data(f); 
l = length(data);
s = 0;



for k = 1:N
   r = ceil(l*rand(ne,1));
   s(k) = mean(data(r));
end

s = sort(s);
i97p5 = round(N*0.975);
i2p5 = round(N*0.025);
sig95 = [s(i97p5) s(i2p5)];
f = find(s>obs_mean);
if(isempty(f))
 f = N;
end
p = f(1)/N;



