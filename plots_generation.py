import pandas as pd
import matplotlib.pyplot as plt

class Drawing_plots():
    def __init__(self, colomn, average_line=False):
        self.colomn = colomn
        self.average_line = average_line

    def drawing_plots(self):
        data = pd.read_json("deviations.json")

        fig, ax = plt.subplots()
        ax.scatter(range(0,len(data)), data[self.colomn], color="red", label=self.colomn, s=5)
        if self.average_line == True:
            plt.axhline(
                y=data[self.colomn].mean(), color="blue", linestyle="--", label="average"
            )
        ax.set(xlabel="Object", ylabel="Angle", title=(self.colomn + " Deviation angles"))
        ax.legend(loc="upper right")
        fig.savefig("plots/" + self.colomn + " deviations.png")
        return "plots/" + self.colomn + " deviations.png"

Drawing_plots("mean",average_line = False).drawing_plots()