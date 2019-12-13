import pandas
import tensorflow as tf
if __name__ == '__main__':
    csv = pandas.read_csv("nao_labels.csv").values
    with tf.python_io.TFRecordWriter("nao.tfrecords") as writer:
        for row in csv:
            features, label = row[:-1], row[-1]
            example = tf.train.Example()
            example.features.feature["features"].float_list.value.extend(features)
            example.features.feature["label"].int64_list.value.append(label)
            writer.write(example.SerializeToString())