function f = mymean(x)
f = find(~isnan(x));
f = mean(x(f));
