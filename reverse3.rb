arg = ARGV[0]
i = arg.length - 1
j = 0
letters = []

while(i>=0) do
  letters[j] = arg[i]
  i-=1
  j+=1
end
p letters.join