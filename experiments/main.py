import numpy as np
import time
from experiments.learners import *
from experiments.tuned_learners import *
from data.data_to_use import *
import random

data = data_miyazaki()
repeats = 20
# methods = 0  # "0" for MRE, "1" for SA
metrics = 1


if __name__ == '__main__':

    for i in range(6):

        if i == 0:
            list_temp = []
            time0 = time.time()
            for i in range(repeats):
                list_temp.append(CART_DE(data, metrics))
            run_time0 = str(time.time() - time0)

            flat_list = np.array(list_temp).flatten()
            list_output = sorted(flat_list.tolist())

            print(list_output)
            print("median for CART_DE:", np.median(list_output))
            print("runtime for CART_DE:", run_time0)

            with open("./output/new_sk_results.txt", "w") as output:
                output.write("CART_DE" + '\n')
                for i in sorted(list_output):
                    output.write(str(i) + " ")

        if i == 1:
            list_temp = []
            time1 = time.time()
            for i in range(repeats):
                list_temp.append(CART_FLASH(data, metrics))
            run_time1 = str(time.time() - time1)

            flat_list = np.array(list_temp).flatten()
            list_output = sorted(flat_list.tolist())

            print(list_output)
            print("median for CART_FLASH:", np.median(list_output))
            print("runtime for CART_FLASH:", run_time1)

            with open("./output/new_sk_results.txt", "a+") as output:
                output.write('\n\n' + "CART_FLASH" + '\n')
                for i in sorted(list_output):
                    output.write(str(i) + " ")

        if i == 2:
            list_temp = []
            time2 = time.time()
            for i in range(repeats):
                list_temp.append(CART(data)[metrics])
            run_time2 = str(time.time() - time2)

            flat_list = np.array(list_temp).flatten()
            list_output = sorted(flat_list.tolist())

            print(list_output)
            print("median for CART0:", np.median(list_output))
            print("runtime for CART0:", run_time2)

            with open("./output/new_sk_results.txt", "a+") as output:
                output.write('\n\n' + "CART0" + '\n')
                for i in sorted(list_output):
                    output.write(str(i) + " ")

        if i == 3:
            list_temp = []
            time3 = time.time()
            for i in range(repeats):
                list_temp.append(RF(data)[metrics])
            run_time3 = str(time.time() - time3)

            flat_list = np.array(list_temp).flatten()
            list_output = sorted(flat_list.tolist())

            print(list_output)
            print("median for RF:", np.median(list_output))
            print("runtime for RF:", run_time3)

            with open("./output/new_sk_results.txt", "a+") as output:
                output.write('\n\n' + "RF" + '\n')
                for i in sorted(list_output):
                    output.write(str(i) + " ")

        if i == 4:
            list_temp = []
            time4 = time.time()
            for i in range(repeats):
                list_temp.append(SVM(data)[metrics])
            run_time4 = str(time.time() - time4)

            flat_list = np.array(list_temp).flatten()
            list_output = sorted(flat_list.tolist())

            print(list_output)
            print("median for SVR:", np.median(list_output))
            print("runtime for SVR:", run_time4)

            with open("./output/new_sk_results.txt", "a+") as output:
                output.write('\n\n' + "SVR" + '\n')
                for i in sorted(list_output):
                    output.write(str(i) + " ")

        if i == 5:
            list_temp = []
            time5 = time.time()
            for i in range(repeats):
                list_temp.append(KNN(data)[metrics])
            run_time5 = str(time.time() - time5)

            flat_list = np.array(list_temp).flatten()
            list_output = sorted(flat_list.tolist())

            print(list_output)
            print("median for ABE0:", np.median(list_output))
            print("runtime for ABE0:", run_time5)

            with open("./output/new_sk_results.txt", "a+") as output:
                output.write('\n\n' + "ABE0" + '\n')
                for i in sorted(list_output):
                    output.write(str(i) + " ")
