AIM: 
To develop a Python application that plots four common probability distributions (Binomial, Normal, 
Poisson, Uniform) by manually calculating their probability formulas and visualizing them with Matplotlib, 
based on user-provided parameters. 
ALGORITHM: 
1. Import Libraries: Import numpy for numerical arrays, matplotlib.pyplot for plotting, and math for 
mathematical functions like factorials and exponents. 
2. Define Mathematical Functions: 
o Create a Python function for each distribution's probability formula (PMF for discrete, PDF 
for continuous). 
o binomial_pmf(k, n, p): Calculates the probability of k successes in n trials. 
o normal_pdf(x, mu, sigma): Calculates the probability density at point x for a given mean and 
standard deviation. 
o poisson_pmf(k, lam): Calculates the probability of k events occurring in a fixed interval. 
o uniform_pdf(x, a, b): Calculates the probability density at point x between bounds a and b. 
3. Define Plotting Functions: 
o Create a separate plotting function for each distribution (plot_binomial, plot_normal, etc.). 
o Each function will generate an appropriate range of x-values and use the corresponding 
mathematical function from Step 2 to calculate the y-values (the probabilities). 
o Use Matplotlib to create and display a titled and labeled graph of the distribution. 
4. Create Main Function for User Interaction: 
o Display a menu prompting the user to select a distribution to plot. 
o Based on the user's choice, ask for the required parameters (e.g., mean and standard deviation 
for Normal). 
o Call the appropriate plotting function with the parameters provided by the user. 
5. Run the Program: Execute the main function to start the application 
