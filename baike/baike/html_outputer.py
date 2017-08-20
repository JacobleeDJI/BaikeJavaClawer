'''
Created on 2017年8月19日

@author: jacob
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    
    def collect_data(self, data):   #收集数据
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.html', 'w', encoding="utf-8")
        
        fout.write("<html>")
        fout.write("<meta charset='utf-8'>")
        fout.write("<body>")
        fout.write("<table>")
        
       
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
        
        fout.write("</table>")
        fout.write("</body>") 
        fout.write("</html>") 
        
        fout.close()
    
    
    
    



