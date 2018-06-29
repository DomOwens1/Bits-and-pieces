#A simple program, adapted to convert course marks into final grades


year1 = {
"Analysis 1A": 77,
"Computational Mathematics": 72,
"Introduction to Group Theory": 72,
"Calculus 1": 66,
"Foundations & Proof": 65,
"Mechanics 1": 78,
"Probability 1": 63,
"Analysis 1B": 77,
"Statistics 1": 72,
"Linear Algebra and Geometry": 72
}
year1_values = year1.values()

year2 = {
"Linear Algebra": 71,
"Algebra 2": 66,
"Statistics 2": 71,
"Probability 2": 67,
"Combinatorics": 74,
"Metric Spaces": 63
}
year2_values = year2.values()

year3 ={}
year3_values = year3.values()


#yearly multiplier used for final grade calculation
weights = [0, 0.25, 0.75]

#function to find the average module score in a year
def average(year_values):
    total = sum(year_values)
    return float(float(total)/len(year_values) )

#calculate yearly averages
year1_ave = average(year1_values)
year2_ave = average(year2_values)
#year3_ave = average(year3_values)

#function to calculate the final, weighted grade
def get_weighted_grade(input_weights):
  return float(input_weights[0]*year1_ave + input_weights[1]*year2_ave #+ input_weights[2]*year3_ave
  )

#function to convert a numerical grade into a classification
def get_classification(score):
  if score>= 70: return "1"
  elif score >=60: return "2:1"
  elif score >=50: return "2:2"
  elif score >= 40: return "3"
  else: return "Fail"

#print out results by year, and final result
print("First year:")
print("Average: ")
print(year1_ave )
print("Classification: ")
print(get_classification( year1_ave ))
print("Second year:")
print("Average: ")
print(year2_ave)
print("Classification: ")
print(get_classification( year2_ave ))
#print("Third year:")
#print("Average: ")
#print( year3_ave )
#print("Classification: ")
#print(get_classification( year3_ave ))
print("Final Average: ")
print(get_weighted_grade(weights))
print("Final Classification: ")
print(get_classification(get_weighted_grade(weights)))
