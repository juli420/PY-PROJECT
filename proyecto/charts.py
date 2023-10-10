import matplotlib.pyplot as plt
import numpy as np

'''# Grafica ¨bar¨
def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  bars = ax.bar(labels, values)'''
  
def generate_bar_chart(year, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{year}.png')
  plt.close()
  

  for bar, value in zip(bar, values):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(value, 2), ha='center', va='bottom')
  plt.savefig(f'./imgs/{year}.png')
  plt.close()

# grafica ¨torta¨
'''def generate_pie_chart(labels, values):
  fig, ax = plt.subplots(figsize=(15, 15))
  
  wedges, texts = ax.pie(values, labels=labels, startangle=90)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()'''
  
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

  # esto muestra otro tipo de grafica pie
  '''sorted_labels, sorted_values = zip(*sorted(zip(labels, values), key=lambda x: x[1], reverse=True))
  
  for i, w in enumerate(wedges):
    angle = (w.theta2 - w.theta1)/2. + w.theta1
    x = 2.5 * np.cos(np.deg2rad(angle))
    y = 2.5 * np.cos(np.deg2rad(angle))
    ax.text(x, y, str(sorted_values[i]), ha='center', va= 'center')'''
    
  
  #plt.show()
  
if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [222, 710, 420]
    #generate_bar_chart(labels, values)
    #generate_pie_chart(labels, values)