arg = ARGV[0].to_i

1.upto(arg) do |num|
  if num % 15 == 0
    p "Fizzbazz"
  elsif num % 3 == 0
    p "Fizz"
  elsif num % 5 == 0
    p "bazz"
  else
    p num
  end
  
end
