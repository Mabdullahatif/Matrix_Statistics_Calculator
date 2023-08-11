
# Matrix Statistics Calculator
## Introduction

This repository contains a Python script that calculates various statistics for a 3x3 matrix using the NumPy library. 

## Table of Contents

- [Code Description](#code-description)
- [Key Points / Learning](#key-points--learning)
- [Applicability](#applicability)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [Initial Contributor](#initial-contributor)

## Code Description
The provided Python code defines a function named `calculate` that takes a list of nine numbers as input and performs various calculations on a 3x3 matrix created from the input list using the `NumPy` library. The code then returns a dictionary containing statistics such as mean, variance, standard deviation, maximum, minimum, and sum along both axes (rows and columns) and for the flattened matrix.

1. The `calculate` function checks if the input list contains exactly nine numbers. If not, it raises a `ValueError` with the message "List must contain nine numbers."
2. The input list is converted into a 3x3 `NumPy` array using the `np.array` function and reshaped with `reshape(3, 3)`.
3. The code calculates various statistics (mean, variance, standard deviation, max, min, sum) using `NumPy` functions:
   - `mean`: Calculated separately for each axis (row and column) and the flattened matrix.
   - `variance`: Similarly calculated for each axis and the flattened matrix.
   - `standard deviation`: Similarly calculated for each axis and the flattened matrix.
   - `max`: Similarly calculated for each axis and the flattened matrix.
   - `min`: Similarly calculated for each axis and the flattened matrix.
   - `sum`: Similarly calculated for each axis and the flattened matrix.

4. The calculated statistics are stored in a dictionary named `calculations`.

5. The `calculate` function returns the `calculations` dictionary.

6. Outside the function, a list of nine numbers (`nums`) is defined for analysis.

7. The `calculate` function is called with the `nums` list, and the resulting `calculations` dictionary is printed.

## Key Points / Learning
- **Use of NumPy:** The code demonstrates the use of the `NumPy` library to efficiently manipulate arrays and perform mathematical operations on them.

- **Array Reshaping:** The code showcases how to reshape a one-dimensional array into a multi-dimensional array (matrix) using NumPy's `reshape` function.

- **Calculation of Statistics:** The code calculates various statistics, such as mean, variance, standard deviation, maximum, minimum, and sum, using NumPy functions along different axes of the matrix.

- **Exception Handling:** The code includes exception handling to raise a `ValueError` when the input list does not contain exactly nine numbers.

- **Dictionary Data Structure:** The code uses a dictionary to organize and store the calculated statistics in a structured format.

## Applicability
This code is applicable in scenarios where you need to analyze a 3x3 matrix of numerical data and compute various statistical measures for different axes and the flattened matrix. Some potential areas of application include:

- **Image Processing:** Analyzing small patches of an image to calculate statistical features like mean, variance, etc.

- **Sensor Data Analysis:** Processing sensor readings in a 3x3 grid to extract statistical information.

- **Game Development:** Working with small grids or tiles in a game environment to calculate metrics for gameplay elements.

- **Scientific Simulations:** Analyzing small portions of simulation data to extract relevant statistics.

- **Education:** Demonstrating basic statistical calculations and NumPy usage in educational contexts.

Remember that while the code is specifically designed for a 3x3 matrix, it can be extended or adapted for larger matrices with minimal modifications.


## How to Use

To use the matrix statistics calculator, follow these steps:

1. Clone the repository to your local machine using `git clone https://github.com/Mabdullahatif/Matrix_Statistics_Calculator.git`.

2. Open the Jupyter Notebook or Google Colab environment.

3. Navigate to the repository directory.

4. Open the `main.py` file

5. Run the code cells to see the calculated statistics for the provided list of nine numbers.

## Contributing

Contributions are welcome! To contribute to the Matrix Statistics Calculator, follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them with descriptive commit messages.

4. Push your changes to your forked repository.

5. Create a pull request detailing your changes and explaining their purpose.

Please make sure to follow the repository's code of conduct and guidelines.

## Initial Contributor

So far, all the work in this repository is purely done by me.
## LinkedIn &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Facebook &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Instagram &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Twitter
<a href="https://www.linkedin.com/in/muhammad-abdullah-atif/">
    <img height="50" src="https://cdn2.iconfinder.com/data/icons/social-icon-3/512/social_style_3_in-306.png"/>
</a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;

<a href="https://www.facebook.com/abdullahatif362/">
    <img height="50" src="https://cdn0.iconfinder.com/data/icons/social-flat-rounded-rects/512/facebook-64.png"/>
</a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<a href="https://www.instagram.com/abdullah._.atif/">
    <img height="50" src="https://cdn2.iconfinder.com/data/icons/social-media-applications/64/social_media_applications_3-instagram-64.png"/>
</a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;

<a href="https://www.twitter.com/abd_allah_atif/">
    <img height="50" src="https://cdn3.iconfinder.com/data/icons/2018-social-media-logotypes/1000/2018_social_media_popular_app_logo_twitter-64.png"/>
</a>

