function i = ytoi(list,year)
% usage i = ytoi(list,year)

c=0;
i=nan;
for k = 1:length(list);
    for j = 1:length(year);
        if list(k)==year(j); 
        c=c+1; 
        i(c)=j;
        end
    end
end
