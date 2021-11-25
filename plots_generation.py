import pandas as pd
import matplotlib.pyplot as plt

class Drawing_plots():
    def __init__(self, plot_type, colomn, average_line=False):
        self.colomn = colomn
        self.average_line = average_line
        self.plot_type = plot_type

    def drawing_plots(self):
        color_array = ["red", "blue", "green","black"]
        data = pd.read_json("deviations.json")

        fig, ax = plt.subplots()
        for i in range(0,len(self.colomn)):
            if self.plot_type == "scatter":
                ax.scatter(range(0,len(data)), data[self.colomn[i]], c=color_array[i], label=self.colomn[i], s=3)
                if self.average_line == True:
                    plt.axhline(
                        y=data[self.colomn[i]].mean(), color=color_array[i], linestyle="--", label=("average " +self.colomn[i]) 
                    )
                ax.set(xlabel="Object", ylabel="Angle", title= (' '.join([i for i in self.colomn]) + " Deviation angles"))
        
        
        ax.legend(loc="upper right")
        file_name = "plots/" + ' '.join([i for i in self.colomn]) + " deviations.png"
        fig.savefig(file_name)
        return file_name

Drawing_plots("scatter", ("min","max"),average_line = True).drawing_plots()