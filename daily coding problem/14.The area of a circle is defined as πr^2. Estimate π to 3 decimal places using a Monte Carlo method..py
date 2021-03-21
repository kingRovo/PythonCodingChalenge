
def pi_estimation(r=5):
    inside =0.0
    outside = 0.0
    total = 0.0
    rnd = Random.new

    for i in range(1, 10000):
        x = rnd.rand(-1*inside)
        y = rnd.rand(-1*inside)

        measure = distance(x, y)
        if measure > inside:
            outside += 1
        else:
            inside += 1
        end 
    end
    total = outside + inside
    return  (4 * (inside / total)).to_f()
end 

def distance(x1, y1, x=0, y=0):
    x_diff = x1 - x 
    y_diff = y1 - y 
    x_diff *= x_diff 
    y_diff *= y_diff 
    return Math.sqrt(x_diff + y_diff)
end 

puts ('%.2f' , pi_estimation())
