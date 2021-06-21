function [year,snow] = readdat(nm)
%a = 'potato_hill'
a = nm;
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

yr = d(:,1);


y0 = 1981;
snow = 0;
for k = 1:35
  snow(k) = -99.9;
  y = y0+k;
  year(k) = y;
  f = find(yr > y-0.1 & yr <y+0.1);
  if(~isempty(f));
    snow(k) = dap(f);
  end
end



year = year(:);
snow = snow(:);


