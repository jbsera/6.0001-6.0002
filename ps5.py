# -*- coding: utf-8 -*-
# Problem Set 5: Modeling Temperature Change
# Name: Joy Bhattacharya 
# Collaborators:
# Time: 8 hours

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2000)
TESTING_INTERVAL = range(2000, 2017)

##########################
#    Begin helper code   #
##########################

def standard_error_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.

    Args:
        x: a 1-d numpy array with length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d numpy array of values estimated by a linear
            regression model
        model: a numpy array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = np.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]


class Dataset(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Dataset instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature

        f.close()

    def get_daily_temps(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d numpy array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return np.array(temperatures)

    def get_temp_on_date(self, city, month, day, year):
        """
        Get the temperature for the given city at the specified date.

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified date and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year {} is not available".format(year)
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

##########################
#    End helper code     #
##########################

    def get_yearly_averages(self, cities, years):
        """
        For each year in the given range of years, computes the average of the
        annual temperatures in the given cities.

        Args:
            cities: a list of the names of cities to include in the average
                annual temperature calculation
            years: a list of years to evaluate the average annual temperatures at

        Returns:
            a 1-d numpy array of floats with length = len(years). Each element in
            this array corresponds to the average annual temperature over the given
            cities for a given year.
        """
        city_dict={}
        length=len(years)
        for city in cities:
            city_temp=[]
            for year in years:
                temp_array=self.get_daily_temps(city,year) #gets the array of daily temp in the city through the year
                mean_year_temp=temp_array.mean() #finds the mean of the daily temp
                city_temp.append(mean_year_temp) #appends that mean to a list, which will have the mean temp for every year in the range for a city
            city_dict[city]=city_temp #make a dictionary mapping the city with it's list of mean yearly temperatures
        city_means_list=[]
        for i in range(length): # iterating over the number of elements in the city_temp list
            L=[]
            for city in city_dict.keys(): #for every city
                L.append(city_dict[city][i]) #append that mean temperature to a list
            overall_city_mean=sum(L)/len(L) #finds the mean temp over multiple cities in the same year 
            city_means_list.append(overall_city_mean) #appends the overall city mean to a list
        city_mean_array=np.array(city_means_list) #cast the list as an array
        return city_mean_array
            
                
        
def linear_regression(x, y):
    """
    Calculates a linear regression model for the set of data points.

    Args:
        x: a 1-d numpy array of length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array of length N, representing the y-coordinates of
            the N sample points

    Returns:
        (m, b): A tuple containing the slope and y-intercept of the regression line,
                both of which are floats.
    """
    x_bar=np.mean(x)
    y_bar=np.mean(y)
    data=np.vstack((x,y)) #adds the two arrays vertically 
    a=0
    b=0
    for column in data.T: #iterates over every column in the array, ie x and y data points
        x_obs=column[0]
        y_obs=column[1]
        a+=(x_obs-x_bar)*(y_obs-y_bar) #sums the top of the formula
        b+=(x_obs-x_bar)**2 #sums the bottom of the formula
    m=a/b
    b=y_bar-(m*x_bar)
    return (m,b)

def squared_error(x, y, m, b):
    '''
    Calculates the squared error of the linear regression model given the set
    of data points.

    Args:
        x: a 1-d numpy array of length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array of length N, representing the y-coordinates of
            the N sample points
        m: The slope of the regression line
        b: The y-intercept of the regression line


    Returns:
        a float for the total squared error of the regression evaluated on the
        data set
    '''
    #array of estimates for y
    Y_est_list=[]
    error=0
    for value in x:
        y_est=m*value+b
        Y_est_list.append(y_est)
    estimated=np.array(Y_est_list)
    y_values=np.vstack((y,estimated)) #adds the two arrays vertically 
    for column in y_values.T: #iterates over every column in the array, ie y and y-est data points
        y_obs_1=column[0]
        y_estimate=column[1]
        error+=(y_obs_1-y_estimate)**2 #calculates total error
    return error

def generate_models(x, y, degrees):
    """
    Generates a list of polynomial regression models with degrees specified by
    degrees for the given set of data points

    Args:
        x: a 1-d numpy array of length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array of length N, representing the y-coordinates of
            the N sample points
        degrees: a list of integers that correspond to the degree of each polynomial
            model that will be fit to the data

    Returns:
        a list of numpy arrays, where each array is a 1-d numpy array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    L=[]
    for degree in degrees:
        model_array=np.polyfit(x,y, degree) #generates model given arrays and degree
        L.append(model_array)
    return L


def evaluate_models(x, y, models, display_graphs=False):
    """
    For each regression model, compute the R-squared value for this model and
    if display_graphs is True, plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (i.e. the model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        Degree of your regression model,
        R-squared of your model evaluated on the given data points,
        and standard error/slope (if this model is linear).

    R-squared and standard error/slope should be rounded to 4 decimal places.

    Args:
        x: a 1-d numpy array of length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array of length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial
        display_graphs: A boolean whose value specifies if the graphs should be
            displayed

    Returns:
        A list holding the R-squared value for each model
    """
    R_list=[]
    for model in models:
        degree=len(model)-1 #calculates the degree of the model
        L=[]
        for x_val in x:
            y_est=np.polyval(model,x_val) #finds the y-est from the model
            L.append(y_est)
        estimated=np.array(L) #creates an estimated y-val array
        R_squared=r2_score(y,estimated) #calculates R^2
        R_list.append(R_squared)
        if display_graphs:
            plt.plot(x,y,'.b')
            plt.plot(x,estimated, '-r')
            plt.xlabel('Year')
            plt.ylabel('Temperature (C)')
            if degree==1:
                se_ratio=round(standard_error_over_slope(x,y,estimated,model),4) #calculates the standard error ratio for linear models
                plt.title("Degree " + str(degree) + " model with R^2 of " + str(round(R_squared,4)) + "." + '\n' + "The standard error over slope ratio is " + str(se_ratio) + ".")
            else:
                plt.title("Degree " + str(degree) + " model with R^2 of " + str(round(R_squared,4)) + ".")
            plt.show()
    return R_list

def find_extreme_trend(x, y, length, positive_slope):
    """
    Args:
        x: a 1-d numpy array of length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array of length N, representing the y-coordinates of
            the N sample points
        length: the length of the interval
        positive_slope: a boolean whose value specifies whether to look for
            an interval with the most extreme positive slope (True) or the most
            extreme negative slope (False)

    Returns:
        a tuple of the form (i, j, m) such that the application of linear (deg=1)
        regression to the data in x[i:j], y[i:j] produces the most extreme
        slope m, with the sign specified by positive_slope and j-i = length.

        In the case of a tie, it returns the first interval. For example,
        if the intervals (2,5) and (8,11) both have slope 3.1, (2,5,3.1) should be returned.

        If no intervals matching the length and sign specified by positive_slope
        exist in the dataset then return None
    """
    L=[]
    interval_dict={}
    lowest_dict={}
    for i in range(len(x)):
        if i<len(x)-length+1: #makes sure not to go out of bounds
            short_x=x[i:i+length] #slice the array acording to the length
            short_y=y[i:i+length] #slice the array according to the length
            m=linear_regression(short_x, short_y)[0] #calculate the slope from the sliced arrays
            interval_dict[(i, i+length)]=m #store the interval with the slope in a dictionary
            L.append(m) #append the slope to a list 
            lowest_dict[(i, i+length)]=i+i+length #keeps track of which one has the lowest interval
    if positive_slope: #if trying to find the most positive slope
        most_extreme_slope=max(L)
        if most_extreme_slope<=0:
            return None
    else: #trying to find the most negative slope
        most_extreme_slope=min(L)
        if most_extreme_slope>=0:
            return None 
    T=[]
    for key in interval_dict.keys():
        if abs(most_extreme_slope-interval_dict[key])<=1e-8: #finds the key whose value matches our most extreme slope
            T.append(sum(key)) #appends tuple interval to a list so we can keep track of which correct tuple comes first numerically
    min_interval=min(T)
    for key in lowest_dict.keys():
        if lowest_dict[key]==min_interval: #gets the min interval
            return (key[0], key[1], interval_dict[key])
    return None
            

def find_all_extreme_trends(x, y):
    """
    Args:
        x: a 1-d numpy array of length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array of length N, representing the y-coordinates of
            the N sample points
        
    Returns:
        a list of tuples of the form (i,j,m) such that the application of linear
        regression to the data in x[i:j], y[i:j] produces the most extreme
        positive OR negative slope m, and j-i=length. 

        The returned list should have len(x) - 1 tuples, with each tuple representing the
        most extreme slope and associated interval for all interval lengths 2 through len(x).
        If there is no positive or negative slope in a given interval length L (m=0 for all
        intervals of length L), the tuple should be of the form (0,L,None).

        The returned list should be ordered by increasing interval length. For example, the first 
        tuple should be for interval length 2, the second should be for interval length 3, and so on.

        If len(x) < 2, return an empty list
    """
    final_tl=[]
    for length in list(range(2,len(x)+1)):
        interval_dict={}
        lowest_dict={}
        L=[]
        for i in range(len(x)):
            if i<len(x)-length+1: #makes sure not to go out of bounds
                short_x=x[i:i+length] #slice the array acording to the length
                short_y=y[i:i+length] #slice the array according to the length
                m=linear_regression(short_x, short_y)[0] #calculate the slope from the sliced arrays
                interval_dict[(i, i+length)]=m #store the interval with the slope in a dictionary
                L.append(m) #append the slope to a list 
                lowest_dict[(i, i+length)]=i+i+length #keeps track of which one has the lowest interval
        if max(L)>0: #finds max if there is one
            pos_most_extreme_slope=max(L)
        else:
            pos_most_extreme_slope=None
        if min(L)<0: #finds min if there is one
            neg_most_extreme_slope=min(L)
        else:
            neg_most_extreme_slope=None
        if max(L)==0 and min(L)==0: #special case
            return (0,length,None)
        if pos_most_extreme_slope!=None and neg_most_extreme_slope!=None:
            if pos_most_extreme_slope-abs(neg_most_extreme_slope)<=1e-8: #in this case use the neg slope
                most_extreme_slope=neg_most_extreme_slope
            else:
                most_extreme_slope=pos_most_extreme_slope
        elif pos_most_extreme_slope==None: #if there was no positive, return the neg
            most_extreme_slope=neg_most_extreme_slope
        elif neg_most_extreme_slope==None: #if there was no neg, return the pos
            most_extreme_slope=pos_most_extreme_slope
        T=[]
        for key in interval_dict.keys():
            if abs(most_extreme_slope-interval_dict[key])<=1e-8: #finds the key whose value matches our most extreme slope
                T.append(sum(key)) #appends tuple interval to a list so we can keep track of which correct tuple comes first numerically
        if len(T)>=1:
            min_interval=min(T)
            for key in lowest_dict.keys():
                if lowest_dict[key]==min_interval: #gets the min interval
                    final_tl.append((key[0], key[1], interval_dict[key])) #appends to our final tuple
    return final_tl

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: a 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d numpy array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    n=len(y) #number of data points 
    data=np.vstack((y,estimated)) #adds the two arrays vertically 
    a=0
    for column in data.T: #iterates over every column in the array, ie x and y data points
        y_obs=column[0]
        y_est=column[1]
        a+=(y_obs-y_est)**2 #sums the top of the formula
    rm_se=np.sqrt(a/n) #finds the rmse
    return rm_se



def evaluate_models_testing(x, y, models, display_graphs=False):
    """
    For each regression model, compute the RMSE for this model and if
    display_graphs is True, plot the test data along with the model's estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points.

    RMSE should be rounded to 4 decimal places.

    Args:
        x: a 1-d numpy array with length N, representing the x-coordinates of
            the N test data sample points
        y: a 1-d numpy array with length N, representing the y-coordinates of
            the N test data sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.
        display_graphs: A boolean whose value specifies if the graphs should be
            displayed

    Returns:
        A list holding the RMSE value for each model
    """
    R_list=[]
    for model in models:
        degree=len(model)-1 #calculates the degree of the model
        y_est=np.polyval(model,x) #finds the y-est from the model
        estimated=np.array(y_est) #creates an estimated y-val array
        rm=rmse(y, estimated) #calculates rmse
        R_list.append(rm)
        if display_graphs:
            plt.plot(x,y,'.b')
            plt.plot(x,estimated, '-r')
            plt.xlabel('Year')
            plt.ylabel('Temperature (C)')
            plt.title("Degree " + str(degree) + " model with rmse of " + str(round(rm,4)) + ".")
            plt.show()
    return R_list
        



if __name__ == '__main__':
    pass
    ##################################################################################
    # Problem 4A: DAILY TEMPERATURE

    # temp_data=Dataset('data.csv') #initializes dataset instance
    # y_temp=[]
    # x_year=[]
    # for year in range(1961,2017):
    #     x_year.append(year)
    #     temp=temp_data.get_temp_on_date('SAN FRANCISCO', 12, 25, year) #gets the temperature for the specific year on the specific date
    #     y_temp.append(temp)
    # x=np.array(x_year) #casts year list to array
    # y=np.array(y_temp) #cast temps to array
    # models=generate_models(x, y, [1])
    # evaluate_models(x, y, models, display_graphs=True)
    #################################################################################
    #Problem 4B: ANNUAL TEMPERATURE
    # temp_data=Dataset('data.csv') #initializes dataset instance
    # x_year=[]
    # for year in range(1961,2017):
    #     x_year.append(year) #create a list of years 
    # y=temp_data.get_yearly_averages(['SAN FRANCISCO'], x_year) #get an array of the yearly averages
    # x=np.array(x_year) #casts year to array
    # models=generate_models(x, y, [1])
    # evaluate_models(x, y, models, display_graphs=True)
    
    #4.1
    #What difference does choosing a specific day to plot the data versus calculating the yearly average have on the goodness of fit of the model? Interpret the results.
    #The specific day creates a model with a worse goodness of fit (R^2=0.0005) than the yearly average model does (R^2=0.4306). With the yearly average model, it looks like in general, as the years go on the average yearly temperature is increasing. With the specific day model, we can't determine any real correlation between x and y.
    #4.2
    #Why do you think these graphs are so noisy?
    #I think the specific day graph is especially noisy because there are a ton of outside variables and factors that could affect the temperature on a given day each year like weather, El Nino/la nina year, etc. The yearly average graph is a little less noisy because taking the average over the year eliminates some of these factors, but again there are variables like El Nino/La Nina or like forest fires that can cause noise in yearly averages'
    
    ##################################################################################
    # Problem 5B: INCREASING TRENDS
    # temp_data=Dataset('data.csv') #initializes dataset instance
    # x_year=[]
    # for year in range(1961,2017):
    #     x_year.append(year) #create a list of years 
    # y=temp_data.get_yearly_averages(['TAMPA'], x_year) #get an array of the yearly averages
    # x=np.array(x_year) #casts year to array
    # final_tup=find_extreme_trend(x, y, 30, positive_slope=True)
    # print(final_tup)
    # print(x[final_tup[0]], x[final_tup[1]])
    # new_x=x[final_tup[0]:final_tup[1]+1]
    # new_y=y[final_tup[0]:final_tup[1]+1]
    # models=generate_models(new_x, new_y, [1])
    # evaluate_models(new_x, new_y, models, display_graphs=True)
    
    ###My starting year was 1962, my ending year was 1992. My slope was around 0.04648
    ##################################################################################
    # Problem 5C: DECREASING TRENDS
    # temp_data=Dataset('data.csv') #initializes dataset instance
    # x_year=[]
    # for year in range(1961,2017):
    #     x_year.append(year) #create a list of years 
    # y=temp_data.get_yearly_averages(['TAMPA'], x_year) #get an array of the yearly averages
    # x=np.array(x_year) #casts year to array
    # final_tup=find_extreme_trend(x, y, 15, positive_slope=False)
    # print(final_tup)
    # print(x[final_tup[0]], x[final_tup[1]])
    # new_x=x[final_tup[0]:final_tup[1]+1]
    # new_y=y[final_tup[0]:final_tup[1]+1]
    # models=generate_models(new_x, new_y, [1])
    # evaluate_models(new_x, new_y, models, display_graphs=True)
    
    ###My starting year was 1970, my ending year was 1985. My slope was around -0.032569
    #The positive slope model has a much higher goodness of fit (0.292) compared to the negative slope model (R^2=0.007 which is basically no correlation). That tells me that the positive slope is a better model and is a better indicator that temp is increasing over time. 

    ##################################################################################
    # Problem 5D: ALL EXTREME TRENDS
    # temp_data=Dataset('data.csv') #initializes dataset instance
    # x_year=[]
    # for year in range(1961,2017):
    #     x_year.append(year) #create a list of years 
    # y=temp_data.get_yearly_averages(['TAMPA'], x_year) #get an array of the yearly averages
    # x=np.array(x_year) #casts year to array
    # final_tup=find_all_extreme_trends(x, y)
    # pos=0
    # neg=0
    # for i in final_tup:
    #     if i[2]>0:
    #         pos+=1
    #     if i[2]<0:
    #         neg+=1
    # print("Number of negative extremes", neg)
    # print('Number of positive extremes', pos)
    ### 54 intervals showed a regression with a more extreme positive slope. 1 interval showed a regression with a more extreme negative slope
    ### It's not a convincing argument because in final all extreme trends you're essentially curing the data to get the results you want. So even if you have a lot more pos than neg, you still manipulated the data in the first place to show what you wanted. The AC people could shows that the interval with the neg slope had the highest magnitude of slope or the highest change than all other intervals. 
            


    ##################################################################################
    # Problem 6B: PREDICTING
    ###training data 
    temp_data=Dataset('data.csv') #initializes dataset instance
    x_year=[]
    for year in range(1961,2000):
        x_year.append(year) #create a list of years 
    y=temp_data.get_yearly_averages(CITIES, x_year) #get an array of the yearly averages over every city
    x=np.array(x_year) #casts year to array
    models=generate_models(x, y, [2,10])
    evaluate_models(x, y, models, display_graphs=True)
    
    #The degree 10 model looks like a better fit since it has an R^2 or 0.775 but it isn't because it is overfitted to the curve and doesn't capture the overall trend. The degree two model has an R^2 of 0.7646 and seems to be a better fit for the data since it captures the overall trend better. 
    ###testing data
    temp_data=Dataset('data.csv') #initializes dataset instance
    x_year=[]
    for year in range(2000,2017):
        x_year.append(year) #create a list of years 
    y=temp_data.get_yearly_averages(CITIES, x_year) #get an array of the yearly averages over every city
    x=np.array(x_year) #casts year to array
    evaluate_models_testing(x, y, models, display_graphs=True)
    
    #It turned out the degree 10 was a much worse model since it had an extremely high rmse value of 6.9717, because it was overfitted. The degree two model was much better with an rsme value of 0.328
    #If we had used just the data from San Francisco, our prediction results for national data would have been much worse and much worse of a fit. We might have thought that temperature is increasing less than it actually is. 
    ##################################################################################
