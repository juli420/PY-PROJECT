import utils
import read
import charts

def run():
  data = read.read_csv('data.csv')
  #data = list(filter(lambda item : item['Year'] == '2016',data))

  año = int(input('Ingresa un año entre 2000 y 2016 => '))
  #result = utils.best_seller_games(data, año)
  
  if 2000 <= año <= 2016:
    top_10 = utils.best_seller_games(data, año)

    if len(top_10) > 0:
        labels = [juego['Name'] for juego in top_10]
        values = [int(juego['Rank']) for juego in top_10]
        charts.generate_pie_chart(labels, values)
        #charts.generate_bar_chart(labels, values)
    else:
        print('Año no válido')

if __name__ == '__main__':
    
  run()
'''
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''