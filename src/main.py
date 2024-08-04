'''
You will run this problem set from main.py, so set things up accordingly
'''
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import part1_etl
import part2_preprocessing
import part3_logistic_regression
import part4_decision_tree
import part5_calibration_plot

# Call functions / instanciate objects from the .py files
def main():

    # PART 1: Instanciate etl, saving the two datasets in `./data/`
    part1_etl.etl()
    # PART 2: Call functions/instanciate objects from preprocessing
    df_arrests = part2_preprocessing.preprocess()
    # PART 3: Call functions/instanciate objects from logistic_regression
    df_arrests_tests = part3_logistic_regression.run_logistic_regression(df_arrests)
    # PART 4: Call functions/instanciate objects from decision_tree
    df_arrests_tests = part4_decision_tree.run_decision_tree(df_arrests_tests)
    # PART 5: Call functions/instanciate objects from calibration_plot
    part5_calibration_plot.run_calibration_plots(df_arrests_tests)

if __name__ == "__main__":
    main()