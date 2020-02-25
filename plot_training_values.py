import re
import matplotlib.pyplot as plt

file = open('/home/tonycalvez/GitHub/DEEPDART/darknet1.sh.out', 'r')

avgIOU = []
totalLoss = []
avgLossError = []
iteration = []

print("Plot Learning YOLO")
for line in file:
    arguments = line.split(", ")

    for argument in arguments:
        # if re.match('^[Region]+\W+\d+', argument) is not None:
        #     try:
        #         avgIOU.append(float(argument.split()[-1]))
        #     except ValueError:
        #         pass
        #
        # if re.match('^[\d]+\W+\D+[\d]', argument) is not None:
        #     try:
        #         totalLoss.append(float(argument.split()[1]))
        #     except ValueError:
        #         pass

        if re.match('^[\d]+\W+[\d]+\W+avg', argument) is not None:
            try:
                avgLossError.append(float(argument.split()[0]))
            except ValueError:
                pass
file.close()

plt.plot(avgIOU)
# plt.title('avgIOU')
# plt.xlim(left=0)
# plt.show()
#
plt.plot(totalLoss)
# plt.title('Total Loss')
# plt.xlabel("Nb Iterations")
# plt.xlim(left=0)
# plt.xlim(right=2000)
# plt.show()
# avgLossErrorTiny = []

# for i in range(0, len(avgLossError), 100):
#     avgLossErrorTiny.append(avgLossError[i])
#     iteration.append(i)

plt.plot(avgLossError)
plt.axhline(y=0.60730, color='r', linestyle='-')
plt.title('Average Loss Error')
plt.yscale('log')
plt.xlabel("Nb Iterations")
plt.xlim(left=0)
plt.xlim(right=10000)

file = open('/home/tonycalvez/GitHub/DEEPDART/darknet4.sh.out', 'r')

avgIOU = []
totalLoss = []
avgLossError = []
iteration = []

print("Plot Learning YOLO")
for line in file:
    arguments = line.split(", ")

    for argument in arguments:
        # if re.match('^[Region]+\W+\d+', argument) is not None:
        #     try:
        #         avgIOU.append(float(argument.split()[-1]))
        #     except ValueError:
        #         pass
        #
        # if re.match('^[\d]+\W+\D+[\d]', argument) is not None:
        #     try:
        #         totalLoss.append(float(argument.split()[1]))
        #     except ValueError:
        #         pass

        if re.match('^[\d]+\W+[\d]+\W+avg', argument) is not None:
            try:
                avgLossError.append(float(argument.split()[0]))
            except ValueError:
                pass
file.close()

plt.plot(avgIOU)
# plt.title('avgIOU')
# plt.xlim(left=0)
# plt.show()
#
plt.plot(totalLoss)
# plt.title('Total Loss')
# plt.xlabel("Nb Iterations")
# plt.xlim(left=0)
# plt.xlim(right=2000)
# plt.show()
# avgLossErrorTiny = []

# for i in range(0, len(avgLossError), 100):
#     avgLossErrorTiny.append(avgLossError[i])
#     iteration.append(i)

plt.plot(avgLossError)
plt.axhline(y=0.60730, color='b', linestyle='-')
plt.title('Average Loss Error')
plt.yscale('log')
plt.xlabel("Nb Iterations")
plt.xlim(left=0)
plt.xlim(right=10000)

file = open('/home/tonycalvez/GitHub/DEEPDART/darknet3.sh.out', 'r')

avgIOU = []
totalLoss = []
avgLossError = []
iteration = []

print("Plot Learning YOLO")
for line in file:
    arguments = line.split(", ")

    for argument in arguments:
        # if re.match('^[Region]+\W+\d+', argument) is not None:
        #     try:
        #         avgIOU.append(float(argument.split()[-1]))
        #     except ValueError:
        #         pass
        #
        # if re.match('^[\d]+\W+\D+[\d]', argument) is not None:
        #     try:
        #         totalLoss.append(float(argument.split()[1]))
        #     except ValueError:
        #         pass

        if re.match('^[\d]+\W+[\d]+\W+avg', argument) is not None:
            try:
                avgLossError.append(float(argument.split()[0]))
            except ValueError:
                pass
file.close()

plt.plot(avgIOU)
# plt.title('avgIOU')
# plt.xlim(left=0)
# plt.show()
#
plt.plot(totalLoss)
# plt.title('Total Loss')
# plt.xlabel("Nb Iterations")
# plt.xlim(left=0)
# plt.xlim(right=2000)
# plt.show()
# avgLossErrorTiny = []

# for i in range(0, len(avgLossError), 100):
#     avgLossErrorTiny.append(avgLossError[i])
#     iteration.append(i)

plt.plot(avgLossError)
plt.axhline(y=0.60730, color='g', linestyle='-')
plt.title('Average Loss Error')
plt.yscale('log')
plt.xlabel("Nb Iterations")
plt.xlim(left=0)
plt.xlim(right=10000)
plt.show()