arg = ARGV[0].to_i
1.upto(arg) do |num|
  if num % 15 == 0
    p "FizzBazz"
  elsif num % 3 == 0
    p "FIzz"
  elsif num % 5 == 0
    p "Bazz"
  else
    p num
  end
end
