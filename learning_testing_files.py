import glob, os



# Current directo
# Directory where the data will reside, relative to 'darknet.exe'
ROOT_DIR = os.path.abspath(os.curdir)
DARKNET_DIR = ROOT_DIR + "/darknet/"
pics_directory_darknet_relative = 'VOCdevkit/'
file_train = open('darknet/cfg/train.txt', 'w')
file_test = open('darknet/cfg/test.txt', 'w')
pics_directory_darknet = "/media/tonycalvez/LAURA/VOCdevkit"

# Percentage of images to be used for the test set
percentage_test = 5;

# Create and/or truncate train.txt and test.txt



# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(pics_directory_darknet, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(pics_directory_darknet_relative + title + '.jpg' + "\n")
    else:
        file_train.write(pics_directory_darknet_relative + title + '.jpg' + "\n")
        counter = counter + 1

file_train.close()
file_test.close()
#
# os.system("mv " + ROOT_DIR + "/test.txt " + DARKNET_DIR + "cfg/")
# os.system("mv " + ROOT_DIR + "/train.txt " + DARKNET_DIR + "cfg/")
