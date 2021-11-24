import pandas as pd
import matplotlib.pyplot as plt


def drawing_plots(colomn, average_line=False):
    data = pd.read_json("deviations.json")

    fig, ax = plt.subplots()
    ax.plot(data[colomn], color="red", label=colomn)
    if average_line == True:
        plt.axhline(
            y=data[colomn].mean(), color="blue", linestyle="--", label="average"
        )
    ax.set(xlabel="Object", ylabel="Angle", title=(colomn + " Deviation angles"))
    ax.legend(loc="upper right")
    fig.savefig("plots/" + colomn + " deviations.png")
    return "plots/" + colomn + " deviations.png"

