# Gradient_Descent_binary_search

Note that this algorithm is still under development... I am just trying to figure out how to apply binary search to gradient descent for functions where local minimum is the global minimum. 

However, the main problem is choosing the end points (the highest and the lowest points in binary search). Usually, when you apply binary search to a list, the highest point is the element at the highest index and the lowest at the lowest. However, here, there is no given boundary, so in the current code I've just tried to say, "Well, if the slope at this point is negative, it is the low and now I just need to choose the point at which the slope is positive and same vice versa."

Of course, there are still huge scopes for errors and optimizations, but this is the algorithm.
