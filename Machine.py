#-----------------------------------------------------------------------
# Ambrose Ryan Xavier
#-----------------------------------------------------------------------

from sklearn import datasets, svm
from sklearn.tree import DecisionTreeClassifier

def learn(classifier, dataset):
    n = len(dataset.data)
    classifier.fit(dataset.data[:-n//2], dataset.target[:-n//2])
    predicted_answers = classifier.predict(dataset.data[-n//2:])
    correct_answers = dataset.target[-n//2:]
    correct = 0
    for predicted, target in zip(predicted_answers, correct_answers):
        if predicted == target:
            correct += 1
    print("Percentage Correct = {:.2f}\n".format(100 * (correct/(n // 2))))

def dataset_demonstration(dataset):
    print("Dataset Data")
    print(dataset.data)
    print("Length: ", len(dataset.data))
    print("Dataset Classifications")
    print(dataset.target)
    print("Length: ", len(dataset.target))

def main():
    digits = datasets.load_digits()
    dataset_demonstration(digits)
    classifier = svm.SVC(gamma=0.001, C=100.0)
    print("Support Vector Machine")
    learn(classifier, digits)

    for depth in range(1, 11):
        classifier = DecisionTreeClassifier(max_depth = depth)
        print("Decision Tree of Depth", depth)
        learn(classifier, digits)

if __name__ == "__main__":
    main()

print("\nRecognize Handwritten Digits\n")
print(__doc__)

# Standard Scientific Python Imports

import matplotlib.pyplot as plt

# Import Datasets, Classifiers, and Performance Metrics

from sklearn import datasets, svm, metrics

# The Digits Dataset

digits = datasets.load_digits()

# The data that we are interested in is comprised of [8x8] images of digits.
# Allow us to examine the first four images, stored in the [images] attribute
# of the dataset. As long as we were working from image files, we could load
# them by utilizing matplotlib.pyplot.imread. Note that each image must have
# the same size. For these images, we know which digits they represent: As
# long as it is given in the [target] of the dataset.

images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index+1)
    plt.axis("Off")
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="Nearest")
    plt.title("Training %i" % label)

# To apply a classifier on this data, we need to flatten the image.
# Thus, we turn the data into a (samples, feature) matrix.

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a Support Vector Classifier

classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits

classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

# Now we predict the value of the digits on the second half

expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])

print("Classification Report for Classifier %s:\n%s\n" %
      (classifier, metrics.classification_report(expected, predicted)))
print("Confusion Matrix: \n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index+5)
    plt.axis("Off")
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="Nearest")
    plt.title("Prediction: %i" % prediction)

plt.show()
