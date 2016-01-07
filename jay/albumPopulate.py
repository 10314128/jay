import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jay.settings')
import django
django.setup()
from album.models import Category, Page

def populate():
    
    category = addCategory('Jay')
    addPage(category, 'Bottle 框架', 'http://bottlepy.org/docs/dev/')
    category = addCategory('范特西')
    
    category = addCategory('八度空間')
            
    category = addCategory('葉惠美')
    
    category = addCategory('葉惠美')
    
    category = addCategory('七里香')
    
    category = addCategory('11月的蕭邦')
    
    category = addCategory('依然范特西')
    
    category = addCategory('我很忙')
    
    category = addCategory('魔杰座')
    
    category = addCategory('跨時代')
    
    category = addCategory('驚嘆號')
    
    category = addCategory('12新作')
    
    category = addCategory('哎呦,不錯哦')
    
    

    
    # 印出所輸入的資料
    for category in Category.objects.all():
        for page in Page.objects.filter(category=category):
            print(category.name, '--', page.title)
    
def addCategory(name):
    category = Category.objects.get_or_create(name=name)[0]
    return category

def addPage(category, title, url):
    Page.objects.get_or_create(category=category, title=title, url=url)
    
if __name__ == '__main__':
    print('開始填入資料...')
    populate()
    print('完成。')