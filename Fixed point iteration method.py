# v. using the fixed point iteration method ## x:- number of loyalty card holders

def fixedp(g,x0, tol, max_iteration):
    e =1
    itera = 0
    xp = []
    while (e > tol and itera <max_iteration):
        
        ## in the fixed point equation is,
        x = g(x0)
        ## error of the current iteration
        e = abs(x0-x) 
        x0 = x
        xp.append(x0) 
        itr =+ 1
        
    print("Root of the equation = ", x)
    print("Number of Iterations = ",len(xp) )

def g(x):
    g = (3*x + 2)**(1/2)
    return g

##given values
x0 =2
tol = 0.001
max_iteration = 100
fixedp(g,x0, tol, max_iteration)








