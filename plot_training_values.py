import re
import matplotlib.pyplot as plt
import numpy

file = open('/usr/tmp/darknet.sh.out4338', 'r')

avgIOU = []
totalLoss = []
avgLossError = []

# Using for loop
print("Plot Learning YOLO")
for line in file:
    # print("{}".format(line.strip()))
    arguments = line.split(", ")

    for argument in arguments:
        if re.match('^[Region]+\W+\d+', argument) is not None:
            try:
                avgIOU.append(float(argument.split()[-1]))
            except ValueError:
                pass

        if re.match('^[\d]+\W+\D+[\d]', argument) is not None:
            try:
                totalLoss.append(float(argument.split()[1]))
            except ValueError:
                pass

        if re.match('^[\d]+\W+[\d]+[ avg]', argument) is not None:
            try:
                avgLossError.append(float(argument.split()[0]))
            except ValueError:
                pass
file.close()

plt.plot(avgIOU)
plt.title('avgIOU')
plt.xlim(left=0)
plt.show()

plt.plot(totalLoss)
plt.title('Total Loss')
plt.xlabel("Nb Iterations")
plt.xlim(left=0)
plt.xlim(right=2000)
plt.show()

# # print(avgLossError)
# plt.plot(avgLossError, color='blue', lw=2)
# # plt.plot(0.060730)
# plt.title('Average Loss Error')
# plt.yscale('log')
# plt.xlabel("Nb Iterations")
# plt.xlim(left=0)
# plt.xlim(right=2000)
# plt.show()


x_min = 0
x_max = 1000
x = numpy.arange(0, x_max, 100)
plt.plot(x, avgLossError)
plt.xlim(x_min,x_max)
plt.yscale('log')
plt.grid(True,which="both", linestyle='--')
plt.show()

