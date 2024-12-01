import matplotlib.pyplot as plt
import numpy as np

# N labels of N number of values in the array
xlabels_som = ['SOM', 'SOM with greedy']
bar_colors = ['#8A9A5B', '#F6AC69']
plot_color_1 = "#355E3B"
plot_color_2 = "#F57C73"

fig, axs = plt.subplots(1, 4, figsize=(12, 3))
x_label = np.array([0.1, 0.2])
x_label_plot_1 = np.array([0.05, 0.15])
x_label_plot_2 = np.array([0.15, 0.25])

# Các trường thuộc tính dữ liệu
m_1_max = 864.8166191017203
m_1_min = 763.7544528987399
m_1_avg = 815.8887811781401
m_1_max_after = 843.657820644596768
m_1_min_after = 822.991277393604832
m_1_avg_after = 830.124313163504098
axs[0].set_ylim(500, 1000)

axs[0].bar(x_label ,np.array([m_1_max, m_1_max_after]) - np.array([m_1_min, m_1_min_after]), 0.05, bottom=np.array([m_1_min, m_1_min_after]), label=xlabels_som, color=bar_colors)
axs[0].xaxis.set_visible(False)

# Add some text for labels, title and custom x-axis tick labels, etc.
axs[0].set_ylabel('Total reward')
axs[0].set_xlim(0, 0.3)
axs[0].set_title('30g_1r_lb')
axs[0].legend()

axs[0].plot(x_label_plot_1, np.array([m_1_avg, m_1_avg]), linestyle = 'dotted', color=plot_color_1)
axs[0].plot(x_label_plot_2, np.array([m_1_avg_after, m_1_avg_after]), linestyle = 'dotted', color=plot_color_2)

m_2_max = 4355.4220388651165
m_2_min = 3794.013129081338
m_2_avg = 4046.281555944204
m_2_max_after = 4267.672927268394233
m_2_min_after = 3772.871213629809972
m_2_avg_after = 3897.587362954360287
axs[1].set_ylim(3000, 5000)

axs[1].bar(x_label ,np.array([m_2_max, m_2_max_after]) - np.array([m_2_min, m_2_min_after]), 0.05, bottom=np.array([m_2_min, m_2_min_after]), label=xlabels_som, color=bar_colors)
axs[1].set_xlim(0, 0.3)
axs[1].xaxis.set_visible(False)
axs[1].set_title('30g_1r_hb')

axs[1].plot(x_label_plot_1, np.array([m_2_avg, m_2_avg]), linestyle = 'dotted', color=plot_color_1)
axs[1].plot(x_label_plot_2, np.array([m_2_avg_after, m_2_avg_after]), linestyle = 'dotted', color=plot_color_2)

m_3_max = 2014.685419568923
m_3_min = 1879.0569941221365
m_3_avg = 1965.828786025737
m_3_max_after = 2009.321502711029552
m_3_min_after = 1929.209084853725926
m_3_avg_after = 1989.447908853795525
axs[2].set_ylim(1500, 2500)

axs[2].bar(x_label ,np.array([m_3_max, m_3_max_after]) - np.array([m_3_min, m_3_min_after]), 0.05, bottom=np.array([m_3_min, m_3_min_after]), label=xlabels_som, color=bar_colors)
axs[2].xaxis.set_visible(False)
axs[2].set_xlim(0, 0.3)
axs[2].set_title('150g_3r_lb')

axs[2].plot(x_label_plot_1, np.array([m_3_avg, m_3_avg]), linestyle = 'dotted', color=plot_color_1)
axs[2].plot(x_label_plot_2, np.array([m_3_avg_after, m_3_avg_after]), linestyle = 'dotted', color=plot_color_2)


m_4_max = 9978.346141096552
m_4_min = 9105.617138761208
m_4_avg = 9584.2631815378
m_4_max_after = 7649.574916449048033
m_4_min_after = 7251.441291135427491
m_4_avg_after = 7432.260968255885018
axs[3].set_ylim(7000, 12000)

axs[3].bar(x_label ,np.array([m_4_max, m_4_max_after]) - np.array([m_4_min, m_4_min_after]), 0.05, bottom=np.array([m_4_min, m_4_min_after]), label=xlabels_som, color=bar_colors)
axs[3].xaxis.set_visible(False)
axs[3].set_xlim(0, 0.3)
axs[3].set_title('150g_3r_hb')

axs[3].plot(x_label_plot_1, np.array([m_4_avg, m_4_avg]), linestyle = 'dotted', color=plot_color_1)
axs[3].plot(x_label_plot_2, np.array([m_4_avg_after, m_4_avg_after]), linestyle = 'dotted', color=plot_color_2)


fig.tight_layout()
plt.show()