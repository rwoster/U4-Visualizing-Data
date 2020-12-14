import matplotlib.pyplot as plt

male_faculty = 251
female_faculty = 206

plt.pie([male_faculty, female_faculty], labels=["Men", "Women"], autopct="%1.0f%%")
plt.title("Gender")
plt.savefig("faculty_gender_diversity.png")

import numpy as np
x = np.random.random(1000)
plt.figure()
plt.hist(x, bins=15, facecolor="purple", edgecolor="yellow")
plt.savefig("histogram.png")
