#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 09:41:34 2024

@author: fozame
"""

import numpy as np

"""

In this script, we will implement a class to do convolution,

In mathematics, the convolution product is a bilinear operator and a commutative product, 
generally denoted “∗”, which, to two functions f and g on the same infinite domain, 
corresponds to another function “f ∗ g” on this domain, 
which at any point therein is equal to the integral over the entire domain 
(or the sum if it is discrete) of one of the two functions around this point, 
weighted by the other function around the origin 
— the two functions being traversed in opposite directions to each other (necessary to guarantee commutativity)



In image processing, a kernel, convolution matrix, or mask is a small matrix used for blurring, image sharpening, embossing, edge detection, and others. 
All this is accomplished by doing a convolution between the kernel and the image.

"""

class Convolution:
    """
    Cette classe va prendre en entree des parametres et retourner la feature map 

    """
    
    def check_dim(self, x_in, kernel): 
        if len(x_in) < len(kernel): 
            raise ValueError('The size of the input matrix must be greater than the size of the convolution kernel')
        
    def shape_conv(self):
        h_out = (self.x_in.shape[0] - self.kernel.shape[0] + 1) / self.stride
        w_out = (self.x_in.shape[1] - self.kernel.shape[1] + 1) / self.stride
        
        return (int(h_out), int(w_out))
            
    
    def fit(self, x_in, kernel, stride = 1, padding = 0, mode = 'valid'):
        self.x_in = x_in
        self.kernel = kernel
        self.stride = stride
        self.padding = padding
        self.mode = mode
        i = 0
        j = 0
        
        try:
            self.check_dim(x_in, kernel)
            
        except Exception as e:
            print(e)
            return None
        
          
        if mode == 'valid':
            h_out, w_out = self.shape_conv()
            conv_matrix = np.zeros((h_out, w_out))
            n_i, n_j = self.kernel.shape[0], self.kernel.shape[1]
            s_i = 0  # Initialize row stride offset
            for i in range(h_out):
                s_j = 0  # Initialize column stride offset
                for j in range(w_out):
                    sub_matrix = self.x_in[i+s_i:i+s_i+n_i, j+s_j:+j+s_j+n_j]  # Extract sub matrix
                    conv_matrix[i, j] = np.sum(sub_matrix * self.kernel)  # Compute convolution
                    s_j += stride - 1  # Increment column stride offset
                s_i += stride - 1  # Increment row stride offset

            
            return conv_matrix
        
        elif mode == 'full':
            return 0
    
                
                    
                        
    
    

C = np.array(([[1, 2, 3, 4, 5, 6, 7, 8, 9],
 [2, 3, 4, 5, 6, 7, 8, 9, 1],
 [3, 4, 5, 6, 7, 8, 9, 1, 2],
 [4, 5, 6, 7, 8, 9, 1, 2, 3],
 [5, 6, 7, 8, 9, 1, 2, 3, 4],
 [6, 7, 8, 9, 1, 2, 3, 4, 5],
 [7, 8, 9, 1, 2, 3, 4, 5, 6],
 [8, 9, 1, 2, 3, 4, 5, 6, 7],
 [9, 1, 2, 3, 4, 5, 6, 7, 8]]))




M = np.array(([2,3,4],[5,6,7],[1,2,3]))

k = np.ones((3,3))#k as kernel for the convolution
k = np.diag(np.diag(k))
print(np.sum(np.multiply(C[0:3, 0:3], k)))

X = Convolution()
score = X.fit(C, k, stride = 1)
print(score)
        
        
        
        
        
    