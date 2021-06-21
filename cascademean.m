function y = cascademean(x);

s = size(x);
y=0;

for k = 1:s(2)
  a = x(:,k);
  y(k) = mymean99(a);
end
