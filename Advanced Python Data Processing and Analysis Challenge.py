import re
from collections import Counter

def analyze_blog_sentiments(blog_file):
    positive_words = ["amazing", "enjoy", "beautiful", "wonderful", "breathtaking", "stunning", "memorable", "excellent", "fantastic", "unique"]
    negative_words = ["bad", "disappointing", "poor", "lackluster", "scarce", "overcrowded"]
    
    pos_count = 0
    neg_count = 0
    
    try:
        with open(blog_file, 'r') as file:
            text = file.read().lower()  
            words = re.findall(r'\b\w+\b', text)
            word_counts = Counter(words)
            
            for word in positive_words:
                pos_count += word_counts[word]

            for word in negative_words:
                neg_count += word_counts[word]
                
    except FileNotFoundError:
        print(f"The file '{blog_file}' does not exist.")
    except PermissionError:
        print(f"Permission denied to read the file '{blog_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Return the counts of positive and negative words
    return pos_count, neg_count

if __name__ == "__main__":
    blog_file = 'travel_blogs.txt'  
    pos_count, neg_count = analyze_blog_sentiments(blog_file)
    print(f"Positive words count: {pos_count}")
    print(f"Negative words count: {neg_count}")

import os

def read_weather_data(file):
    temperatures = []
    
    try:
        with open(file, 'r') as f:
            for line in f:
                date, temp = line.strip().split(',')
                temp = int(temp.replace('°C', ''))
                temperatures.append(temp)
                
    except FileNotFoundError:
        print(f"The file '{file}' does not exist.")
    except PermissionError:
        print(f"Permission denied to read the file '{file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    return temperatures

def calculate_average_temperatures(files):
    yearly_averages = {}
    
    for file in files:
        year = file.split('_')[1].split('.')[0] 
        temperatures = read_weather_data(file)
        if temperatures:
            yearly_averages[year] = sum(temperatures) / len(temperatures)
    
    return yearly_averages

if __name__ == "__main__":
    weather_files = ['weather_2020.txt', 'weather_2021.txt']  # Add more files as needed
    yearly_averages = calculate_average_temperatures(weather_files)
    
    for year, avg_temp in yearly_averages.items():
        print(f"Average temperature for {year}: {avg_temp:.2f}°C")
    
    if yearly_averages:
        warmest_year = max(yearly_averages, key=yearly_averages.get)
        print(f"The year with the highest average temperature is {warmest_year} with an average of {yearly_averages[warmest_year]:.2f}°C")
