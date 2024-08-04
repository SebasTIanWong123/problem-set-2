'''
PART 2: Pre-processing
- Take the time to understand the data before proceeding
- Load `pred_universe_raw.csv` into a dataframe and `arrest_events_raw.csv` into a dataframe
- Perform a full outer join/merge on 'person_id' into a new dataframe called `df_arrests`
- Create a column in `df_arrests` called `y` which equals 1 if the person was arrested for a felony crime in the 365 days after their arrest date in `df_arrests`. 
- - So if a person was arrested on 2016-09-11, you would check to see if there was a felony arrest for that person between 2016-09-12 and 2017-09-11.
- - Use a print statment to print this question and its answer: What share of arrestees in the `df_arrests` table were rearrested for a felony crime in the next year?
- Create a predictive feature for `df_arrests` that is called `current_charge_felony` which will equal one if the current arrest was for a felony charge, and 0 otherwise. 
- - Use a print statment to print this question and its answer: What share of current charges are felonies?
- Create a predictive feature for `df_arrests` that is called `num_fel_arrests_last_year` which is the total number arrests in the one year prior to the current charge. 
- - So if someone was arrested on 2016-09-11, then you would check to see if there was a felony arrest for that person between 2015-09-11 and 2016-09-10.
- - Use a print statment to print this question and its answer: What is the average number of felony arrests in the last year?
- Print the mean of 'num_fel_arrests_last_year' -> pred_universe['num_fel_arrests_last_year'].mean()
- Print pred_universe.head()
- Return `df_arrests` for use in main.py for PART 3; if you can't figure this out, save as a .csv in `data/` and read into PART 3 in main.py
'''

# import the necessary packages
import pandas as pd
# Your code here
def preprocess():
    pred_universe = pd.read_csv('data/pred_universe_raw.csv')
    arrest_events = pd.read_csv('data/arrest_even ts_raw.csv')

    df_arrests = pd.merge(pred_universe, arrest_events, on='person_id', hpw='outer')

    df_arrests['y'] = df_arrests.apply(lambda row: check_felony_arrest(row), axis=1)

    felony_share = df_arrests['y'].mean()
    print(f"The share of arrestees in 'df_arrests' table were rearrested for felony crime for upcoming year? {felony_share}")

    df_arrests['current_charge_felony'] = (df_arrests['charge_type'] == 'Felony'.astype(int))

    felony_current_share = df_arrests['current_charge_felony'].mean()
    print(f"What share of charges are felonies?{felony_current_share}")

    df_arrests['num_fel_arrests_last_year'] = df_arrests.apply(lambda row: count_felony_arrests_last_year(row), axis=1)

    average_felonies_arrests_last_year = df_arrests['num_fel_last_year'].mean()
    print(f'What is the average number of felonies last year? {average_felonies_arrests_last_year}')

    return df_arrests

def check_felony_arrest(row):
    pass
def count_felony_arrests_last_year(row):
    pass



