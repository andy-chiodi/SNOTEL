function [f,l] = mymean(x)
f = find(~isnan(x));
l = length(f);
f = mean(x(f));
