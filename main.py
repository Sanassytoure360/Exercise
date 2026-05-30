#Score obtained by the student
#English = 50
#Maths = 60
#Geography = 56
#Science = 70
#Economics = 13
#print("English:", English)
#print("Maths:", Maths)
#print("Geography:", Geography)
#print("Science:", Science)
#print("Economics:", Economics)
#Calculate the total score
#total_score= English + Maths + Geography + Science + Economics
#calculate the average_score
#average_score = total_score / 5
#print("total_score:", total_score)
#print("average_score:", average_score)


# Text = ("Python is a powerful programming language that is easy to learn and fun to use."
# "It lets you work quickly and integrate systems more effectively."
# "Learning Python can open doors to data science, web development, and artificial intelligence.")
# MYVAR = Text.upper()
# print(MYVAR)
#
# text = "Python is a powerful language that is easy to learn and fun to use, it lets you work quicly and integrate systems more effectively, learning Python can open doors to data science, web development, and artificial intelligence."
# print(text.replace("Python", "JAVA"))
#
# MyVariableName = Text
# print(MyVariableName)
#
# Passage = ("Python is a powerful programming language that is easy to learn and fun to use."
# "It lets you work quickly and integrate systems more effectively."
# "Learning Python can open doors to data science, web development, and artificial intelligence.")
#
# Passage = Passage.split()
# print(Passage)
# X = [Passage]
# X = len(Passage)
# print(X)

Text= """In the modern world, technology is evolving faster than ever before. Many professionals are turning to programming languages to automate their daily tasks. Python has become the most popular choice for beginners and experts alike because its syntax is clean and readable."
"With tools like Pandas for data manipulation, Matplotlib for data visualization, and Scikit-Learn for machine learning, the possibilities are endless. Are you ready to begin your journey? If you invest just thirty minutes a day, you will see massive progress. Start small, stay consistent, and build something amazing today!"""
count = Text.count("data")
print(count)
my_var = Text.lower()
print (my_var)
x = Text
new_text = x.replace("!",".")
print(new_text)
y = Text
Outcome = "Java" in Text
print(Outcome)
count = y.count(" ")
print(count)
List = Text.split(".")
print(List)

List = Text.split(".")

New_list =[]

for item in List:
    item = item.strip()
    if item != " " :New_list.append(item + "?")
print(New_list)

S = Text
clean = S.replace("?" and ".", "").replace("!",".")

words = clean.split()
first_word = words[0]
last_word = words[-1]
print(first_word)
print(last_word)

S = Text
Replace = S.replace("clean and readable","intuitive and powerful")
print(Replace)




















