
"""
Mohr circle in 3D.
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigvalsh
from matplotlib import rcParams
 
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

class mohr():
  def plot_mohr3d(self, S):
    """Plot 3D Mohr circles."""
    ''' This method "plot_mohr3d()" definition should evaluate the principal stress components from any arbitrary stress tensor(S).
        Then, calculate major, minor and intermediate radius of Mohr's circle.'''
    
    #-------Your Code-------- 
    
    # Write func to calculate Eigen values of the stress tensor in increasing order of magnitude i.e. Principal Stresses in this line.

    R_maj =0                #Major radius
    cent_maj = 0            #Centre of the major circle
    
    R_min =0                 #Minor Radius
    cent_min =0              #Centre of the minor circle
    
    R_mid =0                 #Intermediate (Radius of circle which includes both major and minor circle)
    cent_mid =0 
    
    # Plot your FIGURE of Mohr circle
    

    return R_maj, R_min, R_mid
