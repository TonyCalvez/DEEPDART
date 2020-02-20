import cv2
import random
import os
import shutil
import numpy


class dataAugmentation:
    def __init__(self, path, image_name):
        '''
        Import image
        :param path: Path to the image
        :param image_name: image name
        '''
        self.path = path
        self.name = image_name
        self.image = cv2.imread(path + image_name)

    def rotate(self, image, angle=180, scale=1.0):
        '''
        Rotate the image
        :param image: image to be processed
        :param angle: Rotation angle in degrees. Positive values mean counter-clockwise rotation (the coordinate origin is assumed to be the top-left corner).
        :param scale: Isotropic scale factor.
        '''
        w = image.shape[1]
        h = image.shape[0]
        # rotate matrix
        M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, scale)
        # rotate
        image = cv2.warpAffine(image, M, (w, h))
        return image

    def flip(self, image, vflip=True, hflip=True):
        '''
        Flip the image
        :param image: image to be processed
        :param vflip: whether to flip the image vertically
        :param hflip: whether to flip the image horizontally
        '''
        if hflip or vflip:
            if hflip and vflip:
                c = -1
            else:
                c = 0 if vflip else 1
            image = cv2.flip(image, flipCode=c)
        return image

    def gaussian_noisy(self, img):
        row, col, ch = img.shape
        gauss = numpy.random.randn(row, col, ch)
        gauss = gauss.reshape(row, col, ch)
        noisy = img + img * gauss
        return noisy

    def pepper_noisy(self, img):
        row, col, ch = img.shape
        s_vs_p = 1
        amount = round(random.uniform(0.001, 0.1), 4)
        out = numpy.copy(img)
        # Salt mode
        num_salt = numpy.ceil(amount * img.size * s_vs_p)
        coords = [numpy.random.randint(0, i - 1, int(num_salt))
                  for i in img.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = numpy.ceil(amount * img.size * (1. - s_vs_p))
        coords = [numpy.random.randint(0, i - 1, int(num_pepper))
                  for i in img.shape]
        out[coords] = 0
        return out

    def clahe(self, img):
        # -----Converting image to LAB Color model-----------------------------------
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

        # -----Splitting the LAB image to different channels-------------------------
        l, a, b = cv2.split(lab)

        # -----Applying CLAHE to L-channel-------------------------------------------
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        cl = clahe.apply(l)

        # -----Merge the CLAHE enhanced L-channel with the a and b channel-----------
        limg = cv2.merge((cl, a, b))

        # -----Converting image from LAB Color model to RGB model--------------------
        final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        return final

    def adjust_gamma(self, image):
        gamma = round(random.uniform(0.01, 5), 3)

        invGamma = 1.0 / gamma
        table = numpy.array([((i / 255.0) ** invGamma) * 255
                             for i in numpy.arange(0, 256)]).astype("uint8")

        # apply gamma correction using the lookup table
        return cv2.LUT(image, table)

    def image_augment(self, save_path):
        '''
        Create the new image with imge augmentation
        :param path: the path to store the new image
        '''
        img = self.image.copy()
        img_flip = self.flip(img)
        # img_rot = self.rotate(img)
        img_gaussian = cv2.GaussianBlur(img, (25, 25), 0)
        img_median = cv2.medianBlur(img, 9)

        img_gaussian_noisy = self.gaussian_noisy(img)
        img_pepper_noisy = self.pepper_noisy(img)
        img_clahe = self.clahe(img)
        img_gamma = self.adjust_gamma(img)

        name_int = self.name[:len(self.name) - 4]
        cv2.imwrite(save_path + '%s' % str(name_int) + '_Origin.jpg', img)
        cv2.imwrite(save_path + '%s' % str(name_int) + '_Gaussian.jpg', img_gaussian)
        cv2.imwrite(save_path + '%s' % str(name_int) + '_Median.jpg', img_median)
        cv2.imwrite(save_path + '%s' % str(name_int) + '_Clahe.jpg', img_clahe)
        cv2.imwrite(save_path + '%s' % str(name_int) + '_Gamma_Augmentation.jpg', img_gamma)
        cv2.imwrite(save_path + '%s' % str(name_int) + '_Gaussian_Noisy.jpg', img_gaussian_noisy)
        cv2.imwrite(save_path + '%s' % str(name_int) + '_Pepper_Noisy.jpg', img_pepper_noisy)

    def main(self, file_dir, output_path):
        for root, _, files in os.walk(file_dir):
            for file in files:
                filename, file_extension = os.path.splitext(file)

                if file_extension == '.jpg' or file_extension == '.png' or file_extension == '.JPG':
                    raw_image = dataAugmentation(root, file)
                    raw_image.image_augment(output_path)
                elif file_extension == '.txt':
                    shutil.copy2(file_dir + file, output_path + filename + '_Origin.txt')
                    shutil.copy2(file_dir + file, output_path + filename + '_Gaussian.txt')
                    shutil.copy2(file_dir + file, output_path + filename + '_Median.txt')
                    shutil.copy2(file_dir + file, output_path + filename + '_Clahe.txt')
                    shutil.copy2(file_dir + file, output_path + filename + '_Gamma_Augmentation.txt')
                    shutil.copy2(file_dir + file, output_path + filename + '_Gaussian_Noisy.txt')
                    shutil.copy2(file_dir + file, output_path + filename + '_Pepper_Noisy.txt')


if __name__ == '__main__':
    PATH_IMAGE = "/home/tonycalvez/jetson/"
    PATH_IMAGE_GENERATE = "/media/tonycalvez/T_LAGRUE/VideoX/"

    generate = dataAugmentation(PATH_IMAGE, os.listdir(PATH_IMAGE)[0])
    generate.main(PATH_IMAGE, PATH_IMAGE_GENERATE)
    print("It's gooooood!")
