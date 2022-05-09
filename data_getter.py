import requests
import pandas as pd
from bs4 import BeautifulSoup 

pilots_list = []

for j in range(2000, 2022):
    print("\nYear :", j)
    base_url = 'https://www.statsf1.com' #create the url according to the year
    year = str(j)
    lang = 'en'
    url = base_url+'/'+lang+'/'+year+'.aspx'
    resp = requests.get(url, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"})
    html = resp.content

    soup_gp = BeautifulSoup(html, 'html.parser') #get all GP links of the year
    gp_list = soup_gp.find_all("div", {"class": "flag"})
    gp_link = [gp.a['href'] for gp in gp_list]

    for i in range(len(gp_link)):
        print('GP :', i)
        
        url = base_url + gp_link[i][:-5] + '/grille.aspx' #get the starting grid of the GP
        resp = requests.get(url, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"})
        html = resp.content
        soup_grid = BeautifulSoup(html, 'html.parser') 
        starting_grid = soup_grid.find_all("table", {"class": "GPgridline"})
        start_grid = []
        index = int(starting_grid[0].find_all("div")[0].text[0])

        for line in starting_grid:
            pilots = line.find_all("div")
            for pilot in pilots:
                start_grid.append(pilot.a['href'].split('/')[-1][:-5])
        start_grid = list(dict.fromkeys(start_grid))

        if index != 1:
            for n in range(0, len(start_grid), 2):
                try: #error management
                    start_grid[n], start_grid[n+1] = start_grid[n+1], start_grid[n] 
                except IndexError:
                    pass
       
        url = base_url + gp_link[i][:-5] + '/classement.aspx' #get the final grid of the GP
        resp = requests.get(url, headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"})
        html = resp.content
        soup_final = BeautifulSoup(html, 'html.parser')
        final_grid = soup_final.find_all('tr')
        ending_grid = []

        for result in range(len(final_grid)):
            try: #error management
                ending_grid.append(final_grid[result].a['href'].split('/')[-1][:-5])
            except TypeError:
                pass

        for pos in range(len(start_grid)): #save start and final position of the pilot
            if not any(start_grid[pos] == pilot[0] for pilot in pilots_list):
                pilots_list.append([start_grid[pos], []])
                index_pilot = -1
            else:
                for j in range(len(pilots_list)):
                    if pilots_list[j][0] == start_grid[pos]:
                        index_pilot = j 
                
            while pos >= len(pilots_list[index_pilot][1]):
                pilots_list[index_pilot][1].append([])
            
            index_finish = ending_grid.index(start_grid[pos])
            pilots_list[index_pilot][1][pos].append(index_finish)

for i in pilots_list: #saving data in a csv file
    data = {"Start Position": [j+1 for j in range(len(i[1]))], "End Position": i[1]}
    df = pd.DataFrame(data)
    df.to_csv('results/'+i[0]+'_positions.csv', index=False)