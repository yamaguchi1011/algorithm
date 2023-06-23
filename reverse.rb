arg = ARGV[0]
i = arg.length - 1
j = 0
reverse = []

while (i >= 0) do
  reverse[j] = arg[i]
  i-=1
  j+=1
end

p reverse.join