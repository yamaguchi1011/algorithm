arg = ARGV[0]
i = arg.length - 1
j = 0
gyakujunn = []

while(i>=0) do
  gyakujunn[j] = arg[i]
  i-=1
  j+=1
end

p gyakujunn.join