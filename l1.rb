def hello
  out = "Check"
  puts out
end

puts "Sentence"

BEGIN {
  puts "Hello"
}

print <<EOF
Multiple line
String
EOF

puts "Sentence 1"

END {
  puts "End sentence try"
}
BEGIN {
  puts "Initial"
}

class Classname
  def hello1
    puts "Hello"
  end
end

class Sample
  def function
    puts "Ruby"
  end
end

object = Sample.new
object.function

$a = 10
class Name
  def print_global
    puts "Global Variable #$a"
  end
end

class1obj = Name.new
class1obj.print_global


class Customer
  def initialize(id, name, add)
    @cust_id = id
    @cust_name = name
    @cust_addr = add
  end
  def display_details()
    puts "Customer id #@cust_id"
    puts "Customer name #@cust_name"
    puts "Customer address #@cust_add"
  end
end

cust1 = Customer.new("1","Name1", "Address1")
cust2 = Customer.new("2", "Name2", "Address2")

cust1.display_details()
cust2.display_details()
