def get_vgs(video_dict):
  year_dict = {
    '2016': int(video_dict['Year']),
    '2015': int(video_dict['Year']),
    '2014': int(video_dict['Year']),
    '2013': int(video_dict['Year']),
    '2012': int(video_dict['Year']),
    '2011': int(video_dict['Year']),
    '2010': int(video_dict['Year']),
    '2009': int(video_dict['Year']),
    '2008': int(video_dict['Year']),
    '2007': int(video_dict['Year']),
    '2006': int(video_dict['Year']),
    '2005': int(video_dict['Year']),
    '2004': int(video_dict['Year']),
    '2003': int(video_dict['Year']),
    '2002': int(video_dict['Year']),
    '2001': int(video_dict['Year']),
    '2000': int(video_dict['Year']),
  }
  labels = [video_dict['Name']]
  values = [video_dict['Rank']]
  return labels, values

#population_by_country
def best_seller_games(data, year):
  result = list(filter(lambda item: item['Year'] == str(year), data))
  return result[:10]