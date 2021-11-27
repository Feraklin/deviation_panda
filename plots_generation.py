import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Drawing_plots():
    def __init__(self, plot_type, colomn, mean_line=False, aprox_line = False, labels = None):
        self.colomn = colomn
        self.mean_line = mean_line
        self.plot_type = plot_type
        self.aprox_line = aprox_line
        self.labels = labels

    def drawing_plots(self):
        color_array = ["red", "blue", "green","black"]
        data = pd.read_json("deviations.json")

        if self.plot_type == "scatter":
            fig, ax = plt.subplots()
            for i in range(0,len(self.colomn)):
                ax.scatter(range(0,len(data)), data[self.colomn[i]], c=color_array[i], label=self.colomn[i], s=3)
                if self.mean_line == True:
                    plt.axhline(
                        y=data[self.colomn[i]].mean(), color=color_array[i], linestyle="--", label=("average " +self.colomn[i]) 
                    )

                if self.aprox_line == True:
                    aprox_coeficients = np.polyfit(range(0,len(data)),data[self.colomn[i]],1)
                    aprox_rule=np.poly1d(aprox_coeficients)
                    aprox_y = aprox_rule(range(0,len(data)))
                    ax.scatter(range(0,len(data)), aprox_y, c=color_array[i], s=20, marker="_", label=("aprox " +self.colomn[i]))
                
                ax.set(xlabel="Object", ylabel="Angle", title= (' '.join([i for i in self.colomn]) + " Deviation angles"))
            ax.legend(loc="upper right")
            file_name = "plots/" + ' '.join([i for i in self.colomn]) + " deviations.png"

        if self.plot_type == "hist":
            fig, axs = plt.subplots(len(self.colomn),1,figsize=(12, 5*len(self.colomn)))
            for i in range(0,len(self.colomn)):
                axs[i].hist(data[self.colomn[i]],bins=len(data))
                axs[i].set(title= "Чаастотное распределение для "+ self.colomn[i].upper())
                if self.mean_line == True:
                    axs[i].axvline(data[self.colomn[i]].mean(), color = "red", linestyle='dashed', label=("mean = " + str(data[self.colomn[i]].mean())[0:4]))
                    axs[i].legend(loc="upper right")
            file_name = "plots/" + ' '.join([i for i in self.colomn]) + " hist.png"
        
        if self.plot_type == "pie":
            false_corners = len(data.loc[data.gt_corners != data.rb_corners])
            true_corners = len(data.loc[data.gt_corners == data.rb_corners])
            fig, ax = plt.subplots()
            ax.pie([true_corners, false_corners], labels=["True " + str(int(true_corners*100/len(data))) + "%", "False " + str(int(false_corners*100/len(data))) + "%"], colors = color_array)
            fig.set(facecolor = "white")
            ax.set(title= "Процент верного определения количества углов")
            file_name = "plots/" + ' '.join([i for i in self.colomn]) + " pie.png"
        
        if self.plot_type == "boxplot":
            fig, ax = plt.subplots()
            ax.boxplot(self.colomn, labels= self.labels)
            file_name = "plots/" + ' '.join([i for i in self.labels]) + " boxplot.png"
        
        
        fig.savefig(file_name)
        return file_name