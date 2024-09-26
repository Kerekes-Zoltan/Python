"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
#Define examination date
exam_st_date = (11, 12, 2014)

#Display the schedule
print("The examination will start from: {}/{}/{}".format(exam_st_date[0], exam_st_date[1], exam_st_date[2]))