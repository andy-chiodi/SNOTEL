function [composite_mean,p,sig95,l,ne] = boot_with_comments(year,data,cyrs)
%usage: [composite_mean,prob,sig95,num_yrs,num_compyrs] = boot_with_comments(year,data,cyrs)
% where inputs are:
% 'year' is a vector of years associated with each data value, e.g., [1982 1983 1984 ... 2021]
% 'data' is the vector of data values for each year
% 'cyrs' is a vector containing the names of the years comprising the composite, e.g. [1989 1999 2000 2010 2021]
%
% outputs are:
% 'composite_mean' the composite mean based on the subset of years specified in 'cyrs'
% 'p'  percentile of the actual composite mean relative to the random results
% 'sig95' gives the upper and lower 95% confidence interval values based on random sampling w/ repetition
% 'num_yrs' is the length of the input data vector, that is, the number of years with data
% 'num_compyrs' is the number of years in the composite, e.g. 5 in the case cyrs = [1989 1999 2000 2010 2021]     



% convert composite years to vector index values (e.g. 1989 -> 8) using ytoi.m
ie = ytoi(cyrs,year);

% calculate the composite mean based on composite-year index values from last line
% note that lmean.m will automatically average over all real data points it is given
% even if there are NaNs present
[composite_mean,ne] = lmean(data(ie));
% set Monte Carlo repetitions
N = 1000;

% Find just the good data points (exclude NaNs and data set to, say, -99.9)
f = find(~isnan(data) & data > -9.9);
data = data(f); 
l = length(data);

% initialize s, which will be our randomly-selected composite mean in the next step
s = 0;


% Monte Carlo loop starts here
for k = 1:N
   r = ceil(l*rand(ne,1)); % rand(ne,1) generates a vector with ne (#composite yrs) random numbers which get mapped to data indices 
   s(k) = mean(data(r));   % this lines calculates and saves the mean of our data over the subset of indices in 'r' and saves in 's'
end

% sort the record of randomly-chosen pseudo-composite averages
s = sort(s);

% get the 97.5 and 2.5 percentile sorted-values (thus, ~95% of our N random-means will fall between these two limits)
i97p5 = round(N*0.975);
i2p5 = round(N*0.025);
sig95 = [s(i97p5) s(i2p5)];

% determine how many of the random psuedo-composite means are exceeded by the actual composite mean
f = find(s>composite_mean);
if(isempty(f))
 f = N;
end
% translate to probability. The closer p is to 1 (e.g. 0.99) or 0 (e.g. 0.01) the less likely it is
% that randomness can explain the composite average magnitude, wheres p close to 0.5 (e.g. 0.4, 0.6, 0.7)
% means that it is not very hard to recreate the composite mean based on chance alone.
p = f(1)/N;



