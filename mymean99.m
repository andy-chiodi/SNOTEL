function f = mymean(x)
f = find(~isnan(x) & x > -90.0);
f = mean(x(f));
