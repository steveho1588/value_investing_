import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Plotting: ")
    x = np.arange(0, 5, 0.1);
    fig = plt.figure()
    plt.plot(x, np.sin(x), '-')
    plt.plot(x, np.cos(x), '--');
        
    plt.show()
    
if __name__ == "__main__":
    main()





